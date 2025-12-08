#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from datetime import datetime
from pathlib import Path

import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))  # Plan_Level_1
# From mapping_config.py: Metadata columns to exclude
from mapping_config import METADATA_COLUMNS


# ORCHESTRATOR

# Analyze feature outliers and zero values
def outlier_analysis_workflow(input_csv: Path, output_dir: Path) -> None:
    df = load_dataset(input_csv)
    feature_cols = get_feature_columns(df)
    X = df[feature_cols]
    outlier_df = analyze_outliers(X, df)
    zero_df = analyze_zeros(X)
    export_analyses(outlier_df, zero_df, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(input_csv: Path) -> pd.DataFrame:
    return pd.read_csv(input_csv, delimiter=';')


# Get feature columns excluding metadata
def get_feature_columns(df: pd.DataFrame) -> list:
    return [col for col in df.columns if col not in METADATA_COLUMNS]


# Analyze outliers using IQR method
def analyze_outliers(X: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    outlier_rows = []

    for col in X.columns:
        Q1 = X[col].quantile(0.25)
        Q3 = X[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outlier_mask = (X[col] < lower) | (X[col] > upper)
        outliers_total = outlier_mask.sum()

        if outliers_total > 0:
            outlier_templates = df[outlier_mask]['template']
            template_counts = outlier_templates.value_counts()

            dominant_template = template_counts.idxmax()
            dominant_count = template_counts.max()

            pct = outliers_total / len(X) * 100
            outlier_rows.append({
                'feature': col,
                'outlier_count': outliers_total,
                'outlier_percent': pct,
                'Q1': Q1,
                'Q3': Q3,
                'IQR': IQR,
                'lower_bound': lower,
                'upper_bound': upper,
                'template': dominant_template,
                'template_outlier_count': dominant_count
            })

    if outlier_rows:
        return pd.DataFrame(outlier_rows).sort_values('outlier_percent', ascending=False)
    else:
        return pd.DataFrame(outlier_rows)


# Analyze zero values per feature
def analyze_zeros(X: pd.DataFrame) -> pd.DataFrame:
    zero_rows = []

    for col in X.columns:
        zero_count = (X[col] == 0).sum()
        zero_pct = zero_count / len(X) * 100
        zero_rows.append({
            'feature': col,
            'zero_count': zero_count,
            'zero_percent': zero_pct
        })

    return pd.DataFrame(zero_rows).sort_values('zero_count', ascending=False)


# Export outlier and zero analyses to CSV with semicolon delimiter
def export_analyses(outlier_df: pd.DataFrame, zero_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    outlier_file = output_dir / f'A_01c_feature_outliers_{timestamp}.csv'
    outlier_df.to_csv(outlier_file, sep=';', index=False)

    zero_file = output_dir / f'A_01c_feature_zeros_{timestamp}.csv'
    zero_df.to_csv(zero_file, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze feature outliers and zero values")
    parser.add_argument("input_csv", help="Input CSV file with features")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: script_dir/csv)")

    args = parser.parse_args()

    input_path = Path(args.input_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'csv'

    outlier_analysis_workflow(input_path, output_path)
