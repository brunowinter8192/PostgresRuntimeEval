#!/usr/bin/env python3

import sys
import pandas as pd
from pathlib import Path


# Coordinate workflow for InitPlan and SubPlan analysis
def analyze_workflow(input_file, output_dir):
    df = load_data(input_file)
    summary_df = analyze_initplan_subplan(df)
    export_results(summary_df, output_dir)


# Load operator dataset from CSV file
def load_data(input_file):
    return pd.read_csv(input_file, delimiter=';')


# Analyze operators with InitPlan or SubPlan parent relationships
def analyze_initplan_subplan(df):
    init_sub_df = df[df['parent_relationship'].isin(['InitPlan', 'SubPlan'])]
    
    if len(init_sub_df) == 0:
        return pd.DataFrame()
    
    init_sub_df = init_sub_df.copy()
    init_sub_df['template'] = init_sub_df['query_file'].str.extract(r'^(Q\d+)_')
    
    summary_df = init_sub_df.groupby('template').agg({
        'node_id': 'count',
        'parent_relationship': lambda x: ', '.join(sorted(x.unique()))
    }).reset_index()
    
    summary_df.columns = ['template', 'operator_count', 'plan_types']
    
    return summary_df


# Save analysis summary to CSV file
def export_results(summary_df, output_dir):
    output_path = Path(output_dir) / '00_InitSub_Templates.csv'
    summary_df.to_csv(output_path, index=False, sep=';')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_directory = sys.argv[2]
    
    analyze_workflow(input_csv, output_directory)
