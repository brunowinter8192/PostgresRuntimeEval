#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import DPI, TAB20_BLUE, TAB20_ORANGE

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

    fig, ax = plt.subplots(figsize=(16, 8))

    templates = [t for t in TEMPLATES if t in optimizer_df.index and t in ml_df.index]
    optimizer_values = np.array([optimizer_df.loc[t, 'mean_mre_pct'] for t in templates])
    ml_values = np.array([ml_df.loc[t, 'mean_mre_pct'] for t in templates])

    x = np.arange(len(templates))
    width = 0.35

    optimizer_overall = optimizer_values.mean()
    ml_overall = ml_values.mean()

    bars_optimizer = ax.bar(x - width/2, optimizer_values, width,
                            label=f'Optimizer (Overall: {optimizer_overall:.2f}%)',
                            color=TAB20_ORANGE, alpha=0.85)
    bars_ml = ax.bar(x + width/2, ml_values, width,
                     label=f'Plan Level (Overall: {ml_overall:.2f}%)',
                     color=TAB20_BLUE, alpha=0.85)

    ax.bar_label(bars_optimizer, fmt='%.1f%%', padding=2, fontsize=5, rotation=0)
    ax.bar_label(bars_ml, fmt='%.1f%%', padding=2, fontsize=5, rotation=0)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    max_val = max(optimizer_values.max(), ml_values.max())
    ax.set_ylim(0, max_val * 1.15)

    plt.tight_layout()
    plt.savefig(output_dir / 'A_04a_plan_ml_optimizer.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--optimizer-csv", required=True, help="Path to optimizer loto_mre CSV")
    parser.add_argument("--ml-csv", required=True, help="Path to ML loto_mre CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(Path(args.optimizer_csv), Path(args.ml_csv), Path(args.output_dir))
