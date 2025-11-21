#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from collections import defaultdict
from pathlib import Path

import pandas as pd
import psycopg2

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Database connection settings and operator types
from mapping_config import DB_CONFIG, OPERATOR_TYPES


# ORCHESTRATOR

# Extract plan-level features from EXPLAIN output for all queries
def plan_feature_extraction_workflow(query_dir: Path, output_dir: Path) -> None:
    query_files = get_all_query_files(query_dir)
    conn = psycopg2.connect(**DB_CONFIG)
    query_data = extract_features_from_queries(conn, query_files)
    conn.close()
    df = build_feature_dataframe(query_data)
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


# Extract features from all query files
def extract_features_from_queries(conn, query_files: list) -> list:
    query_data = []
    for query_file in query_files:
        with open(query_file, 'r') as f:
            query = f.read().strip()
        row_data = extract_single_query_features(conn, query, query_file)
        query_data.append(row_data)
    return query_data


# Extract all features from a single query's EXPLAIN output
def extract_single_query_features(conn, query: str, query_file: Path) -> dict:
    json_output = get_explain_json(conn, query)
    plan = json_output[0]['Plan']

    metrics = extract_root_metrics(json_output)
    node_metrics = extract_node_metrics(plan)
    op_count = sum(m['count'] for m in node_metrics.values())

    planning_time = json_output[0].get('Planning Time', 0.0)
    jit_functions = json_output[0].get('JIT', {}).get('Functions', 0)

    total_workers = extract_workers_planned(plan)
    parallel_aware_count = count_parallel_aware(plan)
    strategies = count_strategies(plan)
    partial_modes = count_partial_modes(plan)
    group_key_count = count_group_keys(plan)
    group_key_columns = count_group_key_columns(plan)
    sort_key_count = count_sort_keys(plan)
    sort_key_columns = count_sort_key_columns(plan)
    subplan_count = count_subplans(plan)
    initplan_count = count_initplans(plan)
    max_tree_depth = calculate_max_depth(plan)

    row_data = {
        'query_file': query_file.name,
        'template': query_file.parent.name,
        'p_st_cost': metrics['startup_cost'],
        'p_tot_cost': metrics['total_cost'],
        'p_rows': metrics['rows'],
        'p_width': metrics['width'],
        'op_count': op_count,
        'workers_planned': total_workers,
        'parallel_aware_count': parallel_aware_count,
        'strategy_hashed': strategies['Hashed'],
        'strategy_plain': strategies['Plain'],
        'strategy_sorted': strategies['Sorted'],
        'partial_mode_simple': partial_modes['Simple'],
        'partial_mode_partial': partial_modes['Partial'],
        'partial_mode_finalize': partial_modes['Finalize'],
        'group_key_count': group_key_count,
        'group_key_columns': group_key_columns,
        'sort_key_count': sort_key_count,
        'sort_key_columns': sort_key_columns,
        'subplan_count': subplan_count,
        'initplan_count': initplan_count,
        'max_tree_depth': max_tree_depth,
        'planning_time_ms': planning_time,
        'jit_functions': jit_functions
    }

    for node_type in OPERATOR_TYPES:
        base_name = node_type.replace(' ', '_').replace('-', '_')
        count_col = f"{base_name}_cnt"
        row_data[count_col] = node_metrics.get(node_type, {}).get('count', 0)
        rows_col = f"{base_name}_rows"
        row_data[rows_col] = node_metrics.get(node_type, {}).get('rows', 0)

    return row_data


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


# Extract root plan metrics from JSON output
def extract_root_metrics(json_output) -> dict:
    root_plan = json_output[0]["Plan"]
    return {
        'startup_cost': root_plan.get("Startup Cost", 0.0),
        'total_cost': root_plan.get("Total Cost", 0.0),
        'rows': root_plan.get("Plan Rows", 0),
        'width': root_plan.get("Plan Width", 0)
    }


# Extract operator counts and rows from plan tree
def extract_node_metrics(plan_node, node_metrics=None) -> dict:
    if node_metrics is None:
        node_metrics = defaultdict(lambda: {'count': 0, 'rows': 0})

    node_type = plan_node.get("Node Type")
    if node_type:
        node_metrics[node_type]['count'] += 1
        node_metrics[node_type]['rows'] += plan_node.get("Plan Rows", 0)

    for child in plan_node.get("Plans", []):
        extract_node_metrics(child, node_metrics)

    return dict(node_metrics)


# Count total workers planned in plan tree
def extract_workers_planned(plan_node) -> int:
    total_workers = 0
    if 'Workers Planned' in plan_node:
        total_workers += plan_node['Workers Planned']
    if 'Plans' in plan_node:
        for child_plan in plan_node['Plans']:
            total_workers += extract_workers_planned(child_plan)
    return total_workers


# Count parallel aware operators
def count_parallel_aware(plan_node) -> int:
    count = 0
    if plan_node.get('Parallel Aware') is True:
        count += 1
    if 'Plans' in plan_node:
        for child_plan in plan_node['Plans']:
            count += count_parallel_aware(child_plan)
    return count


# Count aggregation strategies in plan tree
def count_strategies(plan_node) -> dict:
    strategies = {'Hashed': 0, 'Plain': 0, 'Sorted': 0}
    if 'Strategy' in plan_node:
        strategy = plan_node['Strategy']
        if strategy in strategies:
            strategies[strategy] += 1
    if 'Plans' in plan_node:
        for child_plan in plan_node['Plans']:
            child_strategies = count_strategies(child_plan)
            for key in strategies:
                strategies[key] += child_strategies[key]
    return strategies


# Count partial aggregation modes
def count_partial_modes(plan_node) -> dict:
    partial_modes = {'Simple': 0, 'Partial': 0, 'Finalize': 0}
    if 'Partial Mode' in plan_node:
        partial_mode = plan_node['Partial Mode']
        if partial_mode in partial_modes:
            partial_modes[partial_mode] += 1
    if 'Plans' in plan_node:
        for child_plan in plan_node['Plans']:
            child_partial_modes = count_partial_modes(child_plan)
            for key in partial_modes:
                partial_modes[key] += child_partial_modes[key]
    return partial_modes


# Count operators with group keys
def count_group_keys(plan_node) -> int:
    count = 0
    if 'Group Key' in plan_node:
        count += 1
    if 'Plans' in plan_node:
        for child_plan in plan_node['Plans']:
            count += count_group_keys(child_plan)
    return count


# Count total group key columns
def count_group_key_columns(plan_node) -> int:
    total_columns = 0
    if 'Group Key' in plan_node:
        total_columns += len(plan_node['Group Key'])
    if 'Plans' in plan_node:
        for child_plan in plan_node['Plans']:
            total_columns += count_group_key_columns(child_plan)
    return total_columns


# Count operators with sort keys
def count_sort_keys(plan_node) -> int:
    count = 0
    if 'Sort Key' in plan_node:
        count += 1
    if 'Plans' in plan_node:
        for child_plan in plan_node['Plans']:
            count += count_sort_keys(child_plan)
    return count


# Count total sort key columns
def count_sort_key_columns(plan_node) -> int:
    total_columns = 0
    if 'Sort Key' in plan_node:
        total_columns += len(plan_node['Sort Key'])
    if 'Plans' in plan_node:
        for child_plan in plan_node['Plans']:
            total_columns += count_sort_key_columns(child_plan)
    return total_columns


# Count subplan nodes in plan tree
def count_subplans(plan_node) -> int:
    count = 0
    if plan_node.get('Parent Relationship') == 'SubPlan':
        count += 1
    if 'Plans' in plan_node:
        for child_plan in plan_node['Plans']:
            count += count_subplans(child_plan)
    return count


# Count initplan nodes in plan tree
def count_initplans(plan_node) -> int:
    count = 0
    if plan_node.get('Parent Relationship') == 'InitPlan':
        count += 1
    if 'Plans' in plan_node:
        for child_plan in plan_node['Plans']:
            count += count_initplans(child_plan)
    return count


# Calculate maximum depth of plan tree
def calculate_max_depth(plan_node, current_depth: int = 1) -> int:
    if 'Plans' not in plan_node or not plan_node['Plans']:
        return current_depth
    max_child_depth = current_depth
    for child_plan in plan_node['Plans']:
        child_depth = calculate_max_depth(child_plan, current_depth + 1)
        max_child_depth = max(max_child_depth, child_depth)
    return max_child_depth


# Build pandas DataFrame from query data
def build_feature_dataframe(query_data: list) -> pd.DataFrame:
    return pd.DataFrame(query_data)


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
    csv_path = output_dir / '02_plan_features.csv'
    df.to_csv(csv_path, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract plan-level features from EXPLAIN output")
    parser.add_argument("query_dir", help="Directory containing Q* template folders with SQL files")
    parser.add_argument("--output-dir", default=None, help="Output directory for CSV (default: script_dir/csv)")

    args = parser.parse_args()

    query_path = Path(args.query_dir)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'csv'

    plan_feature_extraction_workflow(query_path, output_path)
