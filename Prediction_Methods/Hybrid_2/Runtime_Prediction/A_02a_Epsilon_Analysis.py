#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
from pathlib import Path


# ORCHESTRATOR
def run_epsilon_analysis(selection_log_file: str, output_dir: str) -> None:
    df = load_selection_log(selection_log_file)
    stats = calculate_delta_stats(df)
    export_stats(stats, output_dir)


# FUNCTIONS

# Load selection log CSV
def load_selection_log(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')


# Calculate delta statistics for SELECTED patterns
def calculate_delta_stats(df: pd.DataFrame) -> dict:
    selected = df[df['status'] == 'SELECTED']
    deltas = selected['delta'].values

    return {
        'selected_count': len(selected),
        'mean_delta': np.mean(deltas),
        'median_delta': np.median(deltas),
        'min_delta': np.min(deltas),
        'max_delta': np.max(deltas)
    }


# Export delta statistics to CSV
def export_stats(stats: dict, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame([{
        'selected_count': stats['selected_count'],
        'mean_delta': stats['mean_delta'],
        'median_delta': stats['median_delta'],
        'min_delta': stats['min_delta'],
        'max_delta': stats['max_delta']
    }])

    df.to_csv(output_path / 'delta_stats.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('selection_log_file', help='Path to selection_log.csv')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    args = parser.parse_args()

    run_epsilon_analysis(args.selection_log_file, args.output_dir)
