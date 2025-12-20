#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import re
from pathlib import Path
from collections import defaultdict

# ORCHESTRATOR
def pattern_analysis_workflow(run_dir, output_dir):
    selected_data = collect_selected_patterns(run_dir)
    used_data = collect_used_patterns(run_dir)

    selected_stats = aggregate_pattern_stats(selected_data, "selected")
    used_stats = aggregate_pattern_stats(used_data, "used")

    comparison = create_comparison(selected_stats, used_stats)

    export_results(selected_stats, used_stats, comparison, output_dir)

# FUNCTIONS

# Collect all SELECTED patterns from selection_log.csv (status=ACCEPTED)
def collect_selected_patterns(run_dir):
    run_path = Path(run_dir)
    csv_files = list(run_path.glob('*/csv/selection_log.csv'))

    results = []
    for csv_file in csv_files:
        df = pd.read_csv(csv_file, delimiter=';')
        accepted = df[df['status'] == 'ACCEPTED']

        query_folder = csv_file.parent.parent.name
        template = query_folder.split('_')[0]

        for _, row in accepted.iterrows():
            results.append({
                'pattern_hash': row['pattern_hash'],
                'pattern_string': row['pattern_string'],
                'query_folder': query_folder,
                'template': template
            })

    return pd.DataFrame(results) if results else pd.DataFrame()

# Collect all USED patterns from report.md (Pattern Assignments section)
def collect_used_patterns(run_dir):
    run_path = Path(run_dir)
    report_files = list(run_path.glob('*/md/report.md'))

    results = []
    for report_file in report_files:
        query_folder = report_file.parent.parent.name
        template = query_folder.split('_')[0]

        content = report_file.read_text()

        pattern_section = re.search(r'## Pattern Assignments\s*\n\|[^\n]+\n\|[-\s|]+\n((?:\|[^\n]+\n)*)', content)
        if pattern_section:
            rows = pattern_section.group(1).strip().split('\n')
            for row in rows:
                if not row.strip():
                    continue
                parts = [p.strip() for p in row.split('|')[1:-1]]
                if len(parts) >= 2:
                    pattern_string = parts[0]
                    pattern_hash = parts[1]
                    results.append({
                        'pattern_hash': pattern_hash,
                        'pattern_string': pattern_string,
                        'query_folder': query_folder,
                        'template': template
                    })

    return pd.DataFrame(results) if results else pd.DataFrame()

# Aggregate pattern statistics
def aggregate_pattern_stats(df, label):
    if df.empty:
        return pd.DataFrame()

    pattern_data = defaultdict(lambda: {
        'pattern_string': '',
        'count': 0,
        'templates': set(),
        'queries': set()
    })

    for _, row in df.iterrows():
        phash = row['pattern_hash']
        pattern_data[phash]['pattern_string'] = row['pattern_string']
        pattern_data[phash]['count'] += 1
        pattern_data[phash]['templates'].add(row['template'])
        pattern_data[phash]['queries'].add(row['query_folder'])

    rows = []
    for phash, data in pattern_data.items():
        rows.append({
            'pattern_hash': phash,
            'pattern_string': data['pattern_string'],
            f'{label}_count': data['count'],
            'template_count': len(data['templates']),
            'templates': ','.join(sorted(data['templates'], key=lambda x: int(x[1:]))),
            'query_count': len(data['queries'])
        })

    result = pd.DataFrame(rows)
    result = result.sort_values(f'{label}_count', ascending=False)
    return result

# Create comparison between selected and used (handles truncated hashes)
def create_comparison(selected_stats, used_stats):
    if selected_stats.empty or used_stats.empty:
        return pd.DataFrame()

    used_hash_map = {row['pattern_hash'][:8]: row for _, row in used_stats.iterrows()}

    rows = []
    for _, sel_row in selected_stats.iterrows():
        phash = sel_row['pattern_hash']
        short_hash = phash[:8]

        if short_hash in used_hash_map:
            used_row = used_hash_map[short_hash]
            rows.append({
                'pattern_hash': phash,
                'pattern_string': sel_row['pattern_string'],
                'selected_count': sel_row['selected_count'],
                'used_count': used_row['used_count'],
                'usage_rate': f"{used_row['used_count'] / sel_row['selected_count'] * 100:.1f}%",
                'templates': sel_row['templates'],
                'status': 'USED'
            })
        else:
            rows.append({
                'pattern_hash': phash,
                'pattern_string': sel_row['pattern_string'],
                'selected_count': sel_row['selected_count'],
                'used_count': 0,
                'usage_rate': '0%',
                'templates': sel_row['templates'],
                'status': 'NEVER_USED'
            })

    return pd.DataFrame(rows).sort_values('selected_count', ascending=False)

# Export results to CSV
def export_results(selected_stats, used_stats, comparison, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not selected_stats.empty:
        selected_stats.to_csv(output_path / 'patterns_selected.csv', sep=';', index=False)

    if not used_stats.empty:
        used_stats.to_csv(output_path / 'patterns_used.csv', sep=';', index=False)

    if not comparison.empty:
        comparison.to_csv(output_path / 'patterns_comparison.csv', sep=';', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", help="Run directory (e.g. Evaluation/Error)")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()
    pattern_analysis_workflow(args.run_dir, args.output_dir)
