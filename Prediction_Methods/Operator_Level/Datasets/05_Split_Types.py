#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import argparse
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

# From mapping_config.py: Convert operator CSV name to folder name format
from mapping_config import csv_name_to_folder_name

# ORCHESTRATOR
def split_by_type_workflow(training_file, output_base_dir):
    df = load_data(training_file)
    node_type_dfs = split_by_node_type(df)
    export_node_types(node_type_dfs, output_base_dir)

# FUNCTIONS

# Load training dataset from CSV file
def load_data(training_file):
    return pd.read_csv(training_file, delimiter=';')


# Split dataset into separate DataFrames per node type
def split_by_node_type(df):
    node_types = sorted(df['node_type'].unique())
    
    node_type_dfs = {}
    for node_type in node_types:
        node_type_data = df[df['node_type'] == node_type]
        node_type_dfs[node_type] = node_type_data
    
    return node_type_dfs


# Create folder per node type and save corresponding CSV file
def export_node_types(node_type_dfs, base_dir):
    base_path = Path(base_dir)

    for node_type, node_df in node_type_dfs.items():
        folder_name = csv_name_to_folder_name(node_type)

        node_type_dir = base_path / folder_name
        node_type_dir.mkdir(exist_ok=True, parents=True)

        output_csv = node_type_dir / f'{folder_name}.csv'
        node_df.to_csv(output_csv, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("training_file", help="Path to training dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Base directory for node type folders")

    args = parser.parse_args()

    split_by_type_workflow(args.training_file, args.output_dir)
