#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import hashlib
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

# From mapping_config.py: Pattern operator counts
from mapping_config import PATTERN_OPERATOR_COUNT

# ORCHESTRATOR
def aggregate_patterns_workflow(pattern_csv: str, patterns_base_dir: str) -> None:
    pattern_data = load_pattern_data(pattern_csv)
    for _, row in pattern_data.iterrows():
        pattern_folder = Path(patterns_base_dir) / row['pattern_hash']
        if pattern_folder.exists():
            process_pattern_folder(pattern_folder, row['pattern_hash'], row['pattern_length'])


# FUNCTIONS

# Load pattern data from Data_Generation/01_Find_Patterns.py output
def load_pattern_data(pattern_csv: str) -> pd.DataFrame:
    df = pd.read_csv(pattern_csv, delimiter=';')
    return df[['pattern_hash', 'pattern_string', 'pattern_length']]

# Build tree structure from flat DataFrame for single query
def build_tree_from_query(query_ops):
    nodes = {}
    root = None
    min_depth = query_ops['depth'].min()

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'],
            depth=row['depth'],
            node_id=row['node_id'],
            row_data=row
        )
        nodes[row['node_id']] = node

        if row['depth'] == min_depth:
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

# Extract all nodes from tree
def extract_all_nodes(node):
    nodes = [node]
    for child in node.children:
        nodes.extend(extract_all_nodes(child))
    return nodes

# Compute structural hash for pattern at specific depth
def compute_hash_at_depth(node, remaining_depth: int) -> str:
    if remaining_depth == 0 or len(node.children) == 0:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_hash_at_depth(child, remaining_depth - 1)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)

    return hashlib.md5(combined_string.encode()).hexdigest()

# Clean node type for column naming
def clean_node_type(node_type):
    return node_type.replace(' ', '')

# Aggregate subtree into single row with hierarchical prefixes
def aggregate_subtree(node, target_depth, prefix=''):
    aggregated = {}
    is_root = (prefix == '')

    if is_root:
        node_prefix = clean_node_type(node.node_type) + '_'
        if 'query_file' in node.row_data:
            aggregated['query_file'] = node.row_data['query_file']
    else:
        node_prefix = prefix

    for col in node.row_data.index:
        if col == 'query_file':
            continue

        if col in ['actual_startup_time', 'actual_total_time']:
            if is_root:
                aggregated[col] = node.row_data[col]
        else:
            aggregated[node_prefix + col] = node.row_data[col]

    if target_depth > 0 and len(node.children) > 0:
        children_sorted = sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1 if c.parent_relationship == 'Inner' else 2, c.node_type))

        for child in children_sorted:
            child_prefix = clean_node_type(child.node_type) + '_' + child.parent_relationship + '_'
            child_agg = aggregate_subtree(child, target_depth - 1, child_prefix)
            aggregated.update(child_agg)

    return aggregated

# Process single pattern folder
def process_pattern_folder(pattern_folder, pattern_hash, pattern_length):
    training_file = pattern_folder / 'training.csv'

    if not training_file.exists():
        return

    df = pd.read_csv(training_file, delimiter=';')
    operator_count = PATTERN_OPERATOR_COUNT[pattern_hash]

    aggregated_rows = []

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].reset_index(drop=True)

        for i in range(0, len(query_ops), operator_count):
            chunk = query_ops.iloc[i:i+operator_count].reset_index(drop=True)
            root = build_tree_from_query(chunk)
            aggregated_row = aggregate_subtree(root, pattern_length - 1)
            aggregated_rows.append(aggregated_row)

    if aggregated_rows:
        result_df = pd.DataFrame(aggregated_rows)
        output_file = pattern_folder / 'training_aggregated.csv'
        result_df.to_csv(output_file, sep=';', index=False)

# Extract all node IDs from subtree at specific depth
def extract_subtree_node_ids(node, remaining_depth: int) -> set:
    node_ids = {node.node_id}

    if remaining_depth > 0:
        for child in node.children:
            node_ids.update(extract_subtree_node_ids(child, remaining_depth - 1))

    return node_ids


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int, row_data):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.row_data = row_data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern_csv", help="Path to pattern CSV from Data_Generation/01_Find_Patterns.py")
    parser.add_argument("patterns_dir", help="Base directory containing extracted pattern folders")
    args = parser.parse_args()

    aggregate_patterns_workflow(args.pattern_csv, args.patterns_dir)
