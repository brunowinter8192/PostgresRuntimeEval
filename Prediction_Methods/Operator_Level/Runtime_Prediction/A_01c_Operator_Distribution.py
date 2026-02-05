#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
from plot_config import PRIMARY_COLOR, DPI

OPERATOR_ORDER = [
    'Seq Scan', 'Index Scan', 'Index Only Scan',
    'Hash', 'Hash Join', 'Merge Join', 'Nested Loop',
    'Sort', 'Incremental Sort', 'Aggregate',
    'Gather', 'Gather Merge', 'Limit'
]


# ORCHESTRATOR

def operator_distribution_workflow(dataset_csv, output_dir, selected_operators=None):
    df = load_dataset(dataset_csv)
    create_histogram_plot(df, 'actual_startup_time', 'startup_time', output_dir, selected_operators)
    create_histogram_plot(df, 'actual_total_time', 'total_time', output_dir, selected_operators)


# FUNCTIONS

# Load operator dataset from CSV file
def load_dataset(dataset_csv):
    return pd.read_csv(dataset_csv, delimiter=';')


# Create histogram plot with subplots for operators
def create_histogram_plot(df, column, name, output_dir, selected_operators=None):
    if selected_operators:
        operators = [op for op in OPERATOR_ORDER if op in selected_operators]
        rows, cols = 2, 2
        figsize = (12, 10)
    else:
        operators = OPERATOR_ORDER
        rows, cols = 4, 4
        figsize = (16, 14)

    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    axes = axes.flatten()

    for idx, operator in enumerate(operators):
        ax = axes[idx]
        op_data = df[df['node_type'] == operator][column].dropna()

        if len(op_data) == 0:
            ax.set_title(f'{operator}\n(no data)', fontsize=9)
            ax.set_xticks([])
            ax.set_yticks([])
            continue

        ax.hist(op_data, bins=50, color=PRIMARY_COLOR, edgecolor='black', alpha=0.7)
        ax.set_title(f'{operator} (n={len(op_data)})', fontsize=9)
        ax.set_xlabel('ms', fontsize=8)
        ax.set_ylabel('count', fontsize=8)
        ax.tick_params(axis='both', labelsize=7)

    for idx in range(len(operators), len(axes)):
        axes[idx].set_visible(False)

    plt.tight_layout()

    output_path = Path(output_dir) / 'Evaluation'
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / f'A_01c_histogram_{name}.png'
    plt.savefig(output_file, dpi=DPI)
    plt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_csv", help="Path to operator dataset CSV file")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    parser.add_argument("--operators", default=None, help="Comma-separated list of operators (e.g., 'Seq Scan,Hash,Limit,Aggregate')")
    args = parser.parse_args()

    selected = [op.strip() for op in args.operators.split(',')] if args.operators else None
    operator_distribution_workflow(args.dataset_csv, args.output_dir, selected)
