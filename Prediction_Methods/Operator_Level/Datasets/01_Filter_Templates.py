#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path

# ORCHESTRATOR
def cleanup_workflow(input_file, output_dir):
    df = load_data(input_file)
    templates_to_remove = ['Q2', 'Q11', 'Q16', 'Q22']
    df_filtered = filter_templates(df, templates_to_remove)
    export_data(df_filtered, output_dir)

# FUNCTIONS

# Load raw operator dataset from CSV file
def load_data(input_file):
    return pd.read_csv(input_file, delimiter=';')


# Remove operators belonging to specified templates
def filter_templates(df, templates_to_remove):
    return df[~df['query_file'].str.startswith(tuple(templates_to_remove))]


# Save filtered dataset to CSV file
def export_data(df, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    csv_path = output_path / '01_operator_dataset_cleaned.csv'
    df.to_csv(csv_path, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to input operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for cleaned dataset")

    args = parser.parse_args()

    cleanup_workflow(args.input_file, args.output_dir)
