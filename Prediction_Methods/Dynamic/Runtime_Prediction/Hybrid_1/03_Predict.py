#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import argparse
import pickle
import hashlib
import joblib
from pathlib import Path
from multiprocessing import Pool

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

# From mapping_config.py: Configuration constants
from mapping_config import csv_name_to_folder_name, LEAF_OPERATORS

# From report.py: Report export
from report import export_md_report

ALL_TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
ALL_APPROACHES = ['approach_3']

SCRIPT_DIR = Path(__file__).resolve().parent
DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Hybrid_1'
OPERATOR_DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Operator'
OPERATOR_LEVEL_DIR = SCRIPT_DIR.parent / 'Operator_Level'
OUTPUT_DIR = SCRIPT_DIR


# ORCHESTRATOR
def batch_predict(templates: list, approaches: list, report: bool = False) -> None:
    tasks = [(template, approach, report) for template in templates for approach in approaches]
    with Pool(6) as pool:
        pool.map(process_task, tasks)


# FUNCTIONS

# Process single template-approach combination
def process_task(task: tuple) -> None:
    template, approach, report = task
    print(f"{template}/{approach}...")

    template_output = OUTPUT_DIR / template / approach
    pattern_dataset = DATASET_DIR / template / approach

    model_dir = template_output / 'Model'
    if not model_dir.exists():
        print(f"  Skipping: no Model/ directory (run 02_Pretrain_Models.py first)")
        return

    run_predict(template, approach, pattern_dataset, template_output, report)


# Run hybrid prediction for a template
def run_predict(template: str, approach: str, pattern_dataset: Path, output_dir: Path, report: bool = False) -> None:
    test_file = OPERATOR_DATASET_DIR / template / 'test.csv'
    model_dir = output_dir / 'Model'

    df_test = load_test_data(test_file)
    pattern_info, pattern_order = load_pattern_info(pattern_dataset / 'used_patterns.csv')

    operator_level_dir = OPERATOR_LEVEL_DIR / template
    operator_models = load_operator_models(operator_level_dir)
    operator_features = load_operator_features(operator_level_dir)

    pattern_models = load_pattern_models(model_dir, list(pattern_info.keys()))

    if report:
        all_predictions = []
        for query_file in df_test['query_file'].unique():
            query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)

            predictions, steps, consumed_nodes, pattern_assignments = predict_single_query(
                query_ops, operator_models, operator_features, pattern_models, pattern_info, pattern_order,
                collect_steps=True
            )

            all_predictions.extend(predictions)

            export_md_report(
                query_file, query_ops, predictions, steps, consumed_nodes,
                pattern_assignments, pattern_info, str(output_dir)
            )

        export_predictions(all_predictions, output_dir)
    else:
        predictions = predict_all_queries(
            df_test, operator_models, operator_features, pattern_models, pattern_info, pattern_order
        )
        export_predictions(predictions, output_dir)


# ============== IO FUNCTIONS ==============

# Load test data from CSV
def load_test_data(test_file: Path) -> pd.DataFrame:
    df = pd.read_csv(test_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load pattern info from used_patterns.csv
def load_pattern_info(patterns_csv: Path) -> tuple:
    df = pd.read_csv(patterns_csv, delimiter=';')
    df_sorted = df.sort_values(
        ['pattern_length', 'occurrence_count'],
        ascending=[False, False]
    ).reset_index(drop=True)
    pattern_order = df_sorted['pattern_hash'].tolist()

    info = {}
    for _, row in df_sorted.iterrows():
        info[row['pattern_hash']] = {
            'length': int(row['pattern_length']),
            'pattern_string': row.get('pattern_string', '')
        }

    return info, pattern_order


# Load operator models from Operator_Level/{template}/Model/{target}/{op_name}/model.pkl
def load_operator_models(operator_level_dir: Path) -> dict:
    models = {'execution_time': {}, 'start_time': {}}

    for target in ['execution_time', 'start_time']:
        target_dir = operator_level_dir / 'Model' / target

        if not target_dir.exists():
            continue

        for op_dir in target_dir.iterdir():
            if op_dir.is_dir():
                model_file = op_dir / 'model.pkl'

                if model_file.exists():
                    models[target][op_dir.name] = joblib.load(model_file)

    return models


# Load operator features from Operator_Level/{template}/SVM/two_step_evaluation_overview.csv
def load_operator_features(operator_level_dir: Path) -> dict:
    overview_file = operator_level_dir / 'SVM' / 'two_step_evaluation_overview.csv'

    if not overview_file.exists():
        return {'execution_time': {}, 'start_time': {}}

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


# Load pattern models from Model/{target}/{hash}/model.pkl
def load_pattern_models(model_dir: Path, pattern_hashes: list) -> dict:
    models = {'execution_time': {}, 'start_time': {}}

    for pattern_hash in pattern_hashes:
        for target in ['execution_time', 'start_time']:
            model_file = model_dir / target / pattern_hash / 'model.pkl'

            if model_file.exists():
                with open(model_file, 'rb') as f:
                    models[target][pattern_hash] = pickle.load(f)

    return models


# Export predictions to CSV file
def export_predictions(predictions: list, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(predictions)
    df.to_csv(output_dir / 'predictions.csv', sep=';', index=False)


# ============== TREE FUNCTIONS ==============

class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# Build tree structure from flat DataFrame
def build_tree_from_dataframe(query_ops: pd.DataFrame) -> QueryNode:
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


# Extract all nodes from tree recursively
def extract_all_nodes(node: QueryNode) -> list:
    nodes = [node]
    for child in node.children:
        nodes.extend(extract_all_nodes(child))
    return nodes


# Compute MD5 hash for pattern subtree structure
def compute_pattern_hash(node: QueryNode, remaining_length: int) -> str:
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


# Check if node has subtree of required depth
def has_children_at_length(node: QueryNode, pattern_length: int) -> bool:
    if pattern_length == 1:
        return True
    if pattern_length == 2:
        return len(node.children) > 0
    if len(node.children) == 0:
        return False
    return any(has_children_at_length(child, pattern_length - 1) for child in node.children)


# Extract all node IDs in pattern subtree
def extract_pattern_node_ids(node: QueryNode, remaining_length: int) -> list:
    if remaining_length == 1 or len(node.children) == 0:
        return [node.node_id]

    node_ids = [node.node_id]
    for child in node.children:
        child_ids = extract_pattern_node_ids(child, remaining_length - 1)
        node_ids.extend(child_ids)
    return node_ids


# Build pattern assignments matching patterns to query nodes
def build_pattern_assignments(all_nodes: list, pattern_info: dict, pattern_order: list) -> tuple:
    consumed_nodes = set()
    pattern_assignments = {}

    for pattern_hash in pattern_order:
        if pattern_hash not in pattern_info:
            continue

        info = pattern_info[pattern_hash]
        pattern_length = info['length']

        for node in all_nodes:
            if node.node_id in consumed_nodes:
                continue
            if not has_children_at_length(node, pattern_length):
                continue

            pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
            if any(nid in consumed_nodes for nid in pattern_node_ids):
                continue

            computed_hash = compute_pattern_hash(node, pattern_length)
            if computed_hash == pattern_hash:
                # Single-Pattern-Constraint: Skip if this pattern would consume ALL nodes
                would_consume_all = (len(consumed_nodes) == 0 and len(pattern_node_ids) == len(all_nodes))
                if would_consume_all:
                    continue

                consumed_nodes.update(pattern_node_ids)
                pattern_assignments[node.node_id] = pattern_hash

    return consumed_nodes, pattern_assignments


# Get direct children from full query ops by node ID
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


# ============== PREDICTION FUNCTIONS ==============

# Predict all queries in test set
def predict_all_queries(
    df_test: pd.DataFrame,
    operator_models: dict,
    operator_features: dict,
    pattern_models: dict,
    pattern_info: dict,
    pattern_order: list
) -> list:
    all_predictions = []

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)

        predictions, _, _, _ = predict_single_query(
            query_ops, operator_models, operator_features, pattern_models, pattern_info, pattern_order
        )

        all_predictions.extend(predictions)

    return all_predictions


# Predict single query using two-phase bottom-up approach
def predict_single_query(
    query_ops: pd.DataFrame,
    operator_models: dict,
    operator_features: dict,
    pattern_models: dict,
    pattern_info: dict,
    pattern_order: list,
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
                node, query_ops, pattern_models, prediction_cache, info['length'], pattern_hash
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
            result = predict_operator(node, query_ops, operator_models, operator_features, prediction_cache)
            prediction_cache[node.node_id] = result
            predictions.append(create_prediction_result(row, result['start'], result['exec'], result['type']))

            if collect_steps:
                if result['type'] == 'passthrough':
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


# Predict using pattern model
def predict_pattern(
    node: QueryNode,
    query_ops: pd.DataFrame,
    pattern_models: dict,
    prediction_cache: dict,
    pattern_length: int,
    pattern_hash: str
) -> dict:
    pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
    pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]

    aggregated = aggregate_pattern_with_cache(
        pattern_rows, pattern_length, query_ops, prediction_cache, set(pattern_node_ids)
    )

    exec_model_data = pattern_models['execution_time'].get(pattern_hash)
    start_model_data = pattern_models['start_time'].get(pattern_hash)

    if not exec_model_data or not start_model_data:
        return {'start': 0.0, 'exec': 0.0}

    features_exec = exec_model_data['features']
    features_start = start_model_data['features']

    X_exec = pd.DataFrame([[aggregated.get(f, 0) for f in features_exec]], columns=features_exec)
    X_start = pd.DataFrame([[aggregated.get(f, 0) for f in features_start]], columns=features_start)

    pred_exec = max(0.0, exec_model_data['model'].predict(X_exec)[0])
    pred_start = max(0.0, start_model_data['model'].predict(X_start)[0])

    return {'start': pred_start, 'exec': pred_exec}


# Predict using operator model with fallback logic
def predict_operator(
    node: QueryNode,
    query_ops: pd.DataFrame,
    operator_models: dict,
    operator_features: dict,
    prediction_cache: dict
) -> dict:
    op_name = csv_name_to_folder_name(node.node_type)
    row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]
    is_leaf = node.node_type in LEAF_OPERATORS

    exec_model = operator_models['execution_time'].get(op_name)
    start_model = operator_models['start_time'].get(op_name)
    features_exec = operator_features['execution_time'].get(op_name, [])
    features_start = operator_features['start_time'].get(op_name, [])

    if not exec_model or not start_model or not features_exec or not features_start:
        pred_start, pred_exec = predict_passthrough(node, prediction_cache, is_leaf)
        return {'start': pred_start, 'exec': pred_exec, 'type': 'passthrough'}

    features = build_operator_features(row, node, prediction_cache)

    X_exec = pd.DataFrame([[features.get(f, 0) for f in features_exec]], columns=features_exec)
    X_start = pd.DataFrame([[features.get(f, 0) for f in features_start]], columns=features_start)

    pred_exec = max(0.0, exec_model.predict(X_exec)[0])
    pred_start = max(0.0, start_model.predict(X_start)[0])

    return {'start': pred_start, 'exec': pred_exec, 'type': 'operator'}


# Passthrough prediction: copy max child prediction or 0.0 for leaf
def predict_passthrough(node: QueryNode, prediction_cache: dict, is_leaf: bool) -> tuple:
    if is_leaf:
        return 0.0, 0.0

    max_exec = 0.0
    max_start = 0.0

    for child in node.children:
        if child.node_id in prediction_cache:
            pred = prediction_cache[child.node_id]
            if pred['exec'] > max_exec:
                max_exec = pred['exec']
                max_start = pred['start']

    return max_start, max_exec


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


# Create prediction result dictionary
def create_prediction_result(row, pred_start: float, pred_exec: float, prediction_type: str, pattern_hash: str = None) -> dict:
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
        'prediction_type': prediction_type,
        'pattern_hash': pattern_hash
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--templates", nargs="+", default=ALL_TEMPLATES, help="Templates to process")
    parser.add_argument("--approaches", nargs="+", default=ALL_APPROACHES, help="Approaches to process")
    parser.add_argument("--report", action="store_true", help="Generate MD reports for debugging")
    args = parser.parse_args()
    batch_predict(args.templates, args.approaches, args.report)
