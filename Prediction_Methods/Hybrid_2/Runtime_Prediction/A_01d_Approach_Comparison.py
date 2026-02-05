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
from plot_config import DPI, TAB20_BLUE, TAB20_GREEN, TAB20_RED


# ORCHESTRATOR

def approach_comparison_workflow(operator_mre, hybrid1_mre, hybrid2_mre, output_dir):
    data = load_all_mre_data(operator_mre, hybrid1_mre, hybrid2_mre)
    combined_df = create_combined_dataframe(data)
    export_comparison_csv(combined_df, output_dir)
    create_comparison_plot(data, output_dir)


# FUNCTIONS

# Load all MRE data from CSV files
def load_all_mre_data(operator_mre, hybrid1_mre, hybrid2_mre):
    return {
        'Operator': load_template_mre(operator_mre),
        'Hybrid 1': load_template_mre(hybrid1_mre),
        'Hybrid 2': load_template_mre(hybrid2_mre)
    }


# Load template MRE from CSV
def load_template_mre(csv_path):
    df = pd.read_csv(csv_path, delimiter=';', index_col=0)
    overall_mre = df['mean_mre'].mean()
    return {
        'template_mre': df['mean_mre_pct'].to_dict(),
        'overall_mre': overall_mre * 100
    }


# Create combined dataframe with all approaches
def create_combined_dataframe(data):
    rows = []
    templates = sorted(data['Operator']['template_mre'].keys(), key=lambda x: int(x[1:]))

    for template in templates:
        row = {'template': template}
        row['operator_mre_pct'] = data['Operator']['template_mre'].get(template, np.nan)
        row['hybrid1_mre_pct'] = data['Hybrid 1']['template_mre'].get(template, np.nan)
        row['hybrid2_mre_pct'] = data['Hybrid 2']['template_mre'].get(template, np.nan)
        rows.append(row)

    df = pd.DataFrame(rows)
    df.set_index('template', inplace=True)
    return df


# Export comparison CSV
def export_comparison_csv(combined_df, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    combined_df.to_csv(output_path / 'A_01d_approach_comparison.csv', sep=';')


# Create comparison bar plot
def create_comparison_plot(data, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    templates = sorted(data['Operator']['template_mre'].keys(), key=lambda x: int(x[1:]))
    x = np.arange(len(templates))

    approaches = ['Operator', 'Hybrid 1', 'Hybrid 2']
    colors = [TAB20_RED, TAB20_BLUE, TAB20_GREEN]
    offsets = [-1.0, 0.0, 1.0]
    width = 0.25

    fig, ax = plt.subplots(figsize=(18, 8))

    for approach, color, offset in zip(approaches, colors, offsets):
        values = [data[approach]['template_mre'].get(t, 0) for t in templates]
        overall = data[approach]['overall_mre']
        label = f"{approach} (Overall: {overall:.2f}%)"
        bars = ax.bar(x + offset * width, values, width, label=label, color=color, alpha=0.85)
        ax.bar_label(bars, fmt='%.1f%%', padding=2, fontsize=6, rotation=0)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    max_val = max(max(data[a]['template_mre'].values()) for a in approaches)
    ax.set_ylim(0, max_val * 1.35)

    plt.tight_layout()
    plt.savefig(output_path / 'A_01d_approach_comparison_plot.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--operator-mre", required=True, help="Path to Operator Level template_mre.csv")
    parser.add_argument("--hybrid1-mre", required=True, help="Path to Hybrid 1 template_mre.csv")
    parser.add_argument("--hybrid2-mre", required=True, help="Path to Hybrid 2 template_mre.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    approach_comparison_workflow(args.operator_mre, args.hybrid1_mre, args.hybrid2_mre, args.output_dir)
