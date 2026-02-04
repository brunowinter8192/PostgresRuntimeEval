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
from plot_config import DPI, TAB20_BLUE, TAB20_GREEN, TAB20_ORANGE, TAB20_PURPLE

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def comparison_workflow(optimizer_csv: Path, operator_csv: Path, hybrid_csv: Path, online_csv: Path, output_dir: Path) -> None:
    optimizer_df = load_data(optimizer_csv)
    operator_df = load_data(operator_csv)
    hybrid_df = load_data(hybrid_csv)
    online_df = load_data(online_csv)
    create_comparison_plot(optimizer_df, operator_df, hybrid_df, online_df, output_dir)


# FUNCTIONS

# Load CSV and normalize template column
def load_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    if 'loto_template' in df.columns:
        df = df.rename(columns={'loto_template': 'template'})
    return df.set_index('template')


# Add bar labels with clipping for outliers
def add_bar_labels(ax, bars, values, ylim_max: float) -> None:
    for bar, val in zip(bars, values):
        x_pos = bar.get_x() + bar.get_width() / 2
        if val > ylim_max:
            y_pos = ylim_max - 3
        else:
            y_pos = val + 1
        ax.text(x_pos, y_pos, f'{val:.1f}%', ha='center', va='bottom', fontsize=5)


# Create grouped bar plot with 4 methods
def create_comparison_plot(optimizer_df: pd.DataFrame, operator_df: pd.DataFrame,
                           hybrid_df: pd.DataFrame, online_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(18, 8))

    templates = [t for t in TEMPLATES if t in optimizer_df.index and t in operator_df.index
                 and t in hybrid_df.index and t in online_df.index]

    optimizer_values = np.array([optimizer_df.loc[t, 'mean_mre_pct'] for t in templates])
    operator_values = np.array([operator_df.loc[t, 'mean_mre_pct'] for t in templates])
    hybrid_values = np.array([hybrid_df.loc[t, 'mean_mre_pct'] for t in templates])
    online_values = np.array([online_df.loc[t, 'mean_mre_pct'] for t in templates])

    x = np.arange(len(templates))
    width = 0.2

    optimizer_overall = optimizer_values.mean()
    operator_overall = operator_values.mean()
    hybrid_overall = hybrid_values.mean()
    online_overall = online_values.mean()

    bars_optimizer = ax.bar(x - 1.5*width, optimizer_values, width,
                            label=f'Optimizer (Overall: {optimizer_overall:.2f}%)',
                            color=TAB20_ORANGE, alpha=0.85)
    bars_operator = ax.bar(x - 0.5*width, operator_values, width,
                           label=f'Operator Level (Overall: {operator_overall:.2f}%)',
                           color=TAB20_BLUE, alpha=0.85)
    bars_hybrid = ax.bar(x + 0.5*width, hybrid_values, width,
                         label=f'Hybrid_1 (Overall: {hybrid_overall:.2f}%)',
                         color=TAB20_GREEN, alpha=0.85)
    bars_online = ax.bar(x + 1.5*width, online_values, width,
                         label=f'Online_1 (Overall: {online_overall:.2f}%)',
                         color=TAB20_PURPLE, alpha=0.85)

    ylim_max = 90
    add_bar_labels(ax, bars_optimizer, optimizer_values, ylim_max)
    add_bar_labels(ax, bars_operator, operator_values, ylim_max)
    add_bar_labels(ax, bars_hybrid, hybrid_values, ylim_max)
    add_bar_labels(ax, bars_online, online_values, ylim_max)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=10, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    ax.set_ylim(0, ylim_max)

    plt.tight_layout()
    plt.savefig(output_dir / 'A_04b_operator_ml_optimizer.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--optimizer-csv", required=True, help="Path to optimizer loto_mre CSV")
    parser.add_argument("--operator-csv", required=True, help="Path to operator ML loto_mre CSV")
    parser.add_argument("--hybrid-csv", required=True, help="Path to Hybrid_1 loto_mre CSV")
    parser.add_argument("--online-csv", required=True, help="Path to Online_1 loto_mre CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(
        Path(args.optimizer_csv),
        Path(args.operator_csv),
        Path(args.hybrid_csv),
        Path(args.online_csv),
        Path(args.output_dir)
    )
