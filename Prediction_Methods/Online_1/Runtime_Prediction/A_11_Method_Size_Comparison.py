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
from plot_config import DPI, STRATEGY_COLORS, LIGHT_CYAN, GROUPED_BAR_FIGSIZE, GROUPED_BAR_WIDTH, GROUPED_BAR_ALPHA, GRID_AXIS, GRID_ALPHA, GRID_LINESTYLE, apply_top_margin, ONLINE_1_MRE_Y_SCALE, ONLINE_1_MRE_Y_STEP


# ORCHESTRATOR

def comparison_workflow(online1_mre: str, hybrid2_mre: str, output_dir: str) -> None:
    data = load_mre_data(online1_mre, hybrid2_mre)
    create_comparison_plot(data, output_dir)


# FUNCTIONS

# Load MRE data from both CSVs
def load_mre_data(online1_path: str, hybrid2_path: str) -> dict:
    online1 = pd.read_csv(online1_path, delimiter=';', index_col=0)
    hybrid2 = pd.read_csv(hybrid2_path, delimiter=';', index_col=0)

    return {
        'Online_1': {
            'template_mre': online1['mean_mre_pct'].to_dict(),
            'overall_mre': online1['mean_mre'].mean() * 100
        },
        'Hybrid_2': {
            'template_mre': hybrid2['mean_mre_pct'].to_dict(),
            'overall_mre': hybrid2['mean_mre'].mean() * 100
        }
    }


# Create comparison bar plot
def create_comparison_plot(data: dict, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    templates = sorted(data['Online_1']['template_mre'].keys(), key=lambda x: int(x[1:]))
    x = np.arange(len(templates))

    fig, ax = plt.subplots(figsize=GROUPED_BAR_FIGSIZE)

    online1_values = [data['Online_1']['template_mre'].get(t, 0) for t in templates]
    hybrid2_values = [data['Hybrid_2']['template_mre'].get(t, 0) for t in templates]

    online1_overall = data['Online_1']['overall_mre']
    hybrid2_overall = data['Hybrid_2']['overall_mre']

    bars1 = ax.bar(x - GROUPED_BAR_WIDTH/2, online1_values, GROUPED_BAR_WIDTH,
                   label=f'Online_1 Size (Overall: {online1_overall:.2f}%)',
                   color=STRATEGY_COLORS['Size'], alpha=GROUPED_BAR_ALPHA)
    bars2 = ax.bar(x + GROUPED_BAR_WIDTH/2, hybrid2_values, GROUPED_BAR_WIDTH,
                   label=f'Hybrid_2 Size (Overall: {hybrid2_overall:.2f}%)',
                   color=LIGHT_CYAN, alpha=GROUPED_BAR_ALPHA)

    ax.bar_label(bars1, fmt='%.1f%%', padding=2, fontsize=8)
    ax.bar_label(bars2, fmt='%.1f%%', padding=2, fontsize=8)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis=GRID_AXIS, alpha=GRID_ALPHA, linestyle=GRID_LINESTYLE)

    plt.tight_layout()
    apply_top_margin(ax, fig, ONLINE_1_MRE_Y_SCALE, ONLINE_1_MRE_Y_STEP)
    plt.savefig(output_path / 'A_11_size_comparison.png', dpi=DPI, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("online1_mre", help="Path to Online_1 Size template_mre.csv")
    parser.add_argument("hybrid2_mre", help="Path to Hybrid_2 Size template_mre.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(args.online1_mre, args.hybrid2_mre, args.output_dir)
