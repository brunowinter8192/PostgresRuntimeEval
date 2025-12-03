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
    root_ops = extract_root_operators(df)
    metrics = calculate_metrics(root_ops)
    export_metrics(metrics, template_folder)


# FUNCTIONS

# Load predictions from CSV file
def load_predictions(predictions_file: Path) -> pd.DataFrame:
    return pd.read_csv(predictions_file, delimiter=';')


# Extract root operators from predictions
def extract_root_operators(df: pd.DataFrame) -> pd.DataFrame:
    root_ops = df[df['depth'] == 0].copy()
    root_ops['mre_startup'] = np.abs(root_ops['predicted_startup_time'] - root_ops['actual_startup_time']) / root_ops['actual_startup_time'].replace(0, np.nan)
    root_ops['mre_total'] = np.abs(root_ops['predicted_total_time'] - root_ops['actual_total_time']) / root_ops['actual_total_time'].replace(0, np.nan)
    return root_ops


# Calculate evaluation metrics
def calculate_metrics(root_ops: pd.DataFrame) -> dict:
    return {
        'query_count': len(root_ops),
        'mean_actual_total': root_ops['actual_total_time'].mean(),
        'mean_predicted_total': root_ops['predicted_total_time'].mean(),
        'mean_mre_startup': root_ops['mre_startup'].mean(),
        'std_mre_startup': root_ops['mre_startup'].std(),
        'mean_mre_total': root_ops['mre_total'].mean(),
        'std_mre_total': root_ops['mre_total'].std(),
        'mean_mre_startup_pct': root_ops['mre_startup'].mean() * 100,
        'mean_mre_total_pct': root_ops['mre_total'].mean() * 100
    }


# Export metrics to CSV
def export_metrics(metrics: dict, output_folder: Path) -> None:
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_csv(output_folder / 'metrics.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("evaluation_dir", help="Path to Baseline_SVM/Evaluation/ containing template folders")

    args = parser.parse_args()

    evaluate_workflow(args.evaluation_dir)
