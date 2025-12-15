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

# Analyze feature sparsity (zero values)
def sparsity_analysis_workflow(input_csv: Path, output_dir: Path) -> None:
    df = load_dataset(input_csv)
    feature_cols = get_feature_columns(df)
    X = df[feature_cols]
    zero_df = analyze_zeros(X)
    export_analysis(zero_df, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(input_csv: Path) -> pd.DataFrame:
    return pd.read_csv(input_csv, delimiter=';')


# Get feature columns excluding metadata
def get_feature_columns(df: pd.DataFrame) -> list:
    return [col for col in df.columns if col not in METADATA_COLUMNS]


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


# Export sparsity analysis to CSV with semicolon delimiter
def export_analysis(zero_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zero_file = output_dir / f'A_01c_feature_sparsity_{timestamp}.csv'
    zero_df.to_csv(zero_file, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze feature sparsity (zero counts)")
    parser.add_argument("input_csv", help="Input CSV file with features")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: script_dir/csv)")

    args = parser.parse_args()

    input_path = Path(args.input_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'csv'

    sparsity_analysis_workflow(input_path, output_path)
