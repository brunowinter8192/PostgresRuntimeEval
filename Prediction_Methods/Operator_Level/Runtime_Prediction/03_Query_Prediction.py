#!/usr/bin/env python3

# INFRASTRUCTURE

import sys
import argparse
import hashlib
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import joblib

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# From mapping_config.py: Get leaf operator list name conversion and operator features
from mapping_config import LEAF_OPERATORS, csv_name_to_folder_name, OPERATOR_FEATURES


# Get project root via git
def get_project_root():
    import subprocess
    result = subprocess.run(['git', 'rev-parse', '--show-toplevel'],
                          capture_output=True, text=True, check=True)
    return Path(result.stdout.strip())


# Convert absolute path to relative from project root
def to_relative_path(path):
    abs_path = Path(path).resolve()
    return str(abs_path.relative_to(get_project_root()))


# Compute hash for unique plan structure
def compute_plan_hash(query_ops):
    sorted_ops = query_ops.sort_values('node_id')
    structure = [(row['node_type'], row['depth'], row['parent_relationship'])
                 for _, row in sorted_ops.iterrows()]
    return hashlib.md5(str(structure).encode()).hexdigest()


# ORCHESTRATOR

def run_prediction_workflow(test_file, overview_file, models_dir, output_file, md_query=None, report=False, report_dir=None):
    df_test = load_test_data(test_file)
    df_overview = load_overview(overview_file)

    if report:
        run_with_reports(df_test, df_overview, models_dir, test_file, overview_file, output_file, report_dir)
    elif md_query:
        query_ops = df_test[df_test['query_file'] == md_query].copy()
        predictions, steps = predict_single_query_with_steps(query_ops, df_overview, models_dir)
        export_md_report(md_query, test_file, overview_file, models_dir, query_ops, predictions, steps)
    else:
        all_predictions = predict_all_queries(df_test, df_overview, models_dir)
        export_predictions(all_predictions, output_file)


# Run predictions with MD reports for first query of each unique plan
def run_with_reports(df_test, df_overview, models_dir, test_file, overview_file, output_file, report_dir):
    all_predictions = []
    reported_plans = set()

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].copy()

        plan_hash = compute_plan_hash(query_ops)
        should_report = plan_hash not in reported_plans

        if should_report:
            predictions, steps = predict_single_query_with_steps(query_ops, df_overview, models_dir)
            reported_plans.add(plan_hash)
            export_md_report(query_file, test_file, overview_file, models_dir, query_ops, predictions, steps, report_dir, plan_hash)
        else:
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
                'predicted_total_time': pred['predicted_total_time']
            })

    if output_file:
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
                'predicted_total_time': pred['predicted_total_time']
            })

    return all_predictions


# Predict single query bottom-up
def predict_single_query(query_ops, df_overview, models_dir):
    query_ops_main = filter_main_plan_operators(query_ops)
    predictions = {}
    children_map = build_children_map(query_ops_main)
    predict_operators_bottom_up(query_ops_main, predictions, children_map, df_overview, models_dir)
    return predictions


# Predict single query bottom-up with step tracking for MD report
def predict_single_query_with_steps(query_ops, df_overview, models_dir):
    query_ops_main = filter_main_plan_operators(query_ops)
    predictions = {}
    steps = []
    children_map = build_children_map(query_ops_main)
    predict_operators_bottom_up_with_steps(query_ops_main, predictions, steps, children_map, df_overview, models_dir)
    return predictions, steps


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


# Predict all operators bottom-up starting from leafs
def predict_operators_bottom_up(query_ops, predictions, children_map, df_overview, models_dir):
    leaf_nodes = query_ops[query_ops['node_type'].isin(LEAF_OPERATORS)]

    for idx, leaf in leaf_nodes.iterrows():
        node_id = leaf['node_id']
        node_type = leaf['node_type']

        features_exec = get_model_features(df_overview, node_type, 'execution_time')
        features_start = get_model_features(df_overview, node_type, 'start_time')

        if not features_exec or not features_start:
            continue

        X_exec = build_feature_vector(leaf, features_exec)
        X_start = build_feature_vector(leaf, features_start)

        model_exec = load_model(models_dir, node_type, 'execution_time')
        model_start = load_model(models_dir, node_type, 'start_time')

        pred_rt = model_exec.predict(X_exec)[0]
        pred_st = model_start.predict(X_start)[0]

        predictions[node_id] = {
            'predicted_startup_time': pred_st,
            'predicted_total_time': pred_rt,
            'node_type': node_type
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

            features_exec = get_model_features(df_overview, node_type, 'execution_time')
            features_start = get_model_features(df_overview, node_type, 'start_time')

            if not features_exec or not features_start:
                remaining = remaining.drop(idx)
                progress_made = True
                continue

            X_exec = build_feature_vector(op, features_exec, st1, rt1, st2, rt2)
            X_start = build_feature_vector(op, features_start, st1, rt1, st2, rt2)

            model_exec = load_model(models_dir, node_type, 'execution_time')
            model_start = load_model(models_dir, node_type, 'start_time')

            pred_rt = model_exec.predict(X_exec)[0]
            pred_st = model_start.predict(X_start)[0]

            predictions[node_id] = {
                'predicted_startup_time': pred_st,
                'predicted_total_time': pred_rt,
                'node_type': node_type
            }

            remaining = remaining.drop(idx)
            progress_made = True

        if not progress_made:
            break


# Predict all operators bottom-up with step tracking for MD report
def predict_operators_bottom_up_with_steps(query_ops, predictions, steps, children_map, df_overview, models_dir):
    leaf_nodes = query_ops[query_ops['node_type'].isin(LEAF_OPERATORS)]
    step_num = 1

    for idx, leaf in leaf_nodes.iterrows():
        node_id = leaf['node_id']
        node_type = leaf['node_type']
        depth = leaf['depth']

        features_exec = get_model_features(df_overview, node_type, 'execution_time')
        features_start = get_model_features(df_overview, node_type, 'start_time')

        if not features_exec or not features_start:
            continue

        X_exec = build_feature_vector(leaf, features_exec)
        X_start = build_feature_vector(leaf, features_start)

        model_path_exec = get_model_path(models_dir, node_type, 'execution_time')
        model_path_start = get_model_path(models_dir, node_type, 'start_time')

        model_exec = joblib.load(model_path_exec)
        model_start = joblib.load(model_path_start)

        pred_rt = model_exec.predict(X_exec)[0]
        pred_st = model_start.predict(X_start)[0]

        predictions[node_id] = {
            'predicted_startup_time': pred_st,
            'predicted_total_time': pred_rt,
            'node_type': node_type
        }

        steps.append({
            'step': step_num,
            'node_id': node_id,
            'node_type': node_type,
            'depth': depth,
            'is_leaf': True,
            'model_path_exec': to_relative_path(model_path_exec),
            'model_path_start': to_relative_path(model_path_start),
            'features_exec': features_exec,
            'features_start': features_start,
            'input_values_exec': dict(zip(features_exec, X_exec.iloc[0].tolist())),
            'input_values_start': dict(zip(features_start, X_start.iloc[0].tolist())),
            'predicted_startup_time': pred_st,
            'predicted_total_time': pred_rt,
            'actual_startup_time': leaf['actual_startup_time'],
            'actual_total_time': leaf['actual_total_time']
        })
        step_num += 1

    remaining = query_ops[~query_ops['node_type'].isin(LEAF_OPERATORS)].copy()
    max_iterations = 100
    iteration = 0

    while len(remaining) > 0 and iteration < max_iterations:
        iteration += 1
        progress_made = False

        for idx, op in remaining.iterrows():
            node_id = op['node_id']
            node_type = op['node_type']
            depth = op['depth']

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

            features_exec = get_model_features(df_overview, node_type, 'execution_time')
            features_start = get_model_features(df_overview, node_type, 'start_time')

            if not features_exec or not features_start:
                remaining = remaining.drop(idx)
                progress_made = True
                continue

            X_exec = build_feature_vector(op, features_exec, st1, rt1, st2, rt2)
            X_start = build_feature_vector(op, features_start, st1, rt1, st2, rt2)

            model_path_exec = get_model_path(models_dir, node_type, 'execution_time')
            model_path_start = get_model_path(models_dir, node_type, 'start_time')

            model_exec = joblib.load(model_path_exec)
            model_start = joblib.load(model_path_start)

            pred_rt = model_exec.predict(X_exec)[0]
            pred_st = model_start.predict(X_start)[0]

            predictions[node_id] = {
                'predicted_startup_time': pred_st,
                'predicted_total_time': pred_rt,
                'node_type': node_type
            }

            steps.append({
                'step': step_num,
                'node_id': node_id,
                'node_type': node_type,
                'depth': depth,
                'is_leaf': False,
                'model_path_exec': to_relative_path(model_path_exec),
                'model_path_start': to_relative_path(model_path_start),
                'features_exec': features_exec,
                'features_start': features_start,
                'input_values_exec': dict(zip(features_exec, X_exec.iloc[0].tolist())),
                'input_values_start': dict(zip(features_start, X_start.iloc[0].tolist())),
                'predicted_startup_time': pred_st,
                'predicted_total_time': pred_rt,
                'actual_startup_time': op['actual_startup_time'],
                'actual_total_time': op['actual_total_time']
            })
            step_num += 1

            remaining = remaining.drop(idx)
            progress_made = True

        if not progress_made:
            break


# Get model path for operator-target combination
def get_model_path(models_dir, operator, target):
    operator_folder = csv_name_to_folder_name(operator)
    return Path(models_dir) / target / operator_folder / 'model.pkl'


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


# Build query tree string from operators
def build_query_tree(query_ops):
    query_ops_main = query_ops[query_ops['subplan_name'].isna() | (query_ops['subplan_name'] == '')]
    query_ops_sorted = query_ops_main.sort_values('node_id')

    lines = []
    min_depth = query_ops_sorted['depth'].min()

    for idx, row in query_ops_sorted.iterrows():
        depth = row['depth']
        indent = '  ' * (depth - min_depth)
        node_type = row['node_type']
        node_id = row['node_id']
        is_leaf = node_type in LEAF_OPERATORS
        is_root = depth == min_depth

        suffix = ''
        if is_root:
            suffix = ' - ROOT'
        elif is_leaf:
            suffix = ' - LEAF'

        lines.append(f'{indent}Node {node_id} ({node_type}){suffix}')

    return '\n'.join(lines)


# Format feature values for MD output
def format_feature_values(feature_dict):
    parts = []
    for k, v in feature_dict.items():
        if isinstance(v, float):
            parts.append(f'{k}={v:.4f}')
        else:
            parts.append(f'{k}={v}')
    return ', '.join(parts)


# Export MD report for single query prediction
def export_md_report(query_file, test_file, overview_file, models_dir, query_ops, predictions, steps, report_dir=None, plan_hash=None):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    timestamp_display = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if report_dir:
        md_dir = Path(report_dir)
    else:
        md_dir = Path(__file__).parent / 'md'
    md_dir.mkdir(parents=True, exist_ok=True)

    template = query_file.split('_')[0]
    if plan_hash:
        md_file = md_dir / f'03_{template}_{plan_hash[:8]}.md'
    else:
        md_file = md_dir / f'03_query_prediction_{query_file}_{timestamp}.md'

    lines = []
    lines.append('# Query Prediction Report')
    lines.append('')
    lines.append(f'**Query:** {query_file}')
    lines.append(f'**Timestamp:** {timestamp_display}')
    lines.append('')

    lines.append('## Input Summary')
    lines.append('')
    lines.append(f'- **Test File:** {to_relative_path(test_file)}')
    lines.append(f'- **Overview File:** {to_relative_path(overview_file)}')
    lines.append(f'- **Models Directory:** {to_relative_path(models_dir)}')
    lines.append('')

    lines.append('## Query Tree')
    lines.append('')
    lines.append('```')
    lines.append(build_query_tree(query_ops))
    lines.append('```')
    lines.append('')

    lines.append('## Prediction Chain (Bottom-Up)')
    lines.append('')

    for step in steps:
        leaf_marker = ' - LEAF' if step['is_leaf'] else ''
        if step['depth'] == query_ops['depth'].min():
            leaf_marker = ' - ROOT'

        lines.append(f"### Step {step['step']}: Node {step['node_id']} ({step['node_type']}){leaf_marker}")
        lines.append('')
        lines.append(f"**Model (execution_time):** {step['model_path_exec']}")
        lines.append(f"**Model (start_time):** {step['model_path_start']}")
        lines.append('')
        lines.append(f"**Input Features (execution_time):** {format_feature_values(step['input_values_exec'])}")
        lines.append(f"**Input Features (start_time):** {format_feature_values(step['input_values_start'])}")
        lines.append('')
        lines.append(f"**Output:** predicted_startup_time={step['predicted_startup_time']:.2f}, predicted_total_time={step['predicted_total_time']:.2f}")
        lines.append('')

    lines.append('## Prediction Results')
    lines.append('')
    lines.append('| Node | Type | Actual ST | Actual RT | Pred ST | Pred RT | MRE ST (%) | MRE RT (%) |')
    lines.append('|------|------|-----------|-----------|---------|---------|------------|------------|')

    for step in steps:
        actual_st = step['actual_startup_time']
        actual_rt = step['actual_total_time']
        pred_st = step['predicted_startup_time']
        pred_rt = step['predicted_total_time']

        mre_st = abs(actual_st - pred_st) / actual_st * 100 if actual_st > 0 else 0
        mre_rt = abs(actual_rt - pred_rt) / actual_rt * 100 if actual_rt > 0 else 0

        lines.append(f"| {step['node_id']} | {step['node_type']} | {actual_st:.2f} | {actual_rt:.2f} | {pred_st:.2f} | {pred_rt:.2f} | {mre_st:.1f} | {mre_rt:.1f} |")

    lines.append('')

    with open(md_file, 'w') as f:
        f.write('\n'.join(lines))


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
    parser.add_argument("--output-file", help="Output CSV file for predictions")
    parser.add_argument("--md-query", help="Generate MD report for single query")
    parser.add_argument("--report", action="store_true", help="Generate MD report for first query of each unique plan")
    parser.add_argument("--report-dir", help="Output directory for MD reports (default: md/ in script dir)")

    args = parser.parse_args()

    run_prediction_workflow(args.test_file, args.overview_file, args.models_dir, args.output_file, args.md_query, args.report, args.report_dir)
