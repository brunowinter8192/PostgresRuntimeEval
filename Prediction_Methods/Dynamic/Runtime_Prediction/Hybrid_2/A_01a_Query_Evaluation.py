#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
STRATEGIES = ['Size', 'Frequency', 'Error']

SCRIPT_DIR = Path(__file__).resolve().parent


# ORCHESTRATOR

# Evaluate all strategies and create comparison plot
def evaluate_all_strategies(output_dir: str) -> None:
    all_stats = {}
    for strategy in STRATEGIES:
        loto_stats, overall_mre = evaluate_strategy(strategy, output_dir)
        all_stats[strategy] = {'loto': loto_stats, 'overall': overall_mre}
    create_comparison_plot(all_stats, output_dir)
    export_comparison_summary(all_stats, output_dir)


# FUNCTIONS

# Evaluate single strategy
def evaluate_strategy(strategy: str, output_dir: str) -> tuple:
    df = load_predictions(strategy)
    root_ops = extract_root_operators(df)
    overall_mre = calculate_overall_mre(root_ops)
    loto_stats = calculate_loto_stats(root_ops)

    strategy_output = Path(output_dir) / strategy
    export_metrics(overall_mre, loto_stats, strategy_output)
    create_and_save_plot(loto_stats, strategy, strategy_output)

    return loto_stats, overall_mre


# Load predictions for strategy from all LOTO templates
def load_predictions(strategy: str) -> pd.DataFrame:
    dfs = []
    for template in TEMPLATES:
        pred_file = SCRIPT_DIR / 'Evaluation' / template / strategy / 'predictions.csv'
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
def export_metrics(overall_mre: float, loto_stats: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    overall_df = pd.DataFrame({
        'metric': ['mean_mre'],
        'value': [overall_mre],
        'percentage': [overall_mre * 100]
    })

    overall_file = output_dir / 'overall_mre.csv'
    overall_df.to_csv(overall_file, index=False, sep=';')

    loto_file = output_dir / 'loto_mre.csv'
    loto_stats.to_csv(loto_file, sep=';')


# Create and save MRE bar plot for single strategy
def create_and_save_plot(loto_stats: pd.DataFrame, strategy: str, output_dir: Path) -> None:
    fig = create_mre_plot(loto_stats, strategy)
    save_plot(fig, output_dir / 'loto_mre_plot.png')


# Create MRE bar plot by LOTO template
def create_mre_plot(loto_stats: pd.DataFrame, strategy: str) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(16, 8))

    templates = loto_stats.index.tolist()
    mean_mre_values = loto_stats['mean_mre_pct'].values

    x = np.arange(len(templates))
    width = 0.5

    bars = ax.bar(x, mean_mre_values, width, label='Mean MRE',
                   color='steelblue', alpha=0.8, edgecolor='black', linewidth=0.8)

    ax.set_xlabel('LOTO Template (Test Set)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_title(f'Query-Level Prediction Error by LOTO Template ({strategy})',
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


# Create comparison plot for all strategies
def create_comparison_plot(all_stats: dict, output_dir: str) -> None:
    fig, ax = plt.subplots(figsize=(18, 8))

    x = np.arange(len(TEMPLATES))
    width = 0.25
    colors = {'Size': 'steelblue', 'Frequency': 'forestgreen', 'Error': 'coral'}

    for i, strategy in enumerate(STRATEGIES):
        loto_stats = all_stats[strategy]['loto']
        mean_mre_values = loto_stats['mean_mre_pct'].values
        offset = (i - 1) * width
        bars = ax.bar(x + offset, mean_mre_values, width, label=strategy,
                       color=colors[strategy], alpha=0.8, edgecolor='black', linewidth=0.8)

    ax.set_xlabel('LOTO Template (Test Set)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_title('Query-Level Prediction Error by Strategy', fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(TEMPLATES, rotation=0, fontsize=11)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()

    save_plot(fig, Path(output_dir) / 'comparison_plot.png')


# Export comparison summary CSV
def export_comparison_summary(all_stats: dict, output_dir: str) -> None:
    rows = []
    for strategy in STRATEGIES:
        overall_mre = all_stats[strategy]['overall']
        rows.append({
            'strategy': strategy,
            'overall_mre': overall_mre,
            'overall_mre_pct': overall_mre * 100
        })

    df = pd.DataFrame(rows)
    df.to_csv(Path(output_dir) / 'comparison_summary.csv', index=False, sep=';')


# Save plot to file
def save_plot(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=300, bbox_inches='tight')
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True, help="Output directory for evaluation results")

    args = parser.parse_args()

    evaluate_all_strategies(args.output_dir)
