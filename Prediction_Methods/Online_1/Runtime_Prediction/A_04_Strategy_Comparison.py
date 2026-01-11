#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def compare_strategies(evaluation_dir: str, output_dir: str) -> None:
    strategies = ['Error', 'Size', 'Frequency']
    queries = get_all_queries(evaluation_dir, strategies[0])

    selected_diff, used_diff = compare_all_queries(evaluation_dir, queries, strategies)

    export_results(selected_diff, used_diff, output_dir)


# FUNCTIONS

# Get list of all query folders
def get_all_queries(evaluation_dir: str, strategy: str) -> list:
    strategy_dir = Path(evaluation_dir) / strategy
    if not strategy_dir.exists():
        return []
    return sorted([d.name for d in strategy_dir.iterdir() if d.is_dir() and d.name.startswith('Q')])


# Compare all queries across strategies
def compare_all_queries(evaluation_dir: str, queries: list, strategies: list) -> tuple:
    selected_differences = []
    used_differences = []

    for query in queries:
        selected_by_strategy = {}
        used_by_strategy = {}

        for strategy in strategies:
            selected_by_strategy[strategy] = get_selected_patterns(evaluation_dir, strategy, query)
            used_by_strategy[strategy] = get_used_patterns(evaluation_dir, strategy, query)

        selected_diff = find_differences(query, selected_by_strategy, strategies, 'selected')
        used_diff = find_differences(query, used_by_strategy, strategies, 'used')

        if selected_diff:
            selected_differences.append(selected_diff)
        if used_diff:
            used_differences.append(used_diff)

    return selected_differences, used_differences


# Get ACCEPTED patterns from selection_log.csv
def get_selected_patterns(evaluation_dir: str, strategy: str, query: str) -> set:
    log_file = Path(evaluation_dir) / strategy / query / 'csv' / 'selection_log.csv'
    if not log_file.exists():
        return set()

    df = pd.read_csv(log_file, delimiter=';')
    accepted = df[df['status'] == 'ACCEPTED']
    return set(accepted['pattern_hash'].tolist())


# Get USED patterns from models/patterns/ directory
def get_used_patterns(evaluation_dir: str, strategy: str, query: str) -> set:
    patterns_dir = Path(evaluation_dir) / strategy / query / 'models' / 'patterns'
    if not patterns_dir.exists():
        return set()
    return set([d.name for d in patterns_dir.iterdir() if d.is_dir()])


# Find differences between strategies for one query
def find_differences(query: str, patterns_by_strategy: dict, strategies: list, diff_type: str) -> dict:
    all_same = True
    reference = patterns_by_strategy[strategies[0]]

    for strategy in strategies[1:]:
        if patterns_by_strategy[strategy] != reference:
            all_same = False
            break

    if all_same:
        return None

    result = {
        'query': query,
        'template': query.split('_')[0]
    }

    for strategy in strategies:
        patterns = patterns_by_strategy[strategy]
        result[f'{strategy.lower()}_count'] = len(patterns)
        result[f'{strategy.lower()}_hashes'] = ','.join(sorted(patterns)[:5]) if patterns else ''

    all_patterns = set()
    for patterns in patterns_by_strategy.values():
        all_patterns.update(patterns)

    common = all_patterns.copy()
    for patterns in patterns_by_strategy.values():
        common &= patterns

    result['common_count'] = len(common)
    result['total_unique'] = len(all_patterns)

    return result


# Export results to CSV
def export_results(selected_diff: list, used_diff: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    summary = {
        'metric': ['queries_with_different_selection', 'queries_with_different_usage'],
        'count': [len(selected_diff), len(used_diff)]
    }
    pd.DataFrame(summary).to_csv(output_path / 'A_04_strategy_summary.csv', sep=';', index=False)

    if selected_diff:
        pd.DataFrame(selected_diff).to_csv(output_path / 'A_04_selection_differences.csv', sep=';', index=False)

    if used_diff:
        pd.DataFrame(used_diff).to_csv(output_path / 'A_04_usage_differences.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('evaluation_dir', help='Path to Evaluation directory (contains Error/, Size/, Frequency/)')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    args = parser.parse_args()

    compare_strategies(args.evaluation_dir, args.output_dir)
