#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR

def template_operators_workflow(predictions_csv, templates, output_dir):
    df = load_predictions(predictions_csv)
    df = filter_templates(df, templates)
    counts = count_operators(df)
    export_results(counts, templates, output_dir)


# FUNCTIONS

# Load predictions from CSV file
def load_predictions(predictions_csv):
    return pd.read_csv(predictions_csv, delimiter=';')


# Extract template from query filename
def extract_template(query_file):
    return query_file.split('_')[0]


# Filter dataframe to specified templates
def filter_templates(df, templates):
    df['template'] = df['query_file'].apply(extract_template)
    return df[df['template'].isin(templates)]


# Count operator occurrences and sort descending
def count_operators(df):
    counts = df.groupby('node_type').size().reset_index(name='count')
    return counts.sort_values('count', ascending=False)


# Export operator counts to CSV
def export_results(counts, templates, output_dir):
    output_path = Path(output_dir) / 'Evaluation'
    output_path.mkdir(parents=True, exist_ok=True)

    templates_str = '_'.join(sorted(templates))
    output_file = output_path / f'A_01b_template_operators_{templates_str}.csv'
    counts.to_csv(output_file, index=False, sep=';')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions_csv", help="Path to predictions CSV file")
    parser.add_argument("--templates", required=True, help="Comma-separated templates (e.g. Q10,Q7,Q8)")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    templates = [t.strip() for t in args.templates.split(',')]
    template_operators_workflow(args.predictions_csv, templates, args.output_dir)
