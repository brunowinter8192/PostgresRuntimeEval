#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import re
import pandas as pd
from pathlib import Path

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']

SCRIPT_DIR = Path(__file__).resolve().parent
DYNAMIC_PREDICTIONS_DIR = SCRIPT_DIR
DYNAMIC_PATTERNS_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Hybrid_1'


# ORCHESTRATOR
def comparison_workflow(static_predictions: str, static_patterns: str, output_dir: str) -> None:
    static_pattern_info = load_static_pattern_info(static_patterns)
    static_used = collect_static_patterns(static_predictions, static_pattern_info)
    dynamic_used = collect_dynamic_patterns()
    combined = merge_patterns(static_used, dynamic_used)
    export_csv(combined, output_dir)


# FUNCTIONS

# Load pattern info (hash -> string, length) from static patterns.csv
def load_static_pattern_info(patterns_file: str) -> dict:
    df = pd.read_csv(patterns_file, delimiter=';')
    info = {}
    for _, row in df.iterrows():
        info[row['pattern_hash']] = {
            'pattern_string': row['pattern_string'],
            'pattern_length': int(row['pattern_length'])
        }
    return info


# Extract template from query_file (e.g., Q1_100_seed_xxx -> Q1)
def extract_template(query_file: str) -> str:
    match = re.match(r'(Q\d+)_', query_file)
    return match.group(1) if match else None


# Collect unique patterns used in static predictions per template
def collect_static_patterns(predictions_file: str, pattern_info: dict) -> list:
    df = pd.read_csv(predictions_file, delimiter=';')
    df['template'] = df['query_file'].apply(extract_template)
    pattern_preds = df[df['prediction_type'] == 'pattern']

    rows = []
    for template in TEMPLATES:
        template_patterns = pattern_preds[pattern_preds['template'] == template]
        unique_hashes = template_patterns['pattern_hash'].unique()

        for ph in unique_hashes:
            info = pattern_info.get(ph, {})
            rows.append({
                'template': template,
                'pattern_hash': ph,
                'pattern_string': info.get('pattern_string', ''),
                'pattern_length': info.get('pattern_length', 0),
                'source': 'static'
            })

    return rows


# Collect unique patterns used in dynamic predictions per template
def collect_dynamic_patterns() -> list:
    rows = []

    for template in TEMPLATES:
        predictions_file = DYNAMIC_PREDICTIONS_DIR / template / 'approach_3' / 'predictions.csv'
        patterns_file = DYNAMIC_PATTERNS_DIR / template / 'approach_3' / 'used_patterns.csv'

        if not predictions_file.exists() or not patterns_file.exists():
            continue

        df_pred = pd.read_csv(predictions_file, delimiter=';')
        df_patterns = pd.read_csv(patterns_file, delimiter=';')

        pattern_info = {}
        for _, row in df_patterns.iterrows():
            pattern_info[row['pattern_hash']] = {
                'pattern_string': row['pattern_string'],
                'pattern_length': int(row['pattern_length'])
            }

        pattern_preds = df_pred[df_pred['prediction_type'] == 'pattern']
        unique_hashes = pattern_preds['pattern_hash'].unique()

        for ph in unique_hashes:
            info = pattern_info.get(ph, {})
            rows.append({
                'template': template,
                'pattern_hash': ph,
                'pattern_string': info.get('pattern_string', ''),
                'pattern_length': info.get('pattern_length', 0),
                'source': 'dynamic'
            })

    return rows


# Merge static and dynamic patterns, mark overlaps as 'both'
def merge_patterns(static_rows: list, dynamic_rows: list) -> pd.DataFrame:
    df_static = pd.DataFrame(static_rows)
    df_dynamic = pd.DataFrame(dynamic_rows)

    df_static['key'] = df_static['template'] + '_' + df_static['pattern_hash']
    df_dynamic['key'] = df_dynamic['template'] + '_' + df_dynamic['pattern_hash']

    static_keys = set(df_static['key'])
    dynamic_keys = set(df_dynamic['key'])
    both_keys = static_keys & dynamic_keys

    results = []

    for _, row in df_static.iterrows():
        source = 'both' if row['key'] in both_keys else 'static'
        results.append({
            'template': row['template'],
            'pattern_hash': row['pattern_hash'],
            'pattern_string': row['pattern_string'],
            'pattern_length': row['pattern_length'],
            'source': source
        })

    for _, row in df_dynamic.iterrows():
        if row['key'] not in both_keys:
            results.append({
                'template': row['template'],
                'pattern_hash': row['pattern_hash'],
                'pattern_string': row['pattern_string'],
                'pattern_length': row['pattern_length'],
                'source': 'dynamic'
            })

    df = pd.DataFrame(results)
    template_order = {t: i for i, t in enumerate(TEMPLATES)}
    df['order'] = df['template'].map(template_order)
    df = df.sort_values(['order', 'pattern_length'], ascending=[True, False]).drop(columns=['order'])

    return df


# Export combined CSV
def export_csv(df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path / 'A_01c_pattern_comparison.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--static-predictions", required=True, help="Path to static predictions.csv")
    parser.add_argument("--static-patterns", required=True, help="Path to static patterns.csv")
    parser.add_argument("--output-dir", default=str(SCRIPT_DIR / 'Evaluation' / 'approach_3'), help="Output directory")

    args = parser.parse_args()

    comparison_workflow(args.static_predictions, args.static_patterns, args.output_dir)
