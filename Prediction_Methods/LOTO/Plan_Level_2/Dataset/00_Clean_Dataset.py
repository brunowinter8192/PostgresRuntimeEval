#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
from pathlib import Path

EXCLUDE_TEMPLATES = ['Q2', 'Q11', 'Q16', 'Q21', 'Q22']

# ORCHESTRATOR

def clean_workflow(input_csv: str, output_dir: str) -> None:
    df = load_dataset(input_csv)
    df_cleaned = filter_templates(df)
    export_cleaned(df_cleaned, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(input_csv: str) -> pd.DataFrame:
    return pd.read_csv(input_csv, delimiter=';')


# Filter out excluded templates
def filter_templates(df: pd.DataFrame) -> pd.DataFrame:
    return df[~df['template'].isin(EXCLUDE_TEMPLATES)]


# Export cleaned dataset to CSV
def export_cleaned(df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path / 'cleaned_dataset.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", help="Path to complete_dataset.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for cleaned dataset")

    args = parser.parse_args()

    clean_workflow(args.input_csv, args.output_dir)
