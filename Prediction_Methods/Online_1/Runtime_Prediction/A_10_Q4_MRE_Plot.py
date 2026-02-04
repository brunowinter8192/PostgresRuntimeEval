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
from plot_config import DPI, TAB20_BLUE

# ORCHESTRATOR
def q4_mre_plot_workflow(predictions_dir, output_dir):
    df = load_q4_predictions(predictions_dir)
    query_mre = extract_root_mre(df)
    overall_mre = calculate_overall_mre(query_mre)
    create_and_save_plot(query_mre, overall_mre, output_dir)

# FUNCTIONS

# Load predictions.csv files from Q4_* directories only
def load_q4_predictions(predictions_dir):
    predictions_path = Path(predictions_dir)
    csv_files = list(predictions_path.glob('Q4_*/csv/predictions.csv'))

    dfs = []
    for csv_file in csv_files:
        df = pd.read_csv(csv_file, delimiter=';')
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


# Extract MRE for root node per query
def extract_root_mre(df):
    root_ops = df[df['depth'] == 0].copy()
    root_ops['mre'] = np.abs(root_ops['predicted_total_time'] - root_ops['actual_total_time']) / root_ops['actual_total_time']
    root_ops['query_id'] = root_ops['query_file'].apply(extract_query_id)
    root_ops = root_ops.sort_values('query_id')
    return root_ops[['query_file', 'query_id', 'mre']]


# Extract numeric query ID for sorting
def extract_query_id(query_file):
    parts = query_file.split('_')
    return int(parts[1])


# Calculate overall MRE across all queries
def calculate_overall_mre(query_mre):
    return query_mre['mre'].mean()


# Create and save barplot
def create_and_save_plot(query_mre, overall_mre, output_dir):
    fig = create_q4_barplot(query_mre, overall_mre)
    save_plot(fig, output_dir)


# Create barplot with 30 bars for Q4 queries
def create_q4_barplot(query_mre, overall_mre):
    fig, ax = plt.subplots(figsize=(18, 8))

    queries = query_mre['query_file'].tolist()
    mre_values = query_mre['mre'].values * 100

    x = np.arange(len(queries))
    width = 0.7

    bars = ax.bar(x, mre_values, width, color=TAB20_BLUE, alpha=0.8,
                  edgecolor='black', linewidth=0.8)

    ax.set_xlabel('Query', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_title('Online_1: Q4 Query-Level Prediction Error',
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels([q.replace('_seed_', '\n') for q in queries],
                       rotation=90, ha='center', fontsize=8)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontsize=7, fontweight='bold')

    ax.text(0.98, 0.98, f'Overall MRE: {overall_mre*100:.2f}%',
            transform=ax.transAxes, fontsize=12, fontweight='bold',
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='gray'))

    plt.tight_layout()

    return fig


# Save plot to file
def save_plot(fig, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    plot_file = output_path / 'q4_mre_barplot.png'
    fig.savefig(plot_file, dpi=DPI, bbox_inches='tight')
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions_dir", help="Directory containing Q4_* prediction subdirectories")
    parser.add_argument("--output-dir", required=True, help="Output directory for plot")

    args = parser.parse_args()

    q4_mre_plot_workflow(args.predictions_dir, args.output_dir)
