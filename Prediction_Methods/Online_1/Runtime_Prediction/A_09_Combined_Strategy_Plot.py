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
from plot_config import DPI, STRATEGY_COLORS, DEEP_RED


# ORCHESTRATOR
def combined_strategy_workflow(size_mre: str, frequency_mre: str, error_mre: str, optimizer_mre: str, output_dir: str) -> None:
    data = load_all_mre_data(size_mre, frequency_mre, error_mre, optimizer_mre)
    combined_df = create_combined_dataframe(data)
    export_combined_csv(combined_df, output_dir)
    create_combined_plot(data, output_dir)


# FUNCTIONS

# Load all MRE data from CSV files
def load_all_mre_data(size_mre: str, frequency_mre: str, error_mre: str, optimizer_mre: str) -> dict:
    return {
        'Size': load_template_mre(size_mre),
        'Frequency': load_template_mre(frequency_mre),
        'Error': load_template_mre(error_mre),
        'Optimizer': load_optimizer_mre(optimizer_mre)
    }


# Load template MRE from CSV
def load_template_mre(csv_path: str) -> dict:
    df = pd.read_csv(csv_path, delimiter=';', index_col=0)
    overall_mre = df['mean_mre'].mean()
    return {
        'template_mre': df['mean_mre_pct'].to_dict(),
        'overall_mre': overall_mre * 100
    }


# Load optimizer MRE from CSV (different column names)
def load_optimizer_mre(csv_path: str) -> dict:
    df = pd.read_csv(csv_path, delimiter=';', index_col=0)
    overall_mre = df['mre_optimizer'].mean()
    return {
        'template_mre': df['mre_optimizer_pct'].to_dict(),
        'overall_mre': overall_mre * 100
    }


# Create combined dataframe with all strategies
def create_combined_dataframe(data: dict) -> pd.DataFrame:
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
def export_combined_csv(combined_df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    combined_df.to_csv(output_path / 'A_09_combined_strategy_mre.csv', sep=';')


# Create combined bar plot
def create_combined_plot(data: dict, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    templates = sorted(data['Size']['template_mre'].keys(), key=lambda x: int(x[1:]))
    x = np.arange(len(templates))

    fig, ax = plt.subplots(figsize=(18, 8))

    y_limit = 10
    strategies = ['Size', 'Frequency', 'Error', 'Optimizer']
    colors = [STRATEGY_COLORS['Size'], STRATEGY_COLORS['Frequency'], STRATEGY_COLORS['Error'], STRATEGY_COLORS['Optimizer']]
    offsets = [-1.5, -0.5, 0.5, 1.5]
    width = 0.2

    for strategy, color, offset in zip(strategies, colors, offsets):
        actual_values = [data[strategy]['template_mre'].get(t, 0) for t in templates]
        display_values = [min(v, y_limit) for v in actual_values]
        overall = data[strategy]['overall_mre']
        display_name = "Optimizer Cost Model" if strategy == "Optimizer" else strategy
        label = f"{display_name} (Overall: {overall:.2f}%)"
        bars = ax.bar(x + offset * width, display_values, width, label=label, color=color, alpha=0.85)

        for i, bar in enumerate(bars):
            actual = actual_values[i]
            template = templates[i]
            label_color = DEEP_RED if actual > y_limit else 'black'
            if template in ['Q14', 'Q19'] and strategy == 'Optimizer' and actual > y_limit:
                ax.text(bar.get_x() + bar.get_width()/2., 9.0,
                        f'{actual:.1f}%', ha='center', va='top', fontsize=6, color=label_color)
            elif template == 'Q18' and actual > y_limit:
                ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() - 1,
                        f'{actual:.1f}%', ha='center', va='top', fontsize=6, color=label_color)
            else:
                ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
                        f'{actual:.1f}%', ha='center', va='bottom', fontsize=6, color=label_color)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    ax.set_ylim(0, y_limit * 1.1)

    plt.tight_layout()
    plt.savefig(output_path / 'A_09_combined_strategy_plot.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--size-mre", required=True, help="Path to Size template_mre.csv")
    parser.add_argument("--frequency-mre", required=True, help="Path to Frequency template_mre.csv")
    parser.add_argument("--error-mre", required=True, help="Path to Error template_mre.csv")
    parser.add_argument("--optimizer-mre", required=True, help="Path to Optimizer template_mre.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    combined_strategy_workflow(
        args.size_mre, args.frequency_mre, args.error_mre,
        args.optimizer_mre, args.output_dir
    )
