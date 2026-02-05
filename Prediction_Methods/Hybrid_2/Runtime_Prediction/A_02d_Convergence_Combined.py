# INFRASTRUCTURE
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import DPI, STRATEGY_COLORS, STRATEGY_COLORS_EPSILON

STRATEGIES = ['Size', 'Frequency', 'Error']

# Get color based on strategy and variant
def get_color(strategy: str, variant: str) -> str:
    return STRATEGY_COLORS_EPSILON[strategy] if variant == 'Epsilon' else STRATEGY_COLORS[strategy]


# ORCHESTRATOR

# Create combined convergence plot for all strategies
def create_combined_plot(base_dir: str, variant: str, output_dir: str) -> None:
    curves = {}
    for strategy in STRATEGIES:
        log_path = Path(base_dir) / strategy / variant / 'selection_log.csv'
        if log_path.exists():
            df = load_selection_log(log_path)
            curves[strategy] = extract_mre_curve(df)
    export_combined_plot(curves, variant, output_dir)


# FUNCTIONS

# Load selection log CSV
def load_selection_log(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, delimiter=';')


# Extract MRE values per iteration
def extract_mre_curve(df: pd.DataFrame) -> list:
    mre_values = []
    current_mre = df['baseline_mre'].iloc[0]
    for _, row in df.iterrows():
        if row['status'] == 'SELECTED':
            current_mre = row['new_mre']
        mre_values.append(current_mre * 100)
    return mre_values


# Export combined MRE progression plot
def export_combined_plot(curves: dict, variant: str, output_dir: str) -> None:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    max_iterations = max(len(curve) for curve in curves.values())
    plt.figure(figsize=(10, 6))
    for strategy, mre_curve in curves.items():
        extended_curve = mre_curve + [mre_curve[-1]] * (max_iterations - len(mre_curve))
        plt.plot(range(max_iterations), extended_curve, label=strategy, color=get_color(strategy, variant), linewidth=1.5)
    plt.xlabel('Iteration')
    plt.ylabel('MRE (%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path / f'A_02d_convergence_{variant.lower()}.png', dpi=DPI)
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", required=True, help="Path to Pattern_Selection/")
    parser.add_argument("--variant", required=True, choices=['Baseline', 'Epsilon'], help="Variant to plot")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()
    create_combined_plot(args.base_dir, args.variant, args.output_dir)
