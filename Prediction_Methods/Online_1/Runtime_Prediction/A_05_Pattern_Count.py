#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import re
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def analyze_pattern_counts(evaluation_dir: str, strategy: str, output_dir: str) -> None:
    queries = get_all_queries(evaluation_dir, strategy)
    pattern_counts = collect_pattern_counts(evaluation_dir, strategy, queries)
    template_stats = aggregate_by_template(pattern_counts)
    export_results(pattern_counts, template_stats, output_dir)


# FUNCTIONS

# Get list of all query folders
def get_all_queries(evaluation_dir: str, strategy: str) -> list:
    strategy_dir = Path(evaluation_dir) / strategy
    if not strategy_dir.exists():
        return []
    return sorted([d.name for d in strategy_dir.iterdir() if d.is_dir() and d.name.startswith('Q')])


# Collect pattern count for each query from report.md
def collect_pattern_counts(evaluation_dir: str, strategy: str, queries: list) -> list:
    results = []

    for query in queries:
        report_file = Path(evaluation_dir) / strategy / query / 'md' / 'report.md'
        pattern_count = parse_pattern_count(report_file)

        template = query.split('_')[0]
        results.append({
            'query': query,
            'template': template,
            'pattern_count': pattern_count
        })

    return results


# Parse "Total Patterns: N" from report.md
def parse_pattern_count(report_file: Path) -> int:
    if not report_file.exists():
        return 0

    content = report_file.read_text()
    match = re.search(r'Total Patterns:\s*(\d+)', content)
    if match:
        return int(match.group(1))
    return 0


# Aggregate pattern counts by template
def aggregate_by_template(pattern_counts: list) -> pd.DataFrame:
    df = pd.DataFrame(pattern_counts)

    stats = df.groupby('template').agg({
        'pattern_count': ['min', 'max', 'mean', 'std', 'count']
    }).reset_index()

    stats.columns = ['template', 'min_patterns', 'max_patterns', 'avg_patterns', 'std_patterns', 'query_count']
    stats['avg_patterns'] = stats['avg_patterns'].round(2)
    stats['std_patterns'] = stats['std_patterns'].round(2)

    stats = stats.sort_values('template', key=lambda x: x.str.extract(r'Q(\d+)')[0].astype(int))

    return stats


# Export results to CSV
def export_results(pattern_counts: list, template_stats: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    pd.DataFrame(pattern_counts).to_csv(output_path / 'A_05_pattern_counts_per_query.csv', sep=';', index=False)
    template_stats.to_csv(output_path / 'A_05_pattern_counts_per_template.csv', sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('evaluation_dir', help='Path to Evaluation directory')
    parser.add_argument('--strategy', default='Error', help='Strategy to analyze (Error, Size, Frequency)')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    args = parser.parse_args()

    analyze_pattern_counts(args.evaluation_dir, args.strategy, args.output_dir)
