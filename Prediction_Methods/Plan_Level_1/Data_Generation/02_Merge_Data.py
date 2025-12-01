#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Metadata column names for merge operations
from mapping_config import PLAN_METADATA


# ORCHESTRATOR

# Merge runtime, plan features, and row features into complete dataset
def merge_data_workflow(csv_dir: Path) -> None:
    runtimes = load_runtimes(csv_dir)
    plan_features = load_plan_features(csv_dir)
    row_features = load_row_features(csv_dir)
    merged = merge_all_features(runtimes, plan_features, row_features)
    export_merged_dataset(merged, csv_dir)


# FUNCTIONS

# Load runtime measurements from CSV
def load_runtimes(csv_dir: Path) -> pd.DataFrame:
    return pd.read_csv(csv_dir / '01a_runtimes.csv', delimiter=';')


# Load plan-level features from CSV
def load_plan_features(csv_dir: Path) -> pd.DataFrame:
    return pd.read_csv(csv_dir / '01b_plan_features.csv', delimiter=';')


# Load row and byte count features from CSV
def load_row_features(csv_dir: Path) -> pd.DataFrame:
    return pd.read_csv(csv_dir / '01c_row_features.csv', delimiter=';')


# Merge all feature sets on metadata columns
def merge_all_features(runtimes: pd.DataFrame, plan_features: pd.DataFrame, row_features: pd.DataFrame) -> pd.DataFrame:
    merged = plan_features.merge(row_features, on=PLAN_METADATA, how='inner')
    merged = merged.merge(runtimes[PLAN_METADATA + ['runtime']], on=PLAN_METADATA, how='inner')
    return merged


# Export merged dataset to CSV with semicolon delimiter
def export_merged_dataset(df: pd.DataFrame, csv_dir: Path) -> None:
    csv_path = csv_dir / 'complete_dataset.csv'
    df.to_csv(csv_path, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge runtime, plan features, and row features into complete dataset")
    parser.add_argument("csv_dir", help="Directory containing 01a_runtimes.csv, 01b_plan_features.csv, 01c_row_features.csv")

    args = parser.parse_args()

    csv_path = Path(args.csv_dir)

    merge_data_workflow(csv_path)
