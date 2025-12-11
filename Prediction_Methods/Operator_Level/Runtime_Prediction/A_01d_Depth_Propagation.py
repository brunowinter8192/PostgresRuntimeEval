#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import hashlib
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from adjustText import adjust_text


# ORCHESTRATOR

def depth_propagation_workflow(structure_csv, predictions_csv, output_dir):
    df_structure = load_csv(structure_csv)
    df_predictions = load_csv(predictions_csv)
    plan_hash_map = build_plan_hash_map(df_structure)
    df = merge_with_plan_hash(df_predictions, plan_hash_map)
    df = add_template_column(df)
    plan_hashes = get_unique_plan_hashes(df)
    create_depth_plots(df, plan_hashes, output_dir)


# FUNCTIONS

# Load CSV file
def load_csv(csv_path):
    return pd.read_csv(csv_path, delimiter=';')


# Compute hash for unique plan structure (operator types + depths + relationships)
def compute_plan_hash(query_ops):
    sorted_ops = query_ops.sort_values('node_id')
    structure = [(row['node_type'], row['depth'], row['parent_relationship'])
                 for _, row in sorted_ops.iterrows()]
    return hashlib.md5(str(structure).encode()).hexdigest()


# Build plan hash map from structure CSV
def build_plan_hash_map(df_structure):
    plan_hashes = {}
    for query_file in df_structure['query_file'].unique():
        query_ops = df_structure[df_structure['query_file'] == query_file]
        plan_hashes[query_file] = compute_plan_hash(query_ops)
    return plan_hashes


# Merge predictions with plan hash from structure
def merge_with_plan_hash(df_predictions, plan_hash_map):
    df_predictions['plan_hash'] = df_predictions['query_file'].map(plan_hash_map)
    return df_predictions


# Add template column extracted from query filename
def add_template_column(df):
    df['template'] = df['query_file'].apply(lambda x: x.split('_')[0])
    return df


# Get list of unique plan hashes per template
def get_unique_plan_hashes(df):
    return df.groupby(['template', 'plan_hash']).first().reset_index()[['plan_hash', 'template']].values.tolist()


# Create depth propagation plot for each plan hash
def create_depth_plots(df, plan_hashes, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for plan_hash, template in plan_hashes:
        plan_df = df[(df['plan_hash'] == plan_hash) & (df['template'] == template)].copy()

        depth_stats = plan_df.groupby('depth').agg({
            'actual_total_time': 'mean',
            'predicted_total_time': 'mean'
        }).reset_index()

        unique_depths = sorted(depth_stats['depth'].unique(), reverse=True)
        depth_to_x = {d: i for i, d in enumerate(unique_depths)}

        depth_stats['x'] = depth_stats['depth'].map(depth_to_x)
        depth_stats = depth_stats.sort_values('x')

        fig, ax = plt.subplots(figsize=(12, 7))

        ax.plot(depth_stats['x'], depth_stats['actual_total_time'],
                color='tab:orange', marker='o', markersize=8, linewidth=2,
                alpha=0.7, label='Actual', zorder=3)

        ax.plot(depth_stats['x'], depth_stats['predicted_total_time'],
                color='tab:blue', marker='s', markersize=8, linewidth=2,
                alpha=0.7, label='Predicted', zorder=3)

        texts = []
        for _, row in depth_stats.iterrows():
            x = row['x']
            act = row['actual_total_time']
            pred = row['predicted_total_time']
            texts.append(ax.text(x, act, f'A: {act:.2f}', fontsize=8, ha='center'))
            texts.append(ax.text(x, pred, f'P: {pred:.2f}', fontsize=8, ha='center'))

        adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle='-', color='gray', alpha=0.5))

        ax.set_xticks(range(len(unique_depths)))
        ax.set_xticklabels([f'd{d}' for d in unique_depths])
        ax.set_xlabel('Depth (Leaf -> Root)')
        ax.set_ylabel('Total Time (ms)')
        ax.set_title(f'{template} - Depth Propagation (plan: {plan_hash[:8]})')
        ax.legend()
        ax.grid(True, alpha=0.3)

        plt.tight_layout()

        output_file = output_path / f'A_01d_depth_{template}_{plan_hash[:8]}.png'
        plt.savefig(output_file, dpi=150)
        plt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("structure_csv", help="Path to structure CSV (test.csv) for plan hash")
    parser.add_argument("predictions_csv", help="Path to predictions CSV file")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    depth_propagation_workflow(args.structure_csv, args.predictions_csv, args.output_dir)
