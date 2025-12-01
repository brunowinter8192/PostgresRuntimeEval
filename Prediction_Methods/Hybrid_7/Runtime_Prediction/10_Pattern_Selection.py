#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
import hashlib
import json
from pathlib import Path
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
import joblib
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from Runtime_Prediction.ffs_config import SVM_PARAMS

STRATEGIES = ['frequency', 'size', 'error']


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
def run_pattern_selection(
    strategy: str,
    sorted_patterns_file: str,
    pattern_ffs_file: str,
    training_file: str,
    test_file: str,
    operator_model_dir: str,
    operator_ffs_dir: str,
    output_dir: str,
    model_dir: str,
    pretrained_dir: str = None,
    pattern_occurrences_file: str = None
) -> None:
    operator_models = load_operator_models(operator_model_dir)
    operator_ffs = load_operator_ffs(operator_ffs_dir)
    pattern_ffs = load_pattern_ffs(pattern_ffs_file)
    sorted_patterns = load_sorted_patterns(sorted_patterns_file)
    df_training = load_training_data(training_file)
    df_test = load_test_data(test_file)

    if strategy == 'error':
        pattern_occurrences = load_pattern_occurrences(pattern_occurrences_file)
        run_error_selection(
            sorted_patterns, pattern_occurrences, pattern_ffs, df_training, df_test,
            operator_models, operator_ffs, output_dir, model_dir, pretrained_dir
        )
    else:
        run_static_selection(
            sorted_patterns, pattern_ffs, df_training, df_test,
            operator_models, operator_ffs, output_dir, model_dir, pretrained_dir
        )


# Run static selection for frequency/size strategies
def run_static_selection(
    sorted_patterns: pd.DataFrame,
    pattern_ffs: dict,
    df_training: pd.DataFrame,
    df_test: pd.DataFrame,
    operator_models: dict,
    operator_ffs: dict,
    output_dir: str,
    model_dir: str,
    pretrained_dir: str
) -> None:
    baseline_mre = 0.2297
    selected_pattern_models = {}
    selected_pattern_info = {}
    selection_log = []

    for idx, pattern_row in sorted_patterns.iterrows():
        pattern_hash = pattern_row['pattern_hash']
        pattern_string = pattern_row['pattern_string']
        pattern_length = int(pattern_row['pattern_length'])
        operator_count = int(pattern_row['operator_count'])

        if pattern_hash not in pattern_ffs:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_NO_FFS', idx
            ))
            continue

        pattern_model = load_or_train_pattern_model(
            pretrained_dir, df_training, pattern_hash, pattern_length, operator_count, pattern_ffs[pattern_hash]
        )

        if pattern_model is None:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_TRAIN_FAILED', idx
            ))
            continue

        test_models = {**selected_pattern_models, pattern_hash: pattern_model}
        test_info = {**selected_pattern_info, pattern_hash: {'length': pattern_length, 'operator_count': operator_count}}

        predictions = predict_all_queries(
            df_test, operator_models, operator_ffs, test_models, pattern_ffs, test_info
        )

        new_mre = calculate_mre(predictions)

        if new_mre < baseline_mre:
            status = 'SELECTED'
            selected_pattern_models[pattern_hash] = pattern_model
            selected_pattern_info[pattern_hash] = {'length': pattern_length, 'operator_count': operator_count}
            save_pattern_model(model_dir, pattern_hash, pattern_model)
            old_baseline = baseline_mre
            baseline_mre = new_mre
            delta = old_baseline - new_mre
        else:
            status = 'REJECTED'
            delta = new_mre - baseline_mre

        export_pattern_results(output_dir, pattern_hash, pattern_string, predictions, new_mre, status)

        selection_log.append(create_log_entry(
            pattern_hash, pattern_string, baseline_mre, new_mre, delta, status, idx
        ))

    export_selection_summary(output_dir, selection_log)


# Run dynamic error-based selection with re-ranking
def run_error_selection(
    error_baseline: pd.DataFrame,
    pattern_occurrences: pd.DataFrame,
    pattern_ffs: dict,
    df_training: pd.DataFrame,
    df_test: pd.DataFrame,
    operator_models: dict,
    operator_ffs: dict,
    output_dir: str,
    model_dir: str,
    pretrained_dir: str
) -> None:
    baseline_mre = 0.2297
    selected_pattern_models = {}
    selected_pattern_info = {}
    consumed_hashes = set()
    selection_log = []

    current_predictions = predict_all_queries(
        df_test, operator_models, operator_ffs, {}, pattern_ffs, {}
    )

    iteration = 0
    while True:
        error_ranking = calculate_error_ranking(
            current_predictions, pattern_occurrences, consumed_hashes, error_baseline
        )

        if error_ranking.empty:
            break

        candidate = select_next_candidate(error_ranking, pattern_ffs, consumed_hashes)
        if candidate is None:
            break

        pattern_hash = candidate['pattern_hash']
        pattern_info = error_baseline[error_baseline['pattern_hash'] == pattern_hash].iloc[0]
        pattern_string = pattern_info['pattern_string']
        pattern_length = int(pattern_info['pattern_length'])
        operator_count = int(pattern_info['operator_count'])

        consumed_hashes.add(pattern_hash)

        if pattern_hash not in pattern_ffs:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_NO_FFS', iteration
            ))
            continue

        pattern_model = load_or_train_pattern_model(
            pretrained_dir, df_training, pattern_hash, pattern_length, operator_count, pattern_ffs[pattern_hash]
        )

        if pattern_model is None:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_TRAIN_FAILED', iteration
            ))
            continue

        test_models = {**selected_pattern_models, pattern_hash: pattern_model}
        test_info = {**selected_pattern_info, pattern_hash: {'length': pattern_length, 'operator_count': operator_count}}

        new_predictions = predict_all_queries(
            df_test, operator_models, operator_ffs, test_models, pattern_ffs, test_info
        )

        new_mre = calculate_mre(new_predictions)

        if new_mre < baseline_mre:
            status = 'SELECTED'
            selected_pattern_models[pattern_hash] = pattern_model
            selected_pattern_info[pattern_hash] = {'length': pattern_length, 'operator_count': operator_count}
            save_pattern_model(model_dir, pattern_hash, pattern_model)
            old_baseline = baseline_mre
            baseline_mre = new_mre
            delta = old_baseline - new_mre
            current_predictions = new_predictions
        else:
            status = 'REJECTED'
            delta = new_mre - baseline_mre

        export_pattern_results(output_dir, pattern_hash, pattern_string, new_predictions, new_mre, status)

        selection_log.append(create_log_entry(
            pattern_hash, pattern_string, baseline_mre, new_mre, delta, status, iteration
        ))

        iteration += 1

    export_selection_summary(output_dir, selection_log)


# FUNCTIONS

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


# Load operator FFS features from directory (preserving order)
def load_operator_ffs(ffs_dir: str) -> dict:
    features = {'execution_time': {}, 'start_time': {}}
    ffs_path = Path(ffs_dir)

    for target in ['execution_time', 'start_time']:
        target_dir = ffs_path / target
        if not target_dir.exists():
            continue

        for op_folder in target_dir.iterdir():
            if op_folder.is_dir() and op_folder.name.endswith('_csv'):
                op_name = op_folder.name.replace('_csv', '')
                ffs_file = op_folder / 'final_features.csv'
                if ffs_file.exists():
                    df = pd.read_csv(ffs_file, delimiter=';')
                    df = df.sort_values('order')
                    features[target][op_name] = df['feature'].tolist()

    return features


# Load pattern FFS features from overview CSV
def load_pattern_ffs(pattern_ffs_file: str) -> dict:
    df = pd.read_csv(pattern_ffs_file, delimiter=';')
    features = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern']
        target = row['target']

        if pattern_hash not in features:
            features[pattern_hash] = {}

        if pd.isna(row['final_features']) or row['final_features'] == '':
            features[pattern_hash][target] = []
        else:
            features[pattern_hash][target] = [f.strip() for f in row['final_features'].split(',')]

    return features


# Load sorted patterns from CSV
def load_sorted_patterns(sorted_patterns_file: str) -> pd.DataFrame:
    return pd.read_csv(sorted_patterns_file, delimiter=';')


# Load pattern occurrences from CSV (for error strategy)
def load_pattern_occurrences(pattern_occurrences_file: str) -> pd.DataFrame:
    return pd.read_csv(pattern_occurrences_file, delimiter=';')


# Load training data
def load_training_data(training_file: str) -> pd.DataFrame:
    df = pd.read_csv(training_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load test data
def load_test_data(test_file: str) -> pd.DataFrame:
    df = pd.read_csv(test_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Calculate error ranking based on current predictions (for error strategy)
def calculate_error_ranking(
    predictions: list,
    pattern_occurrences: pd.DataFrame,
    consumed_hashes: set,
    error_baseline: pd.DataFrame
) -> pd.DataFrame:
    available = pattern_occurrences[~pattern_occurrences['pattern_hash'].isin(consumed_hashes)]

    if available.empty:
        return pd.DataFrame()

    pred_lookup = {}
    for p in predictions:
        key = (p['query_file'], p['node_id'])
        if p['actual_total_time'] > 0:
            mre = abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time']
            pred_lookup[key] = mre

    metadata_dict = {}
    for _, row in error_baseline.iterrows():
        metadata_dict[row['pattern_hash']] = {
            'pattern_string': row['pattern_string'],
            'pattern_length': row['pattern_length'],
            'operator_count': row['operator_count']
        }

    results = []
    for pattern_hash in available['pattern_hash'].unique():
        occurrences = available[available['pattern_hash'] == pattern_hash]
        mre_values = []

        for _, occ in occurrences.iterrows():
            key = (occ['query_file'], occ['root_node_id'])
            if key in pred_lookup:
                mre_values.append(pred_lookup[key])

        if mre_values:
            avg_mre = np.mean(mre_values)
            error_score = len(occurrences) * avg_mre

            meta = metadata_dict.get(pattern_hash, {})
            results.append({
                'pattern_hash': pattern_hash,
                'pattern_string': meta.get('pattern_string', ''),
                'pattern_length': meta.get('pattern_length', 0),
                'operator_count': meta.get('operator_count', 0),
                'occurrence_count': len(occurrences),
                'avg_mre': avg_mre,
                'avg_mre_pct': avg_mre * 100,
                'error_score': error_score
            })

    if not results:
        return pd.DataFrame()

    return pd.DataFrame(results).sort_values(
        by=['error_score', 'pattern_hash'],
        ascending=[False, True]
    ).reset_index(drop=True)


# Select next candidate pattern with highest error_score that has FFS
def select_next_candidate(
    error_ranking: pd.DataFrame,
    pattern_ffs: dict,
    consumed_hashes: set
) -> dict:
    for _, row in error_ranking.iterrows():
        pattern_hash = row['pattern_hash']
        if pattern_hash in consumed_hashes:
            continue
        if pattern_hash in pattern_ffs:
            return row.to_dict()
    return None


# Create log entry dict
def create_log_entry(
    pattern_hash: str,
    pattern_string: str,
    baseline_mre: float,
    new_mre: float,
    delta: float,
    status: str,
    iteration: int
) -> dict:
    return {
        'iteration': iteration,
        'pattern_hash': pattern_hash,
        'pattern_string': pattern_string,
        'baseline_mre': baseline_mre,
        'new_mre': new_mre,
        'delta': delta,
        'status': status
    }


# Load pretrained model from disk
def load_pretrained_model(pretrained_dir: str, pattern_hash: str) -> dict:
    pattern_path = Path(pretrained_dir) / pattern_hash
    if not pattern_path.exists():
        return None

    model_exec_file = pattern_path / 'model_execution_time.pkl'
    model_start_file = pattern_path / 'model_start_time.pkl'
    features_file = pattern_path / 'features.json'

    if not all(f.exists() for f in [model_exec_file, model_start_file, features_file]):
        return None

    with open(features_file, 'r') as f:
        features = json.load(f)

    return {
        'execution_time': joblib.load(model_exec_file),
        'start_time': joblib.load(model_start_file),
        'features_exec': features['features_exec'],
        'features_start': features['features_start']
    }


# Load pretrained model or train on-the-fly
def load_or_train_pattern_model(
    pretrained_dir: str,
    df_training: pd.DataFrame,
    pattern_hash: str,
    pattern_length: int,
    operator_count: int,
    ffs_features: dict
) -> dict:
    if pretrained_dir:
        pretrained_model = load_pretrained_model(pretrained_dir, pattern_hash)
        if pretrained_model:
            return pretrained_model

    return train_pattern_model(df_training, pattern_hash, pattern_length, operator_count, ffs_features)


# Train pattern model by extracting and aggregating on-the-fly
def train_pattern_model(
    df_training: pd.DataFrame,
    pattern_hash: str,
    pattern_length: int,
    operator_count: int,
    ffs_features: dict
) -> dict:
    aggregated_rows = []

    for query_file in df_training['query_file'].unique():
        query_ops = df_training[df_training['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            if not has_children_at_length(node, pattern_length):
                continue

            computed_hash = compute_pattern_hash(node, pattern_length)
            if computed_hash != pattern_hash:
                continue

            pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
            pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]
            aggregated = aggregate_pattern(pattern_rows, pattern_length)
            if aggregated:
                aggregated_rows.append(aggregated)

    if len(aggregated_rows) < 5:
        return None

    df_agg = pd.DataFrame(aggregated_rows)

    exec_features = ffs_features.get('execution_time', [])
    start_features = ffs_features.get('start_time', [])

    if not exec_features or not start_features:
        return None

    exec_features_valid = [f for f in exec_features if f in df_agg.columns]
    start_features_valid = [f for f in start_features if f in df_agg.columns]

    if not exec_features_valid or not start_features_valid:
        return None

    X_exec = df_agg[exec_features_valid].fillna(0)
    X_start = df_agg[start_features_valid].fillna(0)
    y_exec = df_agg['actual_total_time']
    y_start = df_agg['actual_startup_time']

    model_exec = Pipeline([('scaler', MaxAbsScaler()), ('model', NuSVR(**SVM_PARAMS))])
    model_start = Pipeline([('scaler', MaxAbsScaler()), ('model', NuSVR(**SVM_PARAMS))])

    model_exec.fit(X_exec, y_exec)
    model_start.fit(X_start, y_start)

    return {
        'execution_time': model_exec,
        'start_time': model_start,
        'features_exec': exec_features_valid,
        'features_start': start_features_valid
    }


# Predict all queries using operator and pattern models
def predict_all_queries(
    df_test: pd.DataFrame,
    operator_models: dict,
    operator_ffs: dict,
    pattern_models: dict,
    pattern_ffs: dict,
    pattern_info: dict
) -> list:
    all_predictions = []

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        predictions = predict_single_query(
            query_ops, operator_models, operator_ffs, pattern_models, pattern_ffs, pattern_info
        )
        all_predictions.extend(predictions)

    return all_predictions


# Predict single query bottom-up
def predict_single_query(
    query_ops: pd.DataFrame,
    operator_models: dict,
    operator_ffs: dict,
    pattern_models: dict,
    pattern_ffs: dict,
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

        matched_pattern = match_pattern(node, pattern_info)

        if matched_pattern:
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
                node, query_ops, operator_models, operator_ffs, prediction_cache
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
    aggregated = aggregate_pattern_with_cache(pattern_rows, pattern_length, query_ops, prediction_cache)

    X_exec = pd.DataFrame([[aggregated.get(f, 0) for f in model['features_exec']]], columns=model['features_exec'])
    X_start = pd.DataFrame([[aggregated.get(f, 0) for f in model['features_start']]], columns=model['features_start'])

    pred_exec = model['execution_time'].predict(X_exec)[0]
    pred_start = model['start_time'].predict(X_start)[0]

    return pred_start, pred_exec


# Predict using operator model
def predict_operator(node, query_ops: pd.DataFrame, operator_models: dict, operator_ffs: dict, prediction_cache: dict) -> tuple:
    op_name = node.node_type.replace(' ', '_')

    if op_name not in operator_models['execution_time'] or op_name not in operator_models['start_time']:
        return 0.0, 0.0

    row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
    features = build_operator_features(row, node, query_ops, prediction_cache)

    model_exec = operator_models['execution_time'][op_name]
    model_start = operator_models['start_time'][op_name]

    exec_feature_names = list(model_exec.feature_names_in_)
    start_feature_names = list(model_start.feature_names_in_)

    X_exec = pd.DataFrame([[features.get(f, 0) for f in exec_feature_names]], columns=exec_feature_names)
    X_start = pd.DataFrame([[features.get(f, 0) for f in start_feature_names]], columns=start_feature_names)

    pred_exec = model_exec.predict(X_exec)[0]
    pred_start = model_start.predict(X_start)[0]

    return pred_start, pred_exec


# Build operator features with child predictions
def build_operator_features(row, node, query_ops: pd.DataFrame, prediction_cache: dict) -> dict:
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


# Aggregate pattern rows for training
def aggregate_pattern(pattern_rows: pd.DataFrame, pattern_length: int) -> dict:
    if pattern_rows.empty:
        return None

    pattern_rows = pattern_rows.sort_values('depth').reset_index(drop=True)
    root = build_tree_from_dataframe(pattern_rows)

    return aggregate_subtree(root, pattern_rows, pattern_length - 1, is_root=True)


# Aggregate pattern with prediction cache for test time
def aggregate_pattern_with_cache(
    pattern_rows: pd.DataFrame,
    pattern_length: int,
    full_query_ops: pd.DataFrame,
    prediction_cache: dict
) -> dict:
    if pattern_rows.empty:
        return {}

    pattern_rows = pattern_rows.sort_values('depth').reset_index(drop=True)
    root = build_tree_from_dataframe(pattern_rows)
    pattern_node_ids = set(pattern_rows['node_id'].tolist())

    return aggregate_subtree_with_cache(
        root, pattern_rows, full_query_ops, prediction_cache, pattern_node_ids, pattern_length - 1, is_root=True
    )


# Aggregate subtree recursively for training
def aggregate_subtree(node, pattern_rows: pd.DataFrame, remaining_depth: int, is_root: bool = False) -> dict:
    aggregated = {}
    row = pattern_rows[pattern_rows['node_id'] == node.node_id].iloc[0]
    node_type_clean = node.node_type.replace(' ', '')

    if is_root:
        prefix = node_type_clean + '_'
        aggregated['query_file'] = row['query_file']
        aggregated['actual_startup_time'] = row['actual_startup_time']
        aggregated['actual_total_time'] = row['actual_total_time']
    else:
        prefix = node_type_clean + '_' + node.parent_relationship + '_'

    for col in row.index:
        if col not in ['query_file', 'subplan_name', 'actual_startup_time', 'actual_total_time']:
            aggregated[prefix + col] = row[col]

    aggregated[prefix + 'st1'] = row.get('st1', 0)
    aggregated[prefix + 'rt1'] = row.get('rt1', 0)
    aggregated[prefix + 'st2'] = row.get('st2', 0)
    aggregated[prefix + 'rt2'] = row.get('rt2', 0)

    if remaining_depth > 0:
        children_sorted = sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1, c.node_type))
        for child in children_sorted:
            child_agg = aggregate_subtree(child, pattern_rows, remaining_depth - 1, is_root=False)
            aggregated.update(child_agg)

    return aggregated


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


# Calculate MRE on root operators
def calculate_mre(predictions: list) -> float:
    root_preds = [p for p in predictions if p['depth'] == 0]
    if not root_preds:
        return float('inf')

    mre_values = []
    for p in root_preds:
        if p['actual_total_time'] > 0:
            mre = abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time']
            mre_values.append(mre)

    return np.mean(mre_values) if mre_values else float('inf')


# Create prediction result
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


# Save pattern model
def save_pattern_model(model_dir: str, pattern_hash: str, model: dict) -> None:
    pattern_dir = Path(model_dir) / pattern_hash
    pattern_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(model['execution_time'], pattern_dir / 'model_execution_time.pkl')
    joblib.dump(model['start_time'], pattern_dir / 'model_start_time.pkl')


# Export per-pattern results
def export_pattern_results(
    output_dir: str,
    pattern_hash: str,
    pattern_string: str,
    predictions: list,
    mre: float,
    status: str
) -> None:
    pattern_dir = Path(output_dir) / pattern_hash
    pattern_dir.mkdir(parents=True, exist_ok=True)

    df_preds = pd.DataFrame(predictions)
    df_preds.to_csv(pattern_dir / 'predictions.csv', sep=';', index=False)

    mre_df = pd.DataFrame({
        'pattern_hash': [pattern_hash],
        'pattern_string': [pattern_string],
        'mre': [mre],
        'mre_pct': [mre * 100],
        'status': [status]
    })
    mre_df.to_csv(pattern_dir / 'mre.csv', sep=';', index=False)

    with open(pattern_dir / 'status.txt', 'w') as f:
        f.write(status)


# Export selection summary
def export_selection_summary(output_dir: str, selection_log: list) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    log_df = pd.DataFrame(selection_log)
    log_df.to_csv(output_path / 'selection_log.csv', sep=';', index=False)

    selected_df = log_df[log_df['status'] == 'SELECTED']
    selected_df.to_csv(output_path / 'selected_patterns.csv', sep=';', index=False)

    summary = {
        'total_patterns': len(selection_log),
        'selected': len([s for s in selection_log if s['status'] == 'SELECTED']),
        'rejected': len([s for s in selection_log if s['status'] == 'REJECTED']),
        'skipped_no_ffs': len([s for s in selection_log if s['status'] == 'SKIPPED_NO_FFS']),
        'skipped_train_failed': len([s for s in selection_log if s['status'] == 'SKIPPED_TRAIN_FAILED']),
        'final_mre': selection_log[-1]['baseline_mre'] if selection_log else None
    }
    summary_df = pd.DataFrame([summary])
    summary_df.to_csv(output_path / 'selection_summary.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--strategy', required=True, choices=STRATEGIES, help='Selection strategy')
    parser.add_argument('sorted_patterns_file', help='Path to sorted patterns CSV (06_patterns_by_*.csv or 10_patterns_by_error.csv)')
    parser.add_argument('pattern_ffs_file', help='Path to pattern_ffs_overview.csv')
    parser.add_argument('training_file', help='Path to Training_Training.csv')
    parser.add_argument('test_file', help='Path to Training_Test.csv')
    parser.add_argument('operator_model_dir', help='Path to Model/Operator/')
    parser.add_argument('operator_ffs_dir', help='Path to SVM/Operator/')
    parser.add_argument('--pattern-output-dir', required=True, help='Per-pattern results output directory')
    parser.add_argument('--model-dir', required=True, help='Model output directory')
    parser.add_argument('--pretrained-dir', default=None, help='Path to pretrained models')
    parser.add_argument('--pattern-occurrences-file', default=None, help='Path to 05_test_pattern_occurrences_*.csv (required for error strategy)')
    args = parser.parse_args()

    if args.strategy == 'error' and not args.pattern_occurrences_file:
        parser.error('--pattern-occurrences-file is required for error strategy')

    run_pattern_selection(
        args.strategy,
        args.sorted_patterns_file,
        args.pattern_ffs_file,
        args.training_file,
        args.test_file,
        args.operator_model_dir,
        args.operator_ffs_dir,
        args.pattern_output_dir,
        args.model_dir,
        args.pretrained_dir,
        args.pattern_occurrences_file
    )
