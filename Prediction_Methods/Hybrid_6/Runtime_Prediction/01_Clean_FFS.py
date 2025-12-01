#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime


# ORCHESTRATOR
def clean_ffs_workflow(ffs_csv: str, pattern_plan_leafs_csv: str, output_dir: str) -> None:
    ffs_df = load_ffs_data(ffs_csv)
    plan_leaf_mapping = load_pattern_plan_leaf_mapping(pattern_plan_leafs_csv)
    cleaned_df = clean_pattern_plan_leaf_features(ffs_df, plan_leaf_mapping)
    export_cleaned_ffs(cleaned_df, output_dir)


# FUNCTIONS

# Load FFS overview from CSV
def load_ffs_data(ffs_csv: str) -> pd.DataFrame:
    return pd.read_csv(ffs_csv, delimiter=';')

# Load pattern plan leaf mapping from 04_Identify_Pattern_Plan_Leafs.py output
def load_pattern_plan_leaf_mapping(pattern_plan_leafs_csv: str) -> dict:
    df = pd.read_csv(pattern_plan_leafs_csv, delimiter=';')

    mapping = {}
    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']
        prefix = row['pattern_leaf_prefix']
        is_plan_leaf = row['is_plan_leaf'] == 'ja'

        if pattern_hash not in mapping:
            mapping[pattern_hash] = {}

        mapping[pattern_hash][prefix] = is_plan_leaf

    return mapping

# Clean child features from pattern+plan leaf operators
def clean_pattern_plan_leaf_features(ffs_df: pd.DataFrame, plan_leaf_mapping: dict) -> pd.DataFrame:
    cleaned_rows = []

    for _, row in ffs_df.iterrows():
        pattern_hash = row['pattern']
        final_features = row['final_features']

        if pd.isna(final_features) or pattern_hash not in plan_leaf_mapping:
            cleaned_rows.append(row)
            continue

        feature_list = [f.strip() for f in final_features.split(',')]
        cleaned_features = remove_plan_leaf_child_features(
            feature_list, pattern_hash, plan_leaf_mapping
        )

        cleaned_row = row.copy()
        cleaned_row['final_features'] = ', '.join(cleaned_features)
        cleaned_row['final_feature_count'] = len(cleaned_features)
        cleaned_rows.append(cleaned_row)

    return pd.DataFrame(cleaned_rows)

# Remove child features from pattern leafs that are also plan leafs
def remove_plan_leaf_child_features(features: list, pattern_hash: str, plan_leaf_mapping: dict) -> list:
    pattern_mapping = plan_leaf_mapping[pattern_hash]
    cleaned_features = []

    for feature in features:
        if should_remove_feature(feature, pattern_mapping):
            continue
        cleaned_features.append(feature)

    return cleaned_features

# Check if feature should be removed (child feature of pattern+plan leaf)
def should_remove_feature(feature: str, pattern_mapping: dict) -> bool:
    child_suffixes = ['_rt1', '_rt2', '_st1', '_st2']

    for suffix in child_suffixes:
        if feature.endswith(suffix):
            prefix = feature[:-len(suffix)]

            for pattern_leaf_prefix in pattern_mapping.keys():
                if prefix.endswith(pattern_leaf_prefix):
                    if pattern_mapping[pattern_leaf_prefix]:
                        return True

    return False

# Export cleaned FFS to CSV with timestamp
def export_cleaned_ffs(cleaned_df: pd.DataFrame, output_dir: str) -> None:
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = csv_dir / f'01_cleaned_ffs_{timestamp}.csv'

    cleaned_df.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("ffs_csv", help="Path to FFS overview CSV (e.g., two_step_evaluation_overview.csv)")
    parser.add_argument("pattern_plan_leafs_csv", help="Path to 04_pattern_plan_leafs_*.csv from Data_Generation")
    parser.add_argument("--output-dir", required=True, help="Output directory for cleaned FFS")
    args = parser.parse_args()

    clean_ffs_workflow(args.ffs_csv, args.pattern_plan_leafs_csv, args.output_dir)
