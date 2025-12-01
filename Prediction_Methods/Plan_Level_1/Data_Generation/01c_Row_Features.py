#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path

import pandas as pd
import psycopg2

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Database connection settings
from mapping_config import DB_CONFIG


# ORCHESTRATOR

# Extract row and byte count features from plan tree traversal
def row_feature_extraction_workflow(query_dir: Path, output_dir: Path) -> None:
    query_files = get_all_query_files(query_dir)
    conn = psycopg2.connect(**DB_CONFIG)
    results = extract_row_features_from_queries(conn, query_files)
    conn.close()
    df = build_feature_dataframe(results)
    df_sorted = sort_by_template_and_seed(df)
    export_features(df_sorted, output_dir)


# FUNCTIONS

# Collect all SQL query files from template directories
def get_all_query_files(query_dir: Path) -> list:
    all_files = []
    query_dirs = sorted([d for d in query_dir.iterdir() if d.is_dir() and d.name.startswith('Q')])
    for qdir in query_dirs:
        all_files.extend(sorted(qdir.glob('Q*.sql')))
    return all_files


# Extract row and byte features from all query files
def extract_row_features_from_queries(conn, query_files: list) -> list:
    results = []
    for query_file in query_files:
        with open(query_file, 'r') as f:
            query = f.read().strip()

        json_output = get_explain_json(conn, query)
        plan = json_output[0]["Plan"]
        row_count = calculate_row_count(plan)
        byte_count = calculate_byte_count(plan)

        results.append({
            'query_file': query_file.name,
            'template': query_file.parent.name,
            'row_count': row_count,
            'byte_count': byte_count
        })

    return results


# Get EXPLAIN JSON output from PostgreSQL
def get_explain_json(conn, query: str):
    conn.rollback()
    cursor = conn.cursor()
    explain_query = f"EXPLAIN (ANALYZE false, VERBOSE true, COSTS true, SUMMARY true, FORMAT JSON) {query}"
    cursor.execute(explain_query)
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    return result[0][0]


# Calculate total row count through plan tree traversal
def calculate_row_count(node) -> int:
    output_rows = node.get("Plan Rows", 0)
    children = node.get("Plans", [])

    non_initplan_children = [
        child for child in children
        if child.get("Parent Relationship") != "InitPlan"
    ]

    input_rows = sum(child.get("Plan Rows", 0) for child in non_initplan_children)
    my_contribution = input_rows + output_rows
    children_total = sum(calculate_row_count(child) for child in children)

    return my_contribution + children_total


# Calculate total byte count through plan tree traversal
def calculate_byte_count(node) -> int:
    output_rows = node.get("Plan Rows", 0)
    output_width = node.get("Plan Width", 0)
    output_bytes = output_rows * output_width

    children = node.get("Plans", [])

    non_initplan_children = [
        child for child in children
        if child.get("Parent Relationship") != "InitPlan"
    ]

    input_bytes = sum(
        child.get("Plan Rows", 0) * child.get("Plan Width", 0)
        for child in non_initplan_children
    )

    my_contribution = input_bytes + output_bytes
    children_total = sum(calculate_byte_count(child) for child in children)

    return my_contribution + children_total


# Build pandas DataFrame from results
def build_feature_dataframe(results: list) -> pd.DataFrame:
    return pd.DataFrame(results)


# Sort dataframe by template number and seed number
def sort_by_template_and_seed(df: pd.DataFrame) -> pd.DataFrame:
    df['template_num'] = df['template'].str.extract(r'Q(\d+)').astype(int)
    df['seed_num'] = df['query_file'].str.extract(r'Q\d+_(\d+)_seed').astype(int)
    df = df.sort_values(['template_num', 'seed_num']).drop(columns=['template_num', 'seed_num'])
    df = df.reset_index(drop=True)
    return df


# Export features to CSV file with semicolon delimiter
def export_features(df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    csv_path = output_dir / '01c_row_features.csv'
    df.to_csv(csv_path, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract row and byte count features from plan tree")
    parser.add_argument("query_dir", help="Directory containing Q* template folders with SQL files")
    parser.add_argument("--output-dir", default=None, help="Output directory for CSV (default: script_dir/csv)")

    args = parser.parse_args()

    query_path = Path(args.query_dir)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'csv'

    row_feature_extraction_workflow(query_path, output_path)
