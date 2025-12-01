#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
import numpy as np
import hashlib
import json
from pathlib import Path
import joblib
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

# From mapping_config.py: Leaf operators for bottom-up prediction
from mapping_config import LEAF_OPERATORS, csv_name_to_folder_name


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

def run_prediction(
    test_file: str,
    operator_model_dir: str,
    operator_overview_file: str,
    output_dir: str,
    pattern_model_dir: str = None,
    pattern_ffs_file: str = None,
    selected_patterns_file: str = None,
    pattern_metadata_file: str = None
) -> None:
    df_test = load_test_data(test_file)
    operator_models = load_operator_models(operator_model_dir)
    operator_features = load_operator_features(operator_overview_file)

    pattern_models = {}
    pattern_features = {}
    pattern_info = {}

    if pattern_model_dir and pattern_ffs_file and selected_patterns_file and pattern_metadata_file:
        pattern_models = load_pattern_models(pattern_model_dir)
        pattern_features = load_pattern_features(pattern_ffs_file, pattern_models)
        pattern_info = load_pattern_info(selected_patterns_file, pattern_metadata_file)

    all_predictions = predict_all_queries(
        df_test, operator_models, operator_features,
        pattern_models, pattern_features, pattern_info
    )

    export_predictions(all_predictions, output_dir)


# FUNCTIONS

# Load test dataset filtered to main plan
def load_test_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load operator models from directory
def load_operator_models(model_dir: str) -> dict:
    models = {'execution_time': {}, 'start_time': {}}
    model_path = Path(model_dir)

    for target in ['execution_time', 'start_time']:
        target_dir = model_path / target

        if not target_dir.exists():
            continue

        for op_dir in target_dir.iterdir():
            if op_dir.is_dir():
                model_file = op_dir / 'model.pkl'

                if model_file.exists():
                    models[target][op_dir.name] = joblib.load(model_file)

    return models


# Load operator features from overview CSV
def load_operator_features(overview_file: str) -> dict:
    df = pd.read_csv(overview_file, delimiter=';')
    features = {'execution_time': {}, 'start_time': {}}

    for _, row in df.iterrows():
        operator = row['operator']
        target = row['target']
        features_str = row['final_features']

        if pd.isna(features_str) or features_str.strip() == '':
            continue

        features[target][operator] = [f.strip() for f in features_str.split(',')]

    return features


# Load pattern models from directory
def load_pattern_models(model_dir: str) -> dict:
    models = {}
    model_path = Path(model_dir)

    if not model_path.exists():
        return models

    for pattern_dir in model_path.iterdir():
        if not pattern_dir.is_dir():
            continue

        pattern_hash = pattern_dir.name
        exec_file = pattern_dir / 'model_execution_time.pkl'
        start_file = pattern_dir / 'model_start_time.pkl'
        features_file = pattern_dir / 'features.json'

        if not all(f.exists() for f in [exec_file, start_file, features_file]):
            continue

        with open(features_file, 'r') as f:
            features = json.load(f)

        models[pattern_hash] = {
            'execution_time': joblib.load(exec_file),
            'start_time': joblib.load(start_file),
            'features_exec': features['features_exec'],
            'features_start': features['features_start']
        }

    return models


# Load pattern features for loaded models
def load_pattern_features(ffs_file: str, pattern_models: dict) -> dict:
    df = pd.read_csv(ffs_file, delimiter=';')
    features = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern']

        if pattern_hash not in pattern_models:
            continue

        if pattern_hash not in features:
            features[pattern_hash] = {}

        target = row['target']

        if pd.isna(row['final_features']) or row['final_features'] == '':
            features[pattern_hash][target] = []
        else:
            features[pattern_hash][target] = [f.strip() for f in row['final_features'].split(',')]

    return features


# Load pattern info from selected patterns and metadata file
def load_pattern_info(selected_patterns_file: str, pattern_metadata_file: str) -> dict:
    df_selected = pd.read_csv(selected_patterns_file, delimiter=';')
    df_metadata = pd.read_csv(pattern_metadata_file, delimiter=';')

    df_merged = df_selected.merge(
        df_metadata[['pattern_hash', 'pattern_length', 'operator_count']],
        on='pattern_hash',
        how='left'
    )

    info = {}

    for _, row in df_merged.iterrows():
        info[row['pattern_hash']] = {
            'length': int(row['pattern_length']),
            'operator_count': int(row['operator_count'])
        }

    return info


# Predict all queries in test set
def predict_all_queries(
    df_test: pd.DataFrame,
    operator_models: dict,
    operator_features: dict,
    pattern_models: dict,
    pattern_features: dict,
    pattern_info: dict
) -> list:
    all_predictions = []

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)

        predictions = predict_single_query(
            query_ops, operator_models, operator_features,
            pattern_models, pattern_features, pattern_info
        )

        all_predictions.extend(predictions)

    return all_predictions


# Predict single query bottom-up
def predict_single_query(
    query_ops: pd.DataFrame,
    operator_models: dict,
    operator_features: dict,
    pattern_models: dict,
    pattern_features: dict,
    pattern_info: dict
) -> list:
    root = build_tree_from_dataframe(query_ops)
    all_nodes = extract_all_nodes(root)
    nodes_by_depth = sorted(all_nodes, key=lambda n: n.depth, reverse=True)

    prediction_cache = {}
    consumed_nodes = set()
    predictions = []

    for node in nodes_by_depth:
        if node.node_id in consumed_nodes:
            continue

        matched_pattern = None

        if pattern_info:
            matched_pattern = match_pattern(node, pattern_info)

        if matched_pattern and matched_pattern in pattern_models:
            pattern_hash = matched_pattern
            info = pattern_info[pattern_hash]
            pattern_node_ids = extract_pattern_node_ids(node, info['length'])
            consumed_nodes.update(pattern_node_ids)

            pred_start, pred_exec = predict_pattern(
                node, query_ops, pattern_models[pattern_hash], prediction_cache, info['length']
            )

            for nid in pattern_node_ids:
                prediction_cache[nid] = {'start': pred_start, 'exec': pred_exec}

            row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
            predictions.append(create_prediction_result(row, pred_start, pred_exec, 'pattern'))
        else:
            pred_start, pred_exec = predict_operator(
                node, query_ops, operator_models, operator_features, prediction_cache
            )

            prediction_cache[node.node_id] = {'start': pred_start, 'exec': pred_exec}

            row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
            predictions.append(create_prediction_result(row, pred_start, pred_exec, 'operator'))

    return predictions


# Match node against available patterns
def match_pattern(node, pattern_info: dict) -> str:
    for pattern_hash, info in pattern_info.items():
        pattern_length = info['length']

        if not has_children_at_length(node, pattern_length):
            continue

        computed_hash = compute_pattern_hash(node, pattern_length)

        if computed_hash == pattern_hash:
            return pattern_hash

    return None


# Predict using pattern model
def predict_pattern(node, query_ops: pd.DataFrame, model: dict, prediction_cache: dict, pattern_length: int) -> tuple:
    pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
    pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]
    aggregated = aggregate_pattern_with_cache(pattern_rows, pattern_length, query_ops, prediction_cache, set(pattern_node_ids))

    X_exec = pd.DataFrame([[aggregated.get(f, 0) for f in model['features_exec']]], columns=model['features_exec'])
    X_start = pd.DataFrame([[aggregated.get(f, 0) for f in model['features_start']]], columns=model['features_start'])

    pred_exec = model['execution_time'].predict(X_exec)[0]
    pred_start = model['start_time'].predict(X_start)[0]

    return pred_start, pred_exec


# Predict using operator model
def predict_operator(node, query_ops: pd.DataFrame, operator_models: dict, operator_features: dict, prediction_cache: dict) -> tuple:
    op_name = csv_name_to_folder_name(node.node_type)

    if op_name not in operator_models['execution_time'] or op_name not in operator_models['start_time']:
        return 0.0, 0.0

    row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
    features = build_operator_features(row, node, prediction_cache)

    model_exec = operator_models['execution_time'][op_name]
    model_start = operator_models['start_time'][op_name]

    exec_feature_names = operator_features['execution_time'].get(op_name, [])
    start_feature_names = operator_features['start_time'].get(op_name, [])

    if not exec_feature_names or not start_feature_names:
        return 0.0, 0.0

    X_exec = pd.DataFrame([[features.get(f, 0) for f in exec_feature_names]], columns=exec_feature_names)
    X_start = pd.DataFrame([[features.get(f, 0) for f in start_feature_names]], columns=start_feature_names)

    pred_exec = model_exec.predict(X_exec)[0]
    pred_start = model_start.predict(X_start)[0]

    return pred_start, pred_exec


# Build operator features with child predictions
def build_operator_features(row, node, prediction_cache: dict) -> dict:
    features = {}

    for col in row.index:
        if col not in ['query_file', 'subplan_name', 'actual_startup_time', 'actual_total_time']:
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


# Create prediction result dictionary
def create_prediction_result(row, pred_start: float, pred_exec: float, prediction_type: str) -> dict:
    return {
        'query_file': row['query_file'],
        'node_id': row['node_id'],
        'node_type': row['node_type'],
        'depth': row['depth'],
        'parent_relationship': row['parent_relationship'],
        'subplan_name': row['subplan_name'],
        'actual_startup_time': row['actual_startup_time'],
        'actual_total_time': row['actual_total_time'],
        'predicted_startup_time': pred_start,
        'predicted_total_time': pred_exec,
        'prediction_type': prediction_type
    }


# Export predictions to CSV
def export_predictions(predictions: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(predictions)
    df.to_csv(output_path / 'predictions.csv', sep=';', index=False)


# Aggregate pattern with prediction cache
def aggregate_pattern_with_cache(
    pattern_rows: pd.DataFrame,
    pattern_length: int,
    full_query_ops: pd.DataFrame,
    prediction_cache: dict,
    pattern_node_ids: set
) -> dict:
    if pattern_rows.empty:
        return {}

    pattern_rows = pattern_rows.sort_values('depth').reset_index(drop=True)
    root = build_tree_from_dataframe(pattern_rows)

    return aggregate_subtree_with_cache(
        root, pattern_rows, full_query_ops, prediction_cache, pattern_node_ids, pattern_length - 1, is_root=True
    )


# Aggregate subtree with prediction cache
def aggregate_subtree_with_cache(
    node,
    pattern_rows: pd.DataFrame,
    full_query_ops: pd.DataFrame,
    prediction_cache: dict,
    pattern_node_ids: set,
    remaining_depth: int,
    is_root: bool = False
) -> dict:
    aggregated = {}
    row = pattern_rows[pattern_rows['node_id'] == node.node_id].iloc[0]
    node_type_clean = node.node_type.replace(' ', '')

    if is_root:
        prefix = node_type_clean + '_'
    else:
        prefix = node_type_clean + '_' + node.parent_relationship + '_'

    for col in row.index:
        if col not in ['query_file', 'subplan_name', 'actual_startup_time', 'actual_total_time']:
            aggregated[prefix + col] = row[col]

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
            child_agg = aggregate_subtree_with_cache(
                child, pattern_rows, full_query_ops, prediction_cache, pattern_node_ids, remaining_depth - 1, is_root=False
            )
            aggregated.update(child_agg)

    return aggregated


# Get children from full query ops
def get_children_from_full_query(full_query_ops: pd.DataFrame, parent_node_id: int) -> list:
    parent_row = full_query_ops[full_query_ops['node_id'] == parent_node_id]

    if parent_row.empty:
        return []

    parent_depth = parent_row.iloc[0]['depth']
    parent_idx = parent_row.index[0]
    children = []

    for idx in range(parent_idx + 1, len(full_query_ops)):
        row = full_query_ops.iloc[idx]

        if row['depth'] == parent_depth + 1:
            children.append(row)
        elif row['depth'] <= parent_depth:
            break

    return children


# Build tree from flat DataFrame
def build_tree_from_dataframe(query_ops: pd.DataFrame):
    nodes = {}
    root = None
    min_depth = query_ops['depth'].min()

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'] if pd.notna(row['parent_relationship']) else '',
            depth=row['depth'],
            node_id=row['node_id']
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
def extract_all_nodes(node) -> list:
    nodes = [node]

    for child in node.children:
        nodes.extend(extract_all_nodes(child))

    return nodes


# Check if node has children at target length
def has_children_at_length(node, pattern_length: int) -> bool:
    if pattern_length == 1:
        return True

    if pattern_length == 2:
        return len(node.children) > 0

    if len(node.children) == 0:
        return False

    return any(has_children_at_length(child, pattern_length - 1) for child in node.children)


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


# Extract pattern node IDs
def extract_pattern_node_ids(node, remaining_length: int) -> list:
    if remaining_length == 1 or len(node.children) == 0:
        return [node.node_id]

    node_ids = [node.node_id]

    for child in node.children:
        child_ids = extract_pattern_node_ids(child, remaining_length - 1)
        node_ids.extend(child_ids)

    return node_ids


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file', help='Path to Test.csv')
    parser.add_argument('operator_model_dir', help='Path to Model/Operators_Training/')
    parser.add_argument('operator_overview_file', help='Path to two_step_evaluation_overview.csv')
    parser.add_argument('--pattern-model-dir', default=None, help='Path to pattern models (Model/Patterns_Training_*)')
    parser.add_argument('--pattern-ffs-file', default=None, help='Path to pattern_ffs_overview.csv')
    parser.add_argument('--selected-patterns', default=None, help='Path to selected_patterns.csv')
    parser.add_argument('--pattern-metadata', default=None, help='Path to 06_patterns_by_*.csv (for pattern_length)')
    parser.add_argument('--output-dir', required=True, help='Output directory for predictions')
    args = parser.parse_args()

    run_prediction(
        args.test_file,
        args.operator_model_dir,
        args.operator_overview_file,
        args.output_dir,
        args.pattern_model_dir,
        args.pattern_ffs_file,
        args.selected_patterns,
        args.pattern_metadata
    )
