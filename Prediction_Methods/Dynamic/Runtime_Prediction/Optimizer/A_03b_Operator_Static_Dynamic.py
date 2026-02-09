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
from plot_config import (DPI, DEEP_GRAY, LIGHT_GRAY, GROUPED_BAR_FIGSIZE,
    GROUPED_BAR_WIDTH, GROUPED_BAR_ALPHA, GROUPED_BAR_LABEL_FONTSIZE, LABEL_FONTSIZE,
    TICK_FONTSIZE, GRID_AXIS, GRID_ALPHA, GRID_LINESTYLE, apply_top_margin,
    DYNAMIC_MRE_Y_SCALE, DYNAMIC_MRE_Y_STEP, CAP_OVERFLOW_COLOR, CAP_LABEL_GAP_CM)

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def comparison_workflow(static_csv: Path, dynamic_csv: Path, output_dir: Path) -> None:
    static_df = load_static_data(static_csv)
    dynamic_df = load_dynamic_data(dynamic_csv)
    create_comparison_plot(static_df, dynamic_df, output_dir)


# FUNCTIONS

# Load static optimizer results
def load_static_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    df = df[df['template'].isin(TEMPLATES)]
    return df.set_index('template')


# Load dynamic optimizer results
def load_dynamic_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    return df.set_index('template')


# Create grouped bar plot
def create_comparison_plot(static_df: pd.DataFrame, dynamic_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=GROUPED_BAR_FIGSIZE)

    templates = [t for t in TEMPLATES if t in static_df.index and t in dynamic_df.index]
    static_values = np.array([static_df.loc[t, 'mre_optimizer_pct'] for t in templates])
    dynamic_values = np.array([dynamic_df.loc[t, 'mean_mre_pct'] for t in templates])

    x = np.arange(len(templates))
    y_cap = DYNAMIC_MRE_Y_SCALE

    static_overall = static_values.mean()
    dynamic_overall = dynamic_values.mean()

    static_capped = np.minimum(static_values, y_cap)
    dynamic_capped = np.minimum(dynamic_values, y_cap)

    bars_static = ax.bar(x - GROUPED_BAR_WIDTH/2, static_capped, GROUPED_BAR_WIDTH,
                         label=f'Static (Overall: {static_overall:.2f}%)',
                         color=LIGHT_GRAY, alpha=GROUPED_BAR_ALPHA)
    bars_dynamic = ax.bar(x + GROUPED_BAR_WIDTH/2, dynamic_capped, GROUPED_BAR_WIDTH,
                          label=f'Dynamic (Overall: {dynamic_overall:.2f}%)',
                          color=DEEP_GRAY, alpha=GROUPED_BAR_ALPHA)

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

    shifted_labels_dynamic = ['Q18']

    for bar, val in zip(bars_static, static_values):
        color = CAP_OVERFLOW_COLOR if val > y_cap else 'black'
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                f'{val:.1f}%', ha='center', va='bottom', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=color)
    for i, (bar, val) in enumerate(zip(bars_dynamic, dynamic_values)):
        color = CAP_OVERFLOW_COLOR if val > y_cap else 'black'
        template = templates[i]
        if template in shifted_labels_dynamic:
            ax.text(bar.get_x() + bar.get_width()/2., shifted_y,
                    f'{val:.1f}%', ha='center', va='top', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=color)
        else:
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                    f'{val:.1f}%', ha='center', va='bottom', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=color)
    plt.savefig(output_dir / 'A_03b_operator_static_dynamic.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--static-csv", required=True, help="Path to static optimizer template CSV")
    parser.add_argument("--dynamic-csv", required=True, help="Path to dynamic optimizer loto_mre CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(Path(args.static_csv), Path(args.dynamic_csv), Path(args.output_dir))
