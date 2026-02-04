#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from plot_config import METHOD_COLORS, DPI, PRIMARY_COLOR

# ORCHESTRATOR

# Evaluate predictions and generate metrics
def evaluate_predictions_workflow(predictions_file, output_dir, compare_file=None):
    df = load_predictions(predictions_file)
    root_ops = extract_root_operators(df)
    overall_mre = calculate_overall_mre(root_ops)
    template_stats = calculate_template_stats(root_ops)
    if compare_file:
        comparison_df = load_comparison(compare_file)
        template_stats = add_comparison_columns(template_stats, comparison_df)
    export_metrics(overall_mre, template_stats, output_dir)
    create_and_save_plot(template_stats, output_dir)

# FUNCTIONS

# Load predictions from CSV file
def load_predictions(predictions_file):
    return pd.read_csv(predictions_file, delimiter=';')

# Extract root operators from predictions
def extract_root_operators(df):
    root_ops = df[df['depth'] == 0].copy()
    root_ops['template'] = root_ops['query_file'].apply(extract_template_id)
    root_ops['mre'] = np.abs(root_ops['predicted_total_time'] - root_ops['actual_total_time']) / root_ops['actual_total_time']
    return root_ops

# Extract template ID from query filename
def extract_template_id(query_file):
    return query_file.split('_')[0]

# Calculate overall mean relative error
def calculate_overall_mre(root_ops):
    return root_ops['mre'].mean()

# Extract numeric part from template for sorting
def sort_template_key(template):
    return int(template[1:])

# Calculate statistics per template
def calculate_template_stats(root_ops):
    template_stats = root_ops.groupby('template').agg({
        'mre': ['mean', 'std', 'count'],
        'predicted_total_time': 'mean',
        'actual_total_time': 'mean'
    }).round(4)
    template_stats.columns = ['mean_mre', 'std_mre', 'query_count', 'mean_predicted_ms', 'mean_actual_ms']
    template_stats['mean_mre_pct'] = template_stats['mean_mre'] * 100
    template_stats = template_stats[['mean_mre_pct', 'mean_mre', 'std_mre', 'query_count', 'mean_predicted_ms', 'mean_actual_ms']]
    template_stats = template_stats.sort_index(key=lambda x: x.map(sort_template_key))
    return template_stats


# Load comparison CSV for baseline MRE values
def load_comparison(compare_file):
    df = pd.read_csv(compare_file, delimiter=';', index_col='template')
    return df


# Add comparison columns with delta calculation
def add_comparison_columns(template_stats, comparison_df):
    template_stats['baseline_mre_pct'] = template_stats.index.map(
        lambda t: comparison_df.loc[t, 'mean_mre_pct'] if t in comparison_df.index else np.nan
    )
    template_stats['delta_mre_pct'] = template_stats['baseline_mre_pct'] - template_stats['mean_mre_pct']
    template_stats['delta_formula'] = template_stats.apply(
        lambda row: f"{row['baseline_mre_pct']:.2f} - {row['mean_mre_pct']:.2f} = {row['delta_mre_pct']:.2f}",
        axis=1
    )
    return template_stats

# Save overall and template metrics to CSV
def export_metrics(overall_mre, template_stats, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    overall_df = pd.DataFrame({
        'metric': ['mean_mre'],
        'value': [overall_mre],
        'percentage': [overall_mre * 100]
    })
    overall_file = output_path / 'A_01a_overall_mre.csv'
    overall_df.to_csv(overall_file, index=False, sep=';')
    template_file = output_path / 'A_01a_template_mre.csv'
    template_stats.to_csv(template_file, sep=';')

# Extract approach number from output path
def get_approach_color(output_dir):
    import re
    match = re.search(r'approach_(\d+)', str(output_dir))
    if match:
        approach_key = f"Hybrid_1_Approach_{match.group(1)}"
        return METHOD_COLORS.get(approach_key, PRIMARY_COLOR)
    return PRIMARY_COLOR

# Create and save MRE bar plot by template
def create_and_save_plot(template_stats, output_dir):
    color = get_approach_color(output_dir)
    fig = create_mre_plot(template_stats, color)
    save_plot(fig, output_dir)

# Create MRE bar plot by template
def create_mre_plot(template_stats, color):
    fig, ax = plt.subplots(figsize=(16, 8))
    templates = template_stats.index.tolist()
    mean_mre_values = template_stats['mean_mre_pct'].values
    x = np.arange(len(templates))
    width = 0.5
    bars = ax.bar(x, mean_mre_values, width, label='Mean MRE',
                   color=color, alpha=0.8, edgecolor='black', linewidth=0.8)
    ax.set_xlabel('Template', fontsize=13)
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels(templates, rotation=0, fontsize=11)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim(0, max(mean_mre_values) * 1.1)
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    return fig

# Save plot to file
def save_plot(fig, output_dir):
    plot_file = Path(output_dir) / 'A_01a_template_mre_plot.png'
    fig.savefig(plot_file, dpi=DPI, bbox_inches='tight')
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate query-level predictions')
    parser.add_argument('predictions_file', help='Path to predictions.csv')
    parser.add_argument('--output-dir', required=True, help='Path to output directory')
    parser.add_argument('--compare', help='Path to comparison template_mre.csv (e.g., Operator baseline)')
    args = parser.parse_args()

    evaluate_predictions_workflow(args.predictions_file, args.output_dir, args.compare)
