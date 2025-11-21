#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from collections import defaultdict

PATTERNS = [
    'Hash_Join_Seq_Scan_Outer_Hash_Inner',
    'Hash_Seq_Scan_Outer',
    'Hash_Hash_Join_Outer',
    'Hash_Join_Nested_Loop_Outer_Hash_Inner',
    'Nested_Loop_Hash_Join_Outer_Index_Scan_Inner',
    'Sort_Hash_Join_Outer',
    'Nested_Loop_Seq_Scan_Outer_Index_Scan_Inner',
    'Gather_Aggregate_Outer',
    'Aggregate_Hash_Join_Outer',
    'Aggregate_Gather_Outer',
    'Aggregate_Seq_Scan_Outer',
    'Hash_Join_Hash_Join_Outer_Hash_Inner',
    'Aggregate_Nested_Loop_Outer',
    'Sort_Nested_Loop_Outer',
    'Incremental_Sort_Nested_Loop_Outer',
    'Nested_Loop_Merge_Join_Outer_Index_Scan_Inner',
    'Hash_Aggregate_Outer',
    'Sort_Seq_Scan_Outer',
    'Gather_Nested_Loop_Outer',
    'Gather_Hash_Join_Outer',
    'Hash_Index_Only_Scan_Outer'
]

# ORCHESTRATOR

# Analyze patterns across all templates
def analyze_template_patterns(test_file, pattern_overview_file, output_dir):
    df_test = load_test_data(test_file)
    pattern_features = load_and_extract_pattern_features(pattern_overview_file)
    template_patterns = extract_patterns_per_template(df_test, pattern_features)
    variants = detect_template_variants(template_patterns)
    export_analysis(variants, output_dir)

# FUNCTIONS

# Load test data from CSV
def load_test_data(test_file):
    return pd.read_csv(test_file, delimiter=';')

# Load pattern overview and extract features
def load_and_extract_pattern_features(pattern_file):
    df = pd.read_csv(pattern_file, delimiter=';')
    pattern_dict = {}
    for _, row in df.iterrows():
        pattern_name = row['pattern']
        if pattern_name not in pattern_dict:
            pattern_dict[pattern_name] = {}
        target = row['target']
        missing_child = [] if pd.isna(row['missing_child_features']) else [f.strip() for f in row['missing_child_features'].split(',')]
        pattern_dict[pattern_name][target] = {'missing_child_features': missing_child}
    return pattern_dict

# Extract patterns for each query and group by template
def extract_patterns_per_template(df_test, pattern_features):
    template_patterns = defaultdict(list)
    queries = df_test['query_file'].unique()

    for query in queries:
        template = extract_template_from_query(query)
        df_query = filter_query_data(df_test, query)
        patterns = extract_query_patterns(df_query, pattern_features)
        template_patterns[template].append({
            'query_file': query,
            'patterns': patterns
        })

    return template_patterns

# Extract template ID from query filename
def extract_template_from_query(query_file):
    return query_file.split('_')[0]

# Filter test data for specific query
def filter_query_data(df_test, query):
    df_query = df_test[df_test['query_file'] == query].copy()
    df_query = df_query[df_query['subplan_name'].isna() | (df_query['subplan_name'] == '')]
    return df_query.sort_values('node_id').reset_index(drop=True)

# Extract patterns from single query using bottom-up matching
def extract_query_patterns(df_query, pattern_features):
    patterns_found = []
    consumed_by_pattern = set()
    consumed_by_operator = set()
    predictions = {}
    max_depth = df_query['depth'].max()

    for depth in range(max_depth, -1, -1):
        operators_at_depth = df_query[df_query['depth'] == depth]

        for idx in operators_at_depth.index:
            if idx in consumed_by_pattern or idx in consumed_by_operator:
                continue

            op_row = df_query.loc[idx]
            parent_idx = find_parent_operator(df_query, idx)

            if parent_idx is None:
                consumed_by_operator.add(idx)
                pred_key = (op_row['node_type'], op_row['depth'])
                predictions[pred_key] = True
                continue

            if parent_idx in consumed_by_operator or parent_idx in consumed_by_pattern:
                continue

            parent_row = df_query.loc[parent_idx]

            if parent_row['depth'] < 1:
                continue

            siblings_indices = find_all_siblings(df_query, idx, parent_idx)

            if any(sib_idx in consumed_by_pattern or sib_idx in consumed_by_operator for sib_idx in siblings_indices):
                continue

            children_info = build_children_info_list(df_query, siblings_indices)
            pattern_match = try_match_pattern(parent_row, children_info, pattern_features, predictions, df_query)

            if pattern_match:
                patterns_found.append({
                    'pattern_name': pattern_match,
                    'depth': parent_row['depth']
                })
                consumed_by_pattern.add(parent_idx)
                for sib_idx in siblings_indices:
                    consumed_by_pattern.add(sib_idx)
                pred_key = (parent_row['node_type'], parent_row['depth'])
                predictions[pred_key] = True

        for idx in operators_at_depth.index:
            if idx in consumed_by_pattern or idx in consumed_by_operator:
                continue
            op_row = df_query.loc[idx]
            consumed_by_operator.add(idx)
            pred_key = (op_row['node_type'], op_row['depth'])
            predictions[pred_key] = True

    return patterns_found

# Find parent operator for given operator index
def find_parent_operator(df_query, operator_idx):
    op_row = df_query.loc[operator_idx]
    op_depth = op_row['depth']
    if op_depth == 0:
        return None
    for idx in range(operator_idx - 1, -1, -1):
        row = df_query.iloc[idx]
        if row['depth'] == op_depth - 1:
            return df_query.index[idx]
    return None

# Find all siblings of operator including itself
def find_all_siblings(df_query, operator_idx, parent_idx):
    parent_row = df_query.loc[parent_idx]
    parent_depth = parent_row['depth']
    siblings = []
    for idx in range(parent_idx + 1, len(df_query)):
        row = df_query.iloc[idx]
        if row['depth'] == parent_depth + 1:
            siblings.append(df_query.index[idx])
        elif row['depth'] <= parent_depth:
            break
    return siblings

# Build children info list from sibling indices
def build_children_info_list(df_query, sibling_indices):
    children_info = []
    for idx in sibling_indices:
        row = df_query.loc[idx]
        children_info.append({
            'index': idx,
            'node_type': row['node_type'],
            'depth': row['depth'],
            'parent_relationship': row['parent_relationship']
        })
    return children_info

# Try to match pattern with parent operator
def try_match_pattern(parent_row, children_info, pattern_features, predictions, df_query):
    if len(children_info) == 0:
        return None
    pattern_key = build_pattern_key(parent_row['node_type'], children_info)
    if pattern_key not in PATTERNS:
        return None
    if pattern_key not in pattern_features:
        return None
    pattern_data = pattern_features[pattern_key]
    needs_child_features = len(pattern_data['execution_time']['missing_child_features']) > 0
    if needs_child_features:
        if not check_child_features_available(pattern_key, pattern_features, children_info, predictions, df_query):
            return None
    return pattern_key

# Build pattern key from operator and children
def build_pattern_key(parent_type, children_info):
    parent_normalized = parent_type.replace(' ', '_')
    if len(children_info) == 1:
        child_normalized = children_info[0]['node_type'].replace(' ', '_')
        relationship = children_info[0]['parent_relationship']
        return f"{parent_normalized}_{child_normalized}_{relationship}"
    if len(children_info) == 2:
        children_sorted = sorted(children_info, key=lambda x: (0 if x['parent_relationship'] == 'Outer' else 1))
        outer_normalized = children_sorted[0]['node_type'].replace(' ', '_')
        inner_normalized = children_sorted[1]['node_type'].replace(' ', '_')
        return f"{parent_normalized}_{outer_normalized}_Outer_{inner_normalized}_Inner"
    return None

# Check if child features are available for non-leaf pattern
def check_child_features_available(pattern_key, pattern_features, children_info, predictions, df_query):
    pattern_data = pattern_features[pattern_key]
    missing_child_features = pattern_data['execution_time']['missing_child_features']
    if len(missing_child_features) == 0:
        return True
    for child in children_info:
        grandchildren = get_children_info(df_query, child['index'])
        for grandchild in grandchildren:
            pred_key = (grandchild['node_type'], grandchild['depth'])
            if pred_key not in predictions:
                return False
    return True

# Get children information for operator
def get_children_info(df_query, parent_idx):
    parent_row = df_query.loc[parent_idx]
    parent_depth = parent_row['depth']
    children = []
    for idx in range(parent_idx + 1, len(df_query)):
        row = df_query.iloc[idx]
        if row['depth'] == parent_depth + 1:
            children.append({
                'index': df_query.index[idx],
                'node_type': row['node_type'],
                'depth': row['depth'],
                'parent_relationship': row['parent_relationship']
            })
        elif row['depth'] <= parent_depth:
            break
    return children

# Detect template variants based on pattern combinations
def detect_template_variants(template_patterns):
    variants_list = []
    for template, queries_data in sorted(template_patterns.items()):
        pattern_combinations = group_by_pattern_combination(queries_data)
        variant_id = 1
        for pattern_combo, queries_with_combo in pattern_combinations.items():
            unique_patterns = [p['pattern_name'] for p in queries_with_combo[0]['patterns']]
            unique_depths = [p['depth'] for p in queries_with_combo[0]['patterns']]
            variants_list.append({
                'template': template,
                'variant_id': variant_id,
                'variant_count': len(queries_with_combo),
                'patterns': ','.join(unique_patterns) if unique_patterns else '',
                'pattern_depths': ','.join(map(str, unique_depths)) if unique_depths else ''
            })
            variant_id += 1
    return variants_list

# Group queries by their pattern combination
def group_by_pattern_combination(queries_data):
    combinations = defaultdict(list)
    for query_data in queries_data:
        pattern_combo = create_pattern_signature(query_data['patterns'])
        combinations[pattern_combo].append(query_data)
    return combinations

# Create unique signature for pattern combination
def create_pattern_signature(patterns):
    if not patterns:
        return 'NO_PATTERNS'
    sorted_patterns = sorted([(p['pattern_name'], p['depth']) for p in patterns])
    return '|'.join([f"{name}@{depth}" for name, depth in sorted_patterns])

# Export analysis results to CSV
def export_analysis(variants, output_dir):
    output_path = Path(output_dir) / 'csv'
    output_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'template_pattern_analysis_{timestamp}.csv'
    df_variants = pd.DataFrame(variants)
    df_variants.to_csv(output_path / filename, sep=';', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file', help='Path to test.csv')
    parser.add_argument('pattern_overview', help='Path to pattern overview CSV')
    parser.add_argument('--output-dir', required=True, help='Output directory for analysis results')
    args = parser.parse_args()

    analyze_template_patterns(args.test_file, args.pattern_overview, args.output_dir)
