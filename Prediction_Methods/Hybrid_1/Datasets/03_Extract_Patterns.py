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
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# ORCHESTRATOR
def extract_patterns_workflow(input_file: str, output_base: str, target_length: int, require_operators: bool, no_passthrough: bool) -> None:
    df = load_training_data(input_file)
    max_depth = int(df['depth'].max())
    pattern_data = extract_patterns_at_lengths(df, max_depth, target_length, require_operators, no_passthrough)
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


# Extract node IDs of all nodes in pattern up to specified length
def extract_pattern_node_ids(node, remaining_length: int) -> list:
    if remaining_length == 1 or len(node.children) == 0:
        return [node.node_id]

    node_ids = [node.node_id]
    for child in node.children:
        child_ids = extract_pattern_node_ids(child, remaining_length - 1)
        node_ids.extend(child_ids)

    return node_ids


# Check if pattern passes all active filters
def passes_filter(node, require_operators: bool, no_passthrough: bool) -> bool:
    if require_operators:
        if node.node_type not in REQUIRED_OPERATORS:
            return False

    if no_passthrough:
        if node.node_type in PASSTHROUGH_OPERATORS:
            return False

    return True


# Extract patterns at specified lengths
def extract_patterns_at_lengths(df: pd.DataFrame, max_depth: int, target_length: int, require_operators: bool, no_passthrough: bool) -> dict:
    pattern_data = {}

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)

        root, nodes = build_tree_from_dataframe(query_ops)
        if root is None:
            continue

        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            if node.depth < 0:
                continue

            if not passes_filter(node, require_operators, no_passthrough):
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
                pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
                pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]

                if pattern_hash not in pattern_data:
                    pattern_data[pattern_hash] = {
                        'pattern_string': pattern_string,
                        'pattern_length': pattern_length,
                        'occurrences': []
                    }

                pattern_data[pattern_hash]['occurrences'].append(pattern_rows)

    return pattern_data


# Export all patterns to their respective folders
def export_all_patterns(df: pd.DataFrame, pattern_data: dict, output_base: str) -> None:
    pattern_inventory = []

    for pattern_hash, data in pattern_data.items():
        if len(data['occurrences']) == 0:
            continue

        pattern_dir = Path(output_base) / 'patterns' / pattern_hash
        pattern_dir.mkdir(parents=True, exist_ok=True)

        combined_df = pd.concat(data['occurrences'], ignore_index=True)
        operator_count = len(data['occurrences'][0]) if data['occurrences'] else 0

        output_file = pattern_dir / 'training.csv'
        combined_df.to_csv(output_file, sep=';', index=False)

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

        pattern_inventory.append({
            'pattern_hash': pattern_hash,
            'pattern_string': data['pattern_string'],
            'pattern_length': data['pattern_length'],
            'operator_count': operator_count,
            'occurrence_count': len(data['occurrences'])
        })

    if pattern_inventory:
        inventory_df = pd.DataFrame(pattern_inventory)
        inventory_file = Path(output_base) / 'patterns.csv'
        inventory_df.to_csv(inventory_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Base output directory for pattern folders")
    parser.add_argument("--length", type=int, default=0, help="Pattern length (0 = all lengths, N = specific length)")
    parser.add_argument("--required-operators", action="store_true", help="Filter to patterns containing required operators")
    parser.add_argument("--no-passthrough", action="store_true", help="Exclude patterns with passthrough parent operators")
    args = parser.parse_args()

    extract_patterns_workflow(args.input_file, args.output_dir, args.length, args.required_operators, args.no_passthrough)
