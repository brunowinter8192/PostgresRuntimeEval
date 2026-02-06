#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from adjustText import adjust_text

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
from plot_config import STRATEGY_COLORS, DPI


# ORCHESTRATOR

def propagation_workflow(evaluation_dir: str, template: str, output_dir: str) -> None:
    queries = get_template_queries(evaluation_dir, template)
    ref_query = queries[0]
    ref_size = load_sorted_predictions(evaluation_dir, 'Size', ref_query)
    ref_freq = load_sorted_predictions(evaluation_dir, 'Frequency', ref_query)
    combined_nodes = build_combined_node_list(ref_size, ref_freq)
    node_to_x = {row['node_id']: i for i, (_, row) in enumerate(combined_nodes.iterrows())}
    size_pos, size_means = aggregate_on_positions(evaluation_dir, 'Size', queries, combined_nodes)
    freq_pos, freq_means = aggregate_on_positions(evaluation_dir, 'Frequency', queries, combined_nodes)
    labels = build_labels(combined_nodes, ref_size, ref_freq)
    create_combined_plot(labels, size_pos, size_means, freq_pos, freq_means, template, output_dir)


# FUNCTIONS

# Get all query folders for a template present in both strategies
def get_template_queries(evaluation_dir: str, template: str) -> list:
    size_dir = Path(evaluation_dir) / 'Size'
    freq_dir = Path(evaluation_dir) / 'Frequency'
    size_queries = {d.name for d in size_dir.iterdir() if d.is_dir() and d.name.startswith(template + '_')}
    freq_queries = {d.name for d in freq_dir.iterdir() if d.is_dir() and d.name.startswith(template + '_')}
    return sorted(size_queries & freq_queries)


# Load and sort predictions for one query
def load_sorted_predictions(evaluation_dir: str, strategy: str, query: str) -> pd.DataFrame:
    path = Path(evaluation_dir) / strategy / query / 'csv' / 'predictions.csv'
    df = pd.read_csv(path, delimiter=';')
    relationship_order = {'Outer': 0, 'Inner': 1}
    df = df.copy()
    df['rel_order'] = df['parent_relationship'].map(
        lambda x: relationship_order.get(x, 2) if pd.notna(x) else 2
    )
    df = df.sort_values(['depth', 'rel_order'], ascending=[False, True])
    return df.drop(columns=['rel_order']).reset_index(drop=True)


# Build combined node list from reference query sorted leaf to root
def build_combined_node_list(ref_size: pd.DataFrame, ref_freq: pd.DataFrame) -> pd.DataFrame:
    combined = pd.concat([ref_size, ref_freq]).drop_duplicates(subset='node_id')
    relationship_order = {'Outer': 0, 'Inner': 1}
    combined = combined.copy()
    combined['rel_order'] = combined['parent_relationship'].map(
        lambda x: relationship_order.get(x, 2) if pd.notna(x) else 2
    )
    combined = combined.sort_values(['depth', 'rel_order'], ascending=[False, True])
    return combined.drop(columns=['rel_order']).reset_index(drop=True)


# Aggregate mean predictions for a strategy across all queries using position index
def aggregate_on_positions(evaluation_dir: str, strategy: str, queries: list, combined_nodes: pd.DataFrame) -> tuple:
    ref_query = queries[0]
    ref_df = load_sorted_predictions(evaluation_dir, strategy, ref_query)
    ref_node_ids = ref_df['node_id'].tolist()
    combined_node_ids = combined_nodes['node_id'].tolist()

    positions = [combined_node_ids.index(nid) for nid in ref_node_ids]

    all_values = []
    for query in queries:
        df = load_sorted_predictions(evaluation_dir, strategy, query)
        all_values.append(df['predicted_total_time'].values)

    means = np.mean(all_values, axis=0)
    return positions, means.tolist()


# Build X-axis labels with P_ prefix per strategy
def build_labels(combined_nodes: pd.DataFrame, ref_size: pd.DataFrame, ref_freq: pd.DataFrame) -> list:
    size_ids = set(ref_size['node_id'].tolist())
    freq_ids = set(ref_freq['node_id'].tolist())
    size_patterns = set(ref_size[ref_size['prediction_type'] == 'pattern']['node_id'].tolist())
    freq_patterns = set(ref_freq[ref_freq['prediction_type'] == 'pattern']['node_id'].tolist())

    labels = []
    for _, row in combined_nodes.iterrows():
        nid = row['node_id']
        node_type = row['node_type']
        depth = row['depth']

        in_size_pattern = nid in size_patterns
        in_freq_pattern = nid in freq_patterns

        if in_size_pattern and in_freq_pattern:
            prefix = 'P_'
        elif in_size_pattern:
            prefix = 'Ps_'
        elif in_freq_pattern:
            prefix = 'Pf_'
        else:
            prefix = ''

        labels.append(f"{prefix}{node_type}\n(d{depth})")

    return labels


# Create combined propagation plot with mean values
def create_combined_plot(labels, size_pos, size_means, freq_pos, freq_means,
                         template: str, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(14, 7))

    ax.plot(size_pos, size_means,
            color=STRATEGY_COLORS['Size'], marker='s', markersize=8, linewidth=2,
            alpha=0.7, label='Size', zorder=3)

    ax.plot(freq_pos, freq_means,
            color=STRATEGY_COLORS['Frequency'], marker='o', markersize=8, linewidth=2,
            alpha=0.7, label='Frequency', zorder=3)

    texts = []
    for x, y in zip(size_pos, size_means):
        texts.append(ax.text(x, y, f'{y:.1f}', fontsize=7, ha='center'))
    for x, y in zip(freq_pos, freq_means):
        texts.append(ax.text(x, y, f'{y:.1f}', fontsize=7, ha='center'))

    adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle='-', color='gray', alpha=0.5))

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)
    ax.set_xlabel('Operator (Leaf -> Root)')
    ax.set_ylabel('Mean Predicted Total Time (ms)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path / f'A_14_propagation_{template}.png', dpi=DPI)
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("evaluation_dir", help="Path to Evaluation directory")
    parser.add_argument("--template", required=True, help="Template name (e.g. Q5)")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    propagation_workflow(args.evaluation_dir, args.template, args.output_dir)
