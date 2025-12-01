#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import hashlib
import shutil
import sys
from pathlib import Path
from collections import defaultdict
import pandas as pd
import numpy as np
import pickle
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline

sys.path.insert(0, str(Path(__file__).parent.parent))

# From mapping_config.py: Configuration for dynamic prediction
from mapping_config import THRESHOLD, FEATURE_SET

SVM_PARAMS = {
    'kernel': 'rbf',
    'nu': 0.65,
    'C': 1.5,
    'gamma': 'scale',
    'cache_size': 500
}

# ORCHESTRATOR

def main_workflow(baseline_dir: str, output_dir: str) -> None:
    baseline_path = Path(baseline_dir)
    output_path = Path(output_dir)
    template_folders = sorted([d for d in baseline_path.iterdir() if d.is_dir()])

    for template_folder in template_folders:
        process_template_fold(template_folder, output_path)


def process_template_fold(template_folder: Path, output_path: Path) -> None:
    template_name = template_folder.name
    training_file = template_folder / 'training_cleaned.csv'
    test_file = template_folder / '02_test_cleaned.csv'

    if not training_file.exists() or not test_file.exists():
        return

    model_dir = output_path.parent / 'Model' / template_name
    model_dir.mkdir(parents=True, exist_ok=True)

    df_training = load_data(training_file)
    df_test = load_data(test_file)

    hash_index = build_hash_index(df_training)
    pattern_models = {}
    operator_models = {}
    all_predictions = []

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        predictions = predict_single_query(query_ops, df_training, hash_index, model_dir, pattern_models, operator_models)
        all_predictions.extend(predictions)

    output_folder = output_path / template_name
    output_folder.mkdir(parents=True, exist_ok=True)

    if all_predictions:
        predictions_df = pd.DataFrame(all_predictions)
        predictions_df.to_csv(output_folder / 'predictions.csv', sep=';', index=False)


# FUNCTIONS

# Load data from CSV with semicolon delimiter
def load_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')


# Build hash index from training data
def build_hash_index(df_training: pd.DataFrame) -> dict:
    hash_counts = defaultdict(int)

    for query_file in df_training['query_file'].unique():
        query_ops = df_training[df_training['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree(query_ops)
        collect_subtree_hashes(root, hash_counts)

    return dict(hash_counts)


# Collect all subtree hashes from a node recursively
def collect_subtree_hashes(node, hash_counts: dict) -> None:
    max_depth = get_max_depth(node)

    for depth in range(max_depth + 1):
        subtree_hash = compute_hash_at_depth(node, depth)
        hash_counts[subtree_hash] += 1

    for child in node.children:
        collect_subtree_hashes(child, hash_counts)


# Get maximum depth of subtree from node
def get_max_depth(node) -> int:
    if not node.children:
        return 0
    return 1 + max(get_max_depth(child) for child in node.children)


# Compute structural hash at specific depth
def compute_hash_at_depth(node, remaining_depth: int) -> str:
    if remaining_depth == 0 or not node.children:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_hash_at_depth(child, remaining_depth - 1)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)

    return hashlib.md5(combined_string.encode()).hexdigest()


# Build tree structure from DataFrame
def build_tree(query_ops: pd.DataFrame):
    nodes = {}
    root = None

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'],
            depth=row['depth'],
            node_id=row['node_id'],
            df_index=idx,
            row_data=row
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


# Predict single query with dynamic pattern search
def predict_single_query(query_ops: pd.DataFrame, df_training: pd.DataFrame, hash_index: dict, model_dir: Path, pattern_models: dict, operator_models: dict) -> list:
    root = build_tree(query_ops)
    execution_plan = find_patterns_recursive(root, hash_index, set())

    for step in execution_plan:
        if step['type'] == 'pattern':
            pattern_hash = step['pattern_hash']
            if pattern_hash not in pattern_models:
                training_data = extract_pattern_training_data(df_training, pattern_hash, step['depth'])
                if len(training_data) > 0:
                    pattern_models[pattern_hash] = train_pattern_models(training_data, model_dir, pattern_hash)

        elif step['type'] == 'operator':
            node_type = step['node'].node_type
            if node_type not in operator_models:
                training_data = extract_operator_training_data(df_training, node_type)
                if len(training_data) > 0:
                    operator_models[node_type] = train_operator_models(training_data, model_dir, node_type)

    predictions = execute_bottom_up(execution_plan, query_ops, pattern_models, operator_models)

    return predictions


# Find patterns recursively with threshold-based shrinking
def find_patterns_recursive(node, hash_index: dict, consumed: set) -> list:
    if node.df_index in consumed:
        return []

    execution_plan = []
    max_depth = get_max_depth(node)

    for depth in range(max_depth, -1, -1):
        subtree_hash = compute_hash_at_depth(node, depth)
        count = hash_index.get(subtree_hash, 0)

        if count >= THRESHOLD:
            node_ids = extract_node_ids_at_depth(node, depth)
            consumed.update(node_ids)

            execution_plan.append({
                'type': 'pattern',
                'pattern_hash': subtree_hash,
                'root_node': node,
                'depth': depth,
                'node_ids': node_ids
            })

            leaf_nodes = get_pattern_leaf_nodes(node, depth)
            for leaf in leaf_nodes:
                for child in leaf.children:
                    child_plan = find_patterns_recursive(child, hash_index, consumed)
                    execution_plan.extend(child_plan)

            return execution_plan

    consumed.add(node.df_index)
    execution_plan.append({
        'type': 'operator',
        'node': node,
        'df_index': node.df_index
    })

    for child in node.children:
        child_plan = find_patterns_recursive(child, hash_index, consumed)
        execution_plan.extend(child_plan)

    return execution_plan


# Get leaf nodes of a pattern at specific depth
def get_pattern_leaf_nodes(node, remaining_depth: int) -> list:
    if remaining_depth == 0 or not node.children:
        return [node]

    leaf_nodes = []
    for child in node.children:
        leaf_nodes.extend(get_pattern_leaf_nodes(child, remaining_depth - 1))
    return leaf_nodes


# Extract node IDs at specific depth from node
def extract_node_ids_at_depth(node, remaining_depth: int) -> set:
    if remaining_depth == 0 or not node.children:
        return {node.df_index}

    node_ids = {node.df_index}
    for child in node.children:
        node_ids.update(extract_node_ids_at_depth(child, remaining_depth - 1))

    return node_ids


# Extract and aggregate pattern training data
def extract_pattern_training_data(df_training: pd.DataFrame, pattern_hash: str, pattern_depth: int) -> pd.DataFrame:
    aggregated_rows = []

    for query_file in df_training['query_file'].unique():
        query_ops = df_training[df_training['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree(query_ops)
        matches = find_hash_matches(root, pattern_hash, pattern_depth)

        for match_node in matches:
            aggregated = aggregate_subtree(match_node, pattern_depth)
            aggregated_rows.append(aggregated)

    if not aggregated_rows:
        return pd.DataFrame()

    return pd.DataFrame(aggregated_rows)


# Find all nodes matching a specific hash at depth
def find_hash_matches(node, target_hash: str, target_depth: int) -> list:
    matches = []

    computed_hash = compute_hash_at_depth(node, target_depth)
    if computed_hash == target_hash:
        matches.append(node)

    for child in node.children:
        matches.extend(find_hash_matches(child, target_hash, target_depth))

    return matches


# Aggregate subtree into single row with hierarchical prefixes
def aggregate_subtree(node, target_depth: int, prefix: str = '') -> dict:
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

    if target_depth > 0 and node.children:
        children_sorted = sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1 if c.parent_relationship == 'Inner' else 2, c.node_type))

        for child in children_sorted:
            child_prefix = clean_node_type(child.node_type) + '_' + child.parent_relationship + '_'
            child_agg = aggregate_subtree(child, target_depth - 1, child_prefix)
            aggregated.update(child_agg)

    return aggregated


# Clean node type for column naming
def clean_node_type(node_type: str) -> str:
    return node_type.replace(' ', '')


# Extract operator training data
def extract_operator_training_data(df_training: pd.DataFrame, node_type: str) -> pd.DataFrame:
    return df_training[df_training['node_type'] == node_type].copy()


# Train pattern models for both targets
def train_pattern_models(df: pd.DataFrame, model_dir: Path, pattern_hash: str) -> dict:
    exclude_cols = ['query_file', 'actual_startup_time', 'actual_total_time']
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    feature_cols = [col for col in numeric_cols if col not in exclude_cols]

    if len(feature_cols) == 0 or len(df) < 5:
        return None

    model_exec = train_model(df, feature_cols, 'actual_total_time')
    model_start = train_model(df, feature_cols, 'actual_startup_time')

    with open(model_dir / f'pattern_{pattern_hash[:8]}_exec.pkl', 'wb') as f:
        pickle.dump(model_exec, f)
    with open(model_dir / f'pattern_{pattern_hash[:8]}_start.pkl', 'wb') as f:
        pickle.dump(model_start, f)

    return {
        'execution_time': model_exec,
        'start_time': model_start,
        'features': feature_cols
    }


# Train operator models for both targets
def train_operator_models(df: pd.DataFrame, model_dir: Path, node_type: str) -> dict:
    available_features = [f for f in FEATURE_SET if f in df.columns]

    if len(available_features) == 0 or len(df) < 5:
        return None

    model_exec = train_model(df, available_features, 'actual_total_time')
    model_start = train_model(df, available_features, 'actual_startup_time')

    clean_name = node_type.replace(' ', '_')
    with open(model_dir / f'operator_{clean_name}_exec.pkl', 'wb') as f:
        pickle.dump(model_exec, f)
    with open(model_dir / f'operator_{clean_name}_start.pkl', 'wb') as f:
        pickle.dump(model_start, f)

    return {
        'execution_time': model_exec,
        'start_time': model_start,
        'features': available_features
    }


# Train single SVM model
def train_model(df: pd.DataFrame, features: list, target: str):
    X = df[features].fillna(0)
    y = df[target]

    pipeline = Pipeline([
        ('scaler', MaxAbsScaler()),
        ('model', NuSVR(**SVM_PARAMS))
    ])

    pipeline.fit(X, y)
    return pipeline


# Execute bottom-up prediction
def execute_bottom_up(execution_plan: list, query_ops: pd.DataFrame, pattern_models: dict, operator_models: dict) -> list:
    prediction_cache = {}
    all_predictions = []

    for step in reversed(execution_plan):
        if step['type'] == 'pattern':
            preds = execute_pattern_prediction(step, query_ops, pattern_models, prediction_cache)
            for pred in preds:
                prediction_cache[pred['node_id']] = pred
                all_predictions.append(pred)

        elif step['type'] == 'operator':
            pred = execute_operator_prediction(step, query_ops, operator_models, prediction_cache)
            prediction_cache[pred['node_id']] = pred
            all_predictions.append(pred)

    return all_predictions


# Execute pattern prediction
def execute_pattern_prediction(step: dict, query_ops: pd.DataFrame, pattern_models: dict, prediction_cache: dict) -> list:
    pattern_hash = step['pattern_hash']
    root_node = step['root_node']
    depth = step['depth']

    model_info = pattern_models.get(pattern_hash)
    predictions = []

    aggregated = aggregate_subtree_for_prediction(root_node, depth, prediction_cache)

    node_ids = step['node_ids']
    for idx in node_ids:
        row = query_ops.iloc[idx]

        if model_info:
            pred_startup = predict_with_model(model_info['start_time'], aggregated, model_info['features'])
            pred_total = predict_with_model(model_info['execution_time'], aggregated, model_info['features'])
        else:
            pred_startup = 0.0
            pred_total = 0.0

        predictions.append({
            'query_file': row['query_file'],
            'node_id': row['node_id'],
            'node_type': row['node_type'],
            'depth': row['depth'],
            'parent_relationship': row['parent_relationship'],
            'subplan_name': row.get('subplan_name', ''),
            'actual_startup_time': row.get('actual_startup_time', 0.0),
            'actual_total_time': row.get('actual_total_time', 0.0),
            'predicted_startup_time': pred_startup,
            'predicted_total_time': pred_total,
            'prediction_type': 'pattern'
        })

    return predictions


# Aggregate subtree for prediction with child predictions injected
def aggregate_subtree_for_prediction(node, target_depth: int, prediction_cache: dict, prefix: str = '') -> dict:
    aggregated = {}
    is_root = (prefix == '')

    if is_root:
        node_prefix = clean_node_type(node.node_type) + '_'
    else:
        node_prefix = prefix

    for col in node.row_data.index:
        if col in ['query_file', 'actual_startup_time', 'actual_total_time']:
            continue
        aggregated[node_prefix + col] = node.row_data[col]

    if target_depth > 0 and node.children:
        children_sorted = sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1 if c.parent_relationship == 'Inner' else 2, c.node_type))

        for child in children_sorted:
            child_prefix = clean_node_type(child.node_type) + '_' + child.parent_relationship + '_'

            if child.node_id in prediction_cache:
                child_pred = prediction_cache[child.node_id]
                aggregated[child_prefix + 'st1'] = child_pred['predicted_startup_time']
                aggregated[child_prefix + 'rt1'] = child_pred['predicted_total_time']
            else:
                child_agg = aggregate_subtree_for_prediction(child, target_depth - 1, prediction_cache, child_prefix)
                aggregated.update(child_agg)

    return aggregated


# Execute operator prediction
def execute_operator_prediction(step: dict, query_ops: pd.DataFrame, operator_models: dict, prediction_cache: dict) -> dict:
    node = step['node']
    row = query_ops.iloc[node.df_index]

    node_type = row['node_type']
    model_info = operator_models.get(node_type)

    features = build_operator_features(row, node, prediction_cache)

    if model_info:
        pred_startup = predict_with_model(model_info['start_time'], features, model_info['features'])
        pred_total = predict_with_model(model_info['execution_time'], features, model_info['features'])
    else:
        pred_startup = 0.0
        pred_total = 0.0

    return {
        'query_file': row['query_file'],
        'node_id': row['node_id'],
        'node_type': row['node_type'],
        'depth': row['depth'],
        'parent_relationship': row['parent_relationship'],
        'subplan_name': row.get('subplan_name', ''),
        'actual_startup_time': row.get('actual_startup_time', 0.0),
        'actual_total_time': row.get('actual_total_time', 0.0),
        'predicted_startup_time': pred_startup,
        'predicted_total_time': pred_total,
        'prediction_type': 'operator'
    }


# Build operator features with child predictions
def build_operator_features(row, node, prediction_cache: dict) -> dict:
    features = {}

    for col in FEATURE_SET:
        if col in row.index:
            features[col] = row[col]
        else:
            features[col] = 0.0

    features['st1'] = 0.0
    features['rt1'] = 0.0
    features['st2'] = 0.0
    features['rt2'] = 0.0

    for child in node.children:
        if child.node_id in prediction_cache:
            child_pred = prediction_cache[child.node_id]
            if child.parent_relationship == 'Outer':
                features['st1'] = child_pred['predicted_startup_time']
                features['rt1'] = child_pred['predicted_total_time']
            elif child.parent_relationship == 'Inner':
                features['st2'] = child_pred['predicted_startup_time']
                features['rt2'] = child_pred['predicted_total_time']

    return features


# Predict with trained model
def predict_with_model(model, features_dict: dict, feature_names: list) -> float:
    if model is None:
        return 0.0

    feature_values = []
    for feat in feature_names:
        val = features_dict.get(feat, 0.0)
        if pd.isna(val):
            val = 0.0
        feature_values.append(float(val))

    if len(feature_values) == 0:
        return 0.0

    X = np.array([feature_values])

    prediction = model.predict(X)[0]
    return max(0.0, prediction)


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int, df_index: int = None, row_data=None):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.df_index = df_index
        self.row_data = row_data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline_dir", help="Path to Dynamic/Datasets/Baseline_SVM/ containing 14 template folders")
    parser.add_argument("--output-dir", required=True, help="Output directory for predictions")

    args = parser.parse_args()

    main_workflow(args.baseline_dir, args.output_dir)
