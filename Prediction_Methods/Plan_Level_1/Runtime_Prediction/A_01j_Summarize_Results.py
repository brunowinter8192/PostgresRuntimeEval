#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import re
from pathlib import Path

import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))  # Plan_Level_1
# From mapping_config.py: Metadata column names
from mapping_config import PLAN_METADATA


# ORCHESTRATOR

# Summarize prediction results by template and overall metrics
def summarize_results_workflow(predictions_csv: Path, output_dir: Path) -> None:
    df = load_predictions(predictions_csv)
    df = add_template_ids(df)
    template_summary = compute_template_summary(df)
    overall_summary = compute_overall_summary(df)
    export_summaries(template_summary, overall_summary, output_dir)


# FUNCTIONS

# Load predictions from CSV with semicolon delimiter
def load_predictions(predictions_csv: Path) -> pd.DataFrame:
    return pd.read_csv(predictions_csv, delimiter=';')


# Add template ID column extracted from query_file
def add_template_ids(df: pd.DataFrame) -> pd.DataFrame:
    df[PLAN_METADATA[1]] = df[PLAN_METADATA[0]].apply(extract_template_id)
    return df


# Extract numeric template ID from query file name
def extract_template_id(query_file) -> int:
    match = re.search(r'q(\d+)_', str(query_file).lower())
    if match:
        return int(match.group(1))
    return 0


# Compute summary statistics per template
def compute_template_summary(df: pd.DataFrame) -> pd.DataFrame:
    template_summary = df.groupby(PLAN_METADATA[1]).agg({
        'actual_ms': ['mean', 'std', 'min', 'max', 'count'],
        'predicted_ms': ['mean'],
        'relative_error': ['mean']
    }).reset_index()

    template_summary.columns = [
        PLAN_METADATA[1], 'mean_actual_ms', 'std_actual_ms',
        'min_actual_ms', 'max_actual_ms', 'count',
        'mean_predicted_ms', 'mre'
    ]

    return template_summary


# Compute overall summary statistics
def compute_overall_summary(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{
        'mean_actual_ms': df['actual_ms'].mean(),
        'std_actual_ms': df['actual_ms'].std(),
        'mean_predicted_ms': df['predicted_ms'].mean(),
        'overall_mre': df['relative_error'].mean(),
        'n_queries': len(df),
        'n_templates': df[PLAN_METADATA[1]].nunique()
    }])


# Export summaries to CSV files with semicolon delimiter
def export_summaries(template_summary: pd.DataFrame, overall_summary: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)

    template_file = output_dir / 'A_01j_template_summary.csv'
    template_summary.to_csv(template_file, sep=';', index=False)

    overall_file = output_dir / 'A_01j_overall_summary.csv'
    overall_summary.to_csv(overall_file, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize prediction results by template and overall")
    parser.add_argument("predictions_csv", help="Predictions CSV file from train model script")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: same as predictions CSV)")

    args = parser.parse_args()

    predictions_path = Path(args.predictions_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = predictions_path.parent

    summarize_results_workflow(predictions_path, output_path)
