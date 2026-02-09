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
from plot_config import (DPI, DEEP_GREEN, LIGHT_GREEN, DEEP_RED, GROUPED_BAR_FIGSIZE,
    GROUPED_BAR_WIDTH, GROUPED_BAR_ALPHA, GROUPED_BAR_LABEL_FONTSIZE, LABEL_FONTSIZE,
    TICK_FONTSIZE, GRID_AXIS, GRID_ALPHA, GRID_LINESTYLE, apply_top_margin,
    DYNAMIC_MRE_Y_SCALE, DYNAMIC_MRE_Y_STEP, CAP_OVERFLOW_COLOR, CAP_LABEL_GAP_CM)

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']

SCRIPT_DIR = Path(__file__).resolve().parent


# ORCHESTRATOR
def comparison_workflow(static_csv: str, output_dir: str) -> None:
    static_data = load_static_data(static_csv)
    dynamic_data = load_dynamic_data()
    combined_df = merge_data(static_data, dynamic_data)
    export_csv(combined_df, output_dir)
    create_comparison_plot(combined_df, output_dir)


# FUNCTIONS

# Load static template summary (already in Qx format with mean_mre_pct)
def load_static_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    df = df.rename(columns={'mean_mre_pct': 'static_mre_pct'})
    return df[['template', 'static_mre_pct']]


# Load dynamic LOTO MRE data
def load_dynamic_data() -> pd.DataFrame:
    dynamic_file = SCRIPT_DIR / 'Evaluation' / 'loto_mre.csv'
    df = pd.read_csv(dynamic_file, delimiter=';')
    df = df.rename(columns={'loto_template': 'template', 'mean_mre_pct': 'dynamic_mre_pct'})
    return df[['template', 'dynamic_mre_pct']]


# Merge static and dynamic data on common templates
def merge_data(static_data: pd.DataFrame, dynamic_data: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(static_data, dynamic_data, on='template', how='inner')
    template_order = {t: i for i, t in enumerate(TEMPLATES)}
    merged['order'] = merged['template'].map(template_order)
    merged = merged.sort_values('order').drop(columns=['order'])
    return merged


# Export combined CSV
def export_csv(df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path / 'A_01b_static_dynamic_comparison.csv', sep=';', index=False)


# Create grouped bar plot comparing static vs dynamic
def create_comparison_plot(df: pd.DataFrame, output_dir: str) -> None:
    fig, ax = plt.subplots(figsize=GROUPED_BAR_FIGSIZE)

    templates = df['template'].tolist()
    static_values = df['static_mre_pct'].values
    dynamic_values = df['dynamic_mre_pct'].values

    x = np.arange(len(templates))

    y_cap = DYNAMIC_MRE_Y_SCALE
    static_overall = static_values.mean()
    dynamic_overall = dynamic_values.mean()

    static_capped = np.minimum(static_values, y_cap)
    dynamic_capped = np.minimum(dynamic_values, y_cap)

    bars_static = ax.bar(x - GROUPED_BAR_WIDTH/2, static_capped, GROUPED_BAR_WIDTH,
                         label=f'Static (Overall: {static_overall:.2f}%)',
                         color=LIGHT_GREEN, alpha=GROUPED_BAR_ALPHA)
    bars_dynamic = ax.bar(x + GROUPED_BAR_WIDTH/2, dynamic_capped, GROUPED_BAR_WIDTH,
                          label=f'Dynamic (Overall: {dynamic_overall:.2f}%)',
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

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path / 'A_01b_static_dynamic_comparison.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--static-csv", required=True, help="Path to static template summary CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")

    args = parser.parse_args()

    comparison_workflow(args.static_csv, args.output_dir)
