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

    # Append child node to children list
    def add_child(self, child_node):
        self.children.append(child_node)


# ORCHESTRATOR
def extract_patterns_workflow(input_file: str, patterns_csv: str, output_dir: str) -> None:
    df = load_and_filter_data(input_file)
    pattern_info = load_pattern_info(patterns_csv)
    pattern_datasets = extract_all_pattern_occurrences(df, pattern_info)
    export_pattern_datasets(pattern_datasets, output_dir)


# FUNCTIONS

# Load training data and filter to main plan
def load_and_filter_data(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load pattern information from mining CSV
def load_pattern_info(patterns_csv: str) -> dict:
    patterns_df = pd.read_csv(patterns_csv, delimiter=';')
    pattern_info = {}

    for _, row in patterns_df.iterrows():
        pattern_hash = row['pattern_hash']
        pattern_info[pattern_hash] = {
            'pattern_string': row['pattern_string'],
            'pattern_length': row['pattern_length'],
            'operator_count': row['operator_count']
        }

    return pattern_info


# Extract all pattern occurrences from dataset
def extract_all_pattern_occurrences(df: pd.DataFrame, pattern_info: dict) -> dict:
    pattern_datasets = {pattern_hash: [] for pattern_hash in pattern_info.keys()}

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            for pattern_hash, info in pattern_info.items():
                pattern_length = info['pattern_length']

                if not has_children_at_length(node, pattern_length):
                    continue

                computed_hash = compute_pattern_hash_at_length(node, pattern_length)

                if computed_hash == pattern_hash:
                    pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
                    pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]
                    pattern_datasets[pattern_hash].append(pattern_rows)

    return pattern_datasets


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


# Extract node IDs of all nodes in pattern up to specified length
def extract_pattern_node_ids(node, remaining_length: int) -> list:
    if remaining_length == 1 or len(node.children) == 0:
        return [node.node_id]

    node_ids = [node.node_id]

    for child in node.children:
        child_ids = extract_pattern_node_ids(child, remaining_length - 1)
        node_ids.extend(child_ids)

    return node_ids


# Export pattern datasets to separate directories
def export_pattern_datasets(pattern_datasets: dict, output_dir: str) -> None:
    patterns_dir = Path(output_dir) / 'Patterns'

    for pattern_hash, dataframes in pattern_datasets.items():
        if len(dataframes) == 0:
            continue

        pattern_dir = patterns_dir / pattern_hash
        pattern_dir.mkdir(parents=True, exist_ok=True)

        combined_df = pd.concat(dataframes, ignore_index=True)
        output_file = pattern_dir / 'training.csv'
        combined_df.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to Training_Training.csv")
    parser.add_argument("patterns_csv", help="Path to patterns CSV from Data_Generation")
    parser.add_argument("--output-dir", required=True, help="Output directory (Dataset/)")
    args = parser.parse_args()

    extract_patterns_workflow(args.input_file, args.patterns_csv, args.output_dir)
