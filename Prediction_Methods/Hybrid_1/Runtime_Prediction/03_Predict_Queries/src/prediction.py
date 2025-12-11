# INFRASTRUCTURE

import sys
import pandas as pd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

# From mapping_config.py: Passthrough operators
from mapping_config import PASSTHROUGH_OPERATORS

# From tree.py: Tree building and pattern functions
from src.tree import (
    QueryNode,
    build_tree_from_dataframe,
    extract_all_nodes,
    get_children_from_full_query,
    extract_pattern_node_ids,
    build_pattern_assignments
)

# From io.py: Create prediction result
from src.io import create_prediction_result


# FUNCTIONS

# Predict all queries in test set
def predict_all_queries(
    df_test: pd.DataFrame,
    operator_models: dict,
    operator_features: dict,
    pattern_models: dict,
    pattern_features: dict,
    pattern_info: dict,
    pattern_order: list,
    passthrough: bool = False
) -> list:
    all_predictions = []

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)

        predictions, _, _, _ = predict_single_query(
            query_ops, operator_models, operator_features,
            pattern_models, pattern_features, pattern_info, pattern_order,
            passthrough, collect_steps=False
        )

        all_predictions.extend(predictions)

    return all_predictions


# Predict single query using two-phase bottom-up approach
def predict_single_query(
    query_ops: pd.DataFrame,
    operator_models: dict,
    operator_features: dict,
    pattern_models: dict,
    pattern_features: dict,
    pattern_info: dict,
    pattern_order: list,
    passthrough: bool = False,
    collect_steps: bool = False
) -> tuple:
    root = build_tree_from_dataframe(query_ops)
    all_nodes = extract_all_nodes(root)
    nodes_by_depth = sorted(all_nodes, key=lambda n: n.depth, reverse=True)

    consumed_nodes, pattern_assignments = build_pattern_assignments(
        all_nodes, pattern_info, pattern_order
    )

    prediction_cache = {}
    predictions = []
    steps = []
    step_num = 0

    for node in nodes_by_depth:
        if node.node_id in consumed_nodes and node.node_id not in pattern_assignments:
            continue

        row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
        step_num += 1

        if node.node_id in pattern_assignments:
            pattern_hash = pattern_assignments[node.node_id]
            info = pattern_info[pattern_hash]
            pattern_node_ids = extract_pattern_node_ids(node, info['length'])

            result = predict_pattern(
                node, query_ops, pattern_models, pattern_features,
                prediction_cache, info['length'], pattern_hash
            )

            for nid in pattern_node_ids:
                prediction_cache[nid] = result

            predictions.append(create_prediction_result(row, result['start'], result['exec'], 'pattern', pattern_hash))

            if collect_steps:
                consumed_children = [(c.node_id, c.node_type) for c in node.children]
                steps.append({
                    'step': step_num,
                    'depth': node.depth,
                    'prediction_type': 'pattern',
                    'pattern_hash': pattern_hash,
                    'pattern_string': info.get('pattern_string', ''),
                    'parent_node_id': node.node_id,
                    'parent_node_type': node.node_type,
                    'consumed_children': consumed_children,
                    'predicted_startup_time': result['start'],
                    'predicted_total_time': result['exec']
                })
        else:
            if passthrough and is_passthrough_node(node):
                result = predict_passthrough(node, prediction_cache)
                prediction_cache[node.node_id] = result
                predictions.append(create_prediction_result(row, result['start'], result['exec'], 'passthrough'))

                if collect_steps:
                    steps.append({
                        'step': step_num,
                        'depth': node.depth,
                        'prediction_type': 'passthrough',
                        'node_id': node.node_id,
                        'node_type': node.node_type,
                        'reason': 'Passthrough operator - copying child prediction',
                        'predicted_startup_time': result['start'],
                        'predicted_total_time': result['exec']
                    })
            else:
                result = predict_operator(
                    node, query_ops, operator_models, operator_features, prediction_cache
                )
                prediction_cache[node.node_id] = result
                predictions.append(create_prediction_result(row, result['start'], result['exec'], 'operator'))

                if collect_steps:
                    steps.append({
                        'step': step_num,
                        'depth': node.depth,
                        'prediction_type': 'operator',
                        'node_id': node.node_id,
                        'node_type': node.node_type,
                        'reason': 'No pattern match',
                        'predicted_startup_time': result['start'],
                        'predicted_total_time': result['exec']
                    })

    return predictions, steps, consumed_nodes, pattern_assignments


# Check if node is a passthrough operator
def is_passthrough_node(node: QueryNode) -> bool:
    return node.node_type in PASSTHROUGH_OPERATORS


# Predict using passthrough (copy child prediction)
def predict_passthrough(node: QueryNode, prediction_cache: dict) -> dict:
    for child in node.children:
        if child.node_id in prediction_cache:
            pred = prediction_cache[child.node_id]
            return {'start': pred['start'], 'exec': pred['exec']}

    return {'start': 0.0, 'exec': 0.0}


# Predict using pattern model
def predict_pattern(
    node: QueryNode,
    query_ops: pd.DataFrame,
    pattern_models: dict,
    pattern_features: dict,
    prediction_cache: dict,
    pattern_length: int,
    pattern_hash: str
) -> dict:
    pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
    pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]

    aggregated = aggregate_pattern_with_cache(
        pattern_rows, pattern_length, query_ops, prediction_cache, set(pattern_node_ids)
    )

    features_exec = pattern_features.get(pattern_hash, {}).get('execution_time', [])
    features_start = pattern_features.get(pattern_hash, {}).get('start_time', [])

    if not features_exec or not features_start:
        return {'start': 0.0, 'exec': 0.0}

    if pattern_hash not in pattern_models['execution_time'] or pattern_hash not in pattern_models['start_time']:
        return {'start': 0.0, 'exec': 0.0}

    X_exec = pd.DataFrame([[aggregated.get(f, 0) for f in features_exec]], columns=features_exec)
    X_start = pd.DataFrame([[aggregated.get(f, 0) for f in features_start]], columns=features_start)

    pred_exec = pattern_models['execution_time'][pattern_hash].predict(X_exec)[0]
    pred_start = pattern_models['start_time'][pattern_hash].predict(X_start)[0]

    return {'start': pred_start, 'exec': pred_exec}


# Predict using operator model
def predict_operator(
    node: QueryNode,
    query_ops: pd.DataFrame,
    operator_models: dict,
    operator_features: dict,
    prediction_cache: dict
) -> dict:
    op_name = node.node_type.replace(' ', '_')
    row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]

    if op_name not in operator_models['execution_time'] or op_name not in operator_models['start_time']:
        return {'start': 0.0, 'exec': 0.0}

    features = build_operator_features(row, node, prediction_cache)

    exec_feature_names = operator_features['execution_time'].get(op_name, [])
    start_feature_names = operator_features['start_time'].get(op_name, [])

    if not exec_feature_names or not start_feature_names:
        return {'start': 0.0, 'exec': 0.0}

    X_exec = pd.DataFrame([[features.get(f, 0) for f in exec_feature_names]], columns=exec_feature_names)
    X_start = pd.DataFrame([[features.get(f, 0) for f in start_feature_names]], columns=start_feature_names)

    pred_exec = operator_models['execution_time'][op_name].predict(X_exec)[0]
    pred_start = operator_models['start_time'][op_name].predict(X_start)[0]

    return {'start': pred_start, 'exec': pred_exec}


# Build operator features with child predictions from cache
def build_operator_features(row, node: QueryNode, prediction_cache: dict) -> dict:
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


# Aggregate pattern features with prediction cache
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


# Aggregate subtree with prediction cache recursively
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
