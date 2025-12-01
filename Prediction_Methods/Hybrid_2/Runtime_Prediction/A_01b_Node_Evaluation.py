#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

# ORCHESTRATOR

# Evaluate predictions split by prediction type
def evaluate_cross_predictions(predictions_file, output_dir):
    df = load_predictions(predictions_file)
    df = add_template_column(df)
    df = calculate_mre_metrics(df)
    df_pattern = filter_by_prediction_type(df, 'pattern')
    df_operator = filter_by_prediction_type(df, 'operator')
    pattern_total, pattern_startup = create_pivot_tables(df_pattern)
    operator_total, operator_startup = create_pivot_tables(df_operator)
    overall_total, overall_startup = create_pivot_tables(df)
    export_results(pattern_total, pattern_startup, operator_total, operator_startup, overall_total, overall_startup, output_dir)

# FUNCTIONS

# Load predictions from CSV file
def load_predictions(predictions_file):
    return pd.read_csv(predictions_file, delimiter=';')

# Add template column to dataframe
def add_template_column(df):
    df['template'] = df['query_file'].apply(extract_template)
    return df

# Extract template ID from query filename
def extract_template(query_file):
    return query_file.split('_')[0]

# Calculate MRE metrics for both targets
def calculate_mre_metrics(df):
    df['mre_total'] = np.abs(df['predicted_total_time'] - df['actual_total_time']) / df['actual_total_time']
    df['mre_total_pct'] = df['mre_total'] * 100
    df['mre_startup'] = np.abs(df['predicted_startup_time'] - df['actual_startup_time']) / df['actual_startup_time']
    df['mre_startup_pct'] = df['mre_startup'] * 100
    return df

# Filter dataframe by prediction type
def filter_by_prediction_type(df, prediction_type):
    return df[df['prediction_type'] == prediction_type].copy()

# Create pivot tables for node_type × template
def create_pivot_tables(df):
    cross_total = df.pivot_table(
        values='mre_total_pct',
        index='node_type',
        columns='template',
        aggfunc='mean'
    ).round(2)
    cross_startup = df.pivot_table(
        values='mre_startup_pct',
        index='node_type',
        columns='template',
        aggfunc='mean'
    ).round(2)
    return cross_total, cross_startup

# Export all six pivot tables to CSV
def export_results(pattern_total, pattern_startup, operator_total, operator_startup, overall_total, overall_startup, output_dir):
    output_path = Path(output_dir) / 'csv'
    output_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    pattern_total.index.name = 'node_type (Pattern Mean MRE Total Time %)'
    output_file = output_path / f'pattern_mean_mre_total_pct_{timestamp}.csv'
    pattern_total.to_csv(output_file, sep=';')
    
    pattern_startup.index.name = 'node_type (Pattern Mean MRE Startup Time %)'
    output_file = output_path / f'pattern_mean_mre_startup_pct_{timestamp}.csv'
    pattern_startup.to_csv(output_file, sep=';')
    
    operator_total.index.name = 'node_type (Operator Mean MRE Total Time %)'
    output_file = output_path / f'operator_mean_mre_total_pct_{timestamp}.csv'
    operator_total.to_csv(output_file, sep=';')
    
    operator_startup.index.name = 'node_type (Operator Mean MRE Startup Time %)'
    output_file = output_path / f'operator_mean_mre_startup_pct_{timestamp}.csv'
    operator_startup.to_csv(output_file, sep=';')
    
    overall_total.index.name = 'node_type (Mean MRE Total Time %)'
    output_file = output_path / f'node_type_mean_mre_total_pct_{timestamp}.csv'
    overall_total.to_csv(output_file, sep=';')
    
    overall_startup.index.name = 'node_type (Mean MRE Startup Time %)'
    output_file = output_path / f'node_type_mean_mre_startup_pct_{timestamp}.csv'
    overall_startup.to_csv(output_file, sep=';')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cross-evaluation split by prediction type')
    parser.add_argument('predictions_file', help='Path to predictions.csv')
    parser.add_argument('--output-dir', required=True, help='Path to Evaluation directory')
    args = parser.parse_args()

    evaluate_cross_predictions(args.predictions_file, args.output_dir)
