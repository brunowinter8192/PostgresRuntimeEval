#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))  # Plan_Level_1
# From mapping_config.py: Metadata columns and template column
from mapping_config import METADATA_COLUMNS, PLAN_METADATA


# ORCHESTRATOR

# Create template-feature constancy matrix showing value stability per template
def template_constancy_workflow(input_csv: Path, output_dir: Path) -> None:
    df = load_dataset(input_csv)
    df = validate_templates(df)
    feature_cols = get_feature_columns(df)
    templates = sorted(df[PLAN_METADATA[1]].unique())
    result_df = build_constancy_matrix(df, templates, feature_cols)
    export_matrix(result_df, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(input_csv: Path) -> pd.DataFrame:
    return pd.read_csv(input_csv, delimiter=';')


# Validate and clean template column
def validate_templates(df: pd.DataFrame) -> pd.DataFrame:
    if df[PLAN_METADATA[1]].isna().any():
        df = df.dropna(subset=[PLAN_METADATA[1]])
    return df


# Get feature columns excluding metadata
def get_feature_columns(df: pd.DataFrame) -> list:
    return [col for col in df.columns if col not in METADATA_COLUMNS]


# Build constancy percentage matrix for all templates and features
def build_constancy_matrix(df: pd.DataFrame, templates: list, feature_cols: list) -> pd.DataFrame:
    matrix_data = []

    for template in templates:
        template_df = df[df[PLAN_METADATA[1]] == template]
        row = {PLAN_METADATA[1]: template}

        for feature in feature_cols:
            constancy_pct = calculate_constancy_percentage(template_df[feature])
            row[feature] = constancy_pct

        matrix_data.append(row)

    result_df = pd.DataFrame(matrix_data)
    result_df = result_df.set_index(PLAN_METADATA[1])
    return result_df


# Calculate constancy percentage for a feature column
def calculate_constancy_percentage(series: pd.Series) -> float:
    if len(series) == 0:
        return np.nan

    unique_values = series.nunique()

    if unique_values == 1:
        return 100.0

    value_counts = series.value_counts()
    most_common_count = value_counts.iloc[0]
    total_count = len(series)

    percentage = (most_common_count / total_count) * 100

    return percentage


# Export constancy matrix to CSV with semicolon delimiter
def export_matrix(result_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f'08_template_feature_constancy_{timestamp}.csv'
    result_df.to_csv(output_file, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create template-feature constancy matrix")
    parser.add_argument("input_csv", help="Input CSV file with features and template column")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: script_dir/csv)")

    args = parser.parse_args()

    input_path = Path(args.input_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'csv'

    template_constancy_workflow(input_path, output_path)
