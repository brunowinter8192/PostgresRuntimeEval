#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def order_patterns_workflow(occurrences_file: str, output_dir: str) -> None:
    df = load_occurrences(occurrences_file)
    pattern_stats = aggregate_pattern_stats(df)
    df_by_size = sort_by_size(pattern_stats)
    df_by_frequency = sort_by_frequency(pattern_stats)
    export_ordered_patterns(df_by_size, df_by_frequency, output_dir)


# FUNCTIONS

# Load test pattern occurrences from 06 output
def load_occurrences(occurrences_file: str) -> pd.DataFrame:
    return pd.read_csv(occurrences_file, delimiter=';')


# Aggregate pattern statistics by counting occurrences
def aggregate_pattern_stats(df: pd.DataFrame) -> pd.DataFrame:
    stats = df.groupby('pattern_hash').agg({
        'pattern_string': 'first',
        'pattern_length': 'first',
        'operator_count': 'first',
        'query_file': 'count'
    }).reset_index()

    stats = stats.rename(columns={'query_file': 'occurrence_count'})
    return stats


# Sort patterns by size strategy (operator_count ASC, occurrence_count DESC, hash ASC)
def sort_by_size(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(
        by=['operator_count', 'occurrence_count', 'pattern_hash'],
        ascending=[True, False, True]
    ).reset_index(drop=True)


# Sort patterns by frequency strategy (occurrence_count DESC, operator_count ASC, hash ASC)
def sort_by_frequency(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(
        by=['occurrence_count', 'operator_count', 'pattern_hash'],
        ascending=[False, True, True]
    ).reset_index(drop=True)


# Export sorted pattern lists to CSV files
def export_ordered_patterns(df_by_size: pd.DataFrame, df_by_frequency: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    df_by_size.to_csv(output_path / '07_patterns_by_size.csv', sep=';', index=False)
    df_by_frequency.to_csv(output_path / '07_patterns_by_frequency.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('occurrences_file', help='Path to 06_test_pattern_occurrences_*.csv')
    parser.add_argument('--output-dir', required=True, help='Output directory for sorted pattern lists')
    args = parser.parse_args()

    order_patterns_workflow(args.occurrences_file, args.output_dir)
