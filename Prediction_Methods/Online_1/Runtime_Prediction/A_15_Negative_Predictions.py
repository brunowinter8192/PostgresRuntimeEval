#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path

STRATEGIES = ['Size', 'Frequency', 'Error']


# ORCHESTRATOR
def negative_predictions_workflow(evaluation_dir: str, output_dir: str) -> None:
    all_negatives = collect_negatives(evaluation_dir)
    summary = build_summary(all_negatives)
    export_results(all_negatives, summary, output_dir)


# FUNCTIONS

# Collect all negative predictions across strategies
def collect_negatives(evaluation_dir: str) -> pd.DataFrame:
    rows = []
    for strategy in STRATEGIES:
        strategy_dir = Path(evaluation_dir) / strategy
        for query_dir in sorted(strategy_dir.iterdir()):
            pred_file = query_dir / 'csv' / 'predictions.csv'
            if not pred_file.exists():
                continue
            df = pd.read_csv(pred_file, delimiter=';')
            neg = df[(df['predicted_total_time'] < 0) | (df['predicted_startup_time'] < 0)]
            for _, row in neg.iterrows():
                rows.append({
                    'strategy': strategy,
                    'template': row['query_file'].split('_')[0],
                    'query_file': row['query_file'],
                    'node_id': row['node_id'],
                    'node_type': row['node_type'],
                    'depth': row['depth'],
                    'prediction_type': row['prediction_type'],
                    'actual_total_time': row['actual_total_time'],
                    'predicted_total_time': row['predicted_total_time'],
                    'actual_startup_time': row['actual_startup_time'],
                    'predicted_startup_time': row['predicted_startup_time']
                })
    return pd.DataFrame(rows)


# Build summary per strategy with counts by node_type
def build_summary(all_negatives: pd.DataFrame) -> pd.DataFrame:
    if all_negatives.empty:
        return pd.DataFrame()
    summary = all_negatives.groupby(['strategy', 'node_type']).agg(
        count=('node_id', 'size'),
        templates=('template', lambda x: ','.join(sorted(x.unique())))
    ).reset_index()
    return summary


# Export detail and summary CSVs
def export_results(all_negatives: pd.DataFrame, summary: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    all_negatives.to_csv(output_path / 'A_15_negative_predictions.csv', sep=';', index=False)
    if not summary.empty:
        summary.to_csv(output_path / 'A_15_negative_summary.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("evaluation_dir", help="Path to Evaluation directory")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    negative_predictions_workflow(args.evaluation_dir, args.output_dir)
