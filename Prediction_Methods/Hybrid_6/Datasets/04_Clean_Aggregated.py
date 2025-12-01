#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

# From mapping_config.py: Pattern leaf timing features mapping
from mapping_config import PATTERNS, PATTERN_LEAF_TIMING_FEATURES


# ORCHESTRATOR
def clean_aggregated_datasets(dataset_base_dir: str) -> None:
    for pattern_hash in PATTERNS:
        clean_pattern_dataset(dataset_base_dir, pattern_hash)


# FUNCTIONS

# Clean single pattern dataset by removing non-leaf timing features
def clean_pattern_dataset(dataset_base_dir: str, pattern_hash: str) -> None:
    pattern_dir = Path(dataset_base_dir) / pattern_hash
    aggregated_file = pattern_dir / 'training_aggregated.csv'

    if not aggregated_file.exists():
        return

    df = load_aggregated_data(aggregated_file)
    allowed_timing_features = PATTERN_LEAF_TIMING_FEATURES.get(pattern_hash, [])
    df_cleaned = remove_non_leaf_timing_features(df, allowed_timing_features)
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
    parser.add_argument("dataset_base_dir", help="Base directory containing pattern subdirectories (e.g., Baseline/)")
    args = parser.parse_args()

    clean_aggregated_datasets(args.dataset_base_dir)
