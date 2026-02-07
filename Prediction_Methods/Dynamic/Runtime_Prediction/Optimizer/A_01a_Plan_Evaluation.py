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
from plot_config import DPI, DEEP_BLUE

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def plan_evaluation_workflow(predictions_dir: Path, output_dir: Path) -> None:
    all_predictions = load_all_predictions(predictions_dir)
    mre_stats = calculate_mre_stats(all_predictions)
    export_results(mre_stats, output_dir)
    create_plot(mre_stats, output_dir)


# FUNCTIONS

# Load all predictions from template folders
def load_all_predictions(predictions_dir: Path) -> pd.DataFrame:
    dfs = []
    for template in TEMPLATES:
        csv_path = predictions_dir / template / 'predictions.csv'
        if csv_path.exists():
            df = pd.read_csv(csv_path, delimiter=';')
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)


# Calculate MRE statistics per template
def calculate_mre_stats(df: pd.DataFrame) -> pd.DataFrame:
    df['mre'] = np.abs(df['predicted_runtime'] - df['actual_runtime']) / df['actual_runtime']

    stats = df.groupby('template').agg({
        'mre': ['mean', 'std', 'count']
    }).round(4)
    stats.columns = ['mean_mre', 'std_mre', 'query_count']
    stats['mean_mre_pct'] = stats['mean_mre'] * 100
    stats = stats.reindex(sorted(stats.index, key=lambda x: int(x[1:])))
    stats['overall_mre'] = df['mre'].mean()
    return stats


# Export results to CSV
def export_results(stats: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    stats.to_csv(output_dir / 'loto_mre.csv', sep=';')


# Create bar plot
def create_plot(stats: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(14, 7))

    templates = stats.index.tolist()
    values = stats['mean_mre_pct'].values
    overall = stats['overall_mre'].iloc[0] * 100

    x = np.arange(len(templates))
    bars = ax.bar(x, values, color=DEEP_BLUE, alpha=0.85,
                  label=f'Plan-Level Optimizer (Overall: {overall:.2f}%)')

    ax.bar_label(bars, fmt='%.1f%%', padding=3, fontsize=8)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    ax.set_ylim(0, values.max() * 1.25)

    plt.tight_layout()
    plt.savefig(output_dir / 'A_01a_plan_mre_plot.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions-dir", required=True, help="Directory with template predictions")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    plan_evaluation_workflow(Path(args.predictions_dir), Path(args.output_dir))
