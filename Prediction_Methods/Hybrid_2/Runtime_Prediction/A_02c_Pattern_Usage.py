#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import hashlib
from pathlib import Path


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# ORCHESTRATOR
def analyze_pattern_usage(evaluation_dir: str, selection_dir: str, dataset_file: str, patterns_file: str, output_dir: str) -> None:
    pattern_templates = load_pattern_templates(dataset_file, patterns_file)
    for strategy in ['Size', 'Frequency', 'Error']:
        for config in ['Baseline', 'Epsilon']:
            usage_df = build_usage_for_config(evaluation_dir, selection_dir, strategy, config, pattern_templates)
            export_usage(usage_df, output_dir, strategy, config)


# FUNCTIONS

# Load pattern to templates mapping by scanning dataset
def load_pattern_templates(dataset_file: str, patterns_file: str) -> dict:
    df = pd.read_csv(dataset_file, delimiter=';')
    df = df[df['subplan_name'].isna() | (df['subplan_name'] == '')]
    known_patterns = load_known_patterns(patterns_file)

    templates = {}
    queries = df['query_file'].unique()

    for query_file in queries:
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)
        template = query_file.split('_')[0]

        for node in all_nodes:
            for pattern_length in range(2, max(p['pattern_length'] for p in known_patterns.values()) + 1):
                if not has_children_at_length(node, pattern_length):
                    break
                computed_hash = compute_pattern_hash_at_length(node, pattern_length)
                if computed_hash in known_patterns:
                    if computed_hash not in templates:
                        templates[computed_hash] = set()
                    templates[computed_hash].add(template)

    return templates


# Load known patterns from patterns CSV
def load_known_patterns(patterns_file: str) -> dict:
    df = pd.read_csv(patterns_file, delimiter=';')
    patterns = {}
    for _, row in df.iterrows():
        patterns[row['pattern_hash']] = {
            'pattern_string': row['pattern_string'],
            'pattern_length': row['pattern_length'],
            'operator_count': row['operator_count']
        }
    return patterns


# Build tree structure from flat DataFrame
def build_tree_from_dataframe(query_ops: pd.DataFrame):
    nodes = {}
    root = None

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'] if pd.notna(row['parent_relationship']) else '',
            depth=row['depth'],
            node_id=row['node_id']
        )
        nodes[row['node_id']] = node
        if row['depth'] == 0:
            root = node

    for idx, row in query_ops.iterrows():
        current_node = nodes[row['node_id']]
        current_depth = row['depth']

        for j in range(idx + 1, len(query_ops)):
            next_row = query_ops.iloc[j]
            if next_row['depth'] == current_depth + 1:
                child_node = nodes[next_row['node_id']]
                current_node.add_child(child_node)
            elif next_row['depth'] <= current_depth:
                break

    return root


# Extract all nodes from tree recursively
def extract_all_nodes(node) -> list:
    nodes = [node]
    for child in node.children:
        nodes.extend(extract_all_nodes(child))
    return nodes


# Check if node has children at target pattern length
def has_children_at_length(node, pattern_length: int) -> bool:
    if pattern_length == 1:
        return True
    if pattern_length == 2:
        return len(node.children) > 0
    if len(node.children) == 0:
        return False
    return any(has_children_at_length(child, pattern_length - 1) for child in node.children)


# Compute structural hash for pattern at specific length
def compute_pattern_hash_at_length(node, remaining_length: int) -> str:
    if remaining_length == 1 or len(node.children) == 0:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_pattern_hash_at_length(child, remaining_length - 1)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)
    return hashlib.md5(combined_string.encode()).hexdigest()


# Build usage table for one strategy/config combination
def build_usage_for_config(evaluation_dir: str, selection_dir: str, strategy: str, config: str, pattern_templates: dict) -> pd.DataFrame:
    selected = load_selected_patterns(selection_dir, strategy, config)
    used_patterns = load_used_patterns(evaluation_dir, strategy, config)

    rows = []
    for _, row in selected.iterrows():
        pattern_hash = row['pattern_hash']
        pattern_string = row['pattern_string']
        status = 'genutzt' if pattern_hash in used_patterns else 'beifang'
        templates = sorted(pattern_templates.get(pattern_hash, set()), key=lambda x: int(x[1:]))
        templates_used = sorted(used_patterns.get(pattern_hash, set()), key=lambda x: int(x[1:])) if pattern_hash in used_patterns else []
        rows.append({
            'pattern_hash': pattern_hash,
            'pattern_string': pattern_string,
            'status': status,
            'templates': ','.join(templates),
            'templates_used': ','.join(templates_used)
        })

    return pd.DataFrame(rows)


# Load selected patterns from Pattern_Selection directory
def load_selected_patterns(selection_dir: str, strategy: str, config: str) -> pd.DataFrame:
    sel_file = Path(selection_dir) / strategy / config / 'selected_patterns.csv'
    if sel_file.exists():
        return pd.read_csv(sel_file, delimiter=';')[['pattern_hash', 'pattern_string']]
    return pd.DataFrame(columns=['pattern_hash', 'pattern_string'])


# Load used patterns with their templates from predictions
def load_used_patterns(evaluation_dir: str, strategy: str, config: str) -> dict:
    pred_file = Path(evaluation_dir) / strategy / config / '12_predictions.csv'
    if pred_file.exists():
        df = pd.read_csv(pred_file, delimiter=';')
        pattern_preds = df[df['prediction_type'] == 'pattern']

        used = {}
        for _, row in pattern_preds.iterrows():
            ph = row['pattern_hash']
            if pd.isna(ph):
                continue
            template = row['query_file'].split('_')[0]
            if ph not in used:
                used[ph] = set()
            used[ph].add(template)
        return used
    return {}


# Export usage table for one strategy/config
def export_usage(usage_df: pd.DataFrame, output_dir: str, strategy: str, config: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    filename = f'A_02c_{strategy}_{config}.csv'
    usage_df.to_csv(output_path / filename, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('evaluation_dir', help='Path to Evaluation directory')
    parser.add_argument('--selection-dir', required=True, help='Path to Pattern_Selection directory')
    parser.add_argument('--dataset', required=True, help='Dataset CSV (e.g., Training_Training.csv)')
    parser.add_argument('--patterns', required=True, help='Patterns CSV (e.g., 01_patterns_baseline.csv)')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    args = parser.parse_args()

    analyze_pattern_usage(args.evaluation_dir, args.selection_dir, args.dataset, args.patterns, args.output_dir)
