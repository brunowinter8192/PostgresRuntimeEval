#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import re
import pandas as pd
from pathlib import Path

# ORCHESTRATOR
def split_workflow(input_file, output_dir):
    df = load_data(input_file)
    train_df, test_df = split_by_seeds(df, 120, 30)
    export_splits(train_df, test_df, output_dir)

# FUNCTIONS

# Load operator dataset with child features from CSV file
def load_data(input_file):
    return pd.read_csv(input_file, delimiter=';')


# Extract template and seed number from query filename
def extract_template_seed(query_file):
    match = re.match(r'(Q\d+)_(\d+)_seed_', query_file)
    if match:
        template = match.group(1)
        seed = int(match.group(2))
        return template, seed
    return None, None


# Split dataset into training and test sets using seed ranges per template
def split_by_seeds(df, train_count, test_count):
    df = df.copy()
    df['template'] = df['query_file'].apply(lambda x: extract_template_seed(x)[0])
    df['seed'] = df['query_file'].apply(lambda x: extract_template_seed(x)[1])
    
    templates = sorted(df['template'].unique())
    
    train_rows = []
    test_rows = []
    
    for template in templates:
        template_df = df[df['template'] == template].copy()
        unique_seeds = sorted(template_df['seed'].unique())
        
        train_seeds = unique_seeds[:train_count]
        test_seeds = unique_seeds[-test_count:]
        
        train_data = template_df[template_df['seed'].isin(train_seeds)]
        test_data = template_df[template_df['seed'].isin(test_seeds)]
        
        train_rows.append(train_data)
        test_rows.append(test_data)
    
    train_df = pd.concat(train_rows, ignore_index=True)
    test_df = pd.concat(test_rows, ignore_index=True)
    
    train_df = train_df.drop(columns=['template', 'seed'])
    test_df = test_df.drop(columns=['template', 'seed'])
    
    return train_df, test_df


# Save training and test datasets to separate CSV files
def export_splits(train_df, test_df, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    train_path = output_path / '04_training.csv'
    test_path = output_path / '04_test.csv'
    train_df.to_csv(train_path, index=False, sep=';')
    test_df.to_csv(test_path, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset with child features CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for training and test datasets")

    args = parser.parse_args()

    split_workflow(args.input_file, args.output_dir)
