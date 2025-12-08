#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))  # Plan_Level_1
# From mapping_config.py: Target column name
from mapping_config import PLAN_TARGET


# ORCHESTRATOR

# Create scatter plots of FFS-selected features versus runtime
def scatter_plots_workflow(input_csv: Path, ffs_csv: Path, output_dir: Path) -> None:
    df = load_dataset(input_csv)
    feature_cols = load_ffs_features(ffs_csv)
    create_scatter_plot_grid(df, feature_cols, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(input_csv: Path) -> pd.DataFrame:
    return pd.read_csv(input_csv, delimiter=';')


# Load selected features from FFS summary CSV
def load_ffs_features(ffs_csv: Path, seed: int = 42) -> list:
    df = pd.read_csv(ffs_csv, delimiter=';')
    row = df[df['seed'] == seed].iloc[0]
    features_str = row['selected_features']
    return [f.strip() for f in features_str.split(',')]


# Create grid of scatter plots for all features
def create_scatter_plot_grid(df: pd.DataFrame, feature_cols: list, output_dir: Path) -> None:
    n_features = len(feature_cols)
    n_cols = 5
    n_rows = int(np.ceil(n_features / n_cols))

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(25, n_rows * 4))
    axes = axes.flatten()

    for idx, feature in enumerate(feature_cols):
        ax = axes[idx]

        x = df[feature]
        y = df[PLAN_TARGET]

        corr = x.corr(y)

        ax.scatter(x, y, alpha=0.5, s=10)
        ax.set_xlabel(feature)
        ax.set_ylabel('Runtime (ms)')
        ax.set_title(f'{feature}\nr = {corr:.3f}')
        ax.grid(True, alpha=0.3)

    for idx in range(n_features, len(axes)):
        axes[idx].set_visible(False)

    plt.tight_layout()

    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = output_dir / f'A_01b_scatter_plots_{timestamp}.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create scatter plots of FFS-selected features versus runtime")
    parser.add_argument("input_csv", help="Input CSV file with features and runtime")
    parser.add_argument("--ffs-csv", required=True, help="FFS summary CSV with selected_features")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: script_dir)")

    args = parser.parse_args()

    input_path = Path(args.input_csv)
    ffs_path = Path(args.ffs_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent

    scatter_plots_workflow(input_path, ffs_path, output_path)
