#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime
import hashlib


# ORCHESTRATOR
def identify_pattern_plan_leafs(pattern_csv: str, input_file: str, output_dir: str) -> None:
    patterns = load_pattern_data(pattern_csv)
    df = load_and_filter_data(input_file)
    pattern_leaf_info = process_all_patterns(patterns, df)
    export_results(pattern_leaf_info, output_dir)


# FUNCTIONS

# Load pattern definitions from 01_Find_Patterns.py output
def load_pattern_data(pattern_csv: str) -> pd.DataFrame:
    return pd.read_csv(pattern_csv, delimiter=';')

# Load training data and filter to main plan
def load_and_filter_data(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]

# Process all patterns and identify plan leafs
def process_all_patterns(patterns: pd.DataFrame, df: pd.DataFrame) -> list:
    results = []

    for _, pattern_row in patterns.iterrows():
        pattern_hash = pattern_row['pattern_hash']
        pattern_length = pattern_row['pattern_length']

        leaf_plan_status = analyze_pattern_leafs(
            df, pattern_hash, pattern_length
        )

        for leaf_info in leaf_plan_status:
            results.append({
                'pattern_hash': pattern_hash,
                'pattern_length': pattern_length,
                'pattern_leaf_prefix': leaf_info['prefix'],
                'node_type': leaf_info['node_type'],
                'is_plan_leaf': 'ja' if leaf_info['is_plan_leaf'] else 'nein'
            })

    return results

# Analyze pattern leafs across all occurrences
def analyze_pattern_leafs(df: pd.DataFrame, target_hash: str, pattern_length: int) -> list:
    leaf_map = {}

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            current_hash = compute_pattern_hash_at_length(node, pattern_length)

            if current_hash == target_hash:
                leafs = extract_pattern_leaf_info(node, pattern_length)

                for leaf in leafs:
                    key = (leaf['prefix'], leaf['node_type'])

                    if key not in leaf_map:
                        leaf_map[key] = []

                    leaf_map[key].append(leaf['is_plan_leaf'])

    results = []
    for (prefix, node_type), plan_leaf_flags in leaf_map.items():
        is_plan_leaf = all(plan_leaf_flags)
        results.append({
            'prefix': prefix,
            'node_type': node_type,
            'is_plan_leaf': is_plan_leaf
        })

    return sorted(results, key=lambda x: x['prefix'])

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

# Extract pattern leaf nodes with plan leaf status
def extract_pattern_leaf_info(node, remaining_length: int, is_root: bool = True) -> list:
    if remaining_length == 1 or len(node.children) == 0:
        if is_root:
            return []

        prefix = clean_node_type(node.node_type) + '_' + node.parent_relationship
        is_plan_leaf = len(node.children) == 0

        return [{
            'prefix': prefix,
            'node_type': node.node_type,
            'is_plan_leaf': is_plan_leaf
        }]

    leaf_info = []

    for child in node.children:
        child_leafs = extract_pattern_leaf_info(child, remaining_length - 1, is_root=False)
        leaf_info.extend(child_leafs)

    return leaf_info

# Clean node type for column naming
def clean_node_type(node_type: str) -> str:
    return node_type.replace(' ', '')

# Save pattern leaf plan status to CSV with timestamp
def export_results(pattern_leaf_info: list, output_dir: str) -> None:
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = csv_dir / f'02b_pattern_plan_leafs_{timestamp}.csv'

    df = pd.DataFrame(pattern_leaf_info)
    df.to_csv(output_file, sep=';', index=False)


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern_csv", help="Path to 01_patterns_*.csv from Data_Generation")
    parser.add_argument("input_file", help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for pattern plan leaf info")
    args = parser.parse_args()

    identify_pattern_plan_leafs(args.pattern_csv, args.input_file, args.output_dir)
