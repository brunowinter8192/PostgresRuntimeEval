#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
from pathlib import Path

DATASET_DIR = Path(__file__).resolve().parent.parent.parent / 'Dataset' / 'Dataset_Operator'


# ORCHESTRATOR

def unique_operators_workflow(output_dir: str) -> None:
    templates = get_templates()
    results = find_unique_operators(templates)
    export_results(results, output_dir)


# FUNCTIONS

# Get sorted template list from dataset directory
def get_templates() -> list:
    return sorted(
        [d.name for d in DATASET_DIR.iterdir() if d.is_dir() and d.name.startswith('Q')],
        key=lambda x: int(x[1:])
    )


# Find operators in test but not in training per template
def find_unique_operators(templates: list) -> list:
    results = []

    for template in templates:
        training_file = DATASET_DIR / template / 'training.csv'
        test_file = DATASET_DIR / template / 'test.csv'

        df_train = pd.read_csv(training_file, delimiter=';')
        df_test = pd.read_csv(test_file, delimiter=';')

        train_ops = set(df_train['node_type'].unique())
        test_ops = set(df_test['node_type'].unique())

        for op in sorted(test_ops - train_ops):
            results.append({'template': template, 'operator': op})

    return results


# Export results to CSV
def export_results(results: list, output_dir: str) -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(results)
    df.to_csv(Path(output_dir) / 'A_01c_unique_operators.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    unique_operators_workflow(args.output_dir)
