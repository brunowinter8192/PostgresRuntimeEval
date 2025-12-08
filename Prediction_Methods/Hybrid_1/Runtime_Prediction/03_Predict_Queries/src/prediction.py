# INFRASTRUCTURE

import pandas as pd

# From tree.py: Tree building and hash computation
from src.tree import QueryNode, build_tree_from_dataframe, extract_all_nodes, compute_pattern_hash

# From io.py: Create prediction result
from src.io import create_prediction_result


# FUNCTIONS

# Predict all queries in test set
def predict_all_queries(
    df_test: pd.DataFrame,
    pattern_features: dict,
    operator_features: dict,
    pattern_models: dict,
    operator_models: dict,
    pattern_model_dir: str,
    operator_model_dir: str,
    track_steps: bool = False
) -> tuple:
    all_predictions = []
    all_steps = {}

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].copy()
        query_ops = query_ops[query_ops['subplan_name'].isna() | (query_ops['subplan_name'] == '')]
        query_ops = query_ops.sort_values('node_id').reset_index(drop=True)

        predictions, steps = predict_single_query(
            query_ops, pattern_features, operator_features,
            pattern_models, operator_models,
            pattern_model_dir, operator_model_dir, track_steps
        )

        all_predictions.extend(predictions)
        if track_steps:
            all_steps[query_file] = steps

    return all_predictions, all_steps


# Predict single query using bottom-up approach
def predict_single_query(
    query_ops: pd.DataFrame,
    pattern_features: dict,
    operator_features: dict,
    pattern_models: dict,
    operator_models: dict,
    pattern_model_dir: str,
    operator_model_dir: str,
    track_steps: bool = False
) -> tuple:
    root = build_tree_from_dataframe(query_ops)
    all_nodes = extract_all_nodes(root)
    nodes_by_id = {node.node_id: node for node in all_nodes}
    nodes_by_depth = sorted(all_nodes, key=lambda n: n.depth, reverse=True)

    prediction_cache = {}
    consumed_nodes = set()
    prediction_results = []
    steps = []
    step_num = 1

    for node in nodes_by_depth:
        if node.node_id in consumed_nodes:
            continue

        parent_node = find_parent_node(node, nodes_by_id, query_ops)

        if parent_node is None:
            result, step = predict_with_operator(
                node, query_ops, operator_features, operator_models,
                prediction_cache, operator_model_dir, step_num, track_steps
            )
            prediction_results.append(result)
            prediction_cache[node.node_id] = {
                'predicted_startup_time': result['predicted_startup_time'],
                'predicted_total_time': result['predicted_total_time']
            }
            consumed_nodes.add(node.node_id)
            if track_steps and step:
                step['reason'] = 'Root node (no parent)'
                steps.append(step)
                step_num += 1
            continue

        if parent_node.node_id in consumed_nodes:
            continue

        siblings = parent_node.children
        if any(sib.node_id in consumed_nodes for sib in siblings):
            continue

        pattern_hash = compute_pattern_hash(parent_node)

        if pattern_hash and pattern_hash in pattern_features:
            if check_grandchild_predictions_available(parent_node, prediction_cache):
                result, step = predict_with_pattern(
                    parent_node, query_ops, pattern_features, pattern_models,
                    prediction_cache, pattern_model_dir, pattern_hash, step_num, track_steps
                )
                prediction_results.append(result)
                prediction_cache[parent_node.node_id] = {
                    'predicted_startup_time': result['predicted_startup_time'],
                    'predicted_total_time': result['predicted_total_time']
                }
                consumed_nodes.add(parent_node.node_id)
                for child in parent_node.children:
                    consumed_nodes.add(child.node_id)
                if track_steps and step:
                    steps.append(step)
                    step_num += 1
                continue

    for node in nodes_by_depth:
        if node.node_id in consumed_nodes:
            continue

        result, step = predict_with_operator(
            node, query_ops, operator_features, operator_models,
            prediction_cache, operator_model_dir, step_num, track_steps
        )
        prediction_results.append(result)
        prediction_cache[node.node_id] = {
            'predicted_startup_time': result['predicted_startup_time'],
            'predicted_total_time': result['predicted_total_time']
        }
        consumed_nodes.add(node.node_id)
        if track_steps and step:
            step['reason'] = 'No pattern match available'
            steps.append(step)
            step_num += 1

    return prediction_results, steps


# Find parent node for given node
def find_parent_node(node: QueryNode, nodes_by_id: dict, query_ops: pd.DataFrame) -> QueryNode:
    if node.depth == query_ops['depth'].min():
        return None

    node_idx = query_ops[query_ops['node_id'] == node.node_id].index[0]

    for idx in range(node_idx - 1, -1, -1):
        row = query_ops.iloc[idx]
        if row['depth'] == node.depth - 1:
            return nodes_by_id.get(row['node_id'])

    return None


# Check if grandchild predictions are available for non-leaf pattern
def check_grandchild_predictions_available(parent_node: QueryNode, prediction_cache: dict) -> bool:
    for child in parent_node.children:
        for grandchild in child.children:
            if grandchild.node_id not in prediction_cache:
                return False
    return True


# Predict using pattern model
def predict_with_pattern(
    parent_node: QueryNode,
    query_ops: pd.DataFrame,
    pattern_features: dict,
    pattern_models: dict,
    prediction_cache: dict,
    model_dir: str,
    pattern_hash: str,
    step_num: int,
    track_steps: bool
) -> tuple:
    aggregated = aggregate_pattern_features(parent_node, query_ops, prediction_cache)

    pattern_data = pattern_features[pattern_hash]
    exec_features = pattern_data['execution_time']['final_features']
    start_features = pattern_data['start_time']['final_features']

    X_exec = pd.DataFrame([{f: aggregated.get(f, 0) for f in exec_features}])
    X_start = pd.DataFrame([{f: aggregated.get(f, 0) for f in start_features}])

    pred_exec = pattern_models['execution_time'][pattern_hash].predict(X_exec)[0]
    pred_start = pattern_models['start_time'][pattern_hash].predict(X_start)[0]

    row = query_ops[query_ops['node_id'] == parent_node.node_id].iloc[0]
    result = create_prediction_result(row, pred_start, pred_exec, 'pattern')

    step = None
    if track_steps:
        folder_name = pattern_data['folder_name']
        consumed_children = [(c.node_id, c.node_type) for c in parent_node.children]
        step = {
            'step': step_num,
            'depth': parent_node.depth,
            'prediction_type': 'pattern',
            'pattern_hash': pattern_hash,
            'pattern_folder': folder_name,
            'parent_node_id': parent_node.node_id,
            'parent_node_type': parent_node.node_type,
            'consumed_children': consumed_children,
            'model_path_exec': f'{model_dir}/execution_time/{folder_name}/model.pkl',
            'model_path_start': f'{model_dir}/start_time/{folder_name}/model.pkl',
            'features_exec': exec_features,
            'features_start': start_features,
            'input_values_exec': dict(zip(exec_features, X_exec.iloc[0].tolist())),
            'input_values_start': dict(zip(start_features, X_start.iloc[0].tolist())),
            'predicted_startup_time': pred_start,
            'predicted_total_time': pred_exec,
            'actual_startup_time': row['actual_startup_time'],
            'actual_total_time': row['actual_total_time']
        }

    return result, step


# Predict using operator model
def predict_with_operator(
    node: QueryNode,
    query_ops: pd.DataFrame,
    operator_features: dict,
    operator_models: dict,
    prediction_cache: dict,
    model_dir: str,
    step_num: int,
    track_steps: bool
) -> tuple:
    operator_name = node.node_type.replace(' ', '_')
    row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]

    if operator_name not in operator_features:
        result = create_prediction_result(row, 0.0, 0.0, 'operator')
        return result, None

    aggregated = build_operator_features(node, row, prediction_cache)

    op_data = operator_features[operator_name]
    exec_features = op_data['execution_time']['final_features']
    start_features = op_data['start_time']['final_features']

    X_exec = pd.DataFrame([{f: aggregated.get(f, 0) for f in exec_features}])
    X_start = pd.DataFrame([{f: aggregated.get(f, 0) for f in start_features}])

    pred_exec = operator_models['execution_time'][operator_name].predict(X_exec)[0]
    pred_start = operator_models['start_time'][operator_name].predict(X_start)[0]

    result = create_prediction_result(row, pred_start, pred_exec, 'operator')

    step = None
    if track_steps:
        step = {
            'step': step_num,
            'depth': node.depth,
            'prediction_type': 'operator',
            'operator_name': operator_name,
            'node_id': node.node_id,
            'node_type': node.node_type,
            'consumed_children': [],
            'model_path_exec': f'{model_dir}/execution_time/operators/{operator_name}/model.pkl',
            'model_path_start': f'{model_dir}/start_time/operators/{operator_name}/model.pkl',
            'features_exec': exec_features,
            'features_start': start_features,
            'input_values_exec': dict(zip(exec_features, X_exec.iloc[0].tolist())),
            'input_values_start': dict(zip(start_features, X_start.iloc[0].tolist())),
            'predicted_startup_time': pred_start,
            'predicted_total_time': pred_exec,
            'actual_startup_time': row['actual_startup_time'],
            'actual_total_time': row['actual_total_time']
        }

    return result, step


# Aggregate pattern features from parent and children
def aggregate_pattern_features(parent_node: QueryNode, query_ops: pd.DataFrame, prediction_cache: dict) -> dict:
    aggregated = {}
    parent_row = query_ops[query_ops['node_id'] == parent_node.node_id].iloc[0]

    parent_prefix = parent_node.node_type.replace(' ', '') + '_'
    aggregated['query_file'] = parent_row['query_file']

    for col in parent_row.index:
        if col != 'query_file':
            aggregated[parent_prefix + col] = parent_row[col]

    children_sorted = sorted(parent_node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1))

    for child in children_sorted:
        child_row = query_ops[query_ops['node_id'] == child.node_id].iloc[0]
        child_prefix = child.node_type.replace(' ', '') + '_' + child.parent_relationship + '_'

        for col in child_row.index:
            if col not in ['query_file', 'st1', 'rt1', 'st2', 'rt2']:
                aggregated[child_prefix + col] = child_row[col]

        aggregated[child_prefix + 'st1'] = 0.0
        aggregated[child_prefix + 'rt1'] = 0.0
        aggregated[child_prefix + 'st2'] = 0.0
        aggregated[child_prefix + 'rt2'] = 0.0

        for grandchild in child.children:
            if grandchild.node_id in prediction_cache:
                pred = prediction_cache[grandchild.node_id]
                if grandchild.parent_relationship == 'Outer':
                    aggregated[child_prefix + 'st1'] = pred['predicted_startup_time']
                    aggregated[child_prefix + 'rt1'] = pred['predicted_total_time']
                elif grandchild.parent_relationship == 'Inner':
                    aggregated[child_prefix + 'st2'] = pred['predicted_startup_time']
                    aggregated[child_prefix + 'rt2'] = pred['predicted_total_time']

    return aggregated


# Build operator features with child predictions from cache
def build_operator_features(node: QueryNode, row, prediction_cache: dict) -> dict:
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
                features['st1'] = pred['predicted_startup_time']
                features['rt1'] = pred['predicted_total_time']
            elif child.parent_relationship == 'Inner':
                features['st2'] = pred['predicted_startup_time']
                features['rt2'] = pred['predicted_total_time']

    return features
