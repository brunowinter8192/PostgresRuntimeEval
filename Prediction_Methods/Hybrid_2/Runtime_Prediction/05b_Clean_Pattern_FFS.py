#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from mapping_config import LEAF_OPERATORS

CHILD_SUFFIXES = ['_st1', '_rt1', '_st2', '_rt2']


# ORCHESTRATOR
def clean_pattern_ffs(input_file: str, output_file: str) -> None:
    df = load_overview(input_file)
    df_cleaned = remove_leaf_child_features(df)
    export_cleaned(df_cleaned, output_file)


# FUNCTIONS

# Load pattern FFS overview CSV
def load_overview(input_file: str) -> pd.DataFrame:
    return pd.read_csv(input_file, delimiter=';')


# Remove child features for leaf operators from final_features
def remove_leaf_child_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for idx, row in df.iterrows():
        final_features = row['final_features']
        if pd.isna(final_features) or final_features.strip() == '':
            continue

        features = [f.strip() for f in final_features.split(',')]
        filtered = filter_leaf_child_features(features)
        df.at[idx, 'final_features'] = ', '.join(filtered)
        df.at[idx, 'final_feature_count'] = len(filtered)

    return df


# Filter out child features belonging to leaf operators
def filter_leaf_child_features(features: list) -> list:
    filtered = []
    for feature in features:
        if not is_leaf_child_feature(feature):
            filtered.append(feature)
    return filtered


# Check if feature is a child feature of a leaf operator
def is_leaf_child_feature(feature: str) -> bool:
    if not any(feature.endswith(suffix) for suffix in CHILD_SUFFIXES):
        return False

    leaf_prefixes = [op.replace(' ', '') for op in LEAF_OPERATORS]

    for prefix in leaf_prefixes:
        if feature.startswith(prefix + '_') or f'_{prefix}_' in feature or feature.startswith(prefix + '_Outer_') or feature.startswith(prefix + '_Inner_'):
            return True

    return False


# Export cleaned overview to CSV
def export_cleaned(df: pd.DataFrame, output_file: str) -> None:
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Path to pattern_ffs_overview.csv')
    parser.add_argument('--output-file', required=True, help='Output path for cleaned CSV')
    args = parser.parse_args()

    clean_pattern_ffs(args.input_file, args.output_file)
