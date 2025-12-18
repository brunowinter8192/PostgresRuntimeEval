#!/usr/bin/env python3

# INFRASTRUCTURE
import hashlib
import numpy as np
import pandas as pd

# From tree.py: Query tree data structures
from .tree import build_tree_from_dataframe, extract_all_nodes, has_children_at_length, count_operators


# FUNCTIONS

# Mine all patterns from a single query
def mine_patterns_from_query(query_ops: pd.DataFrame) -> dict:
    root = build_tree_from_dataframe(query_ops)
    all_nodes = extract_all_nodes(root)
    max_depth = int(query_ops['depth'].max()) + 1

    patterns = {}

    for node in all_nodes:
        for pattern_length in range(2, max_depth + 1):
            if not has_children_at_length(node, pattern_length):
                break

            pattern_hash = compute_pattern_hash(node, pattern_length)

            if pattern_hash not in patterns:
                patterns[pattern_hash] = {
                    'pattern_string': generate_pattern_string(node, pattern_length),
                    'pattern_length': pattern_length,
                    'operator_count': count_operators(node, pattern_length),
                    'root_node_id': node.node_id
                }

    return patterns


# Find pattern occurrences in a dataset
def find_pattern_occurrences_in_data(df: pd.DataFrame, patterns: dict) -> dict:
    occurrences = {ph: [] for ph in patterns.keys()}

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            for pattern_hash, pattern_info in patterns.items():
                pattern_length = pattern_info['pattern_length']

                if not has_children_at_length(node, pattern_length):
                    continue

                computed_hash = compute_pattern_hash(node, pattern_length)

                if computed_hash == pattern_hash:
                    occurrences[pattern_hash].append({
                        'query_file': query_file,
                        'root_node_id': node.node_id
                    })

    return occurrences


# Compute pattern hash
def compute_pattern_hash(node, remaining_length: int) -> str:
    if remaining_length == 1 or len(node.children) == 0:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_pattern_hash(child, remaining_length - 1)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)
    return hashlib.md5(combined_string.encode()).hexdigest()


# Generate pattern string
def generate_pattern_string(node, remaining_length: int) -> str:
    if remaining_length == 1 or len(node.children) == 0:
        return node.node_type

    if len(node.children) == 1:
        child = node.children[0]
        child_str = generate_pattern_string(child, remaining_length - 1)
        return f"{node.node_type} -> {child_str} ({child.parent_relationship})"

    children_strs = []
    for child in sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1, c.node_type)):
        child_str = generate_pattern_string(child, remaining_length - 1)
        children_strs.append(f"{child_str} ({child.parent_relationship})")

    children_combined = ', '.join(children_strs)
    return f"{node.node_type} -> [{children_combined}]"


# Calculate ranking for patterns based on strategy
def calculate_ranking(
    predictions: list,
    occurrences: dict,
    patterns: dict,
    consumed_hashes: set = None,
    strategy: str = 'error'
) -> list:
    if consumed_hashes is None:
        consumed_hashes = set()

    pred_lookup = {}
    for p in predictions:
        key = (p['query_file'], p['node_id'])
        if p['actual_total_time'] > 0:
            mre = abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time']
            pred_lookup[key] = mre

    ranking = []
    for pattern_hash, occ_list in occurrences.items():
        if pattern_hash in consumed_hashes:
            continue

        if not occ_list:
            continue

        mre_values = []
        for occ in occ_list:
            key = (occ['query_file'], occ['root_node_id'])
            if key in pred_lookup:
                mre_values.append(pred_lookup[key])

        if mre_values:
            avg_mre = np.mean(mre_values)
            error_score = len(occ_list) * avg_mre

            pattern_info = patterns[pattern_hash]
            ranking.append({
                'pattern_hash': pattern_hash,
                'pattern_string': pattern_info['pattern_string'],
                'pattern_length': pattern_info['pattern_length'],
                'operator_count': pattern_info['operator_count'],
                'occurrence_count': len(occ_list),
                'avg_mre': avg_mre,
                'error_score': error_score
            })

    if strategy == 'error':
        return sorted(ranking, key=lambda x: (-x['error_score'], x['pattern_hash']))
    elif strategy == 'size':
        return sorted(ranking, key=lambda x: (x['pattern_length'], -x['occurrence_count']))
    elif strategy == 'frequency':
        return sorted(ranking, key=lambda x: (-x['occurrence_count'], x['pattern_length']))
    return sorted(ranking, key=lambda x: (-x['error_score'], x['pattern_hash']))
