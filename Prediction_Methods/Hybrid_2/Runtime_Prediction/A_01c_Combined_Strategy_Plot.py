#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import DPI, STRATEGY_COLORS


# ORCHESTRATOR

def combined_strategy_workflow(size_mre, frequency_mre, error_mre, output_dir, variant,
                               optimizer_mre=None, hybrid1_mre=None,
                               size_predictions=None, frequency_predictions=None, error_predictions=None,
                               suffix=None):
    if size_predictions and frequency_predictions and error_predictions:
        data = load_all_mre_from_predictions(size_predictions, frequency_predictions, error_predictions,
                                             optimizer_mre, hybrid1_mre)
    else:
        data = load_all_mre_data(size_mre, frequency_mre, error_mre, optimizer_mre, hybrid1_mre)
    combined_df = create_combined_dataframe(data)
    export_combined_csv(combined_df, output_dir, suffix)
    create_combined_plot(data, output_dir, variant, suffix)


# FUNCTIONS

# Load all MRE from prediction CSVs (unrounded values)
def load_all_mre_from_predictions(size_predictions, frequency_predictions, error_predictions,
                                  optimizer_mre=None, hybrid1_mre=None):
    data = {
        'Size': load_mre_from_predictions(size_predictions),
        'Frequency': load_mre_from_predictions(frequency_predictions),
        'Error': load_mre_from_predictions(error_predictions),
    }
    if optimizer_mre:
        data['Optimizer'] = load_template_mre(optimizer_mre)
    if hybrid1_mre:
        data['Hybrid_1'] = load_template_mre(hybrid1_mre)
    return data


# Load MRE from predictions CSV (root nodes only)
def load_mre_from_predictions(csv_path):
    df = pd.read_csv(csv_path, delimiter=';')
    roots = df[df['depth'] == 0].copy()
    roots['template'] = roots['query_file'].str.extract(r'^(Q\d+)_')
    roots['mre'] = abs(roots['predicted_total_time'] - roots['actual_total_time']) / roots['actual_total_time']
    template_mre = roots.groupby('template')['mre'].mean()
    overall_mre = roots['mre'].mean()
    return {
        'template_mre': (template_mre * 100).to_dict(),
        'overall_mre': overall_mre * 100
    }


# Load all MRE data from CSV files
def load_all_mre_data(size_mre, frequency_mre, error_mre, optimizer_mre=None, hybrid1_mre=None):
    data = {
        'Size': load_template_mre(size_mre),
        'Frequency': load_template_mre(frequency_mre),
        'Error': load_template_mre(error_mre),
    }
    if optimizer_mre:
        data['Optimizer'] = load_template_mre(optimizer_mre)
    if hybrid1_mre:
        data['Hybrid_1'] = load_template_mre(hybrid1_mre)
    return data


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
    strategies = list(data.keys())

    for template in templates:
        row = {'template': template}
        for strategy in strategies:
            row[f'{strategy.lower()}_mre_pct'] = data[strategy]['template_mre'].get(template, np.nan)
        rows.append(row)

    df = pd.DataFrame(rows)
    df.set_index('template', inplace=True)
    return df


# Export combined CSV
def export_combined_csv(combined_df, output_dir, suffix=None):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    filename = f'A_01c_combined_strategy_mre_{suffix}.csv' if suffix else 'A_01c_combined_strategy_mre.csv'
    combined_df.to_csv(output_path / filename, sep=';')




# Create combined bar plot
def create_combined_plot(data, output_dir, variant, suffix=None):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    templates = sorted(data['Size']['template_mre'].keys(), key=lambda x: int(x[1:]))
    x = np.arange(len(templates))

    all_strategies = list(data.keys())
    all_colors = [STRATEGY_COLORS[s] for s in all_strategies]
    all_offsets, all_width = compute_bar_offsets(len(all_strategies))

    combined_filename = f'A_01c_combined_strategy_plot_{suffix}.png' if suffix else 'A_01c_combined_strategy_plot.png'
    create_plot_with_strategies(
        data, templates, x,
        strategies=all_strategies,
        colors=all_colors,
        offsets=all_offsets,
        width=all_width,
        output_file=output_path / combined_filename
    )

    if not suffix:
        hybrid_strategies = ['Size', 'Frequency', 'Error']
        hybrid_colors = [STRATEGY_COLORS[s] for s in hybrid_strategies]
        hybrid_offsets, hybrid_width = compute_bar_offsets(3)

        create_plot_with_strategies(
            data, templates, x,
            strategies=hybrid_strategies,
            colors=hybrid_colors,
            offsets=hybrid_offsets,
            width=hybrid_width,
            output_file=output_path / 'A_01c_hybrid_strategy_plot.png'
        )


# Compute bar offsets for n strategies
def compute_bar_offsets(n):
    if n == 3:
        return [-1.0, 0.0, 1.0], 0.25
    elif n == 4:
        return [-1.5, -0.5, 0.5, 1.5], 0.2
    elif n == 5:
        return [-2.0, -1.0, 0.0, 1.0, 2.0], 0.17
    else:
        width = 0.8 / n
        return [i - (n - 1) / 2 for i in range(n)], width


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
    plt.savefig(output_file, dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--size-mre", help="Path to Size template_mre.csv")
    parser.add_argument("--frequency-mre", help="Path to Frequency template_mre.csv")
    parser.add_argument("--error-mre", help="Path to Error template_mre.csv")
    parser.add_argument("--optimizer-mre", help="Path to Optimizer template_mre.csv (optional)")
    parser.add_argument("--hybrid1-mre", help="Path to Hybrid_1 template_mre.csv (optional)")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    parser.add_argument("--variant", default="Baseline", help="Variant name for title (Baseline/Epsilon)")
    parser.add_argument("--suffix", help="Suffix for output filenames (e.g. 'optimizer' or 'hybrid1')")
    parser.add_argument("--size-predictions", help="Path to Size 12_predictions.csv")
    parser.add_argument("--frequency-predictions", help="Path to Frequency 12_predictions.csv")
    parser.add_argument("--error-predictions", help="Path to Error 12_predictions.csv")
    args = parser.parse_args()

    combined_strategy_workflow(
        args.size_mre, args.frequency_mre, args.error_mre,
        args.output_dir, args.variant,
        args.optimizer_mre, args.hybrid1_mre,
        args.size_predictions, args.frequency_predictions, args.error_predictions,
        args.suffix
    )
