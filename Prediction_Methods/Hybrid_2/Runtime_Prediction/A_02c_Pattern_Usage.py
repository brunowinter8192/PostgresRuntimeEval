#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def analyze_pattern_usage(predictions_file: str, output_dir: str) -> None:
    df = load_predictions(predictions_file)
    pattern_rows = filter_pattern_predictions(df)
    usage_stats = calculate_usage_stats(pattern_rows)
    export_usage_stats(usage_stats, output_dir)


# FUNCTIONS

# Load predictions CSV
def load_predictions(predictions_file: str) -> pd.DataFrame:
    return pd.read_csv(predictions_file, delimiter=';')


# Filter rows where prediction_type is pattern
def filter_pattern_predictions(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['prediction_type'] == 'pattern']


# Calculate usage count and percentage per pattern
def calculate_usage_stats(pattern_rows: pd.DataFrame) -> pd.DataFrame:
    total_pattern_predictions = len(pattern_rows)
    usage = pattern_rows.groupby('pattern_hash').size().reset_index(name='usage_count')
    usage['percentage'] = (usage['usage_count'] / total_pattern_predictions * 100).round(2)
    usage = usage.sort_values('usage_count', ascending=False).reset_index(drop=True)
    return usage


# Export usage statistics to CSV
def export_usage_stats(usage_stats: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    usage_stats.to_csv(output_path / 'pattern_usage.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('predictions_file', help='Path to predictions.csv')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    args = parser.parse_args()

    analyze_pattern_usage(args.predictions_file, args.output_dir)
