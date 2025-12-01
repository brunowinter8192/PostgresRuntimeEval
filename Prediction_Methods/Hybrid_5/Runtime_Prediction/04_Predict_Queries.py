#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import sys
import pandas as pd
import hashlib
from pathlib import Path
import joblib

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Pattern definitions
from mapping_config import PATTERNS


# Data structure for query tree nodes
class QueryNode:
    def __init__(self, node_type, parent_relationship, depth, node_id, df_index):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.df_index = df_index
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# ORCHESTRATOR
def run_prediction_workflow(test_file, pattern_csv, pattern_plan_leafs_csv, pattern_ffs_csv, operator_ffs_csv, pattern_model_dir, operator_model_dir, output_dir):
    df_test = load_test_data(test_file)
    pattern_info = load_pattern_info(pattern_csv)
    plan_leaf_mapping = load_pattern_plan_leaf_mapping(pattern_plan_leafs_csv)
    pattern_features = load_pattern_features(pattern_ffs_csv)
    operator_features = load_operator_features(operator_ffs_csv)
    pattern_models = load_pattern_models(pattern_model_dir)
    operator_models = load_operator_models(operator_model_dir)

    all_predictions = []
    queries = df_test['query_file'].unique()

    for query in queries:
        df_query = df_test[df_test['query_file'] == query].copy()
        df_query = df_query[df_query['subplan_name'].isna() | (df_query['subplan_name'] == '')]
        df_query = df_query.sort_values('node_id').reset_index(drop=True)

        predictions = predict_single_query(
            df_query, pattern_info, plan_leaf_mapping, pattern_features, operator_features, pattern_models, operator_models
        )
        all_predictions.extend(predictions)

    export_predictions(all_predictions, output_dir)


# FUNCTIONS

# Load test data from CSV
def load_test_data(test_file):
    return pd.read_csv(test_file, delimiter=';')

# Load pattern information from pattern mining CSV
def load_pattern_info(pattern_csv):
    df = pd.read_csv(pattern_csv, delimiter=';')
    pattern_map = {}
    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']
        if pattern_hash in PATTERNS:
            pattern_map[pattern_hash] = {
                'string': row['pattern_string'],
                'length': row['pattern_length']
            }
    return pattern_map

# Load pattern plan leaf mapping from 04_Identify_Pattern_Plan_Leafs.py output
def load_pattern_plan_leaf_mapping(pattern_plan_leafs_csv):
    df = pd.read_csv(pattern_plan_leafs_csv, delimiter=';')
    mapping = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']
        prefix = row['pattern_leaf_prefix']
        is_plan_leaf = row['is_plan_leaf'] == 'ja'

        if pattern_hash not in mapping:
            mapping[pattern_hash] = {}

        mapping[pattern_hash][prefix] = is_plan_leaf

    return mapping

# Load pattern features from cleaned FFS CSV
def load_pattern_features(pattern_ffs_csv):
    df = pd.read_csv(pattern_ffs_csv, delimiter=';')
    features = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern']
        target = row['target']

        if pattern_hash not in features:
            features[pattern_hash] = {}

        final_features = [f.strip() for f in row['final_features'].split(',')]
        features[pattern_hash][target] = final_features

    return features

# Load operator features from Operator FFS CSV
def load_operator_features(operator_ffs_csv):
    df = pd.read_csv(operator_ffs_csv, delimiter=';')
    features = {}

    for _, row in df.iterrows():
        operator = row['operator']
        target = row['target']

        if operator not in features:
            features[operator] = {}

        final_features = [f.strip() for f in row['final_features'].split(',')]
        features[operator][target] = final_features

    return features

# Load all pattern models from directory
def load_pattern_models(model_dir):
    models = {}
    model_path = Path(model_dir)

    for target in ['execution_time', 'start_time']:
        models[target] = {}
        target_dir = model_path / target

        if not target_dir.exists():
            continue

        for pattern_dir in target_dir.iterdir():
            if pattern_dir.is_dir():
                model_file = pattern_dir / 'model.pkl'
                if model_file.exists():
                    models[target][pattern_dir.name] = joblib.load(model_file)

    return models

# Load all operator models from directory
def load_operator_models(model_dir):
    models = {}
    model_path = Path(model_dir)

    for target in ['execution_time', 'start_time']:
        models[target] = {}
        target_dir = model_path / target

        if not target_dir.exists():
            continue

        for operator_dir in target_dir.iterdir():
            if operator_dir.is_dir():
                model_file = operator_dir / 'model.pkl'
                if model_file.exists():
                    models[target][operator_dir.name] = joblib.load(model_file)

    return models

# Predict single query using optimized plan
def predict_single_query(df_query, pattern_info, plan_leaf_mapping, pattern_features, operator_features, pattern_models, operator_models):
    root = build_tree_from_dataframe(df_query)
    execution_plan = build_optimized_plan_greedy(root, pattern_info, df_query)
    predictions = execute_prediction_plan(
        execution_plan, df_query, plan_leaf_mapping, pattern_features, operator_features, pattern_models, operator_models
    )
    return predictions

# Build tree structure from flat DataFrame
def build_tree_from_dataframe(df_query):
    return build_subtree_from_index(df_query, 0)

# Build subtree from dataframe index
def build_subtree_from_index(df_query, node_idx):
    if node_idx >= len(df_query):
        return None

    node_row = df_query.iloc[node_idx]
    tree_node = QueryNode(
        node_type=node_row['node_type'],
        parent_relationship=node_row['parent_relationship'],
        depth=node_row['depth'],
        node_id=node_row['node_id'],
        df_index=node_idx
    )

    children_indices = get_children_indices(df_query, node_idx)
    for child_idx in children_indices:
        child_node = build_subtree_from_index(df_query, child_idx)
        if child_node:
            tree_node.add_child(child_node)

    return tree_node

# Get children indices for node
def get_children_indices(df_query, parent_idx):
    parent_row = df_query.iloc[parent_idx]
    parent_depth = parent_row['depth']
    children = []

    for idx in range(parent_idx + 1, len(df_query)):
        row = df_query.iloc[idx]
        if row['depth'] == parent_depth + 1:
            children.append(idx)
        elif row['depth'] <= parent_depth:
            break

    return children

# Build optimized execution plan using greedy pattern matching
def build_optimized_plan_greedy(root, pattern_info, df_query):
    plan_steps = []
    consumed_indices = set()

    patterns_by_length = sorted(pattern_info.items(), key=lambda x: x[1]['length'], reverse=True)

    all_nodes = extract_all_nodes_with_depth(root)
    all_nodes_sorted = sorted(all_nodes, key=lambda n: n.depth)

    for node in all_nodes_sorted:
        if node.df_index in consumed_indices:
            continue

        matched_pattern = try_match_largest_pattern(node, patterns_by_length)

        if matched_pattern:
            pattern_hash, pattern_info_item = matched_pattern
            pattern_length = pattern_info_item['length']
            pattern_string = pattern_info_item['string']
            consumed_nodes = collect_subtree_indices(node, pattern_length)
            consumed_indices.update(consumed_nodes)

            consumed_details = get_consumed_node_details(consumed_nodes, df_query)

            step = {
                'type': 'pattern',
                'pattern_hash': pattern_hash,
                'pattern_length': pattern_length,
                'pattern_string': pattern_string,
                'root_node_id': node.node_id,
                'root_df_index': node.df_index,
                'consumed_node_ids': [d['node_id'] for d in consumed_details],
                'consumed_df_indices': list(consumed_nodes)
            }
            plan_steps.append(step)
        else:
            consumed_indices.add(node.df_index)

            step = {
                'type': 'operator',
                'node_id': node.node_id,
                'df_index': node.df_index,
                'operator': node.node_type,
                'depth': node.depth
            }
            plan_steps.append(step)

    return plan_steps

# Extract all nodes from tree with depth ordering
def extract_all_nodes_with_depth(node):
    nodes = [node]
    for child in node.children:
        nodes.extend(extract_all_nodes_with_depth(child))
    return nodes

# Try to match largest available pattern
def try_match_largest_pattern(node, patterns_by_length):
    for pattern_hash, pattern_info in patterns_by_length:
        pattern_length = pattern_info['length']

        if not has_sufficient_depth(node, pattern_length):
            continue

        computed_hash = compute_hash_at_length(node, pattern_length)

        if computed_hash == pattern_hash:
            return (pattern_hash, pattern_info)

    return None

# Check if node has sufficient depth for pattern
def has_sufficient_depth(node, target_length):
    if target_length == 1:
        return True
    if len(node.children) == 0:
        return False
    return any(has_sufficient_depth(child, target_length - 1) for child in node.children)

# Compute structural hash for pattern at specific length
def compute_hash_at_length(node, remaining_length):
    if remaining_length == 1 or len(node.children) == 0:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_hash_at_length(child, remaining_length - 1)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)

    return hashlib.md5(combined_string.encode()).hexdigest()

# Collect all indices in subtree up to target length
def collect_subtree_indices(node, remaining_length):
    indices = {node.df_index}

    if remaining_length > 1:
        for child in node.children:
            indices.update(collect_subtree_indices(child, remaining_length - 1))

    return indices

# Get details of consumed nodes
def get_consumed_node_details(consumed_indices, df_query):
    details = []
    for idx in sorted(consumed_indices):
        row = df_query.iloc[idx]
        details.append({
            'node_id': row['node_id'],
            'node_type': row['node_type'],
            'depth': row['depth'],
            'parent_relationship': row['parent_relationship']
        })
    return details

# Execute prediction plan step by step
def execute_prediction_plan(execution_plan, df_query, plan_leaf_mapping, pattern_features, operator_features, pattern_models, operator_models):
    prediction_results = []
    prediction_cache = {}

    for step in execution_plan:
        if step['type'] == 'pattern':
            pred_start, pred_exec = predict_pattern_step(
                step, df_query, plan_leaf_mapping, pattern_features, pattern_models, prediction_cache
            )

            root_row = df_query.iloc[step['root_df_index']]
            prediction_results.append(create_prediction_result(
                root_row, pred_start, pred_exec, 'pattern'
            ))

            for node_id in step['consumed_node_ids']:
                prediction_cache[node_id] = {
                    'predicted_startup_time': pred_start,
                    'predicted_total_time': pred_exec
                }
        else:
            pred_start, pred_exec = predict_operator_step(
                step, df_query, operator_features, operator_models, prediction_cache
            )

            op_row = df_query.iloc[step['df_index']]
            prediction_results.append(create_prediction_result(
                op_row, pred_start, pred_exec, 'operator'
            ))

            prediction_cache[step['node_id']] = {
                'predicted_startup_time': pred_start,
                'predicted_total_time': pred_exec
            }

    return prediction_results

# Predict pattern step
def predict_pattern_step(step, df_query, plan_leaf_mapping, pattern_features, pattern_models, prediction_cache):
    pattern_hash = step['pattern_hash']

    if pattern_hash not in pattern_features:
        return 0.0, 0.0

    aggregated_row = aggregate_pattern_features(
        step, df_query, plan_leaf_mapping, prediction_cache
    )

    exec_features = pattern_features[pattern_hash]['execution_time']
    start_features = pattern_features[pattern_hash]['start_time']

    X_exec = pd.DataFrame([{feat: aggregated_row.get(feat, 0.0) for feat in exec_features}])
    X_start = pd.DataFrame([{feat: aggregated_row.get(feat, 0.0) for feat in start_features}])

    pred_exec = pattern_models['execution_time'][pattern_hash].predict(X_exec)[0]
    pred_start = pattern_models['start_time'][pattern_hash].predict(X_start)[0]

    return pred_start, pred_exec

# Aggregate pattern features with child predictions
def aggregate_pattern_features(step, df_query, plan_leaf_mapping, prediction_cache):
    aggregated = {}
    pattern_hash = step['pattern_hash']
    consumed_indices = step['consumed_df_indices']

    for idx in consumed_indices:
        row = df_query.iloc[idx]
        node_type_clean = clean_node_type(row['node_type'])
        parent_rel = row['parent_relationship']

        if pd.isna(parent_rel) or parent_rel == '':
            prefix = node_type_clean + '_'
        else:
            prefix = node_type_clean + '_' + parent_rel + '_'

        for col in row.index:
            if col not in ['query_file', 'subplan_name', 'actual_startup_time', 'actual_total_time']:
                aggregated[prefix + col] = row[col]

        children_indices = get_children_indices(df_query, idx)
        aggregated[prefix + 'st1'] = 0.0
        aggregated[prefix + 'rt1'] = 0.0
        aggregated[prefix + 'st2'] = 0.0
        aggregated[prefix + 'rt2'] = 0.0

        leaf_prefix = node_type_clean + '_' + parent_rel if not pd.isna(parent_rel) and parent_rel != '' else None
        is_plan_leaf = False

        if pattern_hash in plan_leaf_mapping and leaf_prefix and leaf_prefix in plan_leaf_mapping[pattern_hash]:
            is_plan_leaf = plan_leaf_mapping[pattern_hash][leaf_prefix]

        if not is_plan_leaf:
            for child_idx in children_indices:
                child_row = df_query.iloc[child_idx]
                child_node_id = child_row['node_id']

                if child_node_id in prediction_cache:
                    child_rel = child_row['parent_relationship']
                    pred = prediction_cache[child_node_id]

                    if child_rel == 'Outer':
                        aggregated[prefix + 'st1'] = pred['predicted_startup_time']
                        aggregated[prefix + 'rt1'] = pred['predicted_total_time']
                    elif child_rel == 'Inner':
                        aggregated[prefix + 'st2'] = pred['predicted_startup_time']
                        aggregated[prefix + 'rt2'] = pred['predicted_total_time']

    return aggregated

# Predict operator step
def predict_operator_step(step, df_query, operator_features, operator_models, prediction_cache):
    operator_name = step['operator'].replace(' ', '_')

    if operator_name not in operator_features:
        return 0.0, 0.0

    aggregated_row = aggregate_operator_features(
        step, df_query, prediction_cache
    )

    exec_features = operator_features[operator_name]['execution_time']
    start_features = operator_features[operator_name]['start_time']

    X_exec = pd.DataFrame([{feat: aggregated_row.get(feat, 0.0) for feat in exec_features}])
    X_start = pd.DataFrame([{feat: aggregated_row.get(feat, 0.0) for feat in start_features}])

    pred_exec = operator_models['execution_time'][operator_name].predict(X_exec)[0]
    pred_start = operator_models['start_time'][operator_name].predict(X_start)[0]

    return pred_start, pred_exec

# Aggregate operator features with child predictions
def aggregate_operator_features(step, df_query, prediction_cache):
    aggregated = {}
    op_row = df_query.iloc[step['df_index']]

    for col in op_row.index:
        if col not in ['query_file', 'subplan_name', 'actual_startup_time', 'actual_total_time']:
            aggregated[col] = op_row[col]

    children_indices = get_children_indices(df_query, step['df_index'])
    aggregated['st1'] = 0.0
    aggregated['rt1'] = 0.0
    aggregated['st2'] = 0.0
    aggregated['rt2'] = 0.0

    for child_idx in children_indices:
        child_row = df_query.iloc[child_idx]
        child_node_id = child_row['node_id']

        if child_node_id in prediction_cache:
            child_rel = child_row['parent_relationship']
            pred = prediction_cache[child_node_id]

            if child_rel == 'Outer':
                aggregated['st1'] = pred['predicted_startup_time']
                aggregated['rt1'] = pred['predicted_total_time']
            elif child_rel == 'Inner':
                aggregated['st2'] = pred['predicted_startup_time']
                aggregated['rt2'] = pred['predicted_total_time']

    return aggregated

# Clean node type for column naming
def clean_node_type(node_type):
    return node_type.replace(' ', '')

# Create prediction result dictionary
def create_prediction_result(op_row, pred_start, pred_exec, prediction_type):
    return {
        'query_file': op_row['query_file'],
        'node_id': op_row['node_id'],
        'node_type': op_row['node_type'],
        'depth': op_row['depth'],
        'parent_relationship': op_row['parent_relationship'],
        'subplan_name': op_row['subplan_name'],
        'actual_startup_time': op_row['actual_startup_time'],
        'actual_total_time': op_row['actual_total_time'],
        'predicted_startup_time': pred_start,
        'predicted_total_time': pred_exec,
        'prediction_type': prediction_type
    }

# Export predictions to CSV
def export_predictions(predictions, output_dir):
    output_path = Path(output_dir) / 'csv'
    output_path.mkdir(parents=True, exist_ok=True)
    df_predictions = pd.DataFrame(predictions)
    df_predictions.to_csv(output_path / 'predictions.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file', help='Path to test dataset CSV')
    parser.add_argument('pattern_csv', help='Path to 01_patterns_*.csv')
    parser.add_argument('pattern_plan_leafs_csv', help='Path to 04_pattern_plan_leafs_*.csv')
    parser.add_argument('pattern_ffs_csv', help='Path to cleaned pattern FFS CSV')
    parser.add_argument('operator_ffs_csv', help='Path to operator FFS CSV')
    parser.add_argument('pattern_model_dir', help='Path to pattern model directory')
    parser.add_argument('operator_model_dir', help='Path to operator model directory')
    parser.add_argument('--output-dir', required=True, help='Output directory for predictions')
    args = parser.parse_args()

    run_prediction_workflow(
        args.test_file,
        args.pattern_csv,
        args.pattern_plan_leafs_csv,
        args.pattern_ffs_csv,
        args.operator_ffs_csv,
        args.pattern_model_dir,
        args.operator_model_dir,
        args.output_dir
    )
