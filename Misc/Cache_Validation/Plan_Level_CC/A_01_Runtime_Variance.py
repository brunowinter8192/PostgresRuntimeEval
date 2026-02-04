#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd


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
    plot_cv(stats_baseline, templates_sorted, 'Baseline', output_dir / 'A_01_cv_baseline.png')
    plot_cv(stats_state1, templates_sorted, 'State_1', output_dir / 'A_01_cv_state1.png')
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
def plot_cv(stats: pd.DataFrame, templates_sorted: list, label: str, output_path: Path) -> None:
    stats_sorted = stats.set_index('template').loc[templates_sorted].reset_index()

    fig, ax = plt.subplots(figsize=(16, 8))

    x = range(len(templates_sorted))
    bars = ax.bar(x, stats_sorted['cv'], width=0.5,
                  color='steelblue', alpha=0.8, edgecolor='black', linewidth=0.8)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('CV (%)', fontsize=13, fontweight='bold')
    ax.set_title(f'Coefficient of Variation - {label}', fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(templates_sorted, rotation=0, fontsize=11)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.0f}%'))
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)


# Plot CV comparison for both datasets
def plot_cv_comparison(stats_baseline: pd.DataFrame, stats_state1: pd.DataFrame, templates_sorted: list, output_path: Path) -> None:
    baseline_sorted = stats_baseline.set_index('template').loc[templates_sorted].reset_index()
    state1_sorted = stats_state1.set_index('template').loc[templates_sorted].reset_index()

    fig, ax = plt.subplots(figsize=(16, 8))

    x = range(len(templates_sorted))
    width = 0.35

    bars1 = ax.bar([i - width/2 for i in x], baseline_sorted['cv'], width, label='Baseline',
                   color='steelblue', alpha=0.8, edgecolor='black', linewidth=0.8)
    bars2 = ax.bar([i + width/2 for i in x], state1_sorted['cv'], width, label='State_1',
                   color='coral', alpha=0.8, edgecolor='black', linewidth=0.8)

    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
                f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=7, rotation=0)
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
                f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=7, rotation=0)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('CV (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates_sorted, rotation=0, fontsize=11)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.0f}%'))
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
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
