#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def loto_split_workflow(input_file: str, output_dir: str) -> None:
    df = load_dataset(input_file)
    df = filter_templates(df)
    for template in TEMPLATES:
        print(f"{template}...")
        create_loto_split(df, template, output_dir)


# FUNCTIONS
# Load plan-level dataset
def load_dataset(input_file: str) -> pd.DataFrame:
    return pd.read_csv(input_file, delimiter=';')


# Filter dataset to only include valid templates
def filter_templates(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['template'].isin(TEMPLATES)]


# Create LOTO split for one template
def create_loto_split(df: pd.DataFrame, template: str, output_dir: str) -> None:
    template_dir = Path(output_dir) / template
    template_dir.mkdir(exist_ok=True, parents=True)

    test_df = df[df['template'] == template]
    training_df = df[df['template'] != template]

    export_csv(test_df, template_dir / 'test.csv')
    export_csv(training_df, template_dir / 'training.csv')


# Export dataframe to CSV
def export_csv(df: pd.DataFrame, path: Path) -> None:
    df.to_csv(path, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to plan-level complete_dataset.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for LOTO splits")

    args = parser.parse_args()

    loto_split_workflow(args.input_file, args.output_dir)
