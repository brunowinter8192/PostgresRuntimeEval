#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import hashlib


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
def lookup_pattern_templates(selected_patterns_file: str, patterns_file: str, dataset_file: str, output_dir: str, output_name: str, pattern_hash: str = None, pattern_string: str = None) -> None:
    if pattern_hash:
        selected = pd.DataFrame([{'pattern_hash': pattern_hash, 'pattern_string': pattern_string or ''}])
    else:
        selected = load_selected_patterns(selected_patterns_file)
    pattern_lengths = load_pattern_lengths(patterns_file)
    df = load_and_filter_data(dataset_file)
    results = find_all_pattern_templates(df, selected, pattern_lengths)
    export_results(results, output_dir, output_name)


# FUNCTIONS

# Load selected patterns from selection output
def load_selected_patterns(selected_patterns_file: str) -> pd.DataFrame:
    df = pd.read_csv(selected_patterns_file, delimiter=';')
    return df[['pattern_hash', 'pattern_string']]


# Load pattern lengths from patterns.csv
def load_pattern_lengths(patterns_file: str) -> dict:
    df = pd.read_csv(patterns_file, delimiter=';')
    return dict(zip(df['pattern_hash'], df['pattern_length']))


# Load dataset and filter to main plan
def load_and_filter_data(dataset_file: str) -> pd.DataFrame:
    df = pd.read_csv(dataset_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Find templates for all selected patterns
def find_all_pattern_templates(df: pd.DataFrame, selected: pd.DataFrame, pattern_lengths: dict) -> list:
    pattern_templates = {row['pattern_hash']: set() for _, row in selected.iterrows()}

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)
        template = query_file.split('_')[0]

        for _, row in selected.iterrows():
            pattern_hash = row['pattern_hash']
            pattern_length = pattern_lengths.get(pattern_hash, 2)

            for node in all_nodes:
                if not has_children_at_length(node, pattern_length):
                    continue
                node_hash = compute_pattern_hash_at_length(node, pattern_length)
                if node_hash == pattern_hash:
                    pattern_templates[pattern_hash].add(template)
                    break

    results = []
    for _, row in selected.iterrows():
        pattern_hash = row['pattern_hash']
        templates = sorted(pattern_templates[pattern_hash], key=lambda x: int(x[1:]))
        results.append({
            'pattern_hash': pattern_hash,
            'pattern_string': row['pattern_string'],
            'templates': ','.join(templates)
        })

    return results


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


# Export results to CSV
def export_results(results: list, output_dir: str, output_name: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(results)
    df.to_csv(output_path / f'{output_name}.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('selected_patterns', nargs='?', default=None, help='Path to selected_patterns.csv')
    parser.add_argument('--patterns', required=True, help='Path to 01_patterns.csv')
    parser.add_argument('--dataset', required=True, help='Path to dataset CSV')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    parser.add_argument('--output-name', default='A_03c_pattern_templates', help='Output filename (without .csv)')
    parser.add_argument('--pattern-hash', help='Single pattern hash (alternative to selected_patterns file)')
    parser.add_argument('--pattern-string', help='Pattern string for single pattern mode')
    args = parser.parse_args()

    if not args.pattern_hash and not args.selected_patterns:
        parser.error('Either selected_patterns or --pattern-hash is required')

    lookup_pattern_templates(args.selected_patterns, args.patterns, args.dataset, args.output_dir, args.output_name, args.pattern_hash, args.pattern_string)
