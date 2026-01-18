#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
from pathlib import Path


# ORCHESTRATOR
def calculate_avg_mre(pattern_hash: str, predictions_file: str, occurrences_file: str, output_dir: str, threshold: float) -> None:
    occurrences = load_occurrences(occurrences_file, pattern_hash)
    pred_lookup = build_pred_lookup(predictions_file)
    mre_values, details = collect_mre_values(occurrences, pred_lookup)
    avg_mre = np.mean(mre_values) if mre_values else 1.0
    status = 'SKIPPED_LOW_ERROR' if avg_mre < threshold else 'WOULD_EVALUATE'
    export_results(output_dir, pattern_hash, avg_mre, len(mre_values), threshold, status, details)


# FUNCTIONS

# Load pattern occurrences filtered by hash
def load_occurrences(occurrences_file: str, pattern_hash: str) -> pd.DataFrame:
    df = pd.read_csv(occurrences_file, delimiter=';')
    return df[df['pattern_hash'] == pattern_hash]


# Build MRE lookup from predictions
def build_pred_lookup(predictions_file: str) -> dict:
    df = pd.read_csv(predictions_file, delimiter=';')
    pred_lookup = {}
    for _, p in df.iterrows():
        key = (p['query_file'], p['node_id'])
        if p['actual_total_time'] > 0:
            mre = abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time']
            pred_lookup[key] = mre
    return pred_lookup


# Collect MRE values for pattern occurrences
def collect_mre_values(occurrences: pd.DataFrame, pred_lookup: dict) -> tuple:
    mre_values = []
    details = []
    for _, row in occurrences.iterrows():
        key = (row['query_file'], row['root_node_id'])
        template = row['query_file'].split('_')[0]
        if key in pred_lookup:
            mre = pred_lookup[key]
            mre_values.append(mre)
            details.append({'template': template, 'query_file': row['query_file'], 'root_node_id': row['root_node_id'], 'mre': mre})
    return mre_values, details


# Export results to CSV
def export_results(output_dir: str, pattern_hash: str, avg_mre: float, occurrence_count: int, threshold: float, status: str, details: list) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    short_hash = pattern_hash[:8]

    # Summary
    summary = pd.DataFrame([{
        'pattern_hash': pattern_hash,
        'avg_mre': avg_mre,
        'avg_mre_pct': avg_mre * 100,
        'occurrence_count': occurrence_count,
        'threshold': threshold,
        'status': status
    }])
    summary.to_csv(output_path / f'A_03d_{short_hash}_summary.csv', sep=';', index=False)

    # Details per template
    if details:
        df_details = pd.DataFrame(details)
        template_agg = df_details.groupby('template')['mre'].agg(['mean', 'count']).reset_index()
        template_agg.columns = ['template', 'avg_mre', 'count']
        template_agg['avg_mre_pct'] = template_agg['avg_mre'] * 100
        template_agg.to_csv(output_path / f'A_03d_{short_hash}_by_template.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pattern-hash', required=True, help='Pattern hash to analyze')
    parser.add_argument('--predictions', required=True, help='Path to predictions.csv')
    parser.add_argument('--occurrences', required=True, help='Path to 06_test_pattern_occurrences.csv')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    parser.add_argument('--threshold', type=float, default=0.1, help='Min error threshold (default: 0.1)')
    args = parser.parse_args()

    calculate_avg_mre(args.pattern_hash, args.predictions, args.occurrences, args.output_dir, args.threshold)
