#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ORCHESTRATOR

def compare_workflow(evaluation_dir: str, title: str) -> None:
    eval_path = Path(evaluation_dir)
    template_folders = sorted([d for d in eval_path.iterdir() if d.is_dir()])

    all_metrics = collect_all_metrics(template_folders)
    comparison_df = create_comparison_table(all_metrics)
    export_comparison(comparison_df, eval_path)
    create_comparison_plot(comparison_df, eval_path, title)


# FUNCTIONS

# Collect metrics from all template folders
def collect_all_metrics(template_folders: list) -> list:
    all_metrics = []

    for template_folder in template_folders:
        metrics_file = template_folder / 'metrics.csv'

        if not metrics_file.exists():
            continue

        metrics = pd.read_csv(metrics_file, delimiter=';').iloc[0].to_dict()
        metrics['template'] = template_folder.name
        all_metrics.append(metrics)

    return all_metrics


# Create comparison table from collected metrics
def create_comparison_table(all_metrics: list) -> pd.DataFrame:
    df = pd.DataFrame(all_metrics)
    df = df.set_index('template')
    df = df.sort_index()
    return df


# Export comparison table to CSV
def export_comparison(comparison_df: pd.DataFrame, output_path: Path) -> None:
    comparison_df.to_csv(output_path / 'comparison.csv', sep=';')


# Create comparison bar plot
def create_comparison_plot(comparison_df: pd.DataFrame, output_path: Path, title: str) -> None:
    fig, ax = plt.subplots(figsize=(16, 8))

    templates = comparison_df.index.tolist()
    mean_mre_values = comparison_df['mean_mre_pct'].values

    x = np.arange(len(templates))
    width = 0.5

    bars = ax.bar(x, mean_mre_values, width, label='Mean MRE',
                  color='steelblue', alpha=0.8, edgecolor='black', linewidth=0.8)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_title(f'{title}: Query-Level MRE by Template',
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(templates, rotation=0, fontsize=11)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    fig.savefig(output_path / 'comparison_plot.png', dpi=300, bbox_inches='tight')
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("evaluation_dir", help="Path to Evaluation/ containing template folders")
    parser.add_argument("--title", default="LOTO Prediction", help="Plot title prefix")

    args = parser.parse_args()

    compare_workflow(args.evaluation_dir, args.title)
