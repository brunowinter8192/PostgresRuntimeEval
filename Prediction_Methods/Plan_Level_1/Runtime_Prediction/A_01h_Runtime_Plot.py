#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Metadata column names
from mapping_config import PLAN_METADATA

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import PRIMARY_COLOR, DPI, BAR_FIGSIZE, BAR_WIDTH, BAR_ALPHA, BAR_EDGECOLOR, BAR_LINEWIDTH, BAR_LABEL_FONTSIZE, GRID_AXIS, GRID_ALPHA, GRID_LINESTYLE, apply_top_margin, PLAN_LEVEL_RUNTIME_Y_SCALE, PLAN_LEVEL_RUNTIME_Y_STEP


# ORCHESTRATOR

# Create and save mean runtime plot from template summary
def create_plot_workflow(template_summary_csv: Path, output_dir: Path) -> None:
    df = load_template_summary(template_summary_csv)
    runtime_stats = sort_by_runtime(df)
    fig = create_runtime_plot(runtime_stats)
    save_plot(fig, output_dir)


# FUNCTIONS

# Load template summary from CSV with semicolon delimiter
def load_template_summary(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Sort templates by mean actual runtime ascending
def sort_by_runtime(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values('mean_actual_ms')


# Create mean runtime bar plot by template
def create_runtime_plot(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=BAR_FIGSIZE)

    templates = df[PLAN_METADATA[1]].tolist()
    mean_runtime_ms = df['mean_actual_ms'].values

    x = np.arange(len(templates))

    bars = ax.bar(x, mean_runtime_ms, BAR_WIDTH, label='Mean Runtime',
                   color=PRIMARY_COLOR, alpha=BAR_ALPHA, edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH)

    ax.set_xlabel('Template', fontsize=13)
    ax.set_ylabel('Mean Runtime (ms)', fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels([f'Q{t}' for t in templates], rotation=0, fontsize=11)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(axis=GRID_AXIS, alpha=GRID_ALPHA, linestyle=GRID_LINESTYLE)

    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.0f} ms',
                ha='center', va='bottom', fontsize=BAR_LABEL_FONTSIZE)

    plt.tight_layout()
    apply_top_margin(ax, fig, PLAN_LEVEL_RUNTIME_Y_SCALE, PLAN_LEVEL_RUNTIME_Y_STEP)

    return fig


# Save plot to file
def save_plot(fig, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_file = output_dir / 'A_01h_template_runtime_plot.png'
    fig.savefig(plot_file, dpi=DPI, bbox_inches='tight')
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create mean runtime plot from template summary")
    parser.add_argument("template_summary_csv", help="Template summary CSV file from summarize results script")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: script_dir/Evaluation)")

    args = parser.parse_args()

    dataset_path = Path(args.template_summary_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'Evaluation'

    create_plot_workflow(dataset_path, output_path)
