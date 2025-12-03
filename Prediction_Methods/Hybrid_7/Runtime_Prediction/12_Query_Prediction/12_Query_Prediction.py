#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# From io.py: Data loading and export functions
from src.io import (
    load_test_data,
    load_operator_models,
    load_operator_features,
    load_pattern_models,
    load_pattern_features,
    load_pattern_info,
    export_predictions
)

# From prediction.py: Prediction functions
from src.prediction import predict_all_queries

# From report.py: Report generation
from src.report import ReportBuilder

STRATEGIES = ['frequency', 'size', 'error']


# ORCHESTRATOR

# Execute prediction workflow with optional pattern models and MD report
def run_prediction(
    test_file: str,
    operator_model_dir: str,
    operator_overview_file: str,
    output_dir: str,
    strategy: str = None,
    pattern_model_dir: str = None,
    pattern_ffs_file: str = None,
    selected_patterns_file: str = None,
    pattern_metadata_file: str = None
) -> None:
    df_test = load_test_data(test_file)
    operator_models = load_operator_models(operator_model_dir)
    operator_features = load_operator_features(operator_overview_file)

    pattern_models = {}
    pattern_features = {}
    pattern_info = {}
    pattern_order = []

    if pattern_model_dir and pattern_ffs_file and selected_patterns_file and pattern_metadata_file:
        pattern_models = load_pattern_models(pattern_model_dir)
        pattern_features = load_pattern_features(pattern_ffs_file, pattern_models)
        pattern_info, pattern_order = load_pattern_info(selected_patterns_file, pattern_metadata_file)

    report = ReportBuilder(output_dir, strategy)
    report.add_input_summary(
        test_file,
        operator_model_dir,
        pattern_model_dir,
        len(pattern_order)
    )

    all_predictions = predict_all_queries(
        df_test, operator_models, operator_features,
        pattern_models, pattern_features, pattern_info, pattern_order,
        report
    )

    export_predictions(all_predictions, output_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file', help='Path to Test.csv')
    parser.add_argument('operator_model_dir', help='Path to Model/Operators_Training/')
    parser.add_argument('operator_overview_file', help='Path to two_step_evaluation_overview.csv')
    parser.add_argument('--strategy', choices=STRATEGIES, default=None, help='Selection strategy for pattern priority')
    parser.add_argument('--pattern-model-dir', default=None, help='Path to pattern models (Model/Patterns_Training_*)')
    parser.add_argument('--pattern-ffs-file', default=None, help='Path to pattern_ffs_overview.csv')
    parser.add_argument('--selected-patterns', default=None, help='Path to selected_patterns.csv')
    parser.add_argument('--pattern-metadata', default=None, help='Path to 06_patterns_by_*.csv (for pattern_length)')
    parser.add_argument('--output-dir', required=True, help='Output directory for predictions')
    args = parser.parse_args()

    run_prediction(
        args.test_file,
        args.operator_model_dir,
        args.operator_overview_file,
        args.output_dir,
        args.strategy,
        args.pattern_model_dir,
        args.pattern_ffs_file,
        args.selected_patterns,
        args.pattern_metadata
    )
