#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime


# ORCHESTRATOR

def depth_propagation_workflow(predictions_csv, output_dir):
    df = load_predictions(predictions_csv)
    df = add_template_column(df)
    templates = get_unique_templates(df)
    create_depth_plots(df, templates, output_dir)


# FUNCTIONS

# Load predictions from CSV file
def load_predictions(predictions_csv):
    return pd.read_csv(predictions_csv, delimiter=';')


# Add template column extracted from query filename
def add_template_column(df):
    df['template'] = df['query_file'].apply(lambda x: x.split('_')[0])
    return df


# Get list of unique templates
def get_unique_templates(df):
    return sorted(df['template'].unique(), key=lambda x: int(x[1:]))


# Create depth propagation plot for each template (averaged over queries)
def create_depth_plots(df, templates, output_dir):
    output_path = Path(output_dir) / 'Evaluation'
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    for template in templates:
        template_df = df[df['template'] == template].copy()

        depth_stats = template_df.groupby('depth').agg({
            'actual_total_time': 'mean',
            'predicted_total_time': 'mean'
        }).reset_index()
        depth_stats = depth_stats.sort_values('depth', ascending=False)

        fig, ax = plt.subplots(figsize=(10, 6))

        depths = depth_stats['depth'].values
        x_positions = range(len(depths))

        ax.plot(x_positions, depth_stats['actual_total_time'].values,
                'o-', color='tab:orange', label='Actual (mean)', linewidth=2, markersize=8)
        ax.plot(x_positions, depth_stats['predicted_total_time'].values,
                's--', color='tab:blue', label='Predicted (mean)', linewidth=2, markersize=8)

        ax.set_xticks(x_positions)
        ax.set_xticklabels([f'd{d}' for d in depths])
        ax.set_xlabel('Depth (Leaf -> Root)')
        ax.set_ylabel('Total Time (ms)')
        ax.set_title(f'{template} - Depth Propagation (averaged over queries)')
        ax.legend()
        ax.grid(True, alpha=0.3)

        for i, (d, act, pred) in enumerate(zip(depths,
                                                depth_stats['actual_total_time'],
                                                depth_stats['predicted_total_time'])):
            mre = abs(pred - act) / act * 100 if act > 0 else 0
            ax.annotate(f'{mre:.1f}%', (i, max(act, pred)), textcoords="offset points",
                       xytext=(0, 10), ha='center', fontsize=8, color='gray')

        plt.tight_layout()

        output_file = output_path / f'A_01d_depth_{template}_{timestamp}.png'
        plt.savefig(output_file, dpi=150)
        plt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions_csv", help="Path to predictions CSV file")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    depth_propagation_workflow(args.predictions_csv, args.output_dir)
