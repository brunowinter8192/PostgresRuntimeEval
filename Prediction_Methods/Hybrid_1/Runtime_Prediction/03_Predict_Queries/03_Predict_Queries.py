#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# From io.py: Data loading and export functions
from src.io import (
    load_test_data,
    load_pattern_features,
    load_operator_features,
    load_pattern_models,
    load_operator_models,
    export_predictions
)

# From prediction.py: Prediction functions
from src.prediction import predict_all_queries

# From report.py: Report generation
from src.report import export_md_report


# ORCHESTRATOR

# Execute bottom-up prediction workflow for all queries or single query with MD report
def run_prediction(
    test_file: str,
    dataset_dir: str,
    pattern_overview_file: str,
    operator_overview_file: str,
    pattern_model_dir: str,
    operator_model_dir: str,
    output_dir: str,
    md_query: str = None
) -> None:
    df_test = load_test_data(test_file)
    pattern_features = load_pattern_features(pattern_overview_file, dataset_dir)
    operator_features = load_operator_features(operator_overview_file)
    pattern_models = load_pattern_models(pattern_model_dir, pattern_features)
    operator_models = load_operator_models(operator_model_dir)

    track_steps = md_query is not None

    if md_query:
        df_query = df_test[df_test['query_file'] == md_query].copy()
        df_query = df_query[df_query['subplan_name'].isna() | (df_query['subplan_name'] == '')]
        df_query = df_query.sort_values('node_id').reset_index(drop=True)

        all_predictions, all_steps = predict_all_queries(
            df_test[df_test['query_file'] == md_query],
            pattern_features, operator_features,
            pattern_models, operator_models,
            pattern_model_dir, operator_model_dir, track_steps
        )

        steps = all_steps.get(md_query, [])
        export_md_report(
            md_query, test_file, pattern_overview_file, operator_overview_file,
            pattern_model_dir, operator_model_dir, df_query, all_predictions, steps, output_dir
        )
        return

    all_predictions, _ = predict_all_queries(
        df_test, pattern_features, operator_features,
        pattern_models, operator_models,
        pattern_model_dir, operator_model_dir, track_steps=False
    )

    export_predictions(all_predictions, output_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bottom-up prediction for hybrid model')
    parser.add_argument('test_file', help='Path to test.csv')
    parser.add_argument('dataset_dir', help='Path to Datasets directory (contains patterns/ folder)')
    parser.add_argument('pattern_overview', help='Path to pattern overview CSV (two_step_evaluation_overview.csv)')
    parser.add_argument('operator_overview', help='Path to operator overview CSV (operator_overview.csv)')
    parser.add_argument('pattern_model_dir', help='Path to Pattern model directory')
    parser.add_argument('operator_model_dir', help='Path to Operator model directory')
    parser.add_argument('--output-dir', required=True, help='Path to output directory for predictions')
    parser.add_argument('--md-query', help='Generate MD report for single query')
    args = parser.parse_args()

    run_prediction(
        args.test_file,
        args.dataset_dir,
        args.pattern_overview,
        args.operator_overview,
        args.pattern_model_dir,
        args.operator_model_dir,
        args.output_dir,
        args.md_query
    )
