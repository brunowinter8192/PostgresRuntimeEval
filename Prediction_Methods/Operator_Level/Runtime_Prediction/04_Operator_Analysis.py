#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime


# ORCHESTRATOR

def main(predictions_csv, output_dir):
    df = load_predictions(predictions_csv)
    df = add_template_column(df)
    df = calculate_mre_metrics(df)
    cross_total, cross_startup = create_pivot_tables(df)
    export_results(cross_total, cross_startup, output_dir)


# FUNCTIONS

# Load predictions from CSV file
def load_predictions(predictions_csv):
    return pd.read_csv(predictions_csv, delimiter=';')


# Add template column extracted from query filename
def add_template_column(df):
    df['template'] = df['query_file'].apply(extract_template)
    return df


# Extract template ID from query filename
def extract_template(query_file):
    return query_file.split('_')[0]


# Calculate mean relative error metrics
def calculate_mre_metrics(df):
    df['mre_total'] = np.abs(df['predicted_total_time'] - df['actual_total_time']) / df['actual_total_time']
    df['mre_total_pct'] = df['mre_total'] * 100
    df['mre_startup'] = np.abs(df['predicted_startup_time'] - df['actual_startup_time']) / df['actual_startup_time']
    df['mre_startup_pct'] = df['mre_startup'] * 100
    return df


# Create cross-tabulation pivot tables
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


# Export pivot tables to CSV files
def export_results(cross_total, cross_startup, output_dir):
    output_path = Path(output_dir) / 'Evaluation'
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    cross_total.index.name = 'node_type (Mean MRE Total Time %)'
    output_file_total = output_path / f'node_type_mean_mre_total_pct_{timestamp}.csv'
    cross_total.to_csv(output_file_total, sep=';')

    cross_startup.index.name = 'node_type (Mean MRE Startup Time %)'
    output_file_startup = output_path / f'node_type_mean_mre_startup_pct_{timestamp}.csv'
    cross_startup.to_csv(output_file_startup, sep=';')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions_csv", help="Path to predictions CSV file")
    parser.add_argument("--output-dir", required=True, help="Output directory for evaluation results")
    args = parser.parse_args()

    main(args.predictions_csv, args.output_dir)
