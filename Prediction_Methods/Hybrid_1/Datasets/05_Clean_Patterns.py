#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import json
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Leaf operators and suffix constants
from mapping_config import LEAF_OPERATORS, CHILD_ACTUAL_SUFFIXES, CHILD_TIMING_SUFFIXES, PARENT_CHILD_FEATURES


# ORCHESTRATOR
def clean_pattern_training_data(patterns_dir: str) -> None:
    patterns_path = Path(patterns_dir) / 'patterns'
    if not patterns_path.exists():
        return
    pattern_folders = get_pattern_folders(patterns_path)
    process_all_patterns(pattern_folders)


# FUNCTIONS

# Get all pattern folders
def get_pattern_folders(patterns_path):
    return [d for d in patterns_path.iterdir() if d.is_dir()]


# Load pattern info from JSON file
def load_pattern_info(pattern_folder):
    info_file = pattern_folder / 'pattern_info.json'
    if not info_file.exists():
        return None
    with open(info_file, 'r') as f:
        return json.load(f)


# Process all pattern folders
def process_all_patterns(pattern_folders):
    for pattern_folder in pattern_folders:
        aggregated_file = pattern_folder / 'training_aggregated.csv'

        if not aggregated_file.exists():
            continue

        pattern_info = load_pattern_info(pattern_folder)
        if pattern_info is None:
            continue

        df = load_aggregated_data(aggregated_file)
        parent_prefix = identify_parent_prefix(df)
        columns_to_remove = identify_columns_to_remove(df, parent_prefix)
        df_cleaned = remove_columns(df, columns_to_remove)

        export_cleaned_data(df_cleaned, pattern_folder)

# Load aggregated training data from CSV
def load_aggregated_data(file_path):
    return pd.read_csv(file_path, delimiter=';')

# Identify parent operator prefix from column names
def identify_parent_prefix(df):
    for col in df.columns:
        if col.endswith('_actual_startup_time') and '_Outer_' not in col and '_Inner_' not in col:
            return col.replace('_actual_startup_time', '')
    return None

# Identify all columns to remove based on suffix and prefix rules
def identify_columns_to_remove(df, parent_prefix):
    columns_to_remove = []

    for col in df.columns:
        if any(col.endswith(suffix) for suffix in CHILD_ACTUAL_SUFFIXES):
            columns_to_remove.append(col)

    if parent_prefix:
        for suffix in PARENT_CHILD_FEATURES:
            col = f'{parent_prefix}{suffix}'
            if col in df.columns:
                columns_to_remove.append(col)

    for col in df.columns:
        if any(col.endswith(suffix) for suffix in CHILD_TIMING_SUFFIXES):
            is_leaf_operator = any(col.startswith(f'{leaf_op}_') for leaf_op in LEAF_OPERATORS)
            if is_leaf_operator:
                columns_to_remove.append(col)

    return columns_to_remove


# Remove specified columns from dataframe
def remove_columns(df, columns_to_remove):
    existing_cols = [c for c in columns_to_remove if c in df.columns]
    return df.drop(columns=existing_cols)

# Export cleaned data to pattern folder
def export_cleaned_data(df, pattern_folder):
    output_file = pattern_folder / 'training_cleaned.csv'
    df.to_csv(output_file, sep=';', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("patterns_dir", help="Base directory containing patterns subfolder")
    args = parser.parse_args()

    clean_pattern_training_data(args.patterns_dir)
