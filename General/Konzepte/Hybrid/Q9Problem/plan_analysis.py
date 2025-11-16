#!/usr/bin/env python3

# Infrastructure
import pandas as pd
from pathlib import Path
from datetime import datetime
import hashlib

INPUT_FILE = Path('/Users/brunowinter2000/Documents/Thesis/2025_2026/Operator-Level/Datasets/Baseline_SVM/operator_dataset_cleaned.csv')
OUTPUT_DIR = Path('/Users/brunowinter2000/Documents/Thesis/2025_2026/Hybrid/Konzept/csv')

# Orchestrator
def analyze_all_templates():
    df = load_data()
    df_main = filter_main_plan(df)
    templates = get_all_templates(df_main)
    all_results = []
    
    for template in templates:
        queries = filter_template(df_main, template)
        plan_signatures = extract_plan_signatures(queries, df_main)
        template_results = aggregate_plan_counts(plan_signatures, template)
        all_results.append(template_results)
    
    combined_results = combine_results(all_results)
    export_results(combined_results)

# Load dataset with semicolon delimiter
def load_data():
    return pd.read_csv(INPUT_FILE, delimiter=';')

# Filter only main plan operators (exclude sub/init plans)
def filter_main_plan(df):
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]

# Get all unique templates
def get_all_templates(df):
    df['template'] = df['query_file'].str.extract(r'^(Q\d+)_')[0]
    return sorted(df['template'].unique())

# Filter queries for specific template
def filter_template(df, template):
    df['template'] = df['query_file'].str.extract(r'^(Q\d+)_')[0]
    return df[df['template'] == template]['query_file'].unique()

# Extract plan signature for each query
def extract_plan_signatures(queries, df_main):
    signatures = []
    
    for query_file in queries:
        query_ops = df_main[df_main['query_file'] == query_file].sort_values('node_id')
        
        plan_structure = []
        for _, row in query_ops.iterrows():
            rel = row['parent_relationship'] if pd.notna(row['parent_relationship']) else 'Root'
            plan_structure.append(f"{row['depth']}:{row['node_type']}:{rel}")
        
        plan_str = '|'.join(plan_structure)
        plan_hash = hashlib.md5(plan_str.encode()).hexdigest()[:8]
        
        signatures.append({
            'query_file': query_file,
            'plan_hash': plan_hash,
            'num_operators': len(query_ops)
        })
    
    return pd.DataFrame(signatures)

# Count occurrences of each unique plan
def aggregate_plan_counts(df_signatures, template):
    grouped = df_signatures.groupby('plan_hash').agg({
        'query_file': 'count',
        'num_operators': 'first'
    }).reset_index()
    
    grouped.columns = ['plan_hash', 'seed_count', 'num_operators']
    grouped['template'] = template
    grouped = grouped.sort_values('seed_count', ascending=False)
    
    return grouped[['template', 'plan_hash', 'seed_count', 'num_operators']]

# Combine all template results
def combine_results(results_list):
    return pd.concat(results_list, ignore_index=True)

# Save analysis results to CSV
def export_results(results):
    OUTPUT_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = OUTPUT_DIR / f'all_templates_plan_analysis_{timestamp}.csv'
    results.to_csv(output_file, sep=';', index=False)

if __name__ == '__main__':
    analyze_all_templates()
