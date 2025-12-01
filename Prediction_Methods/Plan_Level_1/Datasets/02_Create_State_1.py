#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Feature mappings for State_1 transformation
from mapping_config import FEATURES_TO_REMOVE_FOR_STATE_1, get_state_1_columns


# ORCHESTRATOR

def transform_to_state_1(input_path: Path, output_path: Path) -> None:
    df = load_baseline_dataset(input_path)
    df_state_1 = remove_advanced_features(df)
    df_state_1 = reorder_columns(df_state_1)
    export_state_1_dataset(df_state_1, output_path)


# FUNCTIONS

# Load baseline complete dataset with semicolon delimiter
def load_baseline_dataset(input_path: Path) -> pd.DataFrame:
    return pd.read_csv(input_path, sep=';')


# Remove advanced features to create State_1 dataset
def remove_advanced_features(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(columns=FEATURES_TO_REMOVE_FOR_STATE_1)


# Reorder columns to match State_1 structure
def reorder_columns(df: pd.DataFrame) -> pd.DataFrame:
    state_1_cols = get_state_1_columns()
    return df[state_1_cols]


# Save State_1 dataset to CSV with semicolon delimiter
def export_state_1_dataset(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, sep=';')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Transform Baseline dataset to State_1 by removing advanced features'
    )
    parser.add_argument(
        'input_csv',
        nargs='?',
        default='../Data_Generation/csv/complete_dataset.csv',
        help='Path to baseline complete dataset (default: ../Data_Generation/csv/complete_dataset.csv)'
    )
    parser.add_argument(
        '--output-csv',
        default='State_1/complete_dataset.csv',
        help='Output path for State_1 complete dataset (default: State_1/complete_dataset.csv)'
    )

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    input_path = script_dir / args.input_csv
    output_path = script_dir / args.output_csv

    if not input_path.exists():
        sys.exit(1)

    transform_to_state_1(input_path, output_path)
