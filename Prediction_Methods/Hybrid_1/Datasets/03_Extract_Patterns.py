#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import hashlib
import json
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Pattern discovery constants and folder name conversion
from mapping_config import REQUIRED_OPERATORS, PASSTHROUGH_OPERATORS, pattern_to_folder_name


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int, df_index: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.df_index = df_index
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# ORCHESTRATOR
def extract_patterns_workflow(input_file: str, output_base: str, target_length: int, filter_type: str) -> None:
    df = load_training_data(input_file)
    max_depth = int(df['depth'].max())
    pattern_data = extract_patterns_at_lengths(df, max_depth, target_length, filter_type)
    export_all_patterns(df, pattern_data, output_base)


# FUNCTIONS

# Load training data and filter to main plan only
def load_training_data(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Build tree structure from flat DataFrame
def build_tree_from_dataframe(query_ops: pd.DataFrame):
    nodes = {}
    root = None

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'] if pd.notna(row['parent_relationship']) else '',
            depth=row['depth'],
            node_id=row['node_id'],
            df_index=row['original_index']
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

    return root, nodes


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


# Collect all df_indices for a pattern at specific length
def collect_indices_at_length(node, remaining_length: int) -> list:
    if remaining_length == 1 or len(node.children) == 0:
        return [node.df_index]

    indices = [node.df_index]
    for child in node.children:
        indices.extend(collect_indices_at_length(child, remaining_length - 1))

    return indices


# Check if pattern passes the specified filter
def passes_filter(node, filter_type: str) -> bool:
    if filter_type == 'none':
        return True

    if filter_type == 'required_operators':
        operators = {node.node_type}
        for child in node.children:
            operators.add(child.node_type)
        return bool(operators.intersection(REQUIRED_OPERATORS))

    if filter_type == 'no_passthrough':
        return node.node_type not in PASSTHROUGH_OPERATORS

    return True


# Extract patterns at specified lengths
def extract_patterns_at_lengths(df: pd.DataFrame, max_depth: int, target_length: int, filter_type: str) -> dict:
    pattern_data = {}

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=False)
        query_ops = query_ops.rename(columns={'index': 'original_index'})

        root, nodes = build_tree_from_dataframe(query_ops)
        if root is None:
            continue

        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            if node.depth < 0:
                continue

            if not passes_filter(node, filter_type):
                continue

            if target_length == 0:
                lengths_to_check = range(2, max_depth + 2)
            else:
                lengths_to_check = [target_length]

            for pattern_length in lengths_to_check:
                if not has_children_at_length(node, pattern_length):
                    break

                pattern_hash = compute_pattern_hash_at_length(node, pattern_length)
                pattern_string = generate_pattern_string_at_length(node, pattern_length)
                indices = collect_indices_at_length(node, pattern_length)

                if pattern_hash not in pattern_data:
                    pattern_data[pattern_hash] = {
                        'pattern_string': pattern_string,
                        'pattern_length': pattern_length,
                        'occurrences': []
                    }

                pattern_data[pattern_hash]['occurrences'].append(indices)

    return pattern_data


# Export all patterns to their respective folders
def export_all_patterns(df: pd.DataFrame, pattern_data: dict, output_base: str) -> None:
    for pattern_hash, data in pattern_data.items():
        pattern_dir = Path(output_base) / 'patterns' / pattern_hash
        pattern_dir.mkdir(parents=True, exist_ok=True)

        all_indices = [idx for occurrence in data['occurrences'] for idx in occurrence]
        pattern_df = df.loc[all_indices].sort_index()

        output_file = pattern_dir / 'training.csv'
        pattern_df.to_csv(output_file, sep=';', index=False)

        folder_name = pattern_to_folder_name(data['pattern_string'])
        pattern_info = {
            'pattern_hash': pattern_hash,
            'pattern_string': data['pattern_string'],
            'folder_name': folder_name,
            'pattern_length': data['pattern_length'],
            'occurrence_count': len(data['occurrences'])
        }
        info_file = pattern_dir / 'pattern_info.json'
        with open(info_file, 'w') as f:
            json.dump(pattern_info, f, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Base output directory for pattern folders")
    parser.add_argument("--length", type=int, default=0, help="Pattern length (0 = all lengths, N = specific length)")
    parser.add_argument("--filter", choices=['required_operators', 'no_passthrough', 'none'],
                        default='none', help="Filter type for patterns")
    args = parser.parse_args()

    extract_patterns_workflow(args.input_file, args.output_dir, args.length, args.filter)
