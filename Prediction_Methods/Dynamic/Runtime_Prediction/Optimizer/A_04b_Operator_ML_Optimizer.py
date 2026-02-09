#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import (DPI, DEEP_GRAY, DEEP_GREEN, DEEP_ORANGE, DEEP_CYAN,
    GROUPED_BAR_FIGSIZE_WIDE, GROUPED_BAR_WIDTH_WIDE, GROUPED_BAR_ALPHA,
    GROUPED_BAR_LABEL_FONTSIZE_WIDE, LABEL_FONTSIZE, TICK_FONTSIZE,
    GRID_AXIS, GRID_ALPHA, GRID_LINESTYLE, apply_top_margin,
    DYNAMIC_MRE_Y_SCALE, DYNAMIC_MRE_Y_STEP, CAP_OVERFLOW_COLOR, CAP_LABEL_GAP_CM)

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
SHIFTED_TEMPLATES = ['Q18']


# ORCHESTRATOR
def comparison_workflow(optimizer_csv: Path, operator_csv: Path, hybrid_csv: Path, online_csv: Path, output_dir: Path) -> None:
    optimizer_df = load_data(optimizer_csv)
    operator_df = load_data(operator_csv)
    hybrid_df = load_data(hybrid_csv)
    online_df = load_data(online_csv)
    create_comparison_plot(optimizer_df, operator_df, hybrid_df, online_df, output_dir)


# FUNCTIONS

# Load CSV and normalize template column
def load_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    if 'loto_template' in df.columns:
        df = df.rename(columns={'loto_template': 'template'})
    return df.set_index('template')


# Create grouped bar plot with 4 methods
def create_comparison_plot(optimizer_df: pd.DataFrame, operator_df: pd.DataFrame,
                           hybrid_df: pd.DataFrame, online_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=GROUPED_BAR_FIGSIZE_WIDE)

    templates = [t for t in TEMPLATES if t in optimizer_df.index and t in operator_df.index
                 and t in hybrid_df.index and t in online_df.index]

    optimizer_values = np.array([optimizer_df.loc[t, 'mean_mre_pct'] for t in templates])
    operator_values = np.array([operator_df.loc[t, 'mean_mre_pct'] for t in templates])
    hybrid_values = np.array([hybrid_df.loc[t, 'mean_mre_pct'] for t in templates])
    online_values = np.array([online_df.loc[t, 'mean_mre_pct'] for t in templates])

    x = np.arange(len(templates))
    width = GROUPED_BAR_WIDTH_WIDE
    y_cap = DYNAMIC_MRE_Y_SCALE

    optimizer_overall = optimizer_values.mean()
    operator_overall = operator_values.mean()
    hybrid_overall = hybrid_values.mean()
    online_overall = online_values.mean()

    bars_optimizer = ax.bar(x - 1.5*width, np.minimum(optimizer_values, y_cap), width,
                            label=f'Optimizer Cost Model (Overall: {optimizer_overall:.2f}%)',
                            color=DEEP_GRAY, alpha=GROUPED_BAR_ALPHA)
    bars_operator = ax.bar(x - 0.5*width, np.minimum(operator_values, y_cap), width,
                           label=f'Operator Level (Overall: {operator_overall:.2f}%)',
                           color=DEEP_GREEN, alpha=GROUPED_BAR_ALPHA)
    bars_hybrid = ax.bar(x + 0.5*width, np.minimum(hybrid_values, y_cap), width,
                         label=f'Hybrid_1 (Overall: {hybrid_overall:.2f}%)',
                         color=DEEP_ORANGE, alpha=GROUPED_BAR_ALPHA)
    bars_online = ax.bar(x + 1.5*width, np.minimum(online_values, y_cap), width,
                         label=f'Online_1 (Overall: {online_overall:.2f}%)',
                         color=DEEP_CYAN, alpha=GROUPED_BAR_ALPHA)

    ax.set_xlabel('Template', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=TICK_FONTSIZE)
    legend = ax.legend(fontsize=TICK_FONTSIZE, loc='upper right')
    ax.grid(axis=GRID_AXIS, alpha=GRID_ALPHA, linestyle=GRID_LINESTYLE)

    plt.tight_layout()
    apply_top_margin(ax, fig, DYNAMIC_MRE_Y_SCALE, DYNAMIC_MRE_Y_STEP)

    legend_bbox = legend.get_window_extent(fig.canvas.get_renderer())
    legend_bottom_data = ax.transData.inverted().transform((0, legend_bbox.y0))[1]
    gap_inches = CAP_LABEL_GAP_CM / 2.54
    ax_height_inches = fig.get_size_inches()[1] * ax.get_position().height
    ylim = ax.get_ylim()
    gap_data = (ylim[1] - ylim[0]) * (gap_inches / ax_height_inches)
    shifted_y = legend_bottom_data - gap_data

    all_bar_sets = [
        (bars_optimizer, optimizer_values),
        (bars_operator, operator_values),
        (bars_hybrid, hybrid_values),
        (bars_online, online_values),
    ]
    for bars, values in all_bar_sets:
        for i, (bar, val) in enumerate(zip(bars, values)):
            color = CAP_OVERFLOW_COLOR if val > y_cap else 'black'
            template = templates[i]
            if template in SHIFTED_TEMPLATES:
                ax.text(bar.get_x() + bar.get_width()/2., shifted_y,
                        f'{val:.1f}%', ha='center', va='top',
                        fontsize=GROUPED_BAR_LABEL_FONTSIZE_WIDE, color=color)
            else:
                ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                        f'{val:.1f}%', ha='center', va='bottom',
                        fontsize=GROUPED_BAR_LABEL_FONTSIZE_WIDE, color=color)

    plt.savefig(output_dir / 'A_04b_operator_ml_optimizer.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--optimizer-csv", required=True, help="Path to optimizer loto_mre CSV")
    parser.add_argument("--operator-csv", required=True, help="Path to operator ML loto_mre CSV")
    parser.add_argument("--hybrid-csv", required=True, help="Path to Hybrid_1 loto_mre CSV")
    parser.add_argument("--online-csv", required=True, help="Path to Online_1 loto_mre CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(
        Path(args.optimizer_csv),
        Path(args.operator_csv),
        Path(args.hybrid_csv),
        Path(args.online_csv),
        Path(args.output_dir)
    )
