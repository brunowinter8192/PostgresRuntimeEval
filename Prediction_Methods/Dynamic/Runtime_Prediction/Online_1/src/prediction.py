#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import pandas as pd

# From tree.py: Query tree data structures
from .tree import (
    build_tree_from_dataframe, extract_all_nodes,
    has_children_at_length, extract_pattern_node_ids
)

# From aggregation.py: Pattern aggregation
from .aggregation import aggregate_pattern_for_prediction

# From mining.py: Pattern hash computation
from .mining import compute_pattern_hash

# From metrics.py: Result creation
from .metrics import create_prediction_result

# From mapping_config.py: Configuration constants
from mapping_config import (
    OPERATOR_METADATA, OPERATOR_TARGETS,
    csv_name_to_folder_name
)


# FUNCTIONS

# Build pattern assignments before prediction (Phase 1)
def _build_pattern_assignments(
    all_nodes: list,
    patterns: dict,
    selected_patterns: set
) -> tuple:
    consumed_nodes = set()
    pattern_assignments = {}

    # Sort by pattern_length (longest first) - per Paper Section 3.4
    sorted_patterns = sorted(
        selected_patterns,
        key=lambda ph: patterns[ph]['pattern_length'],
        reverse=True
    )

    for pattern_hash in sorted_patterns:
        if pattern_hash not in patterns:
            continue
        pattern_info = patterns[pattern_hash]
        pattern_length = pattern_info['pattern_length']

        for node in all_nodes:
            if node.node_id in consumed_nodes:
                continue
            if not has_children_at_length(node, pattern_length):
                continue

            computed_hash = compute_pattern_hash(node, pattern_length)
            if computed_hash == pattern_hash:
                pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
                if any(nid in consumed_nodes for nid in pattern_node_ids):
                    continue
                consumed_nodes.update(pattern_node_ids)
                pattern_assignments[node.node_id] = pattern_hash

    return consumed_nodes, pattern_assignments


# Predict all queries using only operator models
def predict_all_queries_operator_only(df: pd.DataFrame, operator_models: dict) -> list:
    all_predictions = []

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        predictions = predict_single_query_operator_only(query_ops, operator_models)
        all_predictions.extend(predictions)

    return all_predictions


# Predict single query bottom-up with operator models only
def predict_single_query_operator_only(query_ops: pd.DataFrame, operator_models: dict) -> list:
    root = build_tree_from_dataframe(query_ops)
    all_nodes = extract_all_nodes(root)
    nodes_by_depth = sorted(all_nodes, key=lambda n: n.depth, reverse=True)

    prediction_cache = {}
    predictions = []

    for node in nodes_by_depth:
        pred_start, pred_exec, _ = _predict_operator(node, query_ops, operator_models, prediction_cache)
        prediction_cache[node.node_id] = {'start': pred_start, 'exec': pred_exec}

        row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
        predictions.append(create_prediction_result(row, pred_start, pred_exec, 'operator'))

    return predictions


# Predict all queries with patterns
def predict_all_queries_with_patterns(
    df: pd.DataFrame,
    operator_models: dict,
    pattern_models: dict,
    patterns: dict,
    selected_patterns: set
) -> list:
    all_predictions = []

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        predictions = predict_single_query_with_patterns(
            query_ops, operator_models, pattern_models, patterns, selected_patterns
        )
        all_predictions.extend(predictions)

    return all_predictions


# Predict single query with patterns (two-phase approach)
def predict_single_query_with_patterns(
    query_ops: pd.DataFrame,
    operator_models: dict,
    pattern_models: dict,
    patterns: dict,
    selected_patterns: set,
    return_details: bool = False
) -> list:
    root = build_tree_from_dataframe(query_ops, include_row_data=True)
    all_nodes = extract_all_nodes(root)
    nodes_by_depth = sorted(all_nodes, key=lambda n: n.depth, reverse=True)

    consumed_nodes, pattern_assignments = _build_pattern_assignments(
        all_nodes, patterns, selected_patterns
    )

    prediction_cache = {}
    predictions = []

    for node in nodes_by_depth:
        if node.node_id in consumed_nodes and node.node_id not in pattern_assignments:
            continue

        child_timing = _get_child_timing(node, prediction_cache)

        if node.node_id in pattern_assignments:
            pattern_hash = pattern_assignments[node.node_id]
            pattern_info = patterns[pattern_hash]
            pattern_node_ids = extract_pattern_node_ids(node, pattern_info['pattern_length'])

            if pattern_hash in pattern_models:
                pred_start, pred_exec, input_features = _predict_pattern(
                    node, query_ops, pattern_models[pattern_hash], prediction_cache, pattern_info['pattern_length']
                )
            else:
                pred_start, pred_exec, input_features = _predict_operator(node, query_ops, operator_models, prediction_cache)

            for nid in pattern_node_ids:
                prediction_cache[nid] = {'start': pred_start, 'exec': pred_exec, 'child_timing': child_timing, 'input_features': input_features}

            row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
            predictions.append(create_prediction_result(row, pred_start, pred_exec, 'pattern'))
        else:
            pred_start, pred_exec, input_features = _predict_operator(node, query_ops, operator_models, prediction_cache)
            prediction_cache[node.node_id] = {'start': pred_start, 'exec': pred_exec, 'child_timing': child_timing, 'input_features': input_features}

            row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
            is_leaf = len(node.children) == 0
            result = create_prediction_result(row, pred_start, pred_exec, 'operator')
            result['is_leaf'] = is_leaf
            predictions.append(result)

    if return_details:
        return predictions, pattern_assignments, consumed_nodes, prediction_cache
    return predictions


# Get child timing from prediction cache
def _get_child_timing(node, prediction_cache: dict) -> dict:
    child_timing = {'st1': 0.0, 'rt1': 0.0, 'st2': 0.0, 'rt2': 0.0}

    for child in node.children:
        if child.node_id in prediction_cache:
            pred = prediction_cache[child.node_id]
            if child.parent_relationship == 'Outer':
                child_timing['st1'] = pred['start']
                child_timing['rt1'] = pred['exec']
            elif child.parent_relationship == 'Inner':
                child_timing['st2'] = pred['start']
                child_timing['rt2'] = pred['exec']

    return child_timing


# Predict single operator
def _predict_operator(node, query_ops: pd.DataFrame, operator_models: dict, prediction_cache: dict) -> tuple:
    op_name = csv_name_to_folder_name(node.node_type)

    if op_name not in operator_models['execution_time'] or op_name not in operator_models['start_time']:
        return 0.0, 0.0, {}

    row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
    features = _build_operator_features(row, node, prediction_cache)

    model_info_exec = operator_models['execution_time'][op_name]
    model_info_start = operator_models['start_time'][op_name]

    X_exec = pd.DataFrame([[features.get(f, 0) for f in model_info_exec['features']]],
                          columns=model_info_exec['features'])
    X_start = pd.DataFrame([[features.get(f, 0) for f in model_info_start['features']]],
                           columns=model_info_start['features'])

    pred_exec = model_info_exec['model'].predict(X_exec)[0]
    pred_start = model_info_start['model'].predict(X_start)[0]

    return pred_start, pred_exec, features


# Build operator features with child predictions
def _build_operator_features(row, node, prediction_cache: dict) -> dict:
    features = {}

    for col in row.index:
        if col not in OPERATOR_METADATA + OPERATOR_TARGETS:
            features[col] = row[col]

    features['st1'] = 0.0
    features['rt1'] = 0.0
    features['st2'] = 0.0
    features['rt2'] = 0.0

    for child in node.children:
        if child.node_id in prediction_cache:
            pred = prediction_cache[child.node_id]
            if child.parent_relationship == 'Outer':
                features['st1'] = pred['start']
                features['rt1'] = pred['exec']
            elif child.parent_relationship == 'Inner':
                features['st2'] = pred['start']
                features['rt2'] = pred['exec']

    return features


# Predict using pattern model
def _predict_pattern(node, query_ops: pd.DataFrame, model: dict, prediction_cache: dict, pattern_length: int) -> tuple:
    pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
    pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]

    aggregated = aggregate_pattern_for_prediction(pattern_rows, pattern_length, query_ops, prediction_cache)

    features = model['features']
    X = pd.DataFrame([[aggregated.get(f, 0) for f in features]], columns=features)

    pred_exec = model['execution_time'].predict(X)[0]
    pred_start = model['start_time'].predict(X)[0]

    input_features = {f: aggregated.get(f, 0) for f in features}
    return pred_start, pred_exec, input_features


# Predict all queries with single pattern active
def predict_all_queries_with_single_pattern(
    df: pd.DataFrame,
    operator_models: dict,
    pattern_model: dict,
    patterns: dict,
    target_pattern_hash: str
) -> list:
    all_predictions = []

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)

        predictions = predict_single_query_with_patterns(
            query_ops, operator_models,
            {target_pattern_hash: pattern_model},
            patterns,
            {target_pattern_hash}
        )
        all_predictions.extend(predictions)

    return all_predictions
