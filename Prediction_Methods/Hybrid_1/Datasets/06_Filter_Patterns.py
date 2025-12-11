#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def filter_patterns_workflow(mining_csv: str, approach_csv: str, output_dir: str, threshold: int) -> None:
    df_mining = load_mining_data(mining_csv)
    df_approach = load_approach_data(approach_csv)
    df_filtered = apply_threshold_filter(df_mining, df_approach, threshold)
    export_filtered_patterns(df_filtered, output_dir)


# FUNCTIONS

# Load pattern mining data with occurrence counts
def load_mining_data(mining_csv: str) -> pd.DataFrame:
    return pd.read_csv(mining_csv, delimiter=';')


# Load approach patterns.csv with already filtered hashes
def load_approach_data(approach_csv: str) -> pd.DataFrame:
    return pd.read_csv(approach_csv, delimiter=';')


# Filter by threshold and return matching approach rows
def apply_threshold_filter(df_mining: pd.DataFrame, df_approach: pd.DataFrame, threshold: int) -> pd.DataFrame:
    if threshold > 0:
        valid_hashes = set(df_mining[df_mining['occurrence_count'] > threshold]['pattern_hash'].tolist())
        return df_approach[df_approach['pattern_hash'].isin(valid_hashes)]
    else:
        return df_approach


# Export filtered patterns
def export_filtered_patterns(df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / 'patterns_filtered.csv'
    df.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("mining_csv", help="Path to Data_Generation pattern mining CSV")
    parser.add_argument("approach_csv", help="Path to approach patterns.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for patterns_filtered.csv")
    parser.add_argument("--threshold", type=int, default=150, help="Occurrence threshold (default: 150)")
    args = parser.parse_args()

    filter_patterns_workflow(args.mining_csv, args.approach_csv, args.output_dir, args.threshold)
