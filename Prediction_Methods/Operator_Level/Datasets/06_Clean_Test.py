#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path

# ORCHESTRATOR

# Coordinate workflow to remove child features from test dataset
def clean_test_workflow(test_file, output_dir):
    df = load_data(test_file)
    df_cleaned = remove_child_features(df)
    export_data(df_cleaned, output_dir)

# FUNCTIONS

# Load test dataset from CSV file
def load_data(test_file):
    return pd.read_csv(test_file, delimiter=';')


# Remove st1, rt1, st2, rt2 columns from dataset
def remove_child_features(df):
    child_features = ['st1', 'rt1', 'st2', 'rt2']
    existing_child_features = [f for f in child_features if f in df.columns]
    
    if existing_child_features:
        return df.drop(columns=existing_child_features)
    
    return df


# Save cleaned test dataset to CSV file
def export_data(df, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    csv_path = output_path / '06_test_cleaned.csv'
    df.to_csv(csv_path, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("test_file", help="Path to test dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for cleaned test dataset")

    args = parser.parse_args()

    clean_test_workflow(args.test_file, args.output_dir)
