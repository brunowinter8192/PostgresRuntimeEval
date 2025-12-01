#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
from pathlib import Path
import pandas as pd

# ORCHESTRATOR

def collect_workflow(svm_dir: Path, output_dir: Path) -> None:
    feature_sets = collect_feature_sets(svm_dir)
    export_feature_sets(feature_sets, output_dir)


# FUNCTIONS

# Collect feature sets from all ffs_summary.csv files
def collect_feature_sets(svm_dir: Path) -> list:
    feature_sets = []

    for template_dir in sorted(svm_dir.iterdir()):
        if not template_dir.is_dir():
            continue

        ffs_file = template_dir / 'ffs_summary.csv'
        if not ffs_file.exists():
            continue

        template_name = template_dir.name
        df = pd.read_csv(ffs_file, delimiter=';')

        row = df.iloc[0]
        feature_sets.append({
            'template': template_name,
            'selected_features': row['selected_features'],
            'n_features': row['n_features'],
            'final_mre': row['final_mre']
        })

    return feature_sets


# Export feature sets to CSV
def export_feature_sets(feature_sets: list, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(feature_sets)
    df.to_csv(output_dir / 'feature_sets.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("svm_dir", help="Path to SVM/ containing template folders with ffs_summary.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for feature_sets.csv")

    args = parser.parse_args()

    collect_workflow(Path(args.svm_dir), Path(args.output_dir))
