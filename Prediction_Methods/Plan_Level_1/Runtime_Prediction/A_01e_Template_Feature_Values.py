#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path

import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))  # Plan_Level_1
# From mapping_config.py: Template column name
from mapping_config import PLAN_METADATA


# ORCHESTRATOR

# Create template-feature value matrix showing constant values per template
def template_values_workflow(input_csv: Path, output_dir: Path, features_file: Path) -> None:
    df = load_dataset(input_csv)
    df = exclude_q9(df)
    feature_cols = load_selected_features(features_file)
    templates = sorted(df[PLAN_METADATA[1]].unique())
    result_df = build_value_matrix(df, templates, feature_cols)
    export_matrix(result_df, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(input_csv: Path) -> pd.DataFrame:
    return pd.read_csv(input_csv, delimiter=';')


# Exclude Q9 due to plan variability
def exclude_q9(df: pd.DataFrame) -> pd.DataFrame:
    return df[df[PLAN_METADATA[1]] != 'Q9']


# Load selected features from FFS summary CSV
def load_selected_features(features_file: Path) -> list:
    ffs_df = pd.read_csv(features_file, delimiter=';')
    features_str = ffs_df['selected_features'].iloc[0]
    return [f.strip() for f in features_str.split(',')]


# Build value matrix for all templates and features
def build_value_matrix(df: pd.DataFrame, templates: list, feature_cols: list) -> pd.DataFrame:
    matrix_data = []

    for template in templates:
        template_df = df[df[PLAN_METADATA[1]] == template]
        row = {PLAN_METADATA[1]: template}

        for feature in feature_cols:
            row[feature] = template_df[feature].iloc[0]

        matrix_data.append(row)

    result_df = pd.DataFrame(matrix_data)
    result_df = result_df.set_index(PLAN_METADATA[1])
    return result_df


# Export value matrix to CSV with semicolon delimiter
def export_matrix(result_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / 'A_01e_template_feature_values.csv'
    result_df.to_csv(output_file, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create template-feature value matrix")
    parser.add_argument("input_csv", help="Input CSV file with features and template column")
    parser.add_argument("--features-file", required=True, help="FFS summary CSV with selected_features column")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: script_dir/csv)")

    args = parser.parse_args()

    input_path = Path(args.input_csv)
    features_path = Path(args.features_file)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'csv'

    template_values_workflow(input_path, output_path, features_path)
