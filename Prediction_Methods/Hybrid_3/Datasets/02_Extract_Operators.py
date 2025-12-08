#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def extract_operators_workflow(training_file: str, output_dir: str) -> None:
    df = load_data(training_file)
    operator_dfs = split_by_node_type(df)
    export_operators(operator_dfs, output_dir)


# FUNCTIONS

# Load training dataset from CSV file
def load_data(training_file: str) -> pd.DataFrame:
    return pd.read_csv(training_file, delimiter=';')


# Split dataset into separate DataFrames per node type
def split_by_node_type(df: pd.DataFrame) -> dict:
    node_types = sorted(df['node_type'].unique())
    return {nt: df[df['node_type'] == nt] for nt in node_types}


# Convert operator name to folder name format
def operator_to_folder_name(operator_name: str) -> str:
    return operator_name.replace(' ', '_')


# Create folder per operator type and save training CSV
def export_operators(operator_dfs: dict, output_dir: str) -> None:
    operators_path = Path(output_dir) / 'operators'
    operators_path.mkdir(parents=True, exist_ok=True)

    for node_type, node_df in operator_dfs.items():
        folder_name = operator_to_folder_name(node_type)
        operator_dir = operators_path / folder_name
        operator_dir.mkdir(exist_ok=True)

        output_csv = operator_dir / 'training.csv'
        node_df.to_csv(output_csv, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("training_file", help="Path to training dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Base directory for operator folders")

    args = parser.parse_args()

    extract_operators_workflow(args.training_file, args.output_dir)
