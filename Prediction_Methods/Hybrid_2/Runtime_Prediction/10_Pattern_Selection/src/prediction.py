# INFRASTRUCTURE

import pandas as pd
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

SVM_PARAMS = {'kernel': 'rbf', 'nu': 0.65, 'C': 1.5, 'gamma': 'scale', 'cache_size': 500}

# From tree.py: Tree building and pattern functions
from src.tree import (
    QueryNode,
    build_tree_from_dataframe,
    extract_all_nodes,
    get_children_from_full_query,
    has_children_at_length,
    compute_pattern_hash,
    extract_pattern_node_ids,
    match_pattern
)

# From io.py: Load pretrained model and create prediction result
from src.io import load_pretrained_model, create_prediction_result


# FUNCTIONS

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
    pattern_info: dict,
    pattern_order: list
) -> list:
    all_predictions = []

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)

        predictions = predict_single_query(
            query_ops, operator_models, operator_ffs, pattern_models, pattern_ffs, pattern_info, pattern_order
        )

        all_predictions.extend(predictions)

    return all_predictions


# Predict single query bottom-up (larger patterns have priority, then selection order)
def predict_single_query(
    query_ops: pd.DataFrame,
    operator_models: dict,
    operator_ffs: dict,
    pattern_models: dict,
    pattern_ffs: dict,
    pattern_info: dict,
    pattern_order: list
) -> list:
    root = build_tree_from_dataframe(query_ops)
    all_nodes = extract_all_nodes(root)

    pattern_matches = []
    for node in all_nodes:
        matched = match_pattern(node, pattern_info)
        if matched:
            info = pattern_info[matched]
            pattern_matches.append((node, matched, info['length'], info['operator_count']))

    def get_pattern_order_index(pattern_hash):
        try:
            return pattern_order.index(pattern_hash)
        except ValueError:
            return len(pattern_order)

    pattern_matches.sort(key=lambda x: (-x[2], get_pattern_order_index(x[1])))

    prediction_cache = {}
    consumed_nodes = set()
    predictions = []

    for node, pattern_hash, pattern_length, _ in pattern_matches:
        pattern_node_ids = extract_pattern_node_ids(node, pattern_length)

        if any(nid in consumed_nodes for nid in pattern_node_ids):
            continue

        consumed_nodes.update(pattern_node_ids)

        pred_start, pred_exec = predict_pattern(
            node, query_ops, pattern_models[pattern_hash], prediction_cache, pattern_length
        )

        for nid in pattern_node_ids:
            prediction_cache[nid] = {'start': pred_start, 'exec': pred_exec}

        row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
        predictions.append(create_prediction_result(row, pred_start, pred_exec, 'pattern'))

    nodes_by_depth = sorted(all_nodes, key=lambda n: n.depth, reverse=True)

    for node in nodes_by_depth:
        if node.node_id in consumed_nodes:
            continue

        pred_start, pred_exec = predict_operator(
            node, query_ops, operator_models, operator_ffs, prediction_cache
        )

        prediction_cache[node.node_id] = {'start': pred_start, 'exec': pred_exec}

        row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
        predictions.append(create_prediction_result(row, pred_start, pred_exec, 'operator'))

    return predictions


# Predict using pattern model
def predict_pattern(node: QueryNode, query_ops: pd.DataFrame, model: dict, prediction_cache: dict, pattern_length: int) -> tuple:
    pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
    pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]
    aggregated = aggregate_pattern_with_cache(pattern_rows, pattern_length, query_ops, prediction_cache)

    X_exec = pd.DataFrame([[aggregated.get(f, 0) for f in model['features_exec']]], columns=model['features_exec'])
    X_start = pd.DataFrame([[aggregated.get(f, 0) for f in model['features_start']]], columns=model['features_start'])

    pred_exec = model['execution_time'].predict(X_exec)[0]
    pred_start = model['start_time'].predict(X_start)[0]

    return pred_start, pred_exec


# Predict using operator model
def predict_operator(node: QueryNode, query_ops: pd.DataFrame, operator_models: dict, operator_ffs: dict, prediction_cache: dict) -> tuple:
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
def build_operator_features(row, node: QueryNode, query_ops: pd.DataFrame, prediction_cache: dict) -> dict:
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


# Aggregate subtree recursively for training
def aggregate_subtree(node: QueryNode, pattern_rows: pd.DataFrame, remaining_depth: int, is_root: bool = False) -> dict:
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


# Aggregate subtree with prediction cache
def aggregate_subtree_with_cache(
    node: QueryNode,
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
