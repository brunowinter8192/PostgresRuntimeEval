#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
from pathlib import Path

# ORCHESTRATOR

def split_workflow(input_csv: str, output_dir: str) -> None:
    df = load_dataset(input_csv)
    templates = get_unique_templates(df)
    create_splits(df, templates, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(input_csv: str) -> pd.DataFrame:
    return pd.read_csv(input_csv, delimiter=';')


# Get unique template values
def get_unique_templates(df: pd.DataFrame) -> list:
    return sorted(df['template'].unique())


# Create train/test splits for each template
def create_splits(df: pd.DataFrame, templates: list, output_dir: str) -> None:
    output_path = Path(output_dir)

    for template in templates:
        template_dir = output_path / template
        template_dir.mkdir(parents=True, exist_ok=True)

        test_df = df[df['template'] == template]
        training_df = df[df['template'] != template]

        test_df.to_csv(template_dir / 'test.csv', sep=';', index=False)
        training_df.to_csv(template_dir / 'training.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", help="Path to complete_dataset.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for template splits")

    args = parser.parse_args()

    split_workflow(args.input_csv, args.output_dir)
