#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import argparse
import pandas as pd

# From src/training.py: Model training
from src.training import train_all_operators, train_selected_patterns

# From src/prediction.py: Query prediction
from src.prediction import predict_all_queries_operator_only, predict_single_query_with_patterns

# From src/mining.py: Pattern mining and ranking
from src.mining import mine_patterns_from_query, find_pattern_occurrences_in_data, calculate_error_ranking

# From src/selection.py: Pattern selection loop
from src.selection import run_pattern_selection

# From src/metrics.py: MRE calculation
from src.metrics import calculate_mre, calculate_query_mre

# From src/output.py: Save models and CSV outputs
from src.output import save_models, save_csv_outputs

# From src/report.py: Markdown report builder
from src.report import ReportBuilder


# ORCHESTRATOR

def online_prediction_workflow(
    test_query_file: str,
    training_training_csv: str,
    training_test_csv: str,
    training_csv: str,
    test_csv: str,
    output_dir: str
) -> None:
    report = ReportBuilder(test_query_file, output_dir)

    df_tt = load_data(training_training_csv)
    df_tv = load_data(training_test_csv)
    df_train = load_data(training_csv)
    df_test = load_data(test_csv)

    report.add_data_summary(df_tt, df_tv, df_train, df_test)

    operator_models = train_all_operators(df_tt, report)

    baseline_predictions = predict_all_queries_operator_only(df_tv, operator_models)
    baseline_mre = calculate_mre(baseline_predictions)
    report.add_operator_baseline(baseline_mre)

    test_query_ops = get_query_operators(df_test, test_query_file)
    patterns = mine_patterns_from_query(test_query_ops)
    pattern_occurrences = find_pattern_occurrences_in_data(df_tv, patterns)
    initial_ranking = calculate_error_ranking(baseline_predictions, pattern_occurrences, patterns)
    report.add_patterns_in_query(patterns, initial_ranking)

    selected_patterns, pattern_models, selection_log = run_pattern_selection(
        df_tt, df_tv, patterns, pattern_occurrences, initial_ranking,
        operator_models, baseline_predictions, baseline_mre, report
    )

    final_operator_models = train_all_operators(df_train, None)
    final_pattern_models = train_selected_patterns(df_train, selected_patterns, patterns)

    final_predictions = predict_single_query_with_patterns(
        test_query_ops, final_operator_models, final_pattern_models, patterns, selected_patterns
    )
    final_mre = calculate_query_mre(final_predictions)

    report.add_final_prediction(final_predictions, final_mre, baseline_mre)

    save_models(output_dir, test_query_file, final_operator_models, final_pattern_models)
    save_csv_outputs(output_dir, test_query_file, selection_log, final_predictions)
    report.save()


# FUNCTIONS

# Load data and filter to main plan
def load_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Get operators for specific query
def get_query_operators(df: pd.DataFrame, query_file: str) -> pd.DataFrame:
    return df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("test_query_file", help="Name of the test query")
    parser.add_argument("training_training_csv", help="Path to Training_Training.csv")
    parser.add_argument("training_test_csv", help="Path to Training_Test.csv")
    parser.add_argument("training_csv", help="Path to Training.csv")
    parser.add_argument("test_csv", help="Path to Test.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    online_prediction_workflow(
        args.test_query_file,
        args.training_training_csv,
        args.training_test_csv,
        args.training_csv,
        args.test_csv,
        args.output_dir
    )
