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
from plot_config import DPI, DEEP_BLUE, DEEP_GREEN, DEEP_ORANGE

SCRIPT_DIR = Path(__file__).resolve().parent
ANALYSIS_DIR = SCRIPT_DIR / 'Evaluation' / 'Analysis'


# ORCHESTRATOR
def combined_strategy_workflow(output_dir: str) -> None:
    data = load_all_mre_data()
    combined_df = create_combined_dataframe(data)
    export_combined_csv(combined_df, output_dir)
    create_combined_plot(data, output_dir)


# FUNCTIONS

# Load all MRE data from CSV files
def load_all_mre_data() -> dict:
    return {
        'Size': load_template_mre(ANALYSIS_DIR / 'Size' / 'template_mre.csv'),
        'Frequency': load_template_mre(ANALYSIS_DIR / 'Frequency' / 'template_mre.csv'),
        'Error': load_template_mre(ANALYSIS_DIR / 'Error' / 'template_mre.csv')
    }


# Load template MRE from CSV
def load_template_mre(csv_path: Path) -> dict:
    df = pd.read_csv(csv_path, delimiter=';', index_col=0)
    overall_mre = df['mean_mre'].mean()
    return {
        'template_mre': df['mean_mre_pct'].to_dict(),
        'overall_mre': overall_mre * 100
    }


# Create combined dataframe with all strategies
def create_combined_dataframe(data: dict) -> pd.DataFrame:
    rows = []
    templates = sorted(data['Size']['template_mre'].keys(), key=lambda x: int(x[1:]))

    for template in templates:
        row = {'template': template}
        for strategy in ['Size', 'Frequency', 'Error']:
            row[f'{strategy.lower()}_mre_pct'] = data[strategy]['template_mre'].get(template, np.nan)
        rows.append(row)

    df = pd.DataFrame(rows)
    df.set_index('template', inplace=True)
    return df


# Export combined CSV
def export_combined_csv(combined_df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    combined_df.to_csv(output_path / 'A_06_strategy_comparison.csv', sep=';')


# Create combined bar plot
def create_combined_plot(data: dict, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    templates = sorted(data['Size']['template_mre'].keys(), key=lambda x: int(x[1:]))
    x = np.arange(len(templates))

    fig, ax = plt.subplots(figsize=(18, 8))

    strategies = ['Size', 'Frequency', 'Error']
    colors = [DEEP_BLUE, DEEP_GREEN, DEEP_ORANGE]
    offsets = [-1.0, 0.0, 1.0]
    width = 0.25

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
    plt.savefig(output_path / 'A_06_strategy_comparison.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(ANALYSIS_DIR / 'Overall'), help="Output directory")
    args = parser.parse_args()

    combined_strategy_workflow(args.output_dir)
