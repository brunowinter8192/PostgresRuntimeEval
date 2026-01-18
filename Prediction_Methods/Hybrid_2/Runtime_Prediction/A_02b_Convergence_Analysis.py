import argparse
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# INFRASTRUCTURE

CONVERGENCE_POINTS = [50, 90, 95]

# ORCHESTRATOR

def analyze_convergence(selection_log: str, output_dir: str, prefix: str = '') -> None:
    df = load_selection_log(selection_log)
    mre_curve = extract_mre_curve(df)
    baseline_mre, final_mre = mre_curve[0], mre_curve[-1]
    total_improvement = baseline_mre - final_mre
    convergence = compute_convergence_points(mre_curve, baseline_mre, total_improvement)
    export_results(convergence, baseline_mre, final_mre, total_improvement, len(mre_curve), output_dir, prefix)
    export_plot(mre_curve, output_dir, prefix)

# FUNCTIONS

# Load selection log CSV
def load_selection_log(path: str) -> pd.DataFrame:
    return pd.read_csv(path, delimiter=';')

# Extract MRE values per iteration
def extract_mre_curve(df: pd.DataFrame) -> list:
    mre_values = []
    current_mre = df['baseline_mre'].iloc[0]
    for _, row in df.iterrows():
        if row['status'] == 'SELECTED':
            current_mre = row['new_mre']
        mre_values.append(current_mre)
    return mre_values

# Find first iteration where MRE drops to or below target
def find_iteration_for_mre(mre_curve: list, target: float) -> int:
    for i, mre in enumerate(mre_curve):
        if mre <= target:
            return i
    return len(mre_curve) - 1

# Compute convergence points (iterations at X% improvement)
def compute_convergence_points(mre_curve: list, baseline_mre: float, total_improvement: float) -> dict:
    convergence = {}
    for pct in CONVERGENCE_POINTS:
        target = baseline_mre - (pct / 100) * total_improvement
        convergence[f'iter_at_{pct}pct'] = find_iteration_for_mre(mre_curve, target)
    return convergence

# Export results to CSV
def export_results(convergence: dict, baseline_mre: float, final_mre: float, total_improvement: float, total_iterations: int, output_dir: str, prefix: str = '') -> None:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    filename = f'{prefix}_A_02b_summary.csv' if prefix else 'A_02b_summary.csv'
    df_summary = pd.DataFrame([{
        'baseline_mre': round(baseline_mre, 6),
        'final_mre': round(final_mre, 6),
        'total_improvement': round(total_improvement, 6),
        'total_iterations': total_iterations,
        **{k: v for k, v in convergence.items()}
    }])
    df_summary.to_csv(out_path / filename, sep=';', index=False)

# Export MRE progression plot
def export_plot(mre_curve: list, output_dir: str, prefix: str = '') -> None:
    out_path = Path(output_dir)
    filename = f'{prefix}_A_02b_mre_progression.png' if prefix else 'A_02b_mre_progression.png'
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(mre_curve)), mre_curve, linewidth=1.5)
    plt.xlabel('Iteration')
    plt.ylabel('MRE')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path / filename, dpi=300)
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("selection_log", help="Path to selection_log.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    parser.add_argument("--prefix", default='', help="Prefix for output filenames")
    args = parser.parse_args()
    analyze_convergence(args.selection_log, args.output_dir, args.prefix)
