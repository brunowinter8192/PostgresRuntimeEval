#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import sys
import pandas as pd
import numpy as np
from pathlib import Path
import joblib

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Pattern definitions and pass-through operator detection
from mapping_config import PATTERNS, is_passthrough_operator

# ORCHESTRATOR

# Execute bottom-up prediction workflow for all queries
def run_bottom_up_prediction(test_file, pattern_overview_file, operator_overview_file, pattern_model_dir, operator_model_dir, output_dir):
    df_test = load_test_data(test_file)
    pattern_features = load_pattern_features(pattern_overview_file)
    operator_features = load_operator_features(operator_overview_file)
    pattern_models = load_pattern_models(pattern_model_dir)
    operator_models = load_operator_models(operator_model_dir)
    
    all_predictions = []
    queries = df_test['query_file'].unique()
    
    for query in queries:
        df_query = df_test[df_test['query_file'] == query].copy()
        df_query = df_query[df_query['subplan_name'].isna() | (df_query['subplan_name'] == '')]
        df_query = df_query.sort_values('node_id').reset_index(drop=True)
        predictions = predict_query_bottom_up(df_query, pattern_features, operator_features, pattern_models, operator_models)
        all_predictions.extend(predictions)
    
    export_predictions(all_predictions, output_dir)

# FUNCTIONS

# Load test data from CSV
def load_test_data(test_file):
    return pd.read_csv(test_file, delimiter=';')

# Load pattern features from overview CSV
def load_pattern_features(pattern_file):
    df = pd.read_csv(pattern_file, delimiter=';')
    pattern_dict = {}
    for _, row in df.iterrows():
        pattern_name = row['pattern']
        if pattern_name not in pattern_dict:
            pattern_dict[pattern_name] = {}
        target = row['target']
        final_features = [f.strip() for f in row['final_features'].split(',')]
        missing_child = [] if pd.isna(row['missing_child_features']) else [f.strip() for f in row['missing_child_features'].split(',')]
        pattern_dict[pattern_name][target] = {
            'final_features': final_features,
            'missing_child_features': missing_child
        }
    return pattern_dict

# Load operator features from overview CSV
def load_operator_features(operator_file):
    df = pd.read_csv(operator_file, delimiter=';')
    operator_dict = {}
    for _, row in df.iterrows():
        operator = row['operator']
        if operator not in operator_dict:
            operator_dict[operator] = {}
        target = row['target']
        final_features = [f.strip() for f in row['final_features'].split(',')]
        operator_dict[operator][target] = {
            'final_features': final_features
        }
    return operator_dict

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

# Predict query bottom-up from deepest depth to root
def predict_query_bottom_up(df_query, pattern_features, operator_features, pattern_models, operator_models):
    prediction_results = []
    consumed_by_pattern = set()
    consumed_by_operator = set()
    consumed_by_passthrough = set()
    predictions = {}
    max_depth = df_query['depth'].max()
    
    for depth in range(max_depth, -1, -1):
        operators_at_depth = df_query[df_query['depth'] == depth]

        for idx in operators_at_depth.index:
            if idx in consumed_by_pattern or idx in consumed_by_operator or idx in consumed_by_passthrough:
                continue

            op_row = df_query.loc[idx]
            op_type = op_row['node_type']
            parent_idx = find_parent_operator(df_query, idx)

            if parent_idx is None:
                if is_passthrough_operator(op_type):
                    continue
                aggregated_row = build_operator_aggregated_row(df_query, idx, predictions)
                pred_start, pred_exec = predict_operator(op_row, aggregated_row, operator_features, operator_models)
                prediction_results.append(create_prediction_result(op_row, pred_start, pred_exec, 'operator'))
                consumed_by_operator.add(idx)
                pred_key = (op_row['node_type'], op_row['depth'])
                predictions[pred_key] = {'predicted_startup_time': pred_start, 'predicted_total_time': pred_exec}
                continue

            if parent_idx in consumed_by_operator or parent_idx in consumed_by_pattern:
                continue

            parent_row = df_query.loc[parent_idx]

            if parent_row['depth'] < 0:
                continue

            if is_passthrough_operator(parent_row['node_type']):
                continue

            siblings_indices = find_all_siblings(df_query, idx, parent_idx)

            if any(sib_idx in consumed_by_pattern or sib_idx in consumed_by_operator for sib_idx in siblings_indices):
                continue

            children_info = build_children_info_list(df_query, siblings_indices)
            pattern_match = try_match_pattern_with_parent(parent_row, children_info, pattern_features, predictions, df_query)

            if pattern_match:
                aggregated_row = aggregate_pattern_rows(df_query, parent_idx, siblings_indices, predictions)
                pred_start, pred_exec = predict_pattern(pattern_match, aggregated_row, pattern_features, pattern_models)
                prediction_results.append(create_prediction_result(parent_row, pred_start, pred_exec, 'pattern'))

                consumed_by_pattern.add(parent_idx)
                for sib_idx in siblings_indices:
                    consumed_by_pattern.add(sib_idx)

                pred_key = (parent_row['node_type'], parent_row['depth'])
                predictions[pred_key] = {'predicted_startup_time': pred_start, 'predicted_total_time': pred_exec}

        for idx in operators_at_depth.index:
            if idx in consumed_by_pattern or idx in consumed_by_operator or idx in consumed_by_passthrough:
                continue

            op_row = df_query.loc[idx]
            op_type = op_row['node_type']

            if is_passthrough_operator(op_type):
                children = get_children_info(df_query, idx)

                if len(children) > 0:
                    pred_key_child = (children[0]['node_type'], children[0]['depth'])

                    if pred_key_child in predictions:
                        pred_start = predictions[pred_key_child]['predicted_startup_time']
                        pred_exec = predictions[pred_key_child]['predicted_total_time']

                        predictions[(op_type, op_row['depth'])] = {
                            'predicted_startup_time': pred_start,
                            'predicted_total_time': pred_exec
                        }

                        prediction_results.append(create_prediction_result(
                            op_row, pred_start, pred_exec, 'passthrough'
                        ))

                        consumed_by_passthrough.add(idx)
                        continue

        for idx in operators_at_depth.index:
            if idx in consumed_by_pattern or idx in consumed_by_operator or idx in consumed_by_passthrough:
                continue

            op_row = df_query.loc[idx]
            aggregated_row = build_operator_aggregated_row(df_query, idx, predictions)
            pred_start, pred_exec = predict_operator(op_row, aggregated_row, operator_features, operator_models)
            prediction_results.append(create_prediction_result(op_row, pred_start, pred_exec, 'operator'))
            consumed_by_operator.add(idx)
            pred_key = (op_row['node_type'], op_row['depth'])
            predictions[pred_key] = {'predicted_startup_time': pred_start, 'predicted_total_time': pred_exec}
    
    return prediction_results

# Find parent operator for given operator
def find_parent_operator(df_query, operator_idx):
    op_row = df_query.loc[operator_idx]
    op_depth = op_row['depth']
    if op_depth == 0:
        return None
    for idx in range(operator_idx - 1, -1, -1):
        row = df_query.iloc[idx]
        if row['depth'] == op_depth - 1:
            return df_query.index[idx]
    return None

# Find all siblings of operator including itself
def find_all_siblings(df_query, operator_idx, parent_idx):
    parent_row = df_query.loc[parent_idx]
    parent_depth = parent_row['depth']
    siblings = []
    for idx in range(parent_idx + 1, len(df_query)):
        row = df_query.iloc[idx]
        if row['depth'] == parent_depth + 1:
            siblings.append(df_query.index[idx])
        elif row['depth'] <= parent_depth:
            break
    return siblings

# Build children info list from sibling indices
def build_children_info_list(df_query, sibling_indices):
    children_info = []
    for idx in sibling_indices:
        row = df_query.loc[idx]
        children_info.append({
            'index': idx,
            'node_type': row['node_type'],
            'depth': row['depth'],
            'parent_relationship': row['parent_relationship']
        })
    return children_info

# Get children information for operator
def get_children_info(df_query, parent_idx):
    parent_row = df_query.loc[parent_idx]
    parent_depth = parent_row['depth']
    children = []
    for idx in range(parent_idx + 1, len(df_query)):
        row = df_query.iloc[idx]
        if row['depth'] == parent_depth + 1:
            children.append({
                'index': df_query.index[idx],
                'node_type': row['node_type'],
                'depth': row['depth'],
                'parent_relationship': row['parent_relationship']
            })
        elif row['depth'] <= parent_depth:
            break
    return children

# Try to match pattern with parent operator
def try_match_pattern_with_parent(parent_row, children_info, pattern_features, predictions, df_query):
    if len(children_info) == 0:
        return None
    pattern_key = build_pattern_key(parent_row['node_type'], children_info)
    if pattern_key not in PATTERNS:
        return None
    if pattern_key not in pattern_features:
        return None
    pattern_data = pattern_features[pattern_key]
    needs_child_features = len(pattern_data['execution_time']['missing_child_features']) > 0
    if needs_child_features:
        if not check_child_features_available(pattern_key, pattern_features, children_info, predictions, df_query):
            return None
    return pattern_key

# Build pattern key from operator and children
def build_pattern_key(parent_type, children_info):
    parent_normalized = parent_type.replace(' ', '_')
    if len(children_info) == 1:
        child_normalized = children_info[0]['node_type'].replace(' ', '_')
        relationship = children_info[0]['parent_relationship']
        return f"{parent_normalized}_{child_normalized}_{relationship}"
    if len(children_info) == 2:
        children_sorted = sorted(children_info, key=lambda x: (0 if x['parent_relationship'] == 'Outer' else 1))
        outer_normalized = children_sorted[0]['node_type'].replace(' ', '_')
        inner_normalized = children_sorted[1]['node_type'].replace(' ', '_')
        return f"{parent_normalized}_{outer_normalized}_Outer_{inner_normalized}_Inner"
    return None

# Check if child features are available for non-leaf pattern
def check_child_features_available(pattern_key, pattern_features, children_info, predictions, df_query):
    pattern_data = pattern_features[pattern_key]
    missing_child_features = pattern_data['execution_time']['missing_child_features']
    if len(missing_child_features) == 0:
        return True
    for child in children_info:
        grandchildren = get_children_info(df_query, child['index'])
        for grandchild in grandchildren:
            pred_key = (grandchild['node_type'], grandchild['depth'])
            if pred_key not in predictions:
                return False
    return True

# Aggregate pattern rows from parent and children
def aggregate_pattern_rows(df_query, parent_idx, children_indices, predictions):
    parent_row = df_query.loc[parent_idx]
    aggregated = {}
    aggregated['query_file'] = parent_row['query_file']
    parent_normalized = parent_row['node_type'].replace(' ', '')
    parent_prefix = parent_normalized + '_'
    for col in parent_row.index:
        if col not in ['query_file']:
            aggregated[parent_prefix + col] = parent_row[col]
    children_sorted = []
    for child_idx in children_indices:
        child_row = df_query.loc[child_idx]
        children_sorted.append({
            'row': child_row,
            'index': child_idx,
            'relationship': child_row['parent_relationship'],
            'node_type': child_row['node_type']
        })
    children_sorted = sorted(children_sorted, key=lambda x: (0 if x['relationship'] == 'Outer' else 1))
    
    for child in children_sorted:
        child_row = child['row']
        child_idx = child['index']
        child_normalized = child['node_type'].replace(' ', '')
        child_prefix = child_normalized + '_' + child['relationship'] + '_'
        for col in child_row.index:
            if col not in ['query_file', 'st1', 'rt1', 'st2', 'rt2']:
                aggregated[child_prefix + col] = child_row[col]
        grandchildren = get_children_info(df_query, child_idx)
        aggregated[child_prefix + 'st1'] = 0.0
        aggregated[child_prefix + 'rt1'] = 0.0
        aggregated[child_prefix + 'st2'] = 0.0
        aggregated[child_prefix + 'rt2'] = 0.0
        for grandchild in grandchildren:
            pred_key = (grandchild['node_type'], grandchild['depth'])
            if pred_key in predictions:
                if grandchild['parent_relationship'] == 'Outer':
                    aggregated[child_prefix + 'st1'] = predictions[pred_key]['predicted_startup_time']
                    aggregated[child_prefix + 'rt1'] = predictions[pred_key]['predicted_total_time']
                elif grandchild['parent_relationship'] == 'Inner':
                    aggregated[child_prefix + 'st2'] = predictions[pred_key]['predicted_startup_time']
                    aggregated[child_prefix + 'rt2'] = predictions[pred_key]['predicted_total_time']
    return aggregated

# Build operator aggregated row with child predictions
def build_operator_aggregated_row(df_query, operator_idx, predictions):
    op_row = df_query.loc[operator_idx]
    aggregated = dict(op_row)
    children = get_children_info(df_query, operator_idx)
    aggregated['st1'] = 0.0
    aggregated['rt1'] = 0.0
    aggregated['st2'] = 0.0
    aggregated['rt2'] = 0.0
    for child in children:
        pred_key = (child['node_type'], child['depth'])
        if pred_key in predictions:
            if child['parent_relationship'] == 'Outer':
                aggregated['st1'] = predictions[pred_key]['predicted_startup_time']
                aggregated['rt1'] = predictions[pred_key]['predicted_total_time']
            elif child['parent_relationship'] == 'Inner':
                aggregated['st2'] = predictions[pred_key]['predicted_startup_time']
                aggregated['rt2'] = predictions[pred_key]['predicted_total_time']
    return aggregated

# Predict pattern using pattern models
def predict_pattern(pattern_key, aggregated_row, pattern_features, pattern_models):
    pattern_data = pattern_features[pattern_key]
    exec_features = pattern_data['execution_time']['final_features']
    start_features = pattern_data['start_time']['final_features']
    X_exec = pd.DataFrame([{feat: aggregated_row[feat] for feat in exec_features}])
    X_start = pd.DataFrame([{feat: aggregated_row[feat] for feat in start_features}])
    pred_exec = pattern_models['execution_time'][pattern_key].predict(X_exec)[0]
    pred_start = pattern_models['start_time'][pattern_key].predict(X_start)[0]
    return pred_start, pred_exec

# Predict operator using operator models
def predict_operator(op_row, aggregated_row, operator_features, operator_models):
    operator_normalized = op_row['node_type'].replace(' ', '_')
    if operator_normalized not in operator_features:
        return 0.0, 0.0
    op_data = operator_features[operator_normalized]
    exec_features = op_data['execution_time']['final_features']
    start_features = op_data['start_time']['final_features']
    X_exec = pd.DataFrame([{feat: aggregated_row[feat] for feat in exec_features}])
    X_start = pd.DataFrame([{feat: aggregated_row[feat] for feat in start_features}])
    pred_exec = operator_models['execution_time'][operator_normalized].predict(X_exec)[0]
    pred_start = operator_models['start_time'][operator_normalized].predict(X_start)[0]
    return pred_start, pred_exec

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
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    df_predictions = pd.DataFrame(predictions)
    df_predictions.to_csv(output_path / 'predictions.csv', sep=';', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bottom-up prediction for hybrid model')
    parser.add_argument('test_file', help='Path to test.csv')
    parser.add_argument('pattern_overview', help='Path to pattern overview CSV')
    parser.add_argument('operator_overview', help='Path to operator overview CSV')
    parser.add_argument('pattern_model_dir', help='Path to Hybrid model directory')
    parser.add_argument('operator_model_dir', help='Path to Operator model directory')
    parser.add_argument('--output-dir', required=True, help='Path to output directory for predictions')
    args = parser.parse_args()

    run_bottom_up_prediction(
        args.test_file,
        args.pattern_overview,
        args.operator_overview,
        args.pattern_model_dir,
        args.operator_model_dir,
        args.output_dir
    )
