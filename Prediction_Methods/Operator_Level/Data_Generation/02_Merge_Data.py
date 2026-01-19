#!/usr/bin/env python3

# INFRASTRUCTURE
import pandas as pd
import argparse
from pathlib import Path

# ORCHESTRATOR
def merge_features_and_targets(features_csv, targets_csv, output_dir):
    df_features = load_features(features_csv)
    df_targets = load_targets(targets_csv)

    validate_row_counts(df_features, df_targets)

    df_merged = merge_datasets(df_features, df_targets)

    validate_merge_result(df_features, df_merged)

    export_merged_dataset(df_merged, output_dir)

# FUNCTIONS

# Load features CSV with semicolon delimiter
def load_features(features_csv):
    return pd.read_csv(features_csv, delimiter=';')

# Load targets CSV with semicolon delimiter
def load_targets(targets_csv):
    return pd.read_csv(targets_csv, delimiter=';')

# Validate that features and targets have same row count
def validate_row_counts(df_features, df_targets):
    if len(df_features) != len(df_targets):
        raise ValueError(f"Row count mismatch: features={len(df_features)}, targets={len(df_targets)}")

# Merge features and targets on query_file and node_id
def merge_datasets(df_features, df_targets):
    return pd.merge(
        df_features,
        df_targets[['query_file', 'node_id', 'actual_startup_time', 'actual_total_time']],
        on=['query_file', 'node_id'],
        how='inner'
    )

# Validate that merge preserved row count
def validate_merge_result(df_features, df_merged):
    if len(df_merged) != len(df_features):
        raise ValueError(f"Merge row count mismatch: expected={len(df_features)}, got={len(df_merged)}")

# Export merged dataset to CSV with semicolon delimiter
def export_merged_dataset(df_merged, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    csv_path = output_path / '02_operator_dataset.csv'

    df_merged.to_csv(csv_path, index=False, sep=';')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--features-csv", required=True, help="Path to features CSV file")
    parser.add_argument("--targets-csv", required=True, help="Path to targets CSV file")
    parser.add_argument("--output-dir", required=True, help="Output directory for merged CSV")

    args = parser.parse_args()

    merge_features_and_targets(
        features_csv=args.features_csv,
        targets_csv=args.targets_csv,
        output_dir=args.output_dir
    )
