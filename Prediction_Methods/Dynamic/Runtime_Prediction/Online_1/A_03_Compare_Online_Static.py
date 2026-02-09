#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import (DPI, DEEP_CYAN, LIGHT_CYAN, GROUPED_BAR_FIGSIZE,
    GROUPED_BAR_WIDTH, GROUPED_BAR_ALPHA, GROUPED_BAR_LABEL_FONTSIZE, LABEL_FONTSIZE,
    TICK_FONTSIZE, GRID_AXIS, GRID_ALPHA, GRID_LINESTYLE, apply_top_margin,
    DYNAMIC_MRE_Y_SCALE, DYNAMIC_MRE_Y_STEP, CAP_OVERFLOW_COLOR, CAP_LABEL_GAP_CM)

# ORCHESTRATOR
def compare_workflow(online_csv: str, static_csv: str, output_dir: str) -> None:
    online_df = load_mre_data(online_csv, "Dynamic")
    static_df = load_mre_data(static_csv, "Static")
    combined = merge_data(online_df, static_df)
    create_comparison_plot(combined, output_dir)

# FUNCTIONS

# Load MRE data and add method label
def load_mre_data(csv_path: str, method: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    df['method'] = method
    return df[['template', 'mean_mre_pct', 'method']]

# Merge online and static dataframes
def merge_data(online_df: pd.DataFrame, static_df: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([online_df, static_df], ignore_index=True)

# Create grouped bar plot comparing methods
def create_comparison_plot(df: pd.DataFrame, output_dir: str) -> None:
    fig, ax = plt.subplots(figsize=GROUPED_BAR_FIGSIZE)

    templates = sorted(df['template'].unique(), key=lambda x: int(x[1:]))

    static_data = df[df['method'] == 'Static']
    online_data = df[df['method'] == 'Dynamic']

    static_values = np.array([static_data[static_data['template'] == t]['mean_mre_pct'].values[0] for t in templates])
    online_values = np.array([online_data[online_data['template'] == t]['mean_mre_pct'].values[0] for t in templates])

    x = np.arange(len(templates))

    y_cap = DYNAMIC_MRE_Y_SCALE
    static_overall = static_values.mean()
    online_overall = online_values.mean()

    static_capped = np.minimum(static_values, y_cap)
    online_capped = np.minimum(online_values, y_cap)

    bars_static = ax.bar(x - GROUPED_BAR_WIDTH/2, static_capped, GROUPED_BAR_WIDTH,
                         label=f'Static (Overall: {static_overall:.2f}%)',
                         color=LIGHT_CYAN, alpha=GROUPED_BAR_ALPHA)
    bars_online = ax.bar(x + GROUPED_BAR_WIDTH/2, online_capped, GROUPED_BAR_WIDTH,
                         label=f'Dynamic (Overall: {online_overall:.2f}%)',
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

    shifted_labels_dynamic = ['Q18']

    for bar, val in zip(bars_static, static_values):
        color = CAP_OVERFLOW_COLOR if val > y_cap else 'black'
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                f'{val:.1f}%', ha='center', va='bottom', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=color)
    for i, (bar, val) in enumerate(zip(bars_online, online_values)):
        color = CAP_OVERFLOW_COLOR if val > y_cap else 'black'
        template = templates[i]
        if template in shifted_labels_dynamic:
            ax.text(bar.get_x() + bar.get_width()/2., shifted_y,
                    f'{val:.1f}%', ha='center', va='top', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=color)
        else:
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                    f'{val:.1f}%', ha='center', va='bottom', fontsize=GROUPED_BAR_LABEL_FONTSIZE, color=color)

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    plt.savefig(f'{output_dir}/compare_online_static.png', dpi=DPI, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("online_csv", help="Path to Dynamic_1 MRE CSV")
    parser.add_argument("static_csv", help="Path to Hybrid_2 Static MRE CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    compare_workflow(args.online_csv, args.static_csv, args.output_dir)
