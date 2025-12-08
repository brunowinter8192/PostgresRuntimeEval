#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import pandas as pd
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline

# From tree.py: Query tree data structures
from .tree import build_tree_from_dataframe, extract_all_nodes, has_children_at_length, extract_pattern_node_ids

# From aggregation.py: Pattern aggregation
from .aggregation import aggregate_pattern_for_training, remove_non_leaf_timing_features

# From mining.py: Pattern hash computation
from .mining import compute_pattern_hash

# From mapping_config.py: Configuration constants
from mapping_config import (
    SVM_PARAMS, MIN_SAMPLES,
    TARGET_TYPES, TARGET_NAME_MAP,
    get_operator_features, csv_name_to_folder_name
)


# FUNCTIONS

# Train models for all operator types
def train_all_operators(df: pd.DataFrame, report) -> dict:
    models = {'execution_time': {}, 'start_time': {}}
    operator_types = df['node_type'].unique()

    for op_type in operator_types:
        op_data = df[df['node_type'] == op_type]

        if len(op_data) < MIN_SAMPLES:
            continue

        features = get_operator_features(op_type)
        available_features = [f for f in features if f in op_data.columns]

        if not available_features:
            continue

        X = op_data[available_features].fillna(0)

        for target_type in TARGET_TYPES:
            target_col = TARGET_NAME_MAP[target_type]
            y = op_data[target_col]

            if y.std() == 0:
                continue

            model = Pipeline([
                ('scaler', MaxAbsScaler()),
                ('model', NuSVR(**SVM_PARAMS))
            ])
            model.fit(X, y)

            op_name = csv_name_to_folder_name(op_type)
            models[target_type][op_name] = {
                'model': model,
                'features': available_features
            }

        if report:
            report.add_operator_training(op_type, len(op_data))

    return models


# Train single pattern model
def train_single_pattern(df: pd.DataFrame, pattern_hash: str, pattern_info: dict) -> dict:
    pattern_length = pattern_info['pattern_length']

    aggregated_rows = []

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops, include_row_data=True)
        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            if not has_children_at_length(node, pattern_length):
                continue

            computed_hash = compute_pattern_hash(node, pattern_length)
            if computed_hash != pattern_hash:
                continue

            pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
            pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]

            aggregated = aggregate_pattern_for_training(pattern_rows, pattern_length)
            if aggregated:
                aggregated_rows.append(aggregated)

    if len(aggregated_rows) < MIN_SAMPLES:
        return None

    df_agg = pd.DataFrame(aggregated_rows)
    df_agg = remove_non_leaf_timing_features(df_agg, pattern_info)

    feature_cols = [c for c in df_agg.columns
                    if c not in ['query_file', 'actual_startup_time', 'actual_total_time']]

    if not feature_cols:
        return None

    X = df_agg[feature_cols].fillna(0)

    models = {}
    for target_type in TARGET_TYPES:
        target_col = TARGET_NAME_MAP[target_type]
        y = df_agg[target_col]

        if y.std() == 0:
            return None

        model = Pipeline([
            ('scaler', MaxAbsScaler()),
            ('model', NuSVR(**SVM_PARAMS))
        ])
        model.fit(X, y)
        models[target_type] = model

    return {
        'execution_time': models['execution_time'],
        'start_time': models['start_time'],
        'features': feature_cols
    }


# Train selected patterns on full training data
def train_selected_patterns(df: pd.DataFrame, selected_patterns: set, patterns: dict) -> dict:
    pattern_models = {}

    for pattern_hash in selected_patterns:
        pattern_info = patterns[pattern_hash]
        model = train_single_pattern(df, pattern_hash, pattern_info)
        if model:
            pattern_models[pattern_hash] = model

    return pattern_models
