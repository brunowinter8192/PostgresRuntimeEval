#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import argparse
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

# From mapping_config.py: Get child timing features to remove from test sets
from mapping_config import CHILD_FEATURES_TIMING

# ORCHESTRATOR

# Process all 14 template test datasets and remove child timing features
def main_workflow(baseline_dir: str) -> None:
    baseline_path = Path(baseline_dir)
    template_dirs = find_template_dirs(baseline_path)
    process_all_templates(baseline_path, template_dirs)

# FUNCTIONS

# Find all template subdirectories in Baseline folder
def find_template_dirs(baseline_dir: Path) -> list:
    template_dirs = [d for d in baseline_dir.iterdir() if d.is_dir()]
    return sorted(template_dirs, key=lambda x: x.name)

# Load test dataset from CSV file
def load_test_data(test_file: Path) -> pd.DataFrame:
    return pd.read_csv(test_file, delimiter=';')

# Remove child timing features from dataset
def remove_child_timing_features(df: pd.DataFrame) -> pd.DataFrame:
    existing_features = [f for f in CHILD_FEATURES_TIMING if f in df.columns]

    if existing_features:
        return df.drop(columns=existing_features)

    return df

# Save cleaned test dataset to CSV file
def export_cleaned_test(df: pd.DataFrame, output_file: Path) -> None:
    df.to_csv(output_file, index=False, sep=';')

# Process all template directories
def process_all_templates(baseline_dir: Path, template_dirs: list) -> None:
    for template_dir in template_dirs:
        test_file = template_dir / 'test_cleaned.csv'

        if not test_file.exists():
            continue

        df = load_test_data(test_file)
        df_cleaned = remove_child_timing_features(df)
        output_file = template_dir / '02_test_cleaned.csv'
        export_cleaned_test(df_cleaned, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline_dir", help="Path to Baseline directory containing template subdirectories")

    args = parser.parse_args()
    main_workflow(args.baseline_dir)
