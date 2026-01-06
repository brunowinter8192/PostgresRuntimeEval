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
def lookup_pattern(pattern_hash: str, patterns_file: str, dataset_file: str, output_dir: str) -> None:
    pattern_info = load_pattern_info(pattern_hash, patterns_file)
    df = load_and_filter_data(dataset_file)
    matches = find_pattern_occurrences(df, pattern_hash, pattern_info['pattern_length'])
    export_results(matches, pattern_info, output_dir)


# FUNCTIONS

# Load pattern metadata from patterns.csv
def load_pattern_info(pattern_hash: str, patterns_file: str) -> dict:
    df = pd.read_csv(patterns_file, delimiter=';')
    row = df[df['pattern_hash'] == pattern_hash]
    if row.empty:
        raise ValueError(f"Pattern hash {pattern_hash} not found in {patterns_file}")
    return row.iloc[0].to_dict()


# Load dataset and filter to main plan
def load_and_filter_data(dataset_file: str) -> pd.DataFrame:
    df = pd.read_csv(dataset_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Find all occurrences of pattern in dataset
def find_pattern_occurrences(df: pd.DataFrame, target_hash: str, pattern_length: int) -> list:
    matches = []

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            if not has_children_at_length(node, pattern_length):
                continue

            node_hash = compute_pattern_hash_at_length(node, pattern_length)
            if node_hash == target_hash:
                matches.append({
                    'query_file': query_file,
                    'root_node_id': node.node_id,
                    'root_node_type': node.node_type,
                    'root_depth': node.depth
                })

    return matches


# Build tree structure from flat DataFrame
def build_tree_from_dataframe(query_ops: pd.DataFrame):
    nodes = {}
    root = None

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'],
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


# Export matches to CSV
def export_results(matches: list, pattern_info: dict, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    pattern_hash = pattern_info['pattern_hash']
    short_hash = pattern_hash[:8]

    df = pd.DataFrame(matches)
    df.to_csv(output_path / f'A_03b_{short_hash}_matches.csv', sep=';', index=False)

    summary = {
        'pattern_hash': pattern_hash,
        'pattern_string': pattern_info['pattern_string'],
        'pattern_length': pattern_info['pattern_length'],
        'operator_count': pattern_info['operator_count'],
        'total_matches': len(matches),
        'unique_queries': df['query_file'].nunique() if len(matches) > 0 else 0
    }

    summary_df = pd.DataFrame([summary])
    summary_df.to_csv(output_path / f'A_03b_{short_hash}_summary.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern_hash", help="Pattern hash to search for")
    parser.add_argument("--patterns-file", required=True, help="Path to patterns.csv")
    parser.add_argument("--dataset-file", required=True, help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    lookup_pattern(args.pattern_hash, args.patterns_file, args.dataset_file, args.output_dir)
