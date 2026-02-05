#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))  # Plan_Level_1
# From mapping_config.py: Target column name
from mapping_config import PLAN_TARGET

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import PRIMARY_COLOR, DPI, PLOTS_PER_PAGE, SUBPLOT_ROWS, SUBPLOT_COLS


# ORCHESTRATOR

# Create scatter plots of FFS-selected features versus runtime
def scatter_plots_workflow(input_csv: Path, ffs_csv: Path, output_dir: Path) -> None:
    df = load_dataset(input_csv)
    feature_cols = load_ffs_features(ffs_csv)
    figures = create_scatter_pages(df, feature_cols)
    save_plots(figures, output_dir)


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


# Create multiple pages of scatter plots (2x2 grid per page)
def create_scatter_pages(df: pd.DataFrame, feature_cols: list) -> list:
    figures = []

    for page_idx in range(0, len(feature_cols), PLOTS_PER_PAGE):
        page_features = feature_cols[page_idx:page_idx + PLOTS_PER_PAGE]
        fig = create_single_scatter_page(df, page_features)
        figures.append(fig)

    return figures


# Create single page with up to 4 scatter plots
def create_single_scatter_page(df: pd.DataFrame, features: list):
    fig, axes = plt.subplots(SUBPLOT_ROWS, SUBPLOT_COLS, figsize=(12, 10))
    axes = axes.flatten()

    for idx, feature in enumerate(features):
        ax = axes[idx]

        x = df[feature]
        y = df[PLAN_TARGET]

        ax.scatter(x, y, alpha=0.5, s=10, color=PRIMARY_COLOR)
        ax.set_xlabel(feature)
        ax.set_ylabel('Runtime (ms)')
        ax.ticklabel_format(style='plain', axis='x')
        ax.grid(True, alpha=0.3)

    for idx in range(len(features), len(axes)):
        axes[idx].set_visible(False)

    plt.tight_layout()

    return fig


# Save multiple plots to files
def save_plots(figures: list, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    for i, fig in enumerate(figures, start=1):
        output_path = output_dir / f'A_01b_scatter_plots_{i}.png'
        fig.savefig(output_path, dpi=DPI, bbox_inches='tight')
        plt.close(fig)


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
