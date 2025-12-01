#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Metadata column names for stratification
from mapping_config import PLAN_METADATA


# ORCHESTRATOR

def split_train_test_workflow(input_path: Path, output_dir: Path, train_size: int, test_size: int, seed: int) -> None:
    df = load_dataset(input_path)
    validate_template_counts(df, train_size + test_size)
    train_df, test_df = split_by_template(df, train_size, test_size, seed)
    export_splits(train_df, test_df, output_dir)


# FUNCTIONS

# Load complete dataset with semicolon delimiter
def load_dataset(input_path: Path) -> pd.DataFrame:
    if not input_path.exists():
        sys.exit(1)
    return pd.read_csv(input_path, sep=';')


# Validate each template has expected sample count
def validate_template_counts(df: pd.DataFrame, expected_count: int) -> None:
    template_counts = df[PLAN_METADATA[1]].value_counts()
    if not all(template_counts == expected_count):
        sys.exit(1)


# Split dataset with stratification by template
def split_by_template(df: pd.DataFrame, train_size: int, test_size: int, random_seed: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    train_dfs = []
    test_dfs = []

    for template in sorted(df[PLAN_METADATA[1]].unique()):
        template_df = df[df[PLAN_METADATA[1]] == template].copy()
        template_df = template_df.sample(frac=1, random_state=random_seed).reset_index(drop=True)
        train_dfs.append(template_df.iloc[:train_size])
        test_dfs.append(template_df.iloc[train_size:train_size + test_size])

    return pd.concat(train_dfs, ignore_index=True), pd.concat(test_dfs, ignore_index=True)


# Export training and test datasets to CSV
def export_splits(train_df: pd.DataFrame, test_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    train_df.to_csv(output_dir / 'training_data.csv', index=False, sep=';')
    test_df.to_csv(output_dir / 'test_data.csv', index=False, sep=';')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Split complete dataset into stratified train/test sets'
    )
    parser.add_argument(
        'input_csv',
        nargs='?',
        default='../Data_Generation/csv/complete_dataset.csv',
        help='Path to input CSV file (default: ../Data_Generation/csv/complete_dataset.csv)'
    )
    parser.add_argument(
        '--output-dir',
        default='Baseline',
        help='Output directory for train/test CSV files (default: Baseline)'
    )
    parser.add_argument(
        '--train-size',
        type=int,
        default=120,
        help='Number of training samples per template (default: 120)'
    )
    parser.add_argument(
        '--test-size',
        type=int,
        default=30,
        help='Number of test samples per template (default: 30)'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
        help='Random seed for reproducibility (default: 42)'
    )

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    input_path = script_dir / args.input_csv
    output_dir = script_dir / args.output_dir

    split_train_test_workflow(input_path, output_dir, args.train_size, args.test_size, args.seed)
