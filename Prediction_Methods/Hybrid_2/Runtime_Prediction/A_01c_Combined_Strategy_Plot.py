#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ORCHESTRATOR

def combined_strategy_workflow(size_mre, frequency_mre, error_mre, optimizer_mre, output_dir, variant):
    data = load_all_mre_data(size_mre, frequency_mre, error_mre, optimizer_mre)
    combined_df = create_combined_dataframe(data)
    export_combined_csv(combined_df, output_dir)
    create_combined_plot(data, output_dir, variant)


# FUNCTIONS

# Load all MRE data from CSV files
def load_all_mre_data(size_mre, frequency_mre, error_mre, optimizer_mre):
    return {
        'Size': load_template_mre(size_mre),
        'Frequency': load_template_mre(frequency_mre),
        'Error': load_template_mre(error_mre),
        'Optimizer': load_template_mre(optimizer_mre)
    }


# Load template MRE from CSV
def load_template_mre(csv_path):
    df = pd.read_csv(csv_path, delimiter=';', index_col=0)
    overall_mre = df['mean_mre'].mean()
    return {
        'template_mre': df['mean_mre_pct'].to_dict(),
        'overall_mre': overall_mre * 100
    }


# Create combined dataframe with all strategies
def create_combined_dataframe(data):
    rows = []
    templates = sorted(data['Size']['template_mre'].keys(), key=lambda x: int(x[1:]))

    for template in templates:
        row = {'template': template}
        for strategy in ['Size', 'Frequency', 'Error', 'Optimizer']:
            row[f'{strategy.lower()}_mre_pct'] = data[strategy]['template_mre'].get(template, np.nan)
        rows.append(row)

    df = pd.DataFrame(rows)
    df.set_index('template', inplace=True)
    return df


# Export combined CSV
def export_combined_csv(combined_df, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    combined_df.to_csv(output_path / 'A_01c_combined_strategy_mre.csv', sep=';')


# Create combined bar plot
def create_combined_plot(data, output_dir, variant):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    templates = sorted(data['Size']['template_mre'].keys(), key=lambda x: int(x[1:]))
    x = np.arange(len(templates))

    create_plot_with_strategies(
        data, templates, x,
        strategies=['Size', 'Frequency', 'Error', 'Optimizer'],
        colors=['steelblue', 'forestgreen', 'darkorange', 'coral'],
        offsets=[-1.5, -0.5, 0.5, 1.5],
        width=0.2,
        output_file=output_path / 'A_01c_combined_strategy_plot.png'
    )

    create_plot_with_strategies(
        data, templates, x,
        strategies=['Size', 'Frequency', 'Error'],
        colors=['steelblue', 'forestgreen', 'darkorange'],
        offsets=[-1.0, 0.0, 1.0],
        width=0.25,
        output_file=output_path / 'A_01c_hybrid_strategy_plot.png'
    )


# Create bar plot with given strategies
def create_plot_with_strategies(data, templates, x, strategies, colors, offsets, width, output_file):
    fig, ax = plt.subplots(figsize=(18, 8))

    for strategy, color, offset in zip(strategies, colors, offsets):
        values = [data[strategy]['template_mre'].get(t, 0) for t in templates]
        overall = data[strategy]['overall_mre']
        label = f"{strategy} (Overall: {overall:.2f}%)"
        bars = ax.bar(x + offset * width, values, width, label=label, color=color, alpha=0.85)
        ax.bar_label(bars, fmt='%.1f%%', padding=2, fontsize=6, rotation=0)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    max_val = max(max(data[s]['template_mre'].values()) for s in strategies)
    ax.set_ylim(0, max_val * 1.35)

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--size-mre", required=True, help="Path to Size template_mre.csv")
    parser.add_argument("--frequency-mre", required=True, help="Path to Frequency template_mre.csv")
    parser.add_argument("--error-mre", required=True, help="Path to Error template_mre.csv")
    parser.add_argument("--optimizer-mre", required=True, help="Path to Optimizer template_mre.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    parser.add_argument("--variant", default="Baseline", help="Variant name for title (Baseline/Epsilon)")
    args = parser.parse_args()

    combined_strategy_workflow(
        args.size_mre, args.frequency_mre, args.error_mre,
        args.optimizer_mre, args.output_dir, args.variant
    )
