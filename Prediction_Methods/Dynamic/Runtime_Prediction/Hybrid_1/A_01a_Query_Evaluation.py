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
from plot_config import DPI, DEEP_BLUE

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']

SCRIPT_DIR = Path(__file__).resolve().parent


# ORCHESTRATOR
def evaluate_loto_workflow(approach: str, output_dir: str) -> None:
    df = load_all_predictions(approach)
    root_ops = extract_root_operators(df)
    overall_mre = calculate_overall_mre(root_ops)
    loto_stats = calculate_loto_stats(root_ops)
    export_metrics(overall_mre, loto_stats, output_dir)
    create_and_save_plot(loto_stats, approach, output_dir)


# FUNCTIONS

# Load and combine predictions from all LOTO templates
def load_all_predictions(approach: str) -> pd.DataFrame:
    dfs = []
    for template in TEMPLATES:
        pred_file = SCRIPT_DIR / template / approach / 'predictions.csv'
        if not pred_file.exists():
            continue
        df = pd.read_csv(pred_file, delimiter=';')
        df['loto_template'] = template
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)


# Extract root operators from predictions
def extract_root_operators(df: pd.DataFrame) -> pd.DataFrame:
    root_ops = df[df['depth'] == 0].copy()
    root_ops['mre'] = np.abs(root_ops['predicted_total_time'] - root_ops['actual_total_time']) / root_ops['actual_total_time']
    return root_ops


# Calculate overall mean relative error
def calculate_overall_mre(root_ops: pd.DataFrame) -> float:
    return root_ops['mre'].mean()


# Calculate statistics per LOTO template
def calculate_loto_stats(root_ops: pd.DataFrame) -> pd.DataFrame:
    loto_stats = root_ops.groupby('loto_template').agg({
        'mre': ['mean', 'std', 'count'],
        'predicted_total_time': 'mean',
        'actual_total_time': 'mean'
    }).round(4)

    loto_stats.columns = ['mean_mre', 'std_mre', 'query_count', 'mean_predicted_ms', 'mean_actual_ms']
    loto_stats['mean_mre_pct'] = loto_stats['mean_mre'] * 100
    loto_stats = loto_stats[['mean_mre_pct', 'mean_mre', 'std_mre', 'query_count', 'mean_predicted_ms', 'mean_actual_ms']]

    loto_stats = loto_stats.reindex(TEMPLATES)

    return loto_stats


# Save overall and LOTO metrics to CSV
def export_metrics(overall_mre: float, loto_stats: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    overall_df = pd.DataFrame({
        'metric': ['mean_mre'],
        'value': [overall_mre],
        'percentage': [overall_mre * 100]
    })

    overall_file = output_path / 'overall_mre.csv'
    overall_df.to_csv(overall_file, index=False, sep=';')

    loto_file = output_path / 'loto_mre.csv'
    loto_stats.to_csv(loto_file, sep=';')


# Create and save MRE bar plot by LOTO template
def create_and_save_plot(loto_stats: pd.DataFrame, approach: str, output_dir: str) -> None:
    fig = create_mre_plot(loto_stats, approach)
    save_plot(fig, output_dir)


# Create MRE bar plot by LOTO template
def create_mre_plot(loto_stats: pd.DataFrame, approach: str) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(16, 8))

    templates = loto_stats.index.tolist()
    mean_mre_values = loto_stats['mean_mre_pct'].values

    x = np.arange(len(templates))
    width = 0.5

    bars = ax.bar(x, mean_mre_values, width, label='Mean MRE',
                   color=DEEP_BLUE, alpha=0.8, edgecolor='black', linewidth=0.8)

    ax.set_xlabel('LOTO Template (Test Set)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_title(f'Query-Level Prediction Error by LOTO Template ({approach})',
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(templates, rotation=0, fontsize=11)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    for i, bar in enumerate(bars):
        height = bar.get_height()
        if not np.isnan(height):
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()

    return fig


# Save plot to file
def save_plot(fig: plt.Figure, output_dir: str) -> None:
    plot_file = Path(output_dir) / 'loto_mre_plot.png'
    plot_file.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(plot_file, dpi=DPI, bbox_inches='tight')
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("approach", help="Approach to evaluate (e.g., approach_3)")
    parser.add_argument("--output-dir", required=True, help="Output directory for evaluation results")

    args = parser.parse_args()

    evaluate_loto_workflow(args.approach, args.output_dir)
