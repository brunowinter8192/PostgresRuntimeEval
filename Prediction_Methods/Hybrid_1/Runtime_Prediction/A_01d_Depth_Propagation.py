#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import hashlib
import sys
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from adjustText import adjust_text

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from plot_config import DEEP_BLUE, DEEP_ORANGE, DPI


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


# Build operator label with prediction type prefix
def build_operator_label(node_type, prediction_type):
    if prediction_type == 'pattern':
        return f'P_{node_type}'
    return node_type


# Create depth propagation plot for each plan hash
def create_depth_plots(df, plan_hashes, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for plan_hash, template in plan_hashes:
        plan_df = df[(df['plan_hash'] == plan_hash) & (df['template'] == template)].copy()
        sample_query = plan_df['query_file'].iloc[0]
        query_ops = plan_df[plan_df['query_file'] == sample_query].copy()
        query_ops = sort_tree_order(query_ops)

        fig, ax = plt.subplots(figsize=(14, 7))

        x_positions = range(len(query_ops))
        actual_values = query_ops['actual_total_time'].values
        predicted_values = query_ops['predicted_total_time'].values

        ax.plot(x_positions, actual_values,
                color=DEEP_ORANGE, marker='o', markersize=8, linewidth=2,
                alpha=0.7, label='Actual', zorder=3)

        ax.plot(x_positions, predicted_values,
                color=DEEP_BLUE, marker='s', markersize=8, linewidth=2,
                alpha=0.7, label='Predicted', zorder=3)

        texts = []
        for i, (_, row) in enumerate(query_ops.iterrows()):
            act = row['actual_total_time']
            pred = row['predicted_total_time']
            texts.append(ax.text(i, act, f'{act:.1f}', fontsize=7, ha='center'))
            texts.append(ax.text(i, pred, f'{pred:.1f}', fontsize=7, ha='center'))

        adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle='-', color='gray', alpha=0.5))

        labels = [f"{build_operator_label(row['node_type'], row['prediction_type'])}\n(d{row['depth']})"
                  for _, row in query_ops.iterrows()]
        ax.set_xticks(x_positions)
        ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)
        ax.set_xlabel('Operator (Leaf -> Root)')
        ax.set_ylabel('Total Time (ms)')
        ax.legend()
        ax.grid(True, alpha=0.3)

        plt.tight_layout()

        output_file = output_path / f'A_01d_depth_{template}_{plan_hash[:8]}.png'
        plt.savefig(output_file, dpi=DPI)
        plt.close()


# Sort operators in tree traversal order (highest depth left, root right, Outer before Inner)
def sort_tree_order(query_ops):
    query_ops = query_ops[
        (query_ops['actual_total_time'] > 0.0001) | (query_ops['predicted_total_time'] > 0.0001)
    ].copy()
    relationship_order = {'Outer': 0, 'Inner': 1, '': 2}
    query_ops['rel_order'] = query_ops['parent_relationship'].map(
        lambda x: relationship_order.get(x, 2) if pd.notna(x) else 2
    )
    query_ops = query_ops.sort_values(['depth', 'rel_order'], ascending=[False, True])
    return query_ops.drop(columns=['rel_order'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("structure_csv", help="Path to structure CSV (test.csv) for plan hash")
    parser.add_argument("predictions_csv", help="Path to predictions CSV file")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    depth_propagation_workflow(args.structure_csv, args.predictions_csv, args.output_dir)
