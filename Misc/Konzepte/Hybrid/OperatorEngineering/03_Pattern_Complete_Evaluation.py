#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

# ORCHESTRATOR

# Analyze pattern predictions with complete pattern names
def analyze_pattern_complete_mre(predictions_file, operator_dataset, output_dir):
    df_predictions = load_pattern_predictions(predictions_file)
    df_operators = load_operator_dataset(operator_dataset)
    df_with_patterns = reconstruct_pattern_names(df_predictions, df_operators)
    df_with_mre = calculate_pattern_mre(df_with_patterns)
    pivot_execution, pivot_startup = create_pivot_tables(df_with_mre)
    export_results(pivot_execution, pivot_startup, output_dir)

# FUNCTIONS

# Load predictions and filter for pattern predictions only
def load_pattern_predictions(predictions_file):
    df = pd.read_csv(predictions_file, delimiter=';')
    return df[df['prediction_type'] == 'pattern'].copy()

# Load operator dataset for pattern reconstruction
def load_operator_dataset(operator_dataset):
    return pd.read_csv(operator_dataset, delimiter=';')

# Reconstruct complete pattern names for each prediction
def reconstruct_pattern_names(df_predictions, df_operators):
    pattern_names = []

    for _, pred_row in df_predictions.iterrows():
        query_file = pred_row['query_file']
        node_id = pred_row['node_id']
        node_type = pred_row['node_type']
        depth = pred_row['depth']

        parent_row = df_operators[
            (df_operators['query_file'] == query_file) &
            (df_operators['node_id'] == node_id)
        ]

        if len(parent_row) == 0:
            pattern_names.append('UNKNOWN')
            continue

        parent_row = parent_row.iloc[0]
        children = get_children_info(df_operators, query_file, node_id, depth)
        pattern_name = build_pattern_key(node_type, children)
        pattern_names.append(pattern_name)

    df_predictions['pattern_name'] = pattern_names
    return df_predictions

# Get children information for operator
def get_children_info(df_operators, query_file, parent_node_id, parent_depth):
    df_query = df_operators[df_operators['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
    parent_idx_list = df_query[df_query['node_id'] == parent_node_id].index.tolist()

    if len(parent_idx_list) == 0:
        return []

    parent_idx = parent_idx_list[0]
    children = []

    for idx in range(parent_idx + 1, len(df_query)):
        row = df_query.iloc[idx]
        if row['depth'] == parent_depth + 1:
            children.append({
                'node_type': row['node_type'],
                'parent_relationship': row['parent_relationship']
            })
        elif row['depth'] <= parent_depth:
            break

    return children

# Build pattern key from operator and children
def build_pattern_key(parent_type, children_info):
    parent_normalized = parent_type.replace(' ', '_')

    if len(children_info) == 0:
        return parent_normalized

    if len(children_info) == 1:
        child_normalized = children_info[0]['node_type'].replace(' ', '_')
        relationship = children_info[0]['parent_relationship']
        return f"{parent_normalized}_{child_normalized}_{relationship}"

    if len(children_info) == 2:
        children_sorted = sorted(children_info, key=lambda x: (0 if x['parent_relationship'] == 'Outer' else 1))
        outer_normalized = children_sorted[0]['node_type'].replace(' ', '_')
        inner_normalized = children_sorted[1]['node_type'].replace(' ', '_')
        return f"{parent_normalized}_{outer_normalized}_Outer_{inner_normalized}_Inner"

    return 'UNKNOWN_PATTERN'

# Calculate MRE for execution_time and start_time
def calculate_pattern_mre(df_predictions):
    df_predictions['mre_execution_time'] = (
        abs(df_predictions['actual_total_time'] - df_predictions['predicted_total_time']) /
        df_predictions['actual_total_time'] * 100
    )

    df_predictions['mre_start_time'] = (
        abs(df_predictions['actual_startup_time'] - df_predictions['predicted_startup_time']) /
        df_predictions['actual_startup_time'] * 100
    )

    df_predictions['template'] = df_predictions['query_file'].str.split('_').str[0]
    return df_predictions

# Create pivot tables for execution_time and start_time
def create_pivot_tables(df_predictions):
    grouped_execution = df_predictions.groupby(['pattern_name', 'template'])['mre_execution_time'].mean().reset_index()
    pivot_execution = grouped_execution.pivot(index='pattern_name', columns='template', values='mre_execution_time')

    grouped_startup = df_predictions.groupby(['pattern_name', 'template'])['mre_start_time'].mean().reset_index()
    pivot_startup = grouped_startup.pivot(index='pattern_name', columns='template', values='mre_start_time')

    template_order = ['Q1', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9']
    existing_cols_execution = [col for col in template_order if col in pivot_execution.columns]
    pivot_execution = pivot_execution[existing_cols_execution]

    existing_cols_startup = [col for col in template_order if col in pivot_startup.columns]
    pivot_startup = pivot_startup[existing_cols_startup]

    return pivot_execution, pivot_startup

# Export results to CSV files
def export_results(pivot_execution, pivot_startup, output_dir):
    output_path = Path(output_dir) / 'csv'
    output_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    filename_execution = f'pattern_complete_mean_mre_execution_time_pct_{timestamp}.csv'
    pivot_execution.to_csv(output_path / filename_execution, sep=';')

    filename_startup = f'pattern_complete_mean_mre_start_time_pct_{timestamp}.csv'
    pivot_startup.to_csv(output_path / filename_startup, sep=';')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('predictions_file', help='Path to predictions.csv')
    parser.add_argument('operator_dataset', help='Path to operator_dataset.csv')
    parser.add_argument('--output-dir', required=True, help='Output directory for analysis results')
    args = parser.parse_args()

    analyze_pattern_complete_mre(args.predictions_file, args.operator_dataset, args.output_dir)
