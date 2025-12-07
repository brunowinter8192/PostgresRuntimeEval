#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

OPERATOR_ORDER = [
    'Seq Scan', 'Index Scan', 'Index Only Scan',
    'Hash', 'Hash Join', 'Merge Join', 'Nested Loop',
    'Sort', 'Incremental Sort', 'Aggregate',
    'Gather', 'Gather Merge', 'Limit'
]


# ORCHESTRATOR

def operator_distribution_workflow(predictions_csv, output_dir):
    df = load_predictions(predictions_csv)
    create_histogram_plot(df, 'actual_startup_time', 'startup_time', output_dir)
    create_histogram_plot(df, 'actual_total_time', 'total_time', output_dir)


# FUNCTIONS

# Load predictions from CSV file
def load_predictions(predictions_csv):
    return pd.read_csv(predictions_csv, delimiter=';')


# Create histogram plot with 13 subplots for all operators
def create_histogram_plot(df, column, name, output_dir):
    fig, axes = plt.subplots(4, 4, figsize=(16, 14))
    axes = axes.flatten()

    for idx, operator in enumerate(OPERATOR_ORDER):
        ax = axes[idx]
        op_data = df[df['node_type'] == operator][column].dropna()

        if len(op_data) == 0:
            ax.set_title(f'{operator}\n(no data)', fontsize=9)
            ax.set_xticks([])
            ax.set_yticks([])
            continue

        ax.hist(op_data, bins=50, edgecolor='black', alpha=0.7)
        ax.set_title(f'{operator} (n={len(op_data)})', fontsize=9)
        ax.set_xlabel('ms', fontsize=8)
        ax.set_ylabel('count', fontsize=8)
        ax.tick_params(axis='both', labelsize=7)

    for idx in range(len(OPERATOR_ORDER), len(axes)):
        axes[idx].set_visible(False)

    fig.suptitle(f'Operator {name.replace("_", " ").title()} Distribution (Histogram)', fontsize=12)
    plt.tight_layout()

    output_path = Path(output_dir) / 'Evaluation'
    output_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = output_path / f'A_01c_histogram_{name}_{timestamp}.png'
    plt.savefig(output_file, dpi=150)
    plt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions_csv", help="Path to predictions CSV file")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    operator_distribution_workflow(args.predictions_csv, args.output_dir)
