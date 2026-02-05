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
from plot_config import DPI, TAB20_BLUE, TAB20_GREEN

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']

SCRIPT_DIR = Path(__file__).resolve().parent


# ORCHESTRATOR
def comparison_workflow(static_csv: str, output_dir: str) -> None:
    static_data = load_static_data(static_csv)
    dynamic_data = load_dynamic_data()
    combined_df = merge_data(static_data, dynamic_data)
    export_csv(combined_df, output_dir)
    create_comparison_plot(combined_df, output_dir)


# FUNCTIONS

# Load static template summary (already in Qx format with mean_mre_pct)
def load_static_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    df = df.rename(columns={'mean_mre_pct': 'static_mre_pct'})
    return df[['template', 'static_mre_pct']]


# Load dynamic LOTO MRE data
def load_dynamic_data() -> pd.DataFrame:
    dynamic_file = SCRIPT_DIR / 'Evaluation' / 'loto_mre.csv'
    df = pd.read_csv(dynamic_file, delimiter=';')
    df = df.rename(columns={'loto_template': 'template', 'mean_mre_pct': 'dynamic_mre_pct'})
    return df[['template', 'dynamic_mre_pct']]


# Merge static and dynamic data on common templates
def merge_data(static_data: pd.DataFrame, dynamic_data: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(static_data, dynamic_data, on='template', how='inner')
    template_order = {t: i for i, t in enumerate(TEMPLATES)}
    merged['order'] = merged['template'].map(template_order)
    merged = merged.sort_values('order').drop(columns=['order'])
    return merged


# Export combined CSV
def export_csv(df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path / 'A_01b_static_dynamic_comparison.csv', sep=';', index=False)


# Create grouped bar plot comparing static vs dynamic
def create_comparison_plot(df: pd.DataFrame, output_dir: str) -> None:
    fig, ax = plt.subplots(figsize=(16, 8))

    templates = df['template'].tolist()
    static_values = df['static_mre_pct'].values
    dynamic_values = df['dynamic_mre_pct'].values

    x = np.arange(len(templates))
    width = 0.35

    static_overall = static_values.mean()
    dynamic_overall = dynamic_values.mean()

    bars_static = ax.bar(x - width/2, static_values, width,
                         label=f'Static (Overall: {static_overall:.2f}%)',
                         color=TAB20_BLUE, alpha=0.85)
    bars_dynamic = ax.bar(x + width/2, dynamic_values, width,
                          label=f'Dynamic (Overall: {dynamic_overall:.2f}%)',
                          color=TAB20_GREEN, alpha=0.85)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    max_val = max(static_values.max(), dynamic_values.max())
    ax.set_ylim(0, max_val * 1.15)

    ax.bar_label(bars_static, fmt='%.1f%%', padding=2, fontsize=7, rotation=0)
    ax.bar_label(bars_dynamic, fmt='%.1f%%', padding=2, fontsize=7, rotation=0)

    plt.tight_layout()

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path / 'A_01b_static_dynamic_comparison.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--static-csv", required=True, help="Path to static template summary CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")

    args = parser.parse_args()

    comparison_workflow(args.static_csv, args.output_dir)
