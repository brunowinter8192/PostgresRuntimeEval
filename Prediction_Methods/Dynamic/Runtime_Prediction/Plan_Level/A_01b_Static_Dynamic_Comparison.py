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
from plot_config import DPI, DEEP_GREEN, LIGHT_GREEN, DEEP_RED

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

# Load static template summary and convert to Qx format
def load_static_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    df['template'] = 'Q' + df['template'].astype(str)
    df['static_mre_pct'] = df['mre'] * 100
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

    y_cap = 70
    static_overall = static_values.mean()
    dynamic_overall = dynamic_values.mean()

    static_capped = np.minimum(static_values, y_cap)
    dynamic_capped = np.minimum(dynamic_values, y_cap)

    bars_static = ax.bar(x - width/2, static_capped, width,
                         label=f'Static (Overall: {static_overall:.2f}%)',
                         color=LIGHT_GREEN, alpha=0.85)
    bars_dynamic = ax.bar(x + width/2, dynamic_capped, width,
                          label=f'Dynamic (Overall: {dynamic_overall:.2f}%)',
                          color=DEEP_GREEN, alpha=0.85)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    ax.set_ylim(0, y_cap * 1.1)
    ax.set_yticks(np.arange(0, y_cap + 1, 10))

    for bar, val in zip(bars_static, static_values):
        color = DEEP_RED if val > y_cap else 'black'
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                f'{val:.1f}%', ha='center', va='bottom', fontsize=7, color=color)
    for bar, val in zip(bars_dynamic, dynamic_values):
        color = DEEP_RED if val > y_cap else 'black'
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                f'{val:.1f}%', ha='center', va='bottom', fontsize=7, color=color)

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
