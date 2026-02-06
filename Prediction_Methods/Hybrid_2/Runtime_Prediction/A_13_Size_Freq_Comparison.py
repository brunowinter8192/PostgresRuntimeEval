#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def comparison_workflow(evaluation_dir: str, output_dir: str) -> None:
    size_patterns = get_template_patterns(evaluation_dir, 'Size')
    freq_patterns = get_template_patterns(evaluation_dir, 'Frequency')
    comparison = compare_templates(size_patterns, freq_patterns)
    export_results(comparison, output_dir)


# FUNCTIONS

# Extract unique pattern hashes per template from predictions CSV
def get_template_patterns(evaluation_dir: str, strategy: str) -> dict:
    predictions_file = Path(evaluation_dir) / strategy / 'Baseline' / '12_predictions.csv'
    df = pd.read_csv(predictions_file, delimiter=';')
    df_patterns = df[df['prediction_type'] == 'pattern'].dropna(subset=['pattern_hash'])
    df_patterns = df_patterns.assign(template=df_patterns['query_file'].str.split('_').str[0])
    result = {}
    for template, group in df_patterns.groupby('template'):
        result[template] = set(group['pattern_hash'].str[:12].unique())
    return result


# Compare Size vs Frequency patterns per template
def compare_templates(size_patterns: dict, freq_patterns: dict) -> pd.DataFrame:
    rows = []
    for t in TEMPLATES:
        s = size_patterns.get(t, set())
        f = freq_patterns.get(t, set())
        rows.append({
            'template': t,
            'size_patterns': ','.join(sorted(s)),
            'frequency_patterns': ','.join(sorted(f)),
            'match': s == f,
            'status': 'IDENTICAL' if s == f else 'DIFFERS'
        })
    return pd.DataFrame(rows)


# Export comparison to CSV
def export_results(comparison: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    comparison.to_csv(output_path / 'A_13_template_comparison.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("evaluation_dir", help="Path to Evaluation directory (contains Size/, Frequency/)")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    comparison_workflow(args.evaluation_dir, args.output_dir)
