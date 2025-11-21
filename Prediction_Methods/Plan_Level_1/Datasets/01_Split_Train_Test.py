#!/usr/bin/env python3
"""
Split complete dataset into training and test sets with stratification by template.

Split ratio: 120 training samples / 30 test samples per template (80/20 split)

Author: Auto-generated
Date: 2025-11-19
"""

import argparse
import os
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Dataset metadata and target definitions
from mapping_config import PLAN_METADATA, PLAN_TARGET


def validate_template_counts(df: pd.DataFrame, expected_count: int = 150) -> bool:
    """
    Validate that each template has exactly expected_count samples.

    Args:
        df: Input DataFrame with 'template' column
        expected_count: Expected number of samples per template

    Returns:
        True if all templates have expected count, False otherwise
    """
    template_counts = df['template'].value_counts()

    print(f"\nTemplate sample counts:")
    for template in sorted(template_counts.index):
        count = template_counts[template]
        status = "✓" if count == expected_count else "✗"
        print(f"  {status} {template}: {count} samples")

    if not all(template_counts == expected_count):
        print(f"\n✗ Error: Not all templates have exactly {expected_count} samples")
        return False

    print(f"\n✓ All templates have exactly {expected_count} samples")
    return True


def split_by_template(
    df: pd.DataFrame,
    train_size: int = 120,
    test_size: int = 30,
    random_seed: int = 42
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split dataset into training and test sets with stratification by template.

    Args:
        df: Input DataFrame with 'template' column
        train_size: Number of training samples per template
        test_size: Number of test samples per template
        random_seed: Random seed for reproducibility

    Returns:
        Tuple of (train_df, test_df)
    """
    train_dfs = []
    test_dfs = []

    for template in sorted(df['template'].unique()):
        template_df = df[df['template'] == template].copy()

        # Shuffle and split
        template_df = template_df.sample(frac=1, random_state=random_seed).reset_index(drop=True)

        train_df = template_df.iloc[:train_size]
        test_df = template_df.iloc[train_size:train_size + test_size]

        train_dfs.append(train_df)
        test_dfs.append(test_df)

        print(f"  Template {template}: {len(train_df)} train, {len(test_df)} test")

    train_combined = pd.concat(train_dfs, ignore_index=True)
    test_combined = pd.concat(test_dfs, ignore_index=True)

    return train_combined, test_combined


def main():
    """Main execution function."""
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

    # Resolve paths
    script_dir = Path(__file__).parent
    input_path = script_dir / args.input_csv
    output_dir = script_dir / args.output_dir

    # Validate input file
    if not input_path.exists():
        print(f"✗ Error: Input file not found: {input_path}")
        sys.exit(1)

    print(f"Loading dataset from: {input_path}")

    # Load dataset (semicolon-delimited from Data_Generation)
    df = pd.read_csv(input_path, sep=';')

    print(f"Total samples: {len(df)}")
    print(f"Total features: {len(df.columns) - len(PLAN_METADATA) - 1}")  # Exclude metadata + target
    print(f"Templates: {sorted(df['template'].unique())}")

    # Validate template counts
    expected_count = args.train_size + args.test_size
    if not validate_template_counts(df, expected_count):
        sys.exit(1)

    # Perform stratified split
    print(f"\nSplitting dataset ({args.train_size}/{args.test_size} per template, seed={args.seed}):")
    train_df, test_df = split_by_template(
        df,
        train_size=args.train_size,
        test_size=args.test_size,
        random_seed=args.seed
    )

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save to CSV (semicolon-delimited for consistency with Data_Generation and Runtime_Prediction)
    train_path = output_dir / 'training_data.csv'
    test_path = output_dir / 'test_data.csv'

    train_df.to_csv(train_path, index=False, sep=';')
    test_df.to_csv(test_path, index=False, sep=';')

    print(f"\n✓ Training data saved: {train_path} ({len(train_df)} samples)")
    print(f"✓ Test data saved: {test_path} ({len(test_df)} samples)")

    # Summary statistics
    train_ratio = len(train_df) / (len(train_df) + len(test_df)) * 100
    test_ratio = len(test_df) / (len(train_df) + len(test_df)) * 100

    print(f"\nSplit ratio: {train_ratio:.1f}% train / {test_ratio:.1f}% test")
    print(f"Templates in training set: {len(train_df['template'].unique())}")
    print(f"Templates in test set: {len(test_df['template'].unique())}")


if __name__ == '__main__':
    main()
