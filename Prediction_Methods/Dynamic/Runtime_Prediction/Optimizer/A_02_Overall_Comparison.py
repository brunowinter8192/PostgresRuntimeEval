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
from plot_config import DPI, DEEP_BLUE, DEEP_GREEN

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def comparison_workflow(plan_csv: Path, operator_csv: Path, output_dir: Path) -> None:
    plan_stats = load_mre_stats(plan_csv, 'Plan')
    operator_stats = load_mre_stats(operator_csv, 'Operator')
    create_comparison_plot(plan_stats, operator_stats, output_dir)


# FUNCTIONS

# Load MRE statistics from CSV
def load_mre_stats(csv_path: Path, method: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';', index_col=0)
    df['method'] = method
    return df


# Create grouped bar plot comparing Plan vs Operator
def create_comparison_plot(plan_stats: pd.DataFrame, operator_stats: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(16, 8))

    templates = [t for t in TEMPLATES if t in plan_stats.index and t in operator_stats.index]
    plan_values = np.array([plan_stats.loc[t, 'mean_mre_pct'] for t in templates])
    operator_values = np.array([operator_stats.loc[t, 'mean_mre_pct'] for t in templates])

    x = np.arange(len(templates))
    width = 0.35

    plan_overall = plan_values.mean()
    operator_overall = operator_values.mean()

    bars_plan = ax.bar(x - width/2, plan_values, width,
                       label=f'Plan-Level (Overall: {plan_overall:.2f}%)',
                       color=DEEP_BLUE, alpha=0.85)
    bars_operator = ax.bar(x + width/2, operator_values, width,
                           label=f'Operator-Level (Overall: {operator_overall:.2f}%)',
                           color=DEEP_GREEN, alpha=0.85)

    ax.bar_label(bars_plan, fmt='%.1f%%', padding=2, fontsize=7, rotation=0)
    ax.bar_label(bars_operator, fmt='%.1f%%', padding=2, fontsize=7, rotation=0)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    max_val = max(plan_values.max(), operator_values.max())
    ax.set_ylim(0, max_val * 1.15)

    plt.tight_layout()
    plt.savefig(output_dir / 'A_02_comparison_plot.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan-csv", required=True, help="Path to Plan_Level/loto_mre.csv")
    parser.add_argument("--operator-csv", required=True, help="Path to Operator_Level/loto_mre.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(Path(args.plan_csv), Path(args.operator_csv), Path(args.output_dir))
