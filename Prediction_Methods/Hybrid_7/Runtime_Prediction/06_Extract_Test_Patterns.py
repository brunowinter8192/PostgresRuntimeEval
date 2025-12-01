#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import hashlib
from pathlib import Path
from datetime import datetime


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int, df_index: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.df_index = df_index
        self.children = []

    # Append child node to children list
    def add_child(self, child_node):
        self.children.append(child_node)


# ORCHESTRATOR
def extract_test_patterns(test_file: str, patterns_file: str, output_dir: str) -> None:
    df_test = load_test_data(test_file)
    known_patterns = load_known_patterns(patterns_file)
    occurrences = find_all_pattern_occurrences(df_test, known_patterns)
    export_occurrences(occurrences, output_dir)


# FUNCTIONS

# Load test dataset filtered to main plan
def load_test_data(test_file: str) -> pd.DataFrame:
    df = pd.read_csv(test_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load known patterns from mining CSV
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


# Find all pattern occurrences in test set
def find_all_pattern_occurrences(df_test: pd.DataFrame, known_patterns: dict) -> list:
    occurrences = []
    queries = df_test['query_file'].unique()

    for query_file in queries:
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)
        query_occurrences = find_patterns_in_query(all_nodes, known_patterns, query_file, query_ops)
        occurrences.extend(query_occurrences)

    return occurrences


# Build tree structure from flat DataFrame
def build_tree_from_dataframe(query_ops: pd.DataFrame):
    nodes = {}
    root = None

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'],
            depth=row['depth'],
            node_id=row['node_id'],
            df_index=idx
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


# Find patterns in query by matching known pattern hashes
def find_patterns_in_query(all_nodes: list, known_patterns: dict, query_file: str, query_ops: pd.DataFrame) -> list:
    occurrences = []
    max_pattern_length = max(p['pattern_length'] for p in known_patterns.values())

    for node in all_nodes:
        for pattern_length in range(2, max_pattern_length + 1):
            if not has_children_at_length(node, pattern_length):
                break

            computed_hash = compute_pattern_hash_at_length(node, pattern_length)

            if computed_hash in known_patterns:
                pattern_info = known_patterns[computed_hash]
                occurrences.append({
                    'pattern_hash': computed_hash,
                    'pattern_string': pattern_info['pattern_string'],
                    'pattern_length': pattern_info['pattern_length'],
                    'operator_count': pattern_info['operator_count'],
                    'query_file': query_file,
                    'root_node_id': node.node_id,
                    'root_node_type': node.node_type,
                    'root_depth': node.depth
                })

    return occurrences


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


# Export occurrences to CSV
def export_occurrences(occurrences: list, output_dir: str) -> None:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = out_path / f'06_test_pattern_occurrences_{timestamp}.csv'

    df = pd.DataFrame(occurrences)
    df.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file', help='Path to Training_Test.csv')
    parser.add_argument('patterns_file', help='Path to 01_patterns_*.csv')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    args = parser.parse_args()

    extract_test_patterns(args.test_file, args.patterns_file, args.output_dir)
