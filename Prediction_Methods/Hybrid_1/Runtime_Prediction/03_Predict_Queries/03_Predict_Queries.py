#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# From io.py: Data loading and export functions
from src.io import (
    load_test_data,
    load_pattern_info,
    load_pattern_features,
    load_pattern_models,
    load_operator_features,
    load_operator_models,
    export_predictions
)

# From prediction.py: Prediction functions
from src.prediction import predict_all_queries, predict_single_query

# From report.py: MD report generation
from src.report import export_md_report

# From tree.py: Plan hash computation
from src.tree import compute_plan_hash


# ORCHESTRATOR

# Execute prediction workflow with patterns and operators
def run_prediction(
    test_file: str,
    patterns_csv: str,
    pattern_overview_file: str,
    operator_overview_file: str,
    model_dir: str,
    output_dir: str,
    passthrough: bool = False,
    report: bool = False
) -> None:
    df_test = load_test_data(test_file)

    pattern_info, pattern_order = load_pattern_info(patterns_csv)
    pattern_features = load_pattern_features(pattern_overview_file, pattern_order)
    pattern_models = load_pattern_models(model_dir, pattern_order)

    operator_features = load_operator_features(operator_overview_file)
    operator_models = load_operator_models(model_dir)

    if report:
        run_with_reports(
            df_test, operator_models, operator_features,
            pattern_models, pattern_features, pattern_info, pattern_order,
            passthrough, output_dir
        )
    else:
        all_predictions = predict_all_queries(
            df_test, operator_models, operator_features,
            pattern_models, pattern_features, pattern_info, pattern_order,
            passthrough
        )
        export_predictions(all_predictions, output_dir)


# Run predictions with MD reports for first query of each unique plan
def run_with_reports(
    df_test, operator_models, operator_features,
    pattern_models, pattern_features, pattern_info, pattern_order,
    passthrough, output_dir
) -> None:
    all_predictions = []
    reported_plans = set()

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)

        plan_hash = compute_plan_hash(query_ops)
        should_report = plan_hash not in reported_plans

        predictions, steps, consumed_nodes, pattern_assignments = predict_single_query(
            query_ops, operator_models, operator_features,
            pattern_models, pattern_features, pattern_info, pattern_order,
            passthrough, collect_steps=should_report
        )

        all_predictions.extend(predictions)

        if should_report:
            reported_plans.add(plan_hash)
            export_md_report(
                query_file, query_ops, predictions, steps,
                consumed_nodes, pattern_assignments, pattern_info, output_dir, plan_hash,
                passthrough
            )

    export_predictions(all_predictions, output_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bottom-up prediction for hybrid model')
    parser.add_argument('test_file', help='Path to test.csv')
    parser.add_argument('patterns_csv', help='Path to patterns.csv (with pattern_hash and pattern_length)')
    parser.add_argument('pattern_overview', help='Path to pattern FFS overview (two_step_evaluation_overview.csv)')
    parser.add_argument('operator_overview', help='Path to operator overview (operator_overview.csv)')
    parser.add_argument('model_dir', help='Path to Model directory')
    parser.add_argument('--output-dir', required=True, help='Path to output directory for predictions')
    parser.add_argument('--passthrough', action='store_true', help='Enable passthrough for non-pattern passthrough operators')
    parser.add_argument('--report', action='store_true', help='Generate MD report for first query of each template')
    args = parser.parse_args()

    run_prediction(
        args.test_file,
        args.patterns_csv,
        args.pattern_overview,
        args.operator_overview,
        args.model_dir,
        args.output_dir,
        args.passthrough,
        args.report
    )
