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
from plot_config import DPI, DEEP_BLUE, DEEP_GREEN

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def comparison_workflow(static_csv: Path, dynamic_csv: Path, output_dir: Path) -> None:
    static_df = load_static_data(static_csv)
    dynamic_df = load_dynamic_data(dynamic_csv)
    create_comparison_plot(static_df, dynamic_df, output_dir)


# FUNCTIONS

# Load static optimizer results
def load_static_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    df = df[df['template'].isin(TEMPLATES)]
    return df.set_index('template')


# Load dynamic optimizer results
def load_dynamic_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    return df.set_index('template')


# Create grouped bar plot
def create_comparison_plot(static_df: pd.DataFrame, dynamic_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(16, 8))

    templates = [t for t in TEMPLATES if t in static_df.index and t in dynamic_df.index]
    static_values = np.array([static_df.loc[t, 'mre_optimizer_pct'] for t in templates])
    dynamic_values = np.array([dynamic_df.loc[t, 'mean_mre_pct'] for t in templates])

    x = np.arange(len(templates))
    width = 0.35

    static_overall = static_values.mean()
    dynamic_overall = dynamic_values.mean()

    bars_static = ax.bar(x - width/2, static_values, width,
                         label=f'Static (Overall: {static_overall:.2f}%)',
                         color=DEEP_BLUE, alpha=0.85)
    bars_dynamic = ax.bar(x + width/2, dynamic_values, width,
                          label=f'Dynamic (Overall: {dynamic_overall:.2f}%)',
                          color=DEEP_GREEN, alpha=0.85)

    ax.bar_label(bars_static, fmt='%.1f%%', padding=2, fontsize=7, rotation=0)
    ax.bar_label(bars_dynamic, fmt='%.1f%%', padding=2, fontsize=7, rotation=0)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    max_val = max(static_values.max(), dynamic_values.max())
    ax.set_ylim(0, max_val * 1.15)

    plt.tight_layout()
    plt.savefig(output_dir / 'A_03b_operator_static_dynamic.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--static-csv", required=True, help="Path to static optimizer template CSV")
    parser.add_argument("--dynamic-csv", required=True, help="Path to dynamic optimizer loto_mre CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(Path(args.static_csv), Path(args.dynamic_csv), Path(args.output_dir))
