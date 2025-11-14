#!/usr/bin/env python3
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import sys

OUTPUT_DIR_NAME = 'csv'

def main(dataset_csv):
    df = load_dataset(dataset_csv)
    df = add_template_column(df)
    stats = calculate_operator_stats(df)
    stats = add_template_extremes(stats, df)
    stats = calculate_ranges(stats)
    stats = sort_by_total_range(stats)
    export_results(stats, dataset_csv)

def load_dataset(dataset_csv):
    return pd.read_csv(dataset_csv, delimiter=';')

def add_template_column(df):
    df['template'] = df['query_file'].apply(extract_template)
    return df

def extract_template(query_file):
    return query_file.split('_')[0]

def calculate_operator_stats(df):
    stats = df.groupby('node_type').agg({
        'actual_startup_time': ['mean', 'min', 'max', 'count'],
        'actual_total_time': ['mean', 'min', 'max']
    }).reset_index()
    
    stats.columns = ['node_type', 'mean_startup_ms', 'min_startup_ms', 'max_startup_ms', 'count',
                     'mean_total_ms', 'min_total_ms', 'max_total_ms']
    return stats

def add_template_extremes(stats, df):
    template_min_startup = df.loc[df.groupby('node_type')['actual_startup_time'].idxmin(), 
                                   ['node_type', 'template']]
    template_min_startup.columns = ['node_type', 'template_min_startup']
    
    template_max_startup = df.loc[df.groupby('node_type')['actual_startup_time'].idxmax(), 
                                   ['node_type', 'template']]
    template_max_startup.columns = ['node_type', 'template_max_startup']
    
    template_min_total = df.loc[df.groupby('node_type')['actual_total_time'].idxmin(), 
                                 ['node_type', 'template']]
    template_min_total.columns = ['node_type', 'template_min_total']
    
    template_max_total = df.loc[df.groupby('node_type')['actual_total_time'].idxmax(), 
                                 ['node_type', 'template']]
    template_max_total.columns = ['node_type', 'template_max_total']
    
    stats = stats.merge(template_min_startup, on='node_type')
    stats = stats.merge(template_max_startup, on='node_type')
    stats = stats.merge(template_min_total, on='node_type')
    stats = stats.merge(template_max_total, on='node_type')
    
    return stats

def calculate_ranges(stats):
    stats['startup_range_ms'] = stats['max_startup_ms'] - stats['min_startup_ms']
    stats['startup_range_pct'] = (stats['startup_range_ms'] / stats['min_startup_ms']) * 100
    stats['total_range_ms'] = stats['max_total_ms'] - stats['min_total_ms']
    stats['total_range_pct'] = (stats['total_range_ms'] / stats['min_total_ms']) * 100
    return stats.round(2)

def sort_by_total_range(stats):
    return stats.sort_values('total_range_ms', ascending=False)

def export_results(stats, dataset_csv):
    output_dir = Path(dataset_csv).parent.parent / 'Runtime_Prediction/Baseline_SVM/Evaluation' / OUTPUT_DIR_NAME
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = output_dir / f'operator_range_analysis_{timestamp}.csv'
    stats.to_csv(output_file, index=False, sep=';')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(1)
    main(sys.argv[1])
