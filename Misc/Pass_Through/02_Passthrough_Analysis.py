#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime


# ORCHESTRATOR
def analyze_passthrough(input_file: str, output_dir: str) -> None:
    df = load_data(input_file)
    ratios = compute_passthrough_ratios(df)
    export_results(ratios, output_dir)


# FUNCTIONS

# Load operator dataset
def load_data(input_file: str) -> pd.DataFrame:
    return pd.read_csv(input_file, delimiter=';')


# Compute passthrough ratio for each operator type
def compute_passthrough_ratios(df: pd.DataFrame) -> pd.DataFrame:
    records = []

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        children_map = build_children_map(query_ops)

        for idx, row in query_ops.iterrows():
            parent_type = row['node_type']
            parent_time = row['actual_total_time']
            parent_node_id = row['node_id']

            children = children_map.get(parent_node_id, [])

            if not children:
                continue

            max_child_time = max(c['actual_total_time'] for c in children)

            if max_child_time > 0:
                ratio = (parent_time / max_child_time) * 100
            else:
                ratio = None

            records.append({
                'node_type': parent_type,
                'parent_time': parent_time,
                'max_child_time': max_child_time,
                'ratio': ratio
            })

    records_df = pd.DataFrame(records)

    result = records_df.groupby('node_type').agg(
        instance_count=('ratio', 'count'),
        mean_parent_time=('parent_time', 'mean'),
        mean_max_child_time=('max_child_time', 'mean'),
        ratio_pct=('ratio', 'mean')
    ).reset_index()

    return result.sort_values('ratio_pct')


# Build map of direct children for each node
def build_children_map(query_ops: pd.DataFrame) -> dict:
    children_map = {}

    for idx in range(len(query_ops)):
        current_row = query_ops.iloc[idx]
        current_depth = current_row['depth']
        current_node_id = current_row['node_id']

        children = []

        for j in range(idx + 1, len(query_ops)):
            next_row = query_ops.iloc[j]

            if next_row['depth'] == current_depth + 1:
                children.append({
                    'node_id': next_row['node_id'],
                    'node_type': next_row['node_type'],
                    'actual_total_time': next_row['actual_total_time']
                })
            elif next_row['depth'] <= current_depth:
                break

        children_map[current_node_id] = children

    return children_map


# Export results to CSV
def export_results(results: pd.DataFrame, output_dir: str) -> None:
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = csv_dir / f'02_passthrough_analysis_{timestamp}.csv'
    results.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    analyze_passthrough(args.input_file, args.output_dir)
