#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


STRATEGIES = ['Frequency_Baseline', 'Frequency_Epsilon', 'Size_Baseline',
              'Size_Epsilon', 'Error_Baseline', 'Error_Epsilon']


# ORCHESTRATOR
def analyze_pattern_usage(evaluation_dir: str, selection_dir: str, output_dir: str) -> None:
    predictions = load_all_predictions(evaluation_dir)
    usage_table = build_usage_table(predictions)
    selected_counts = load_selected_counts(selection_dir)
    summary = build_summary(usage_table, selected_counts)
    export_usage_table(usage_table, output_dir)
    export_summary(summary, output_dir)


# FUNCTIONS

# Scan evaluation directory for all predictions.csv files
def load_all_predictions(evaluation_dir: str) -> dict:
    eval_path = Path(evaluation_dir)
    predictions = {}

    for strategy in ['Frequency', 'Size', 'Error']:
        for config in ['Baseline', 'Epsilon']:
            pred_file = eval_path / strategy / config / 'predictions.csv'
            if pred_file.exists():
                key = f"{strategy}_{config}"
                df = pd.read_csv(pred_file, delimiter=';')
                predictions[key] = df[df['prediction_type'] == 'pattern']

    return predictions


# Build cross-strategy usage table
def build_usage_table(predictions: dict) -> pd.DataFrame:
    all_hashes = set()
    usage_counts = {}

    for key, df in predictions.items():
        counts = df.groupby('pattern_hash').size().to_dict()
        usage_counts[key] = counts
        all_hashes.update(counts.keys())

    rows = []
    for pattern_hash in sorted(all_hashes):
        row = {'pattern_hash': pattern_hash}
        count = 0
        for col in STRATEGIES:
            if col in usage_counts and pattern_hash in usage_counts[col]:
                row[col] = usage_counts[col][pattern_hash]
                count += 1
            else:
                row[col] = ''
        row['count'] = count
        rows.append(row)

    return pd.DataFrame(rows, columns=['pattern_hash'] + STRATEGIES + ['count'])


# Load selected pattern counts from Pattern_Selection directory
def load_selected_counts(selection_dir: str) -> dict:
    sel_path = Path(selection_dir)
    counts = {}

    for strategy in ['Frequency', 'Size', 'Error']:
        for config in ['Baseline', 'Epsilon']:
            sel_file = sel_path / strategy / config / 'selected_patterns.csv'
            key = f"{strategy}_{config}"
            if sel_file.exists():
                df = pd.read_csv(sel_file, delimiter=';')
                counts[key] = len(df)
            else:
                counts[key] = 0

    return counts


# Build summary comparing selected vs used patterns
def build_summary(usage_table: pd.DataFrame, selected_counts: dict) -> pd.DataFrame:
    rows = []

    for strategy in STRATEGIES:
        selected = selected_counts.get(strategy, 0)
        used = usage_table[strategy].apply(lambda x: x != '').sum()
        beifang = selected - used

        rows.append({
            'strategy': strategy,
            'selected': selected,
            'used': used,
            'beifang': beifang
        })

    return pd.DataFrame(rows)


# Export usage table to CSV
def export_usage_table(usage_table: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    usage_table.to_csv(output_path / 'A_02c_patterns.csv', sep=';', index=False)


# Export summary to CSV
def export_summary(summary: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    summary.to_csv(output_path / 'A_02c_summary.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('evaluation_dir', help='Path to Evaluation directory')
    parser.add_argument('--selection-dir', required=True, help='Path to Pattern_Selection directory')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    args = parser.parse_args()

    analyze_pattern_usage(args.evaluation_dir, args.selection_dir, args.output_dir)
