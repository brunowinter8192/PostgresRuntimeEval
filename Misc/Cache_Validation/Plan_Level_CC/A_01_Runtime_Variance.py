#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

# From plot_config.py: Centralized plot styling constants
from plot_config import (
    DEEP_BLUE, LIGHT_BLUE, DPI, TITLE_FONTSIZE, LABEL_FONTSIZE, TICK_FONTSIZE,
    BAR_FIGSIZE, BAR_WIDTH, BAR_ALPHA, BAR_EDGECOLOR, BAR_LINEWIDTH, BAR_LABEL_FONTSIZE,
    GROUPED_BAR_FIGSIZE, GROUPED_BAR_WIDTH, GROUPED_BAR_ALPHA, GROUPED_BAR_EDGECOLOR,
    GROUPED_BAR_LINEWIDTH, GROUPED_BAR_LABEL_FONTSIZE,
    GRID_AXIS, GRID_ALPHA, GRID_LINESTYLE,
    CACHE_VALIDATION_CV_Y_SCALE, CACHE_VALIDATION_CV_Y_STEP, apply_top_margin,
)


# ORCHESTRATOR

# Analyze runtime variance per template for two datasets and compare
def variance_analysis_workflow(baseline_csv: Path, state1_csv: Path, output_dir: Path) -> None:
    df_baseline = load_dataset(baseline_csv)
    df_state1 = load_dataset(state1_csv)
    stats_baseline = calculate_variance_stats(df_baseline)
    stats_state1 = calculate_variance_stats(df_state1)
    comparison = create_comparison(stats_baseline, stats_state1)
    export_results(stats_baseline, stats_state1, comparison, output_dir)
    templates_sorted = sort_templates(stats_baseline['template'].tolist())
    plot_cv(stats_baseline, templates_sorted, 'Baseline', DEEP_BLUE, output_dir / 'A_01_cv_baseline.png')
    plot_cv(stats_state1, templates_sorted, 'State_1', LIGHT_BLUE, output_dir / 'A_01_cv_state1.png')
    plot_cv_comparison(stats_baseline, stats_state1, templates_sorted, output_dir / 'A_01_cv_comparison.png')


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Calculate variance statistics per template
def calculate_variance_stats(df: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby('template')['runtime']

    stats = pd.DataFrame({
        'count': grouped.count(),
        'mean': grouped.mean(),
        'std': grouped.std(),
        'min': grouped.min(),
        'max': grouped.max()
    })

    stats['cv'] = (stats['std'] / stats['mean']) * 100
    stats['range'] = stats['max'] - stats['min']

    return stats.reset_index()


# Create side-by-side comparison with delta columns
def create_comparison(stats_baseline: pd.DataFrame, stats_state1: pd.DataFrame) -> pd.DataFrame:
    comparison = stats_baseline.merge(
        stats_state1,
        on='template',
        suffixes=('_baseline', '_state1')
    )

    comparison['mean_delta'] = abs(comparison['mean_state1'] - comparison['mean_baseline'])
    comparison['cv_delta'] = abs(comparison['cv_state1'] - comparison['cv_baseline'])

    return comparison


# Export all three result CSVs
def export_results(
    stats_baseline: pd.DataFrame,
    stats_state1: pd.DataFrame,
    comparison: pd.DataFrame,
    output_dir: Path
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    stats_baseline.to_csv(output_dir / 'A_01_baseline_variance.csv', sep=';', index=False)
    stats_state1.to_csv(output_dir / 'A_01_state1_variance.csv', sep=';', index=False)
    comparison.to_csv(output_dir / 'A_01_comparison.csv', sep=';', index=False)


# Sort templates by numeric value (Q1, Q2, ... Q10, Q11)
def sort_templates(templates: list) -> list:
    return sorted(templates, key=lambda x: int(x[1:]))


# Plot CV values for a single dataset
def plot_cv(stats: pd.DataFrame, templates_sorted: list, label: str, color: str, output_path: Path) -> None:
    stats_sorted = stats.set_index('template').loc[templates_sorted].reset_index()

    fig, ax = plt.subplots(figsize=BAR_FIGSIZE)

    x = range(len(templates_sorted))
    ax.bar(x, stats_sorted['cv'], width=BAR_WIDTH,
           color=color, alpha=BAR_ALPHA, edgecolor=BAR_EDGECOLOR, linewidth=BAR_LINEWIDTH)

    ax.set_xlabel('Template', fontsize=LABEL_FONTSIZE)
    ax.set_ylabel('CV (%)', fontsize=LABEL_FONTSIZE)
    ax.set_title(f'Coefficient of Variation - {label}', fontsize=TITLE_FONTSIZE, pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(templates_sorted, rotation=0, fontsize=TICK_FONTSIZE)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.0f}%'))
    ax.grid(axis=GRID_AXIS, alpha=GRID_ALPHA, linestyle=GRID_LINESTYLE)

    apply_top_margin(ax, fig, CACHE_VALIDATION_CV_Y_SCALE, CACHE_VALIDATION_CV_Y_STEP)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)


# Plot CV comparison for both datasets
def plot_cv_comparison(stats_baseline: pd.DataFrame, stats_state1: pd.DataFrame, templates_sorted: list, output_path: Path) -> None:
    baseline_sorted = stats_baseline.set_index('template').loc[templates_sorted].reset_index()
    state1_sorted = stats_state1.set_index('template').loc[templates_sorted].reset_index()

    fig, ax = plt.subplots(figsize=GROUPED_BAR_FIGSIZE)

    x = range(len(templates_sorted))

    ax.bar([i - GROUPED_BAR_WIDTH/2 for i in x], baseline_sorted['cv'], GROUPED_BAR_WIDTH, label='Baseline',
           color=DEEP_BLUE, alpha=GROUPED_BAR_ALPHA, edgecolor=GROUPED_BAR_EDGECOLOR, linewidth=GROUPED_BAR_LINEWIDTH)
    ax.bar([i + GROUPED_BAR_WIDTH/2 for i in x], state1_sorted['cv'], GROUPED_BAR_WIDTH, label='State_1',
           color=LIGHT_BLUE, alpha=GROUPED_BAR_ALPHA, edgecolor=GROUPED_BAR_EDGECOLOR, linewidth=GROUPED_BAR_LINEWIDTH)

    for container in ax.containers:
        for bar in container:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
                    f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=GROUPED_BAR_LABEL_FONTSIZE, rotation=0)

    ax.set_xlabel('Template', fontsize=LABEL_FONTSIZE)
    ax.set_ylabel('CV (%)', fontsize=LABEL_FONTSIZE)
    ax.set_xticks(x)
    ax.set_xticklabels(templates_sorted, rotation=0, fontsize=TICK_FONTSIZE)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.0f}%'))
    ax.legend(fontsize=TICK_FONTSIZE, loc='upper left')
    ax.grid(axis=GRID_AXIS, alpha=GRID_ALPHA, linestyle=GRID_LINESTYLE)

    apply_top_margin(ax, fig, CACHE_VALIDATION_CV_Y_SCALE, CACHE_VALIDATION_CV_Y_STEP)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze runtime variance per template")
    parser.add_argument("baseline_csv", help="Baseline dataset CSV")
    parser.add_argument("state1_csv", help="State_1 dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for CSVs")

    args = parser.parse_args()

    variance_analysis_workflow(
        Path(args.baseline_csv),
        Path(args.state1_csv),
        Path(args.output_dir)
    )
