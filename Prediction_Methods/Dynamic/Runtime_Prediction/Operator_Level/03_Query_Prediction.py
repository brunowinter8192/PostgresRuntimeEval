#!/usr/bin/env python3
"""
Local copy for LOTO workflow.
Adds passthrough logic for operators without trained models.
When a model is missing, copies max child prediction (like passthrough operators in Hybrid_1).
"""

# INFRASTRUCTURE

import sys
import argparse
import pandas as pd
from pathlib import Path
import joblib

STATIC_OPERATOR_LEVEL = Path(__file__).resolve().parents[3] / 'Operator_Level'

sys.path.insert(0, str(STATIC_OPERATOR_LEVEL))

# From mapping_config.py: Get leaf operator list, name conversion, and operator features
from mapping_config import LEAF_OPERATORS, csv_name_to_folder_name, OPERATOR_FEATURES


# ORCHESTRATOR

def run_prediction_workflow(test_file, overview_file, models_dir, output_file):
    df_test = load_test_data(test_file)
    df_overview = load_overview(overview_file)

    all_predictions = predict_all_queries(df_test, df_overview, models_dir)
    export_predictions(all_predictions, output_file)


# FUNCTIONS

# Load test dataset from CSV file
def load_test_data(test_file):
    return pd.read_csv(test_file, delimiter=';')


# Load feature overview from CSV file
def load_overview(overview_file):
    return pd.read_csv(overview_file, delimiter=';')


# Predict all queries in test set
def predict_all_queries(df_test, df_overview, models_dir):
    unique_queries = df_test['query_file'].unique()
    all_predictions = []

    for query_file in unique_queries:
        query_ops = df_test[df_test['query_file'] == query_file].copy()

        predictions = predict_single_query(query_ops, df_overview, models_dir)

        for node_id, pred in predictions.items():
            op_row = query_ops[query_ops['node_id'] == node_id].iloc[0]
            all_predictions.append({
                'query_file': query_file,
                'node_id': node_id,
                'node_type': pred['node_type'],
                'depth': op_row['depth'],
                'parent_relationship': op_row['parent_relationship'],
                'subplan_name': op_row['subplan_name'],
                'actual_startup_time': op_row['actual_startup_time'],
                'actual_total_time': op_row['actual_total_time'],
                'predicted_startup_time': pred['predicted_startup_time'],
                'predicted_total_time': pred['predicted_total_time'],
                'prediction_type': pred.get('prediction_type', 'model')
            })

    return all_predictions


# Predict single query bottom-up
def predict_single_query(query_ops, df_overview, models_dir):
    query_ops_main = filter_main_plan_operators(query_ops)
    predictions = {}
    children_map = build_children_map(query_ops_main)
    predict_operators_bottom_up(query_ops_main, predictions, children_map, df_overview, models_dir)
    return predictions


# Filter main plan operators excluding subplans and initplans
def filter_main_plan_operators(query_ops):
    return query_ops[query_ops['subplan_name'].isna() | (query_ops['subplan_name'] == '')]


# Build children map for operator relationships
def build_children_map(query_ops):
    children_map = {}

    for idx in range(len(query_ops)):
        current_row = query_ops.iloc[idx]
        current_depth = current_row['depth']
        current_node_id = current_row['node_id']

        children = []

        for j in range(idx + 1, len(query_ops)):
            next_row = query_ops.iloc[j]

            if next_row['depth'] == current_depth + 1:
                children.append({
                    'node_id': next_row['node_id'],
                    'relationship': next_row['parent_relationship']
                })
            elif next_row['depth'] <= current_depth:
                break

        children_map[current_node_id] = children

    return children_map


# Check if model exists for operator-target combination
def model_exists(models_dir, operator, target):
    operator_folder = csv_name_to_folder_name(operator)
    model_path = Path(models_dir) / target / operator_folder / 'model.pkl'
    return model_path.exists()


# Passthrough prediction: copy max child prediction
def predict_passthrough(node_id, children, predictions):
    max_exec = 0.0
    max_start = 0.0

    for child in children:
        child_id = child['node_id']
        if child_id in predictions:
            pred = predictions[child_id]
            if pred['predicted_total_time'] > max_exec:
                max_exec = pred['predicted_total_time']
                max_start = pred['predicted_startup_time']

    return max_start, max_exec


# Predict all operators bottom-up starting from leafs
def predict_operators_bottom_up(query_ops, predictions, children_map, df_overview, models_dir):
    leaf_nodes = query_ops[query_ops['node_type'].isin(LEAF_OPERATORS)]

    for idx, leaf in leaf_nodes.iterrows():
        node_id = leaf['node_id']
        node_type = leaf['node_type']
        children = children_map.get(node_id, [])

        if not model_exists(models_dir, node_type, 'execution_time'):
            pred_st, pred_rt = predict_passthrough(node_id, children, predictions)
            predictions[node_id] = {
                'predicted_startup_time': pred_st,
                'predicted_total_time': pred_rt,
                'node_type': node_type,
                'prediction_type': 'passthrough'
            }
            continue

        features_exec = get_model_features(df_overview, node_type, 'execution_time')
        features_start = get_model_features(df_overview, node_type, 'start_time')

        if not features_exec or not features_start:
            pred_st, pred_rt = predict_passthrough(node_id, children, predictions)
            predictions[node_id] = {
                'predicted_startup_time': pred_st,
                'predicted_total_time': pred_rt,
                'node_type': node_type,
                'prediction_type': 'passthrough'
            }
            continue

        X_exec = build_feature_vector(leaf, features_exec)
        X_start = build_feature_vector(leaf, features_start)

        model_exec = load_model(models_dir, node_type, 'execution_time')
        model_start = load_model(models_dir, node_type, 'start_time')

        pred_rt = max(0.0, model_exec.predict(X_exec)[0])
        pred_st = max(0.0, model_start.predict(X_start)[0])

        predictions[node_id] = {
            'predicted_startup_time': pred_st,
            'predicted_total_time': pred_rt,
            'node_type': node_type,
            'prediction_type': 'model'
        }

    remaining = query_ops[~query_ops['node_type'].isin(LEAF_OPERATORS)].copy()

    max_iterations = 100
    iteration = 0

    while len(remaining) > 0 and iteration < max_iterations:
        iteration += 1
        progress_made = False

        for idx, op in remaining.iterrows():
            node_id = op['node_id']
            node_type = op['node_type']

            children = children_map.get(node_id, [])

            if len(children) == 0:
                children_ready = True
            else:
                children_ready = all(child['node_id'] in predictions for child in children)

            if not children_ready:
                continue

            st1, rt1, st2, rt2 = 0, 0, 0, 0

            for child in children:
                if child['relationship'] == 'Outer':
                    child_id = child['node_id']
                    st1 = predictions[child_id]['predicted_startup_time']
                    rt1 = predictions[child_id]['predicted_total_time']
                elif child['relationship'] == 'Inner':
                    child_id = child['node_id']
                    st2 = predictions[child_id]['predicted_startup_time']
                    rt2 = predictions[child_id]['predicted_total_time']

            if not model_exists(models_dir, node_type, 'execution_time'):
                pred_st, pred_rt = predict_passthrough(node_id, children, predictions)
                predictions[node_id] = {
                    'predicted_startup_time': pred_st,
                    'predicted_total_time': pred_rt,
                    'node_type': node_type,
                    'prediction_type': 'passthrough'
                }
                remaining = remaining.drop(idx)
                progress_made = True
                continue

            features_exec = get_model_features(df_overview, node_type, 'execution_time')
            features_start = get_model_features(df_overview, node_type, 'start_time')

            if not features_exec or not features_start:
                pred_st, pred_rt = predict_passthrough(node_id, children, predictions)
                predictions[node_id] = {
                    'predicted_startup_time': pred_st,
                    'predicted_total_time': pred_rt,
                    'node_type': node_type,
                    'prediction_type': 'passthrough'
                }
                remaining = remaining.drop(idx)
                progress_made = True
                continue

            X_exec = build_feature_vector(op, features_exec, st1, rt1, st2, rt2)
            X_start = build_feature_vector(op, features_start, st1, rt1, st2, rt2)

            model_exec = load_model(models_dir, node_type, 'execution_time')
            model_start = load_model(models_dir, node_type, 'start_time')

            pred_rt = max(0.0, model_exec.predict(X_exec)[0])
            pred_st = max(0.0, model_start.predict(X_start)[0])

            predictions[node_id] = {
                'predicted_startup_time': pred_st,
                'predicted_total_time': pred_rt,
                'node_type': node_type,
                'prediction_type': 'model'
            }

            remaining = remaining.drop(idx)
            progress_made = True

        if not progress_made:
            break


# Load model for operator-target combination
def load_model(models_dir, operator, target):
    operator_folder = csv_name_to_folder_name(operator)
    model_path = Path(models_dir) / target / operator_folder / 'model.pkl'
    return joblib.load(model_path)


# Get selected features from overview for operator-target combination
def get_model_features(df_overview, operator, target):
    operator_folder = csv_name_to_folder_name(operator)
    row = df_overview[(df_overview['operator'] == operator_folder) &
                      (df_overview['target'] == target)]

    if row.empty:
        return []

    features_str = row.iloc[0]['final_features']

    if pd.isna(features_str):
        return []

    return [f.strip() for f in features_str.split(',')]


# Build feature vector with child predictions
def build_feature_vector(operator_row, features, st1=0, rt1=0, st2=0, rt2=0):
    feature_dict = {}

    for feat in OPERATOR_FEATURES:
        feature_dict[feat] = operator_row[feat]

    feature_dict['st1'] = st1
    feature_dict['rt1'] = rt1
    feature_dict['st2'] = st2
    feature_dict['rt2'] = rt2

    feature_values = [feature_dict[f] for f in features]
    return pd.DataFrame([feature_values], columns=features)


# Save all predictions to CSV file
def export_predictions(all_predictions, output_file):
    df_predictions = pd.DataFrame(all_predictions)

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df_predictions.to_csv(output_path, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("test_file", help="Path to test dataset CSV file")
    parser.add_argument("overview_file", help="Path to two_step_evaluation_overview.csv")
    parser.add_argument("models_dir", help="Directory containing trained models")
    parser.add_argument("--output-file", required=True, help="Output CSV file for predictions")

    args = parser.parse_args()

    run_prediction_workflow(args.test_file, args.overview_file, args.models_dir, args.output_file)
