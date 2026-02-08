#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import DPI, STRATEGY_COLORS, GROUPED_BAR_FIGSIZE, GROUPED_BAR_ALPHA, GROUPED_BAR_LABEL_FONTSIZE, GRID_AXIS, GRID_ALPHA, GRID_LINESTYLE, CAP_OVERFLOW_COLOR, apply_top_margin, ONLINE_1_MRE_Y_SCALE, ONLINE_1_MRE_Y_STEP

SCRIPT_DIR = Path(__file__).resolve().parent
ANALYSIS_DIR = SCRIPT_DIR / 'Evaluation' / 'Analysis'


# ORCHESTRATOR
def combined_strategy_workflow(output_dir: str) -> None:
    data = load_all_mre_data()
    combined_df = create_combined_dataframe(data)
    export_combined_csv(combined_df, output_dir)
    create_combined_plot(data, output_dir)


# FUNCTIONS

# Load all MRE data from CSV files
def load_all_mre_data() -> dict:
    return {
        'Size': load_template_mre(ANALYSIS_DIR / 'Size' / 'template_mre.csv'),
        'Frequency': load_template_mre(ANALYSIS_DIR / 'Frequency' / 'template_mre.csv'),
        'Error': load_template_mre(ANALYSIS_DIR / 'Error' / 'template_mre.csv')
    }


# Load template MRE from CSV
def load_template_mre(csv_path: Path) -> dict:
    df = pd.read_csv(csv_path, delimiter=';', index_col=0)
    overall_mre = df['mean_mre'].mean()
    return {
        'template_mre': df['mean_mre_pct'].to_dict(),
        'overall_mre': overall_mre * 100
    }


# Create combined dataframe with all strategies
def create_combined_dataframe(data: dict) -> pd.DataFrame:
    rows = []
    templates = sorted(data['Size']['template_mre'].keys(), key=lambda x: int(x[1:]))

    for template in templates:
        row = {'template': template}
        for strategy in ['Size', 'Frequency', 'Error']:
            row[f'{strategy.lower()}_mre_pct'] = data[strategy]['template_mre'].get(template, np.nan)
        rows.append(row)

    df = pd.DataFrame(rows)
    df.set_index('template', inplace=True)
    return df


# Export combined CSV
def export_combined_csv(combined_df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    combined_df.to_csv(output_path / 'A_06_strategy_comparison.csv', sep=';')


# Create combined bar plot
def create_combined_plot(data: dict, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    templates = sorted(data['Size']['template_mre'].keys(), key=lambda x: int(x[1:]))
    x = np.arange(len(templates))

    fig, ax = plt.subplots(figsize=GROUPED_BAR_FIGSIZE)

    strategies = ['Size', 'Frequency', 'Error']
    colors = [STRATEGY_COLORS['Size'], STRATEGY_COLORS['Frequency'], STRATEGY_COLORS['Error']]
    offsets = [-1.0, 0.0, 1.0]
    width = 0.25

    y_limit = ONLINE_1_MRE_Y_SCALE

    for strategy, color, offset in zip(strategies, colors, offsets):
        actual_values = [data[strategy]['template_mre'].get(t, 0) for t in templates]
        display_values = [min(v, y_limit) for v in actual_values]
        overall = data[strategy]['overall_mre']
        label = f"{strategy} (Overall: {overall:.2f}%)"
        bars = ax.bar(x + offset * width, display_values, width, label=label, color=color, alpha=GROUPED_BAR_ALPHA)

        for i, bar in enumerate(bars):
            actual = actual_values[i]
            label_color = CAP_OVERFLOW_COLOR if actual > y_limit else 'black'
            if actual > y_limit:
                ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() - 0.2,
                        f'{actual:.1f}%', ha='center', va='top', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=label_color)
            else:
                ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1,
                        f'{actual:.1f}%', ha='center', va='bottom', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=label_color)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis=GRID_AXIS, alpha=GRID_ALPHA, linestyle=GRID_LINESTYLE)

    plt.tight_layout()
    apply_top_margin(ax, fig, ONLINE_1_MRE_Y_SCALE, ONLINE_1_MRE_Y_STEP)

    plt.savefig(output_path / 'A_06_strategy_comparison.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(ANALYSIS_DIR / 'Overall'), help="Output directory")
    args = parser.parse_args()

    combined_strategy_workflow(args.output_dir)
