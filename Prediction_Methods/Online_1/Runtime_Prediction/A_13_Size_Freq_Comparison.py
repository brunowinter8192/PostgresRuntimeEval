#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import re
import pandas as pd
from pathlib import Path

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def comparison_workflow(evaluation_dir: str, output_dir: str) -> None:
    queries = get_all_queries(evaluation_dir)
    query_results = compare_all_queries(evaluation_dir, queries)
    template_summary = aggregate_to_templates(query_results)
    differences = collect_differences(query_results)
    export_results(template_summary, differences, output_dir)


# FUNCTIONS

# Get sorted list of all query folders present in both Size and Frequency
def get_all_queries(evaluation_dir: str) -> list:
    size_dir = Path(evaluation_dir) / 'Size'
    freq_dir = Path(evaluation_dir) / 'Frequency'
    size_queries = {d.name for d in size_dir.iterdir() if d.is_dir() and d.name.startswith('Q')}
    freq_queries = {d.name for d in freq_dir.iterdir() if d.is_dir() and d.name.startswith('Q')}
    return sorted(size_queries & freq_queries)


# Extract assigned pattern hashes from report.md Query Tree section
def get_assigned_patterns(evaluation_dir: str, strategy: str, query: str) -> set:
    report_file = Path(evaluation_dir) / strategy / query / 'md' / 'report.md'
    if not report_file.exists():
        return set()
    content = report_file.read_text()
    return set(re.findall(r'\[PATTERN: (\w+)\]', content))


# Compare used patterns for all queries between Size and Frequency
def compare_all_queries(evaluation_dir: str, queries: list) -> list:
    results = []
    for query in queries:
        size_patterns = get_assigned_patterns(evaluation_dir, 'Size', query)
        freq_patterns = get_assigned_patterns(evaluation_dir, 'Frequency', query)
        template = query.split('_')[0]
        results.append({
            'template': template,
            'query': query,
            'size_patterns': size_patterns,
            'freq_patterns': freq_patterns,
            'match': size_patterns == freq_patterns
        })
    return results


# Aggregate query-level results to template-level summary
def aggregate_to_templates(query_results: list) -> pd.DataFrame:
    template_data = {}
    for r in query_results:
        t = r['template']
        if t not in template_data:
            template_data[t] = {'total': 0, 'same': 0, 'different': 0}
        template_data[t]['total'] += 1
        if r['match']:
            template_data[t]['same'] += 1
        else:
            template_data[t]['different'] += 1

    rows = []
    for t in TEMPLATES:
        if t not in template_data:
            continue
        d = template_data[t]
        match_rate = round(d['same'] / d['total'] * 100, 1)
        rows.append({
            'template': t,
            'total_queries': d['total'],
            'queries_same': d['same'],
            'queries_different': d['different'],
            'match_rate': match_rate,
            'status': 'IDENTICAL' if d['different'] == 0 else 'DIFFERS'
        })

    return pd.DataFrame(rows)


# Collect detail rows for queries where Size != Frequency
def collect_differences(query_results: list) -> pd.DataFrame:
    rows = []
    for r in query_results:
        if r['match']:
            continue
        only_size = r['size_patterns'] - r['freq_patterns']
        only_freq = r['freq_patterns'] - r['size_patterns']
        rows.append({
            'template': r['template'],
            'query': r['query'],
            'size_patterns': ','.join(sorted(r['size_patterns'])),
            'frequency_patterns': ','.join(sorted(r['freq_patterns'])),
            'only_size': ','.join(sorted(only_size)),
            'only_frequency': ','.join(sorted(only_freq))
        })

    return pd.DataFrame(rows)


# Export template summary and query differences to CSV
def export_results(template_summary: pd.DataFrame, differences: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    template_summary.to_csv(output_path / 'A_13_template_comparison.csv', sep=';', index=False)
    if not differences.empty:
        differences.to_csv(output_path / 'A_13_query_differences.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("evaluation_dir", help="Path to Evaluation directory (contains Size/, Frequency/)")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(args.evaluation_dir, args.output_dir)
