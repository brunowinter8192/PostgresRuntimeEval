#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
from pathlib import Path


# ORCHESTRATOR
def calculate_error_baseline(
    pattern_occurrences_file: str,
    operator_predictions_file: str,
    patterns_metadata_file: str,
    output_dir: str
) -> None:
    occurrences = load_pattern_occurrences(pattern_occurrences_file)
    predictions = load_operator_predictions(operator_predictions_file)
    metadata = load_patterns_metadata(patterns_metadata_file)
    pred_lookup = build_prediction_lookup(predictions)
    error_ranking = calculate_pattern_errors(occurrences, pred_lookup, metadata)
    export_error_baseline(error_ranking, output_dir)


# FUNCTIONS

# Load pattern occurrences from CSV
def load_pattern_occurrences(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')


# Load operator predictions from CSV
def load_operator_predictions(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')


# Load patterns metadata for pattern_string, pattern_length, operator_count
def load_patterns_metadata(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')


# Build lookup dict (query_file, node_id) -> MRE
def build_prediction_lookup(predictions: pd.DataFrame) -> dict:
    lookup = {}
    for _, row in predictions.iterrows():
        if row['actual_total_time'] > 0:
            mre = abs(row['predicted_total_time'] - row['actual_total_time']) / row['actual_total_time']
            lookup[(row['query_file'], row['node_id'])] = mre
    return lookup


# Calculate error scores for all patterns
def calculate_pattern_errors(
    occurrences: pd.DataFrame,
    pred_lookup: dict,
    metadata: pd.DataFrame
) -> pd.DataFrame:
    metadata_dict = {}
    for _, row in metadata.iterrows():
        metadata_dict[row['pattern_hash']] = {
            'pattern_string': row['pattern_string'],
            'pattern_length': row['pattern_length'],
            'operator_count': row['operator_count'],
            'unique_template_count': row.get('unique_template_count', 1)
        }

    results = []
    for pattern_hash in occurrences['pattern_hash'].unique():
        pattern_occs = occurrences[occurrences['pattern_hash'] == pattern_hash]
        mre_values = []

        for _, occ in pattern_occs.iterrows():
            key = (occ['query_file'], occ['root_node_id'])
            if key in pred_lookup:
                mre_values.append(pred_lookup[key])

        if mre_values:
            avg_mre = np.mean(mre_values)
            occurrence_count = len(pattern_occs)
            error_score = occurrence_count * avg_mre

            meta = metadata_dict.get(pattern_hash, {})
            results.append({
                'pattern_hash': pattern_hash,
                'pattern_string': meta.get('pattern_string', ''),
                'pattern_length': meta.get('pattern_length', 0),
                'operator_count': meta.get('operator_count', 0),
                'occurrence_count': occurrence_count,
                'unique_template_count': meta.get('unique_template_count', 1),
                'avg_mre': avg_mre,
                'avg_mre_pct': avg_mre * 100,
                'error_score': error_score
            })

    df = pd.DataFrame(results)
    return df.sort_values(
        by=['error_score', 'pattern_hash'],
        ascending=[False, True]
    ).reset_index(drop=True)


# Export error baseline to CSV
def export_error_baseline(error_ranking: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    error_ranking.to_csv(output_path / '08_patterns_by_error.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern_occurrences_file', help='Path to 06_test_pattern_occurrences_*.csv')
    parser.add_argument('operator_predictions_file', help='Path to Evaluation/Operator_Training_Test/predictions.csv')
    parser.add_argument('patterns_metadata_file', help='Path to 07_patterns_by_frequency.csv')
    parser.add_argument('--output-dir', required=True, help='Output directory (Selected_Patterns/)')
    args = parser.parse_args()

    calculate_error_baseline(
        args.pattern_occurrences_file,
        args.operator_predictions_file,
        args.patterns_metadata_file,
        args.output_dir
    )
