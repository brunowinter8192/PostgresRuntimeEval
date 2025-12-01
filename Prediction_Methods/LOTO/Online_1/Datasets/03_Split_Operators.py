#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR

def split_operators_workflow(baseline_dir: str) -> None:
    baseline_path = Path(baseline_dir)
    template_dirs = find_template_dirs(baseline_path)
    for template_dir in template_dirs:
        process_template(template_dir)


# FUNCTIONS

# Find all template subdirectories in Baseline folder
def find_template_dirs(baseline_dir: Path) -> list:
    template_dirs = [d for d in baseline_dir.iterdir() if d.is_dir()]
    return sorted(template_dirs, key=lambda x: x.name)

# Process single template directory
def process_template(template_dir: Path) -> None:
    training_file = template_dir / 'training_cleaned.csv'
    if not training_file.exists():
        return

    df = pd.read_csv(training_file, delimiter=';')
    operators = df['node_type'].unique()

    for operator in operators:
        export_operator_data(df, operator, template_dir)

# Export operator-specific data to subdirectory
def export_operator_data(df: pd.DataFrame, operator: str, template_dir: Path) -> None:
    operator_folder_name = operator.replace(' ', '_')
    operator_dir = template_dir / operator_folder_name
    operator_dir.mkdir(parents=True, exist_ok=True)

    df_operator = df[df['node_type'] == operator].copy()
    output_file = operator_dir / f'{operator_folder_name}.csv'
    df_operator.to_csv(output_file, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline_dir", help="Path to Baseline directory containing template subdirectories")

    args = parser.parse_args()
    split_operators_workflow(args.baseline_dir)
