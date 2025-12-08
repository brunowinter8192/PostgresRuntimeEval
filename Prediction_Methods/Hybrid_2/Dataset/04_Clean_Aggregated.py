#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def clean_aggregated_datasets(pattern_leafs_csv: str, patterns_base_dir: str) -> None:
    pattern_leaf_features = load_pattern_leaf_features(pattern_leafs_csv)
    for pattern_hash, allowed_features in pattern_leaf_features.items():
        clean_pattern_dataset(patterns_base_dir, pattern_hash, allowed_features)


# FUNCTIONS

# Load pattern leaf features from 03_Extract_Pattern_Leafs.py output
def load_pattern_leaf_features(pattern_leafs_csv: str) -> dict:
    df = pd.read_csv(pattern_leafs_csv, delimiter=';')
    pattern_features = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']
        leaf_prefixes_str = row['leaf_prefixes']

        if pd.isna(leaf_prefixes_str) or leaf_prefixes_str == '':
            pattern_features[pattern_hash] = []
            continue

        leaf_prefixes = leaf_prefixes_str.split(',')
        timing_features = []

        for prefix in leaf_prefixes:
            timing_features.extend([
                f'{prefix}_st1',
                f'{prefix}_rt1',
                f'{prefix}_st2',
                f'{prefix}_rt2'
            ])

        pattern_features[pattern_hash] = timing_features

    return pattern_features


# Clean single pattern dataset by removing non-leaf timing features
def clean_pattern_dataset(patterns_base_dir: str, pattern_hash: str, allowed_features: list) -> None:
    pattern_dir = Path(patterns_base_dir) / pattern_hash
    aggregated_file = pattern_dir / 'training_aggregated.csv'

    if not aggregated_file.exists():
        return

    df = load_aggregated_data(aggregated_file)
    df_cleaned = remove_non_leaf_timing_features(df, allowed_features)
    export_cleaned_data(df_cleaned, pattern_dir)


# Load aggregated pattern dataset
def load_aggregated_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')


# Remove all timing features except pattern leaf features
def remove_non_leaf_timing_features(df: pd.DataFrame, allowed_features: list) -> pd.DataFrame:
    all_timing_cols = identify_all_timing_columns(df)
    cols_to_drop = identify_columns_to_drop(all_timing_cols, allowed_features)
    return df.drop(columns=cols_to_drop)


# Identify all timing columns in dataset
def identify_all_timing_columns(df: pd.DataFrame) -> list:
    timing_suffixes = ['_st1', '_rt1', '_st2', '_rt2']
    timing_cols = []

    for col in df.columns:
        if any(col.endswith(suffix) for suffix in timing_suffixes):
            timing_cols.append(col)

    return timing_cols


# Identify which timing columns should be dropped
def identify_columns_to_drop(all_timing_cols: list, allowed_features: list) -> list:
    allowed_set = set(allowed_features)
    cols_to_drop = []

    for col in all_timing_cols:
        if col not in allowed_set:
            cols_to_drop.append(col)

    return cols_to_drop


# Save cleaned dataset
def export_cleaned_data(df: pd.DataFrame, pattern_dir: Path) -> None:
    output_file = pattern_dir / 'training_cleaned.csv'
    df.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern_leafs_csv", help="Path to 03_pattern_leafs_*.csv")
    parser.add_argument("patterns_dir", help="Base directory containing pattern subdirectories (Dataset/Patterns/)")
    args = parser.parse_args()

    clean_aggregated_datasets(args.pattern_leafs_csv, args.patterns_dir)
