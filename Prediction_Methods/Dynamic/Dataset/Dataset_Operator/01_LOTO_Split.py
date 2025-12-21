#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import re
import pandas as pd
from pathlib import Path

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']

ALL_OPERATORS = [
    'Aggregate', 'Gather', 'Gather Merge', 'Hash', 'Hash Join',
    'Incremental Sort', 'Index Only Scan', 'Index Scan', 'Limit',
    'Merge Join', 'Nested Loop', 'Seq Scan', 'Sort'
]


# ORCHESTRATOR
def loto_split_workflow(input_file: str, output_dir: str) -> None:
    df = load_dataset(input_file)
    df = add_template_column(df)
    for template in TEMPLATES:
        print(f"{template}...")
        create_loto_split(df, template, output_dir)


# FUNCTIONS
# Load operator dataset with child features
def load_dataset(input_file: str) -> pd.DataFrame:
    return pd.read_csv(input_file, delimiter=';')


# Extract template from query_file and add as column
def add_template_column(df: pd.DataFrame) -> pd.DataFrame:
    df['template'] = df['query_file'].apply(extract_template)
    return df


# Extract template ID from query filename (Q1_100_seed_xxx -> Q1)
def extract_template(query_file: str) -> str:
    match = re.match(r'(Q\d+)_', query_file)
    return match.group(1) if match else None


# Create LOTO split for one template
def create_loto_split(df: pd.DataFrame, template: str, output_dir: str) -> None:
    template_dir = Path(output_dir) / template
    template_dir.mkdir(exist_ok=True, parents=True)

    test_df = df[df['template'] == template].drop(columns=['template'])
    training_df = df[df['template'] != template].drop(columns=['template'])

    export_test(test_df, template_dir)
    export_training(training_df, template_dir)
    export_operator_splits(training_df, template_dir)


# Export test dataset
def export_test(df: pd.DataFrame, template_dir: Path) -> None:
    df.to_csv(template_dir / 'test.csv', index=False, sep=';')


# Export full training dataset
def export_training(df: pd.DataFrame, template_dir: Path) -> None:
    df.to_csv(template_dir / 'training.csv', index=False, sep=';')


# Split training data by node_type into operator folders (only operators with data)
def export_operator_splits(df: pd.DataFrame, template_dir: Path) -> None:
    for node_type in ALL_OPERATORS:
        operator_df = df[df['node_type'] == node_type]

        if len(operator_df) == 0:
            continue

        folder_name = csv_name_to_folder_name(node_type)
        prefixed_folder = f'04a_{folder_name}'

        operator_dir = template_dir / prefixed_folder
        operator_dir.mkdir(exist_ok=True, parents=True)

        operator_df.to_csv(operator_dir / f'04a_{folder_name}.csv', index=False, sep=';')


# Convert operator CSV name to folder name (Gather Merge -> Gather_Merge)
def csv_name_to_folder_name(csv_name: str) -> str:
    return csv_name.replace(' ', '_')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset with child features")
    parser.add_argument("--output-dir", required=True, help="Output directory for LOTO splits")

    args = parser.parse_args()

    loto_split_workflow(args.input_file, args.output_dir)
