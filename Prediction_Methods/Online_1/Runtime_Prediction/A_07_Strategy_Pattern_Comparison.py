#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import re
import pandas as pd
from pathlib import Path

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
STRATEGIES = ['Error', 'Size', 'Frequency']


# ORCHESTRATOR
def comparison_workflow(evaluation_dir: str, output_dir: str) -> None:
    patterns_by_strategy = collect_all_patterns(evaluation_dir)
    combined = merge_patterns(patterns_by_strategy)
    export_csv(combined, output_dir)


# FUNCTIONS

# Collect used patterns for all strategies
def collect_all_patterns(evaluation_dir: str) -> dict:
    eval_path = Path(evaluation_dir)
    result = {}

    for strategy in STRATEGIES:
        result[strategy] = collect_strategy_patterns(eval_path / strategy)

    return result


# Collect USED patterns for one strategy
def collect_strategy_patterns(strategy_dir: Path) -> dict:
    patterns = {}

    if not strategy_dir.exists():
        return patterns

    for query_dir in strategy_dir.iterdir():
        if not query_dir.is_dir() or not query_dir.name.startswith('Q'):
            continue

        template = query_dir.name.split('_')[0]
        report_file = query_dir / 'md' / 'report.md'
        selection_log = query_dir / 'csv' / 'selection_log.csv'

        if not report_file.exists():
            continue

        used_hashes = extract_used_hashes(report_file)
        pattern_info = load_pattern_info(selection_log)

        for pattern_hash in used_hashes:
            key = f"{template}_{pattern_hash}"

            if key not in patterns and pattern_hash in pattern_info:
                info = pattern_info[pattern_hash]
                patterns[key] = {
                    'template': template,
                    'pattern_hash': pattern_hash,
                    'pattern_string': info['pattern_string'],
                    'pattern_length': info['pattern_length']
                }

    return patterns


# Extract used pattern hashes from report.md Pattern Assignments
def extract_used_hashes(report_file: Path) -> set:
    content = report_file.read_text()
    used_hashes = set()

    pattern_section = re.search(r'## Pattern Assignments\s*\n\|[^\n]+\n\|[-\s|]+\n((?:\|[^\n]+\n)*)', content)
    if pattern_section:
        rows = pattern_section.group(1).strip().split('\n')
        for row in rows:
            if not row.strip():
                continue
            parts = [p.strip() for p in row.split('|')[1:-1]]
            if len(parts) >= 2:
                pattern_hash = parts[1]
                used_hashes.add(pattern_hash)

    return used_hashes


# Load pattern info (full string, length) from selection_log.csv
def load_pattern_info(selection_log: Path) -> dict:
    info = {}

    if not selection_log.exists():
        return info

    df = pd.read_csv(selection_log, delimiter=';')

    for _, row in df.iterrows():
        full_hash = row['pattern_hash']
        short_hash = full_hash[:8]
        pattern_string = row['pattern_string']
        pattern_length = len(pattern_string.split(' -> '))

        info[short_hash] = {
            'pattern_string': pattern_string,
            'pattern_length': pattern_length
        }

    return info


# Merge patterns from all strategies and determine source
def merge_patterns(patterns_by_strategy: dict) -> pd.DataFrame:
    all_keys = set()
    for strategy_patterns in patterns_by_strategy.values():
        all_keys.update(strategy_patterns.keys())

    rows = []
    for key in all_keys:
        in_strategies = []
        pattern_info = None

        for strategy in STRATEGIES:
            if key in patterns_by_strategy[strategy]:
                in_strategies.append(strategy.lower())
                if pattern_info is None:
                    pattern_info = patterns_by_strategy[strategy][key]

        if len(in_strategies) == 3:
            source = 'all'
        elif len(in_strategies) == 2:
            source = '+'.join(sorted(in_strategies))
        else:
            source = in_strategies[0]

        rows.append({
            'template': pattern_info['template'],
            'pattern_hash': pattern_info['pattern_hash'],
            'pattern_string': pattern_info['pattern_string'],
            'pattern_length': pattern_info['pattern_length'],
            'source': source
        })

    df = pd.DataFrame(rows)
    template_order = {t: i for i, t in enumerate(TEMPLATES)}
    df['order'] = df['template'].map(template_order)
    df = df.sort_values(['order', 'pattern_length'], ascending=[True, False]).drop(columns=['order'])

    return df


# Export CSV
def export_csv(df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path / 'A_07_strategy_pattern_comparison.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("evaluation_dir", help="Path to Evaluation directory")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(args.evaluation_dir, args.output_dir)
