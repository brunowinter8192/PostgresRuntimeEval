#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import numpy as np
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def order_patterns_workflow(occurrences_file: str, operator_predictions_file: str, output_dir: str) -> None:
    df = load_occurrences(occurrences_file)
    predictions = load_operator_predictions(operator_predictions_file)
    avg_mre_map = calculate_avg_mre(df, predictions)
    pattern_stats = aggregate_pattern_stats(df, avg_mre_map)
    df_by_size = sort_by_size(pattern_stats)
    df_by_frequency = sort_by_frequency(pattern_stats)
    export_ordered_patterns(df_by_size, df_by_frequency, output_dir)


# FUNCTIONS

# Load test pattern occurrences from 06 output
def load_occurrences(occurrences_file: str) -> pd.DataFrame:
    return pd.read_csv(occurrences_file, delimiter=';')


# Load operator predictions from CSV
def load_operator_predictions(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')


# Calculate avg_mre per pattern from operator predictions
def calculate_avg_mre(occurrences: pd.DataFrame, predictions: pd.DataFrame) -> dict:
    pred_lookup = {}
    for _, row in predictions.iterrows():
        if row['actual_total_time'] > 0:
            mre = abs(row['predicted_total_time'] - row['actual_total_time']) / row['actual_total_time']
            pred_lookup[(row['query_file'], row['node_id'])] = mre

    avg_mre_map = {}
    for pattern_hash in occurrences['pattern_hash'].unique():
        pattern_occs = occurrences[occurrences['pattern_hash'] == pattern_hash]
        mre_values = []
        for _, occ in pattern_occs.iterrows():
            key = (occ['query_file'], occ['root_node_id'])
            if key in pred_lookup:
                mre_values.append(pred_lookup[key])
        if mre_values:
            avg_mre_map[pattern_hash] = np.mean(mre_values)
    return avg_mre_map


# Aggregate pattern statistics by counting occurrences
def aggregate_pattern_stats(df: pd.DataFrame, avg_mre_map: dict) -> pd.DataFrame:
    stats = df.groupby('pattern_hash').agg({
        'pattern_string': 'first',
        'pattern_length': 'first',
        'operator_count': 'first',
        'query_file': 'count'
    }).reset_index()

    stats = stats.rename(columns={'query_file': 'occurrence_count'})
    stats['avg_mre'] = stats['pattern_hash'].map(avg_mre_map)
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
    parser.add_argument('--operator-predictions', required=True, help='Path to operator predictions CSV')
    parser.add_argument('--output-dir', required=True, help='Output directory for sorted pattern lists')
    args = parser.parse_args()

    order_patterns_workflow(args.occurrences_file, args.operator_predictions, args.output_dir)
