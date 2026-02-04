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

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import PRIMARY_COLOR, DPI


# ORCHESTRATOR

# Create and save MRE plot from template summary
def create_plot_workflow(template_summary_csv: Path, output_dir: Path) -> None:
    df = load_template_summary(template_summary_csv)
    fig = create_mre_plot(df)
    save_plot(fig, output_dir)


# FUNCTIONS

# Load template summary from CSV with semicolon delimiter
def load_template_summary(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Create MRE bar plot by template
def create_mre_plot(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(16, 8))

    templates = df[PLAN_METADATA[1]].tolist()
    mean_mre_pct = df['mre'].values * 100
    x = np.arange(len(templates))
    width = 0.5

    bars = ax.bar(x, mean_mre_pct, width, label='Mean MRE',
                   color=PRIMARY_COLOR, alpha=0.8, edgecolor='black', linewidth=0.8)

    ax.set_xlabel('Template', fontsize=13)
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels([f'Q{t}' for t in templates], rotation=0, fontsize=11)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim(0, max(mean_mre_pct) * 1.1)

    for i, bar in enumerate(bars):
        actual_value = mean_mre_pct[i]
        display_height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., display_height,
                f'{actual_value:.1f}%',
                ha='center', va='bottom', fontsize=9)

    plt.tight_layout()

    return fig


# Save plot to file
def save_plot(fig, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_file = output_dir / 'A_01g_template_mre_plot.png'
    fig.savefig(plot_file, dpi=DPI, bbox_inches='tight')
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create MRE plot from template summary")
    parser.add_argument("template_summary_csv", help="Template summary CSV file from summarize results script")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: script_dir/Evaluation)")

    args = parser.parse_args()

    template_path = Path(args.template_summary_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'Evaluation'

    create_plot_workflow(template_path, output_path)
