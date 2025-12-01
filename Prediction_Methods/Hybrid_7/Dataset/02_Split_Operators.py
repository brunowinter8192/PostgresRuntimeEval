#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# From mapping_config.py: Get operator folder names
from mapping_config import OPERATOR_CSV_TO_FOLDER


# ORCHESTRATOR

def split_operators(input_file: str, output_dir: str) -> None:
    df = load_data(input_file)
    operators_found = get_unique_operators(df)
    for operator_csv, operator_folder in OPERATOR_CSV_TO_FOLDER.items():
        if operator_csv in operators_found:
            export_operator_data(df, operator_csv, operator_folder, output_dir)


# FUNCTIONS

# Load operator dataset with semicolon delimiter
def load_data(input_file: str) -> pd.DataFrame:
    return pd.read_csv(input_file, delimiter=';')

# Get unique operator types from dataset
def get_unique_operators(df: pd.DataFrame) -> set:
    return set(df['node_type'].unique())

# Export data for single operator type
def export_operator_data(df: pd.DataFrame, operator_csv: str, operator_folder: str, output_dir: str) -> None:
    operator_df = df[df['node_type'] == operator_csv]
    output_path = Path(output_dir) / operator_folder
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / f'{operator_folder}.csv'
    operator_df.to_csv(output_file, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to Training.csv or Training_Training.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for operator datasets")

    args = parser.parse_args()

    split_operators(args.input_file, args.output_dir)
