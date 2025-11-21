#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime

# ORCHESTRATOR

# Execute operator runtime analysis workflow
def analyze_operator_runtimes(input_file, output_dir):
    df = load_operator_data(input_file)
    df_main = filter_main_plan(df)
    stats = calculate_operator_statistics(df_main)
    stats_ranked = rank_by_total_time(stats)
    export_analysis(stats_ranked, output_dir)

# FUNCTIONS

# Load operator dataset from CSV
def load_operator_data(input_file):
    return pd.read_csv(input_file, delimiter=';')

# Filter to main plan operators only
def filter_main_plan(df):
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]

# Calculate statistics per operator type
def calculate_operator_statistics(df):
    stats_list = []
    for node_type in df['node_type'].unique():
        df_op = df[df['node_type'] == node_type]
        stats_list.append({
            'node_type': node_type,
            'count': len(df_op),
            'mean_total_ms': df_op['actual_total_time'].mean(),
            'std_total_ms': df_op['actual_total_time'].std(),
            'min_total_ms': df_op['actual_total_time'].min(),
            'max_total_ms': df_op['actual_total_time'].max(),
            'mean_startup_ms': df_op['actual_startup_time'].mean(),
            'std_startup_ms': df_op['actual_startup_time'].std(),
            'min_startup_ms': df_op['actual_startup_time'].min(),
            'max_startup_ms': df_op['actual_startup_time'].max(),
            'startup_total_ratio': (df_op['actual_startup_time'] / df_op['actual_total_time']).mean()
        })
    return pd.DataFrame(stats_list)

# Rank operators by mean total time descending
def rank_by_total_time(df_stats):
    return df_stats.sort_values('mean_total_ms', ascending=False).reset_index(drop=True)

# Export analysis results to CSV
def export_analysis(df_stats, output_dir):
    output_path = Path(output_dir) / 'csv'
    output_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'operator_runtime_analysis_{timestamp}.csv'
    df_stats.to_csv(output_path / filename, sep=';', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Path to operator dataset CSV')
    parser.add_argument('--output-dir', required=True, help='Output directory for analysis results')
    args = parser.parse_args()

    analyze_operator_runtimes(args.input, args.output_dir)
