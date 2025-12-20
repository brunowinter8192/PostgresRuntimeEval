# INFRASTRUCTURE

import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

# From mapping_config.py: Convert CSV operator name to folder name
from mapping_config import csv_name_to_folder_name

# From tree.py: Tree building and pattern functions
from src.tree import (
    QueryNode,
    build_tree_from_dataframe,
    extract_all_nodes,
    get_children_from_full_query,
    extract_pattern_node_ids,
    build_pattern_assignments,
    compute_plan_hash
)

# From io.py: Create prediction result
from src.io import create_prediction_result

# From report.py: MD report export
from src.report import export_md_report


# FUNCTIONS

# Predict all queries in test set
def predict_all_queries(
    df_test: pd.DataFrame,
    operator_models: dict,
    operator_features: dict,
    pattern_models: dict,
    pattern_info: dict,
    pattern_order: list,
    output_dir: str = '',
    operator_model_dir: str = '',
    pattern_model_dir: str = ''
) -> list:
    all_predictions = []
    reported_plans = set()

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)

        plan_hash = compute_plan_hash(query_ops)
        should_report = output_dir and plan_hash not in reported_plans

        predictions, steps, consumed_nodes, pattern_assignments = predict_single_query(
            query_ops, operator_models, operator_features,
            pattern_models, pattern_info, pattern_order,
            operator_model_dir, pattern_model_dir
        )

        all_predictions.extend(predictions)

        if should_report:
            reported_plans.add(plan_hash)
            export_md_report(
                query_file, query_ops, predictions, steps,
                consumed_nodes, pattern_assignments, pattern_info, output_dir, plan_hash
            )

    return all_predictions


# Predict single query using two-phase bottom-up approach
def predict_single_query(
    query_ops: pd.DataFrame,
    operator_models: dict,
    operator_features: dict,
    pattern_models: dict,
    pattern_info: dict,
    pattern_order: list,
    operator_model_dir: str = '',
    pattern_model_dir: str = ''
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
    step_counter = 1

    for node in nodes_by_depth:
        if node.node_id in consumed_nodes and node.node_id not in pattern_assignments:
            continue

        if node.node_id in pattern_assignments:
            pattern_hash = pattern_assignments[node.node_id]
            info = pattern_info[pattern_hash]
            pattern_node_ids = extract_pattern_node_ids(node, info['length'])

            result = predict_pattern(
                node, query_ops, pattern_models[pattern_hash], prediction_cache, info['length'],
                pattern_hash, pattern_model_dir
            )

            for nid in pattern_node_ids:
                prediction_cache[nid] = result

            row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
            predictions.append(create_prediction_result(row, result['start'], result['exec'], 'pattern', pattern_hash))

            consumed_children = []
            for nid in pattern_node_ids:
                if nid != node.node_id:
                    child_row = query_ops[query_ops['node_id'] == nid].iloc[0]
                    consumed_children.append((nid, child_row['node_type']))

            steps.append({
                'step': step_counter,
                'depth': node.depth,
                'prediction_type': 'pattern',
                'node_id': node.node_id,
                'node_type': node.node_type,
                'pattern_hash': pattern_hash,
                'pattern_string': info.get('pattern_string', 'N/A'),
                'consumed_children': consumed_children,
                'predicted_startup_time': result['start'],
                'predicted_total_time': result['exec']
            })
        else:
            result = predict_operator(
                node, query_ops, operator_models, operator_features, prediction_cache, operator_model_dir
            )

            prediction_cache[node.node_id] = result

            row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
            predictions.append(create_prediction_result(row, result['start'], result['exec'], 'operator'))

            steps.append({
                'step': step_counter,
                'depth': node.depth,
                'prediction_type': 'operator',
                'node_id': node.node_id,
                'node_type': node.node_type,
                'reason': 'No pattern match',
                'predicted_startup_time': result['start'],
                'predicted_total_time': result['exec']
            })

        step_counter += 1

    return predictions, steps, consumed_nodes, pattern_assignments


# Predict using pattern model
def predict_pattern(node: QueryNode, query_ops: pd.DataFrame, model: dict, prediction_cache: dict, pattern_length: int, pattern_hash: str, model_dir: str) -> dict:
    pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
    pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]
    aggregated = aggregate_pattern_with_cache(pattern_rows, pattern_length, query_ops, prediction_cache, set(pattern_node_ids))

    X_exec = pd.DataFrame([[aggregated.get(f, 0) for f in model['features_exec']]], columns=model['features_exec'])
    X_start = pd.DataFrame([[aggregated.get(f, 0) for f in model['features_start']]], columns=model['features_start'])

    pred_exec = model['execution_time'].predict(X_exec)[0]
    pred_start = model['start_time'].predict(X_start)[0]

    return {
        'start': pred_start,
        'exec': pred_exec
    }


# Predict using operator model
def predict_operator(node: QueryNode, query_ops: pd.DataFrame, operator_models: dict, operator_features: dict, prediction_cache: dict, operator_model_dir: str) -> dict:
    op_name = csv_name_to_folder_name(node.node_type)

    if op_name not in operator_models['execution_time'] or op_name not in operator_models['start_time']:
        return {'start': 0.0, 'exec': 0.0}

    row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
    features = build_operator_features(row, node, prediction_cache)

    model_exec = operator_models['execution_time'][op_name]
    model_start = operator_models['start_time'][op_name]

    exec_feature_names = operator_features['execution_time'].get(op_name, [])
    start_feature_names = operator_features['start_time'].get(op_name, [])

    if not exec_feature_names or not start_feature_names:
        return {'start': 0.0, 'exec': 0.0}

    X_exec = pd.DataFrame([[features.get(f, 0) for f in exec_feature_names]], columns=exec_feature_names)
    X_start = pd.DataFrame([[features.get(f, 0) for f in start_feature_names]], columns=start_feature_names)

    pred_exec = model_exec.predict(X_exec)[0]
    pred_start = model_start.predict(X_start)[0]

    return {
        'start': pred_start,
        'exec': pred_exec
    }


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
