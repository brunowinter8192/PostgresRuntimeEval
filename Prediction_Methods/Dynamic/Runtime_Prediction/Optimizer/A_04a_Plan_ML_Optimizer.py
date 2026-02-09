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
from plot_config import (DPI, DEEP_GRAY, DEEP_GREEN, GROUPED_BAR_FIGSIZE,
    GROUPED_BAR_WIDTH, GROUPED_BAR_ALPHA, GROUPED_BAR_LABEL_FONTSIZE, LABEL_FONTSIZE,
    TICK_FONTSIZE, GRID_AXIS, GRID_ALPHA, GRID_LINESTYLE, apply_top_margin,
    DYNAMIC_MRE_Y_SCALE, DYNAMIC_MRE_Y_STEP)

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def comparison_workflow(optimizer_csv: Path, ml_csv: Path, output_dir: Path) -> None:
    optimizer_df = load_optimizer_data(optimizer_csv)
    ml_df = load_ml_data(ml_csv)
    create_comparison_plot(optimizer_df, ml_df, output_dir)


# FUNCTIONS

# Load optimizer results
def load_optimizer_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    return df.set_index('template')


# Load ML results (normalize column name)
def load_ml_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    if 'loto_template' in df.columns:
        df = df.rename(columns={'loto_template': 'template'})
    return df.set_index('template')


# Create grouped bar plot
def create_comparison_plot(optimizer_df: pd.DataFrame, ml_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=GROUPED_BAR_FIGSIZE)

    templates = [t for t in TEMPLATES if t in optimizer_df.index and t in ml_df.index]
    optimizer_values = np.array([optimizer_df.loc[t, 'mean_mre_pct'] for t in templates])
    ml_values = np.array([ml_df.loc[t, 'mean_mre_pct'] for t in templates])

    x = np.arange(len(templates))

    optimizer_overall = optimizer_values.mean()
    ml_overall = ml_values.mean()

    bars_optimizer = ax.bar(x - GROUPED_BAR_WIDTH/2, optimizer_values, GROUPED_BAR_WIDTH,
                            label=f'Optimizer (Overall: {optimizer_overall:.2f}%)',
                            color=DEEP_GRAY, alpha=GROUPED_BAR_ALPHA)
    bars_ml = ax.bar(x + GROUPED_BAR_WIDTH/2, ml_values, GROUPED_BAR_WIDTH,
                     label=f'Plan Level (Overall: {ml_overall:.2f}%)',
                     color=DEEP_GREEN, alpha=GROUPED_BAR_ALPHA)

    ax.bar_label(bars_optimizer, fmt='%.1f%%', padding=2, fontsize=GROUPED_BAR_LABEL_FONTSIZE, rotation=0)
    ax.bar_label(bars_ml, fmt='%.1f%%', padding=2, fontsize=GROUPED_BAR_LABEL_FONTSIZE, rotation=0)

    ax.set_xlabel('Template', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=TICK_FONTSIZE)
    ax.legend(fontsize=TICK_FONTSIZE, loc='upper right')
    ax.grid(axis=GRID_AXIS, alpha=GRID_ALPHA, linestyle=GRID_LINESTYLE)

    plt.tight_layout()
    apply_top_margin(ax, fig, DYNAMIC_MRE_Y_SCALE, DYNAMIC_MRE_Y_STEP)
    plt.savefig(output_dir / 'A_04a_plan_ml_optimizer.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--optimizer-csv", required=True, help="Path to optimizer loto_mre CSV")
    parser.add_argument("--ml-csv", required=True, help="Path to ML loto_mre CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(Path(args.optimizer_csv), Path(args.ml_csv), Path(args.output_dir))
