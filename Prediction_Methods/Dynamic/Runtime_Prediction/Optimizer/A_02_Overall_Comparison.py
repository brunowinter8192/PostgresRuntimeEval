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
from plot_config import (DPI, DEEP_BLUE, DEEP_GREEN, GROUPED_BAR_FIGSIZE,
    GROUPED_BAR_WIDTH, GROUPED_BAR_ALPHA, GROUPED_BAR_LABEL_FONTSIZE, LABEL_FONTSIZE,
    TICK_FONTSIZE, GRID_AXIS, GRID_ALPHA, GRID_LINESTYLE, apply_top_margin,
    DYNAMIC_MRE_Y_SCALE, DYNAMIC_MRE_Y_STEP, CAP_OVERFLOW_COLOR, CAP_LABEL_GAP_CM)

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def comparison_workflow(plan_csv: Path, operator_csv: Path, output_dir: Path) -> None:
    plan_stats = load_mre_stats(plan_csv, 'Plan')
    operator_stats = load_mre_stats(operator_csv, 'Operator')
    create_comparison_plot(plan_stats, operator_stats, output_dir)


# FUNCTIONS

# Load MRE statistics from CSV
def load_mre_stats(csv_path: Path, method: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';', index_col=0)
    df['method'] = method
    return df


# Create grouped bar plot comparing Plan vs Operator
def create_comparison_plot(plan_stats: pd.DataFrame, operator_stats: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=GROUPED_BAR_FIGSIZE)

    templates = [t for t in TEMPLATES if t in plan_stats.index and t in operator_stats.index]
    plan_values = np.array([plan_stats.loc[t, 'mean_mre_pct'] for t in templates])
    operator_values = np.array([operator_stats.loc[t, 'mean_mre_pct'] for t in templates])

    x = np.arange(len(templates))
    y_cap = DYNAMIC_MRE_Y_SCALE

    plan_overall = plan_values.mean()
    operator_overall = operator_values.mean()

    plan_capped = np.minimum(plan_values, y_cap)
    operator_capped = np.minimum(operator_values, y_cap)

    bars_plan = ax.bar(x - GROUPED_BAR_WIDTH/2, plan_capped, GROUPED_BAR_WIDTH,
                       label=f'Plan-Level (Overall: {plan_overall:.2f}%)',
                       color=DEEP_BLUE, alpha=GROUPED_BAR_ALPHA)
    bars_operator = ax.bar(x + GROUPED_BAR_WIDTH/2, operator_capped, GROUPED_BAR_WIDTH,
                           label=f'Operator-Level (Overall: {operator_overall:.2f}%)',
                           color=DEEP_GREEN, alpha=GROUPED_BAR_ALPHA)

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

    shifted_labels_operator = ['Q18']

    for bar, val in zip(bars_plan, plan_values):
        color = CAP_OVERFLOW_COLOR if val > y_cap else 'black'
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                f'{val:.1f}%', ha='center', va='bottom', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=color)
    for i, (bar, val) in enumerate(zip(bars_operator, operator_values)):
        color = CAP_OVERFLOW_COLOR if val > y_cap else 'black'
        template = templates[i]
        if template in shifted_labels_operator:
            ax.text(bar.get_x() + bar.get_width()/2., shifted_y,
                    f'{val:.1f}%', ha='center', va='top', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=color)
        else:
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                    f'{val:.1f}%', ha='center', va='bottom', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=color)
    plt.savefig(output_dir / 'A_02_comparison_plot.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan-csv", required=True, help="Path to Plan_Level/loto_mre.csv")
    parser.add_argument("--operator-csv", required=True, help="Path to Operator_Level/loto_mre.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(Path(args.plan_csv), Path(args.operator_csv), Path(args.output_dir))
