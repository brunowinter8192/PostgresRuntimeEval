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

# Analyze feature correlations and identify highly correlated pairs
def correlation_analysis_workflow(input_csv: Path, output_dir: Path, threshold: float) -> None:
    df = load_dataset(input_csv)
    feature_cols = get_feature_columns(df)
    X = df[feature_cols]
    high_corr_pairs = find_high_correlations(X, threshold)
    export_correlations(high_corr_pairs, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(input_csv: Path) -> pd.DataFrame:
    return pd.read_csv(input_csv, delimiter=';')


# Get feature columns excluding metadata
def get_feature_columns(df: pd.DataFrame) -> list:
    return [col for col in df.columns if col not in METADATA_COLUMNS]


# Find highly correlated feature pairs above threshold
def find_high_correlations(X: pd.DataFrame, threshold: float) -> list:
    corr = X.corr().abs()

    high_corr = []
    for i in range(len(corr.columns)):
        for j in range(i + 1, len(corr.columns)):
            if corr.iloc[i, j] > threshold:
                high_corr.append({
                    'feature_1': corr.columns[i],
                    'feature_2': corr.columns[j],
                    'correlation': corr.iloc[i, j]
                })

    return high_corr


# Export high correlations to CSV with semicolon delimiter
def export_correlations(high_corr_pairs: list, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    high_corr_file = output_dir / f'05_feature_correlations_{timestamp}.csv'
    pd.DataFrame(high_corr_pairs).to_csv(high_corr_file, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze feature correlations")
    parser.add_argument("input_csv", help="Input CSV file with features")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: script_dir/csv)")
    parser.add_argument("--threshold", type=float, default=0.95, help="Correlation threshold (default: 0.95)")

    args = parser.parse_args()

    input_path = Path(args.input_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'csv'

    correlation_analysis_workflow(input_path, output_path, args.threshold)
