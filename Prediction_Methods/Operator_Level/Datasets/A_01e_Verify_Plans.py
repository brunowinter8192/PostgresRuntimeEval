#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import hashlib
import pandas as pd
from pathlib import Path


# ORCHESTRATOR

def verify_plans_workflow(dataset_csv, output_dir):
    df = load_dataset(dataset_csv)
    df = add_plan_hash_column(df)
    df = add_template_column(df)
    distribution = compute_distribution(df)
    export_distribution(distribution, output_dir)


# FUNCTIONS

# Load dataset from CSV file
def load_dataset(dataset_csv):
    return pd.read_csv(dataset_csv, delimiter=';')


# Compute hash for unique plan structure (operator types + depths + relationships)
def compute_plan_hash(query_ops):
    sorted_ops = query_ops.sort_values('node_id')
    structure = [(row['node_type'], row['depth'], row['parent_relationship'])
                 for _, row in sorted_ops.iterrows()]
    return hashlib.md5(str(structure).encode()).hexdigest()


# Add plan_hash column for each query_file
def add_plan_hash_column(df):
    plan_hashes = {}
    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file]
        plan_hashes[query_file] = compute_plan_hash(query_ops)
    df['plan_hash'] = df['query_file'].map(plan_hashes)
    return df


# Add template column extracted from query filename
def add_template_column(df):
    if 'template' not in df.columns:
        df['template'] = df['query_file'].apply(lambda x: x.split('_')[0])
    return df


# Compute distribution of plan hashes per template
def compute_distribution(df):
    distribution = df.groupby(['template', 'plan_hash']).agg({
        'query_file': 'nunique'
    }).reset_index()
    distribution.columns = ['template', 'plan_hash', 'query_count']
    distribution['plan_hash_short'] = distribution['plan_hash'].apply(lambda x: x[:8])
    distribution = distribution.sort_values(['template', 'query_count'], ascending=[True, False])
    return distribution


# Export distribution to CSV
def export_distribution(distribution, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / 'plan_hash_distribution.csv'
    distribution.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_csv", help="Path to dataset CSV (training.csv or test.csv)")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    verify_plans_workflow(args.dataset_csv, args.output_dir)
