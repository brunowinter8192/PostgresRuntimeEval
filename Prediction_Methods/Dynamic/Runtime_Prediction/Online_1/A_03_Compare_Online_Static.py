#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import DPI, TAB20_BLUE, TAB20_GREEN

# ORCHESTRATOR
def compare_workflow(online_csv: str, static_csv: str, output_dir: str) -> None:
    online_df = load_mre_data(online_csv, "Dynamic")
    static_df = load_mre_data(static_csv, "Static")
    combined = merge_data(online_df, static_df)
    create_comparison_plot(combined, output_dir)

# FUNCTIONS

# Load MRE data and add method label
def load_mre_data(csv_path: str, method: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    df['method'] = method
    return df[['template', 'mean_mre_pct', 'method']]

# Merge online and static dataframes
def merge_data(online_df: pd.DataFrame, static_df: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([online_df, static_df], ignore_index=True)

# Create grouped bar plot comparing methods
def create_comparison_plot(df: pd.DataFrame, output_dir: str) -> None:
    fig, ax = plt.subplots(figsize=(16, 8))

    templates = sorted(df['template'].unique(), key=lambda x: int(x[1:]))

    static_data = df[df['method'] == 'Static']
    online_data = df[df['method'] == 'Dynamic']

    static_values = np.array([static_data[static_data['template'] == t]['mean_mre_pct'].values[0] for t in templates])
    online_values = np.array([online_data[online_data['template'] == t]['mean_mre_pct'].values[0] for t in templates])

    x = np.arange(len(templates))
    width = 0.35

    static_overall = static_values.mean()
    online_overall = online_values.mean()

    bars_static = ax.bar(x - width/2, static_values, width,
                         label=f'Static (Overall: {static_overall:.2f}%)',
                         color=TAB20_BLUE, alpha=0.85)
    bars_online = ax.bar(x + width/2, online_values, width,
                         label=f'Dynamic (Overall: {online_overall:.2f}%)',
                         color=TAB20_GREEN, alpha=0.85)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    max_val = max(static_values.max(), online_values.max())
    ax.set_ylim(0, max_val * 1.15)

    ax.bar_label(bars_static, fmt='%.1f%%', padding=2, fontsize=7, rotation=0)
    ax.bar_label(bars_online, fmt='%.1f%%', padding=2, fontsize=7, rotation=0)

    plt.tight_layout()

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    plt.savefig(f'{output_dir}/compare_online_static.png', dpi=DPI, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("online_csv", help="Path to Dynamic_1 MRE CSV")
    parser.add_argument("static_csv", help="Path to Hybrid_2 Static MRE CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    compare_workflow(args.online_csv, args.static_csv, args.output_dir)
