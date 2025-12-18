#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ORCHESTRATOR

# Create and save mean runtime plot from dataset
def create_plot_workflow(dataset_csv: Path, output_dir: Path) -> None:
    df = load_dataset(dataset_csv)
    runtime_stats = calculate_template_runtimes(df)
    fig = create_runtime_plot(runtime_stats)
    save_plot(fig, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Calculate mean runtime per template, sorted ascending
def calculate_template_runtimes(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('template')['runtime'].mean().reset_index().sort_values('runtime')


# Create mean runtime bar plot by template
def create_runtime_plot(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(16, 8))

    templates = df['template'].tolist()
    mean_runtime_ms = df['runtime'].values

    x = np.arange(len(templates))
    width = 0.5

    bars = ax.bar(x, mean_runtime_ms, width, label='Mean Runtime',
                   color='steelblue', alpha=0.8, edgecolor='black', linewidth=0.8)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Runtime (ms)', fontsize=13, fontweight='bold')
    ax.set_title('Mean Query Runtime by Template',
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(templates, rotation=0, fontsize=11)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.0f}',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()

    return fig


# Save plot to file
def save_plot(fig, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_file = output_dir / 'A_01h_template_runtime_plot.png'
    fig.savefig(plot_file, dpi=300, bbox_inches='tight')
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create mean runtime plot from dataset")
    parser.add_argument("dataset_csv", help="Complete dataset CSV file")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: script_dir/Evaluation)")

    args = parser.parse_args()

    dataset_path = Path(args.dataset_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'Evaluation'

    create_plot_workflow(dataset_path, output_path)
