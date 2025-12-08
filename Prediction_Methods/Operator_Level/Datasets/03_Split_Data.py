#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import sys
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split


# ORCHESTRATOR
def split_workflow(input_file, output_dir, train_size, test_size, seed):
    df = load_data(input_file)
    df = add_template_column(df)
    validate_template_counts(df, train_size + test_size)
    train_queries, test_queries = split_queries_by_template(df, train_size, test_size, seed)
    train_df, test_df = filter_by_queries(df, train_queries, test_queries)
    export_splits(train_df, test_df, output_dir)


# FUNCTIONS

# Load operator dataset with child features from CSV file
def load_data(input_file):
    return pd.read_csv(input_file, delimiter=';')


# Extract template from query_file column
def add_template_column(df):
    df['template'] = df['query_file'].str.extract(r'^(Q\d+)_')[0]
    return df


# Validate each template has expected query count
def validate_template_counts(df, expected_count):
    query_counts = df.groupby('template')['query_file'].nunique()
    if not all(query_counts == expected_count):
        sys.exit(1)


# Split query_files with stratification by template
def split_queries_by_template(df, train_size, test_size, seed):
    train_queries = []
    test_queries = []

    for template in sorted(df['template'].unique()):
        template_queries = df[df['template'] == template]['query_file'].unique().tolist()
        train_q, test_q = train_test_split(
            template_queries,
            train_size=train_size,
            test_size=test_size,
            random_state=seed,
            shuffle=True
        )
        train_queries.extend(train_q)
        test_queries.extend(test_q)

    return train_queries, test_queries


# Filter dataframe by query lists
def filter_by_queries(df, train_queries, test_queries):
    train_df = df[df['query_file'].isin(train_queries)].reset_index(drop=True)
    test_df = df[df['query_file'].isin(test_queries)].reset_index(drop=True)
    return train_df, test_df


# Save training and test datasets to separate CSV files
def export_splits(train_df, test_df, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    train_path = output_path / '03_training.csv'
    test_path = output_path / '03_test.csv'
    train_df.to_csv(train_path, index=False, sep=';')
    test_df.to_csv(test_path, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset with child features CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for training and test datasets")
    parser.add_argument("--train-size", type=int, default=120, help="Queries per template for training")
    parser.add_argument("--test-size", type=int, default=30, help="Queries per template for testing")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")

    args = parser.parse_args()

    split_workflow(args.input_file, args.output_dir, args.train_size, args.test_size, args.seed)
