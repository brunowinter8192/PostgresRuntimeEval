#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def analyze_operator_ranges(input_file: str, output_dir: str) -> None:
    df = load_dataset(input_file)
    df = add_template_column(df)
    stats = compute_operator_statistics(df)
    stats = add_template_extremes(stats, df)
    stats = compute_range_metrics(stats)
    export_results(stats, output_dir)


# FUNCTIONS

# Load operator dataset from CSV
def load_dataset(input_file: str) -> pd.DataFrame:
    return pd.read_csv(input_file, delimiter=';')


# Extract template name from query file and add as column
def add_template_column(df: pd.DataFrame) -> pd.DataFrame:
    df['template'] = df['query_file'].apply(lambda x: x.split('_')[0])
    return df


# Compute mean, min, max statistics per operator
def compute_operator_statistics(df: pd.DataFrame) -> pd.DataFrame:
    stats = df.groupby('node_type').agg({
        'actual_startup_time': ['mean', 'min', 'max', 'count'],
        'actual_total_time': ['mean', 'min', 'max']
    }).reset_index()

    stats.columns = ['node_type', 'mean_startup_ms', 'min_startup_ms', 'max_startup_ms', 'count',
                     'mean_total_ms', 'min_total_ms', 'max_total_ms']
    return stats


# Add template information for min/max values
def add_template_extremes(stats: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
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


# Calculate range metrics for startup and total times
def compute_range_metrics(stats: pd.DataFrame) -> pd.DataFrame:
    stats['startup_range_ms'] = stats['max_startup_ms'] - stats['min_startup_ms']
    stats['startup_range_pct'] = (stats['startup_range_ms'] / stats['min_startup_ms']) * 100
    stats['total_range_ms'] = stats['max_total_ms'] - stats['min_total_ms']
    stats['total_range_pct'] = (stats['total_range_ms'] / stats['min_total_ms']) * 100
    stats = stats.round(2)
    stats = stats.sort_values('total_range_ms', ascending=False)
    return stats


# Export operator range analysis to CSV
def export_results(stats: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    output_file = output_path / 'A_01c_operator_range_analysis.csv'
    stats.to_csv(output_file, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for analysis results")
    args = parser.parse_args()

    analyze_operator_ranges(args.input_file, args.output_dir)
