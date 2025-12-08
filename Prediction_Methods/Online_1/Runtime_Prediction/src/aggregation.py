#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import pandas as pd

# From tree.py: Query tree data structures
from .tree import build_tree_from_dataframe, get_children_from_full_query

# From mapping_config.py: Metadata and target columns
from mapping_config import OPERATOR_METADATA, OPERATOR_TARGETS


# FUNCTIONS

# Aggregate pattern for training (with actual child times)
def aggregate_pattern_for_training(pattern_rows: pd.DataFrame, pattern_length: int) -> dict:
    if pattern_rows.empty:
        return None

    pattern_rows = pattern_rows.sort_values('depth').reset_index(drop=True)
    root = build_tree_from_dataframe(pattern_rows, include_row_data=True)

    return _aggregate_subtree(root, pattern_length - 1, is_root=True)


# Aggregate pattern for prediction (with predicted child times)
def aggregate_pattern_for_prediction(
    pattern_rows: pd.DataFrame,
    pattern_length: int,
    full_query_ops: pd.DataFrame,
    prediction_cache: dict
) -> dict:
    if pattern_rows.empty:
        return {}

    pattern_rows = pattern_rows.sort_values('depth').reset_index(drop=True)
    root = build_tree_from_dataframe(pattern_rows, include_row_data=True)
    pattern_node_ids = set(pattern_rows['node_id'].tolist())

    return _aggregate_subtree_with_cache(
        root, full_query_ops, prediction_cache, pattern_node_ids, pattern_length - 1, is_root=True
    )


# Remove non-leaf timing features from aggregated data
def remove_non_leaf_timing_features(df: pd.DataFrame, pattern_info: dict) -> pd.DataFrame:
    timing_suffixes = ['_st1', '_rt1', '_st2', '_rt2']
    cols_to_drop = []

    for col in df.columns:
        if any(col.endswith(suffix) for suffix in timing_suffixes):
            cols_to_drop.append(col)

    return df.drop(columns=cols_to_drop, errors='ignore')


# Aggregate subtree for training
def _aggregate_subtree(node, remaining_depth: int, is_root: bool = False) -> dict:
    aggregated = {}
    node_type_clean = node.node_type.replace(' ', '')

    if is_root:
        prefix = node_type_clean + '_'
        aggregated['query_file'] = node.row_data['query_file']
        aggregated['actual_startup_time'] = node.row_data['actual_startup_time']
        aggregated['actual_total_time'] = node.row_data['actual_total_time']
    else:
        prefix = node_type_clean + '_' + node.parent_relationship + '_'

    for col in node.row_data.index:
        if col not in OPERATOR_METADATA + OPERATOR_TARGETS:
            aggregated[prefix + col] = node.row_data[col]

    if remaining_depth > 0:
        children_sorted = sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1, c.node_type))
        for child in children_sorted:
            child_agg = _aggregate_subtree(child, remaining_depth - 1, is_root=False)
            aggregated.update(child_agg)

    return aggregated


# Aggregate subtree with prediction cache
def _aggregate_subtree_with_cache(
    node,
    full_query_ops: pd.DataFrame,
    prediction_cache: dict,
    pattern_node_ids: set,
    remaining_depth: int,
    is_root: bool = False
) -> dict:
    aggregated = {}
    node_type_clean = node.node_type.replace(' ', '')

    if is_root:
        prefix = node_type_clean + '_'
    else:
        prefix = node_type_clean + '_' + node.parent_relationship + '_'

    for col in node.row_data.index:
        if col not in OPERATOR_METADATA + OPERATOR_TARGETS:
            aggregated[prefix + col] = node.row_data[col]

    aggregated[prefix + 'st1'] = 0.0
    aggregated[prefix + 'rt1'] = 0.0
    aggregated[prefix + 'st2'] = 0.0
    aggregated[prefix + 'rt2'] = 0.0

    full_children = get_children_from_full_query(full_query_ops, node.node_id)
    for child_row in full_children:
        child_id = child_row['node_id']
        if child_id not in pattern_node_ids and child_id in prediction_cache:
            pred = prediction_cache[child_id]
            if child_row['parent_relationship'] == 'Outer':
                aggregated[prefix + 'st1'] = pred['start']
                aggregated[prefix + 'rt1'] = pred['exec']
            elif child_row['parent_relationship'] == 'Inner':
                aggregated[prefix + 'st2'] = pred['start']
                aggregated[prefix + 'rt2'] = pred['exec']

    if remaining_depth > 0:
        children_sorted = sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1, c.node_type))
        for child in children_sorted:
            child_agg = _aggregate_subtree_with_cache(
                child, full_query_ops, prediction_cache, pattern_node_ids, remaining_depth - 1, is_root=False
            )
            aggregated.update(child_agg)

    return aggregated
