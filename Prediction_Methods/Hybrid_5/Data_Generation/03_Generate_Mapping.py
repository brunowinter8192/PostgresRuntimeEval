#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def generate_mapping(leaf_csv: str, output_dir: str) -> None:
    df = load_leaf_data(leaf_csv)
    mapping_code = build_mapping_dict(df)
    export_mapping(mapping_code, output_dir)


# FUNCTIONS

# Load pattern leaf data from 02a_Extract_Pattern_Leafs.py output
def load_leaf_data(leaf_csv: str) -> pd.DataFrame:
    return pd.read_csv(leaf_csv, delimiter=';')

# Build mapping dictionary
def build_mapping_dict(df: pd.DataFrame) -> dict:
    mapping = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']
        leaf_prefixes = row['leaf_prefixes'].split(',') if pd.notna(row['leaf_prefixes']) and row['leaf_prefixes'] else []

        timing_features = []
        for prefix in leaf_prefixes:
            for suffix in ['st1', 'rt1', 'st2', 'rt2']:
                timing_features.append(f"{prefix}_{suffix}")

        mapping[pattern_hash] = timing_features

    return mapping

# Export mapping as Python code to file
def export_mapping(mapping: dict, output_dir: str) -> None:
    output_path = Path(output_dir) / 'mapping_addition.txt'

    lines = [
        "# Pattern leaf timing features to retain during cleaning",
        "# Generated from Data_Generation/csv/02a_pattern_leafs_*.csv",
        "# Format: {hash: [list of timing feature column names]}",
        "PATTERN_LEAF_TIMING_FEATURES = {"
    ]

    for pattern_hash, features in mapping.items():
        if features:
            features_str = ", ".join([f"'{f}'" for f in features])
            lines.append(f"    '{pattern_hash}': [{features_str}],")
        else:
            lines.append(f"    '{pattern_hash}': [],")

    lines.append("}")

    output_path.write_text('\n'.join(lines) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("leaf_csv", help="Path to 02a_pattern_leafs_*.csv from Data_Generation")
    parser.add_argument("--output-dir", required=True, help="Output directory for mapping file")
    args = parser.parse_args()

    generate_mapping(args.leaf_csv, args.output_dir)
