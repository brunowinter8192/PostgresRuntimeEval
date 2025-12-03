#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
import numpy as np
from pathlib import Path

# ORCHESTRATOR

def evaluate_workflow(evaluation_dir: str) -> None:
    eval_path = Path(evaluation_dir)
    template_folders = sorted([d for d in eval_path.iterdir() if d.is_dir()])

    for template_folder in template_folders:
        evaluate_template(template_folder)


def evaluate_template(template_folder: Path) -> None:
    predictions_file = template_folder / 'predictions.csv'

    if not predictions_file.exists():
        return

    df = load_predictions(predictions_file)
    metrics = calculate_metrics(df)
    export_metrics(metrics, template_folder)


# FUNCTIONS

# Load predictions from CSV file
def load_predictions(predictions_file: Path) -> pd.DataFrame:
    return pd.read_csv(predictions_file, delimiter=';')


# Calculate evaluation metrics
def calculate_metrics(df: pd.DataFrame) -> dict:
    return {
        'query_count': len(df),
        'mean_actual_ms': df['actual_ms'].mean(),
        'mean_predicted_ms': df['predicted_ms'].mean(),
        'mean_mre': df['relative_error'].mean(),
        'std_mre': df['relative_error'].std(),
        'mean_mre_pct': df['relative_error'].mean() * 100
    }


# Export metrics to CSV
def export_metrics(metrics: dict, output_folder: Path) -> None:
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_csv(output_folder / 'metrics.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("evaluation_dir", help="Path to Evaluation/ containing template folders")

    args = parser.parse_args()

    evaluate_workflow(args.evaluation_dir)
