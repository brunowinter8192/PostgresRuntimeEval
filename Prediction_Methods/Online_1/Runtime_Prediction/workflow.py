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
from src.prediction import predict_all_queries_operator_only, predict_single_query_operator_only, predict_single_query_with_patterns

# From src/mining.py: Pattern mining and ranking
from src.mining import mine_patterns_from_query, find_pattern_occurrences_in_data, calculate_ranking

# From mapping_config.py: Configuration constants
from mapping_config import STRATEGIES, DEFAULT_STRATEGY

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
    output_dir: str,
    strategy: str = DEFAULT_STRATEGY,
    epsilon: float = 0.0
) -> None:
    query_output_dir = str(Path(output_dir) / strategy.capitalize() / test_query_file)
    report = ReportBuilder(test_query_file, query_output_dir)

    df_tt = load_data(training_training_csv)
    df_tv = load_data(training_test_csv)
    df_train = load_data(training_csv)
    df_test = load_data(test_csv)

    report.add_data_summary(df_tt, df_tv, df_train, df_test)

    operator_models = train_all_operators(df_tt, report)

    baseline_predictions = predict_all_queries_operator_only(df_tv, operator_models)
    baseline_mre = calculate_mre(baseline_predictions)

    test_query_ops = get_query_operators(df_test, test_query_file)
    test_query_baseline = predict_single_query_operator_only(test_query_ops, operator_models)
    test_query_baseline_mre = calculate_query_mre(test_query_baseline)
    report.add_operator_baseline(test_query_baseline_mre)
    patterns = mine_patterns_from_query(test_query_ops)
    pattern_occurrences = find_pattern_occurrences_in_data(df_tv, patterns)
    initial_ranking = calculate_ranking(baseline_predictions, pattern_occurrences, patterns, strategy=strategy)
    report.add_patterns_in_query(patterns, initial_ranking)

    selected_patterns, pattern_models, selection_log = run_pattern_selection(
        df_tt, df_tv, patterns, pattern_occurrences, initial_ranking,
        operator_models, baseline_predictions, baseline_mre, report,
        epsilon=epsilon, strategy=strategy
    )

    final_operator_models = train_all_operators(df_train, None)
    final_pattern_models = train_selected_patterns(df_train, selected_patterns, patterns)

    final_predictions, pattern_assignments, consumed_nodes, prediction_cache = predict_single_query_with_patterns(
        test_query_ops, final_operator_models, final_pattern_models, patterns, selected_patterns,
        return_details=True
    )
    final_mre = calculate_query_mre(final_predictions)

    report.add_query_tree(test_query_ops, pattern_assignments, consumed_nodes, patterns)
    report.add_pattern_assignments(pattern_assignments, consumed_nodes, patterns)
    report.add_final_prediction(final_predictions, final_mre, test_query_baseline_mre)
    report.add_prediction_chain(final_predictions, prediction_cache, pattern_assignments, consumed_nodes, patterns)

    save_models(query_output_dir, test_query_file, final_operator_models, final_pattern_models)
    save_csv_outputs(query_output_dir, test_query_file, selection_log, final_predictions)
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
    parser.add_argument("--strategy", choices=STRATEGIES, default=DEFAULT_STRATEGY, help="Pattern ordering strategy")
    parser.add_argument("--epsilon", type=float, default=0.0, help="Min MRE improvement for pattern acceptance")
    args = parser.parse_args()

    online_prediction_workflow(
        args.test_query_file,
        args.training_training_csv,
        args.training_test_csv,
        args.training_csv,
        args.test_csv,
        args.output_dir,
        args.strategy,
        args.epsilon
    )
