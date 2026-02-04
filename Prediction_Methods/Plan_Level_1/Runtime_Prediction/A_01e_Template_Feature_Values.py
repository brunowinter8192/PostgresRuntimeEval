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

# Create template-feature value matrix or single-template comparison
def template_values_workflow(input_csv: Path, output_dir: Path, features_file: Path, template: str = None) -> None:
    df = load_dataset(input_csv)
    df = split_q9_variants(df)
    feature_cols = load_selected_features(features_file)
    templates = sorted(df[PLAN_METADATA[1]].unique())

    if template:
        result_df = build_comparison(df, templates, feature_cols, template)
        export_comparison(result_df, output_dir, template)
    else:
        result_df = build_value_matrix(df, templates, feature_cols)
        export_matrix(result_df, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(input_csv: Path) -> pd.DataFrame:
    return pd.read_csv(input_csv, delimiter=';')


# Split Q9 into plan variants Q9_A and Q9_B based on op_count
def split_q9_variants(df: pd.DataFrame) -> pd.DataFrame:
    q9_mask = df[PLAN_METADATA[1]] == 'Q9'
    q9 = df[q9_mask]
    op_counts = sorted(q9['op_count'].unique())
    df.loc[q9_mask & (df['op_count'] == op_counts[0]), PLAN_METADATA[1]] = 'Q9_A'
    df.loc[q9_mask & (df['op_count'] == op_counts[1]), PLAN_METADATA[1]] = 'Q9_B'
    return df


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


# Filter features that are constant (1 unique value) in the target template
def filter_constant_features(df: pd.DataFrame, feature_cols: list, template: str) -> list:
    target_df = df[df[PLAN_METADATA[1]] == template]
    return [f for f in feature_cols if target_df[f].nunique() == 1]


# Build comparison for a single template: value and shared_by count
def build_comparison(df: pd.DataFrame, templates: list, feature_cols: list, template: str) -> pd.DataFrame:
    constant_cols = filter_constant_features(df, feature_cols, template)
    target_df = df[df[PLAN_METADATA[1]] == template]
    others_df = df[df[PLAN_METADATA[1]] != template]
    rows = []

    for feature in constant_cols:
        value = target_df[feature].iloc[0]
        shared_by = others_df[others_df[feature] == value][PLAN_METADATA[1]].nunique()
        rows.append({'feature': feature, 'value': value, 'shared_by': shared_by})

    return pd.DataFrame(rows)


# Export single-template comparison to CSV
def export_comparison(result_df: pd.DataFrame, output_dir: Path, template: str) -> None:
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / f'A_01e_{template}_feature_comparison.csv'
    result_df.to_csv(output_file, sep=';', index=False)


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
    parser.add_argument("--template", default=None, help="Target template for comparison (e.g. Q18)")

    args = parser.parse_args()

    input_path = Path(args.input_csv)
    features_path = Path(args.features_file)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'csv'

    template_values_workflow(input_path, output_path, features_path, args.template)
