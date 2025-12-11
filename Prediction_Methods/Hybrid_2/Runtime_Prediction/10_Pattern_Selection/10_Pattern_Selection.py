#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# From io.py: Data loading functions
from src.io import (
    load_operator_models,
    load_operator_ffs,
    load_pattern_ffs,
    load_sorted_patterns,
    load_pattern_occurrences,
    load_training_data,
    load_test_data
)

# From selection.py: Selection strategy functions
from src.selection import run_static_selection, run_error_selection

STRATEGIES = ['frequency', 'size', 'error']


# ORCHESTRATOR

# Execute pattern selection workflow based on strategy
def run_pattern_selection(
    strategy: str,
    sorted_patterns_file: str,
    pattern_ffs_file: str,
    training_file: str,
    test_file: str,
    operator_model_dir: str,
    operator_ffs_dir: str,
    output_dir: str,
    model_dir: str,
    pretrained_dir: str = None,
    pattern_occurrences_file: str = None,
    min_error_threshold: float = 0.1
) -> None:
    operator_models = load_operator_models(operator_model_dir)
    operator_ffs = load_operator_ffs(operator_ffs_dir)
    pattern_ffs = load_pattern_ffs(pattern_ffs_file)
    sorted_patterns = load_sorted_patterns(sorted_patterns_file)
    df_training = load_training_data(training_file)
    df_test = load_test_data(test_file)

    if strategy == 'error':
        pattern_occurrences = load_pattern_occurrences(pattern_occurrences_file)
        run_error_selection(
            sorted_patterns, pattern_occurrences, pattern_ffs, df_training, df_test,
            operator_models, operator_ffs, output_dir, model_dir, pretrained_dir
        )
    else:
        run_static_selection(
            sorted_patterns, pattern_ffs, df_training, df_test,
            operator_models, operator_ffs, output_dir, model_dir, pretrained_dir,
            min_error_threshold
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--strategy', required=True, choices=STRATEGIES, help='Selection strategy')
    parser.add_argument('sorted_patterns_file', help='Path to sorted patterns CSV (06_patterns_by_*.csv or 10_patterns_by_error.csv)')
    parser.add_argument('pattern_ffs_file', help='Path to pattern_ffs_overview.csv')
    parser.add_argument('training_file', help='Path to Training_Training.csv')
    parser.add_argument('test_file', help='Path to Training_Test.csv')
    parser.add_argument('operator_model_dir', help='Path to Model/Operator/')
    parser.add_argument('operator_ffs_dir', help='Path to SVM/Operator/')
    parser.add_argument('--pattern-output-dir', required=True, help='Per-pattern results output directory')
    parser.add_argument('--model-dir', required=True, help='Model output directory')
    parser.add_argument('--pretrained-dir', default=None, help='Path to pretrained models')
    parser.add_argument('--pattern-occurrences-file', default=None, help='Path to 05_test_pattern_occurrences_*.csv (required for error strategy)')
    parser.add_argument('--min-error-threshold', type=float, default=0.1, help='Min avg_mre threshold for size/frequency (default: 0.1)')
    args = parser.parse_args()

    if args.strategy == 'error' and not args.pattern_occurrences_file:
        parser.error('--pattern-occurrences-file is required for error strategy')

    run_pattern_selection(
        args.strategy,
        args.sorted_patterns_file,
        args.pattern_ffs_file,
        args.training_file,
        args.test_file,
        args.operator_model_dir,
        args.operator_ffs_dir,
        args.pattern_output_dir,
        args.model_dir,
        args.pretrained_dir,
        args.pattern_occurrences_file,
        args.min_error_threshold
    )
