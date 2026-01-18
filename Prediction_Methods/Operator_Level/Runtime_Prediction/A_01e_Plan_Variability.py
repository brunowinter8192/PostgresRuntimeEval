#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR

def plan_variability_workflow(predictions_csv, output_dir):
    df = load_predictions(predictions_csv)
    df = add_template_column(df)
    signatures = compute_plan_signatures(df)
    summary = analyze_variability(signatures)
    export_results(summary, signatures, output_dir)


# FUNCTIONS

# Load predictions from CSV file
def load_predictions(predictions_csv):
    return pd.read_csv(predictions_csv, delimiter=';')


# Add template column extracted from query filename
def add_template_column(df):
    df['template'] = df['query_file'].apply(lambda x: x.split('_')[0])
    return df


# Compute plan signature for each query (sorted tuple of depth + node_type)
def compute_plan_signatures(df):
    signatures = {}
    for query_file, group in df.groupby('query_file'):
        template = group['template'].iloc[0]
        sig = tuple(sorted(zip(group['depth'], group['node_type'])))
        if template not in signatures:
            signatures[template] = {}
        if sig not in signatures[template]:
            signatures[template][sig] = []
        signatures[template][sig].append(query_file)
    return signatures


# Analyze variability per template
def analyze_variability(signatures):
    results = []
    for template in sorted(signatures.keys(), key=lambda x: int(x[1:])):
        plans = signatures[template]
        n_unique = len(plans)
        n_queries = sum(len(q) for q in plans.values())
        results.append({
            'template': template,
            'n_queries': n_queries,
            'n_unique_plans': n_unique,
            'has_variability': 'yes' if n_unique > 1 else 'no'
        })
    return pd.DataFrame(results)


# Export summary and detail to CSV
def export_results(summary, signatures, output_dir):
    output_path = Path(output_dir) / 'Evaluation'
    output_path.mkdir(parents=True, exist_ok=True)
    summary_file = output_path / 'A_01e_plan_variability_summary.csv'
    summary.to_csv(summary_file, index=False, sep=';')

    detail_rows = []
    for template, plans in signatures.items():
        for plan_idx, (sig, queries) in enumerate(plans.items()):
            for query in queries:
                detail_rows.append({
                    'template': template,
                    'query_file': query,
                    'plan_variant': plan_idx + 1,
                    'plan_signature': str(sig)
                })
    detail_df = pd.DataFrame(detail_rows)
    detail_file = output_path / 'A_01e_plan_variability_detail.csv'
    detail_df.to_csv(detail_file, index=False, sep=';')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions_csv", help="Path to predictions CSV file")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    plan_variability_workflow(args.predictions_csv, args.output_dir)
