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
def analyze_patterns(input_file: str, output_dir: str) -> None:
    df = load_and_filter_data(input_file)
    max_depth = scan_max_depth(df)
    pattern_counts = mine_patterns_iteratively(df, max_depth)
    all_patterns = collect_all_patterns(pattern_counts)
    sorted_patterns = sort_by_size(all_patterns)
    export_results(sorted_patterns, output_dir)


# FUNCTIONS

# Load training data and filter to main plan
def load_and_filter_data(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]

# Find maximum depth in dataset
def scan_max_depth(df: pd.DataFrame) -> int:
    return int(df['depth'].max())

# Mine patterns iteratively from length 2 to max_depth
def mine_patterns_iteratively(df: pd.DataFrame, max_depth: int) -> dict:
    pattern_counts = {}

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            for pattern_length in range(2, max_depth + 2):
                if not has_children_at_length(node, pattern_length):
                    break

                pattern_hash = compute_pattern_hash_at_length(node, pattern_length)
                operator_count = count_operators_at_length(node, pattern_length)

                if pattern_hash not in pattern_counts:
                    pattern_counts[pattern_hash] = {
                        'pattern_string': generate_pattern_string_at_length(node, pattern_length),
                        'length': pattern_length,
                        'operator_count': operator_count,
                        'count': 0,
                        'example_query': query_file
                    }

                pattern_counts[pattern_hash]['count'] += 1

    return pattern_counts

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

# Count total operators in pattern at specific length
def count_operators_at_length(node, remaining_length: int) -> int:
    if remaining_length == 1 or len(node.children) == 0:
        return 1

    child_counts = sum(count_operators_at_length(child, remaining_length - 1) for child in node.children)
    return 1 + child_counts

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

# Generate readable pattern string at specific length
def generate_pattern_string_at_length(node, remaining_length: int) -> str:
    if remaining_length == 1 or len(node.children) == 0:
        return node.node_type

    if len(node.children) == 1:
        child = node.children[0]
        child_str = generate_pattern_string_at_length(child, remaining_length - 1)
        return f"{node.node_type} -> {child_str} ({child.parent_relationship})"

    children_strs = []
    for child in sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1 if c.parent_relationship == 'Inner' else 2, c.node_type)):
        child_str = generate_pattern_string_at_length(child, remaining_length - 1)
        children_strs.append(f"{child_str} ({child.parent_relationship})")

    children_combined = ', '.join(children_strs)
    return f"{node.node_type} -> [{children_combined}]"

# Collect all patterns without threshold filtering
def collect_all_patterns(pattern_counts: dict) -> list:
    patterns = []

    for pattern_hash, data in pattern_counts.items():
        patterns.append({
            'pattern_hash': pattern_hash,
            'pattern_string': data['pattern_string'],
            'pattern_length': data['length'],
            'operator_count': data['operator_count'],
            'occurrence_count': data['count'],
            'example_query_file': data['example_query']
        })

    return patterns

# Sort patterns by size (operator_count ASC), then by occurrence (DESC)
def sort_by_size(patterns: list) -> list:
    return sorted(patterns, key=lambda x: (x['operator_count'], -x['occurrence_count']))

# Save patterns to CSV
def export_results(patterns: list, output_dir: str) -> None:
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    output_file = csv_dir / '01_patterns.csv'

    df = pd.DataFrame(patterns)
    df.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to training dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for pattern analysis")
    args = parser.parse_args()

    analyze_patterns(args.input_file, args.output_dir)
