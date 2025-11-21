#!/usr/bin/env python3

import pandas as pd
from pathlib import Path
from datetime import datetime
import sys

REQUIRED_OPERATORS = {'Gather', 'Hash', 'Hash Join', 'Nested Loop', 'Seq Scan'}

def analyze_multi_pattern_queries_workflow(input_file, output_dir):
    df = load_and_filter_data(input_file)
    template_stats = analyze_multi_pattern_queries(df)
    export_template_stats(template_stats, output_dir)

def load_and_filter_data(input_file):
    df = pd.read_csv(input_file, delimiter=';')
    df['template'] = df['query_file'].str.extract(r'^(Q\d+)_')[0]
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]

def build_children_map(query_ops):
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
                    'relationship': next_row['parent_relationship']
                })
            elif next_row['depth'] <= current_depth:
                break
        
        children_map[current_node_id] = children
    
    return children_map

def count_patterns_in_query(query_ops, children_map):
    pattern_count = 0
    
    for idx, row in query_ops.iterrows():
        parent_depth = row['depth']
        parent_type = row['node_type']
        parent_node_id = row['node_id']
        
        if parent_depth < 1:
            continue
        
        children = children_map[parent_node_id]
        
        if len(children) == 0:
            continue
        
        pattern_operators = {parent_type} | {child['node_type'] for child in children}
        if not pattern_operators.intersection(REQUIRED_OPERATORS):
            continue
        
        pattern_count += 1
    
    return pattern_count

def analyze_multi_pattern_queries(df):
    template_stats = {}
    
    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        template = query_ops.iloc[0]['template']
        
        children_map = build_children_map(query_ops)
        pattern_count = count_patterns_in_query(query_ops, children_map)
        
        if pattern_count > 2:
            if template not in template_stats:
                template_stats[template] = {
                    'queries_with_3plus_patterns': 0,
                    'total_patterns': 0,
                    'max_patterns': 0
                }
            
            template_stats[template]['queries_with_3plus_patterns'] += 1
            template_stats[template]['total_patterns'] += pattern_count
            template_stats[template]['max_patterns'] = max(template_stats[template]['max_patterns'], pattern_count)
    
    results = []
    for template, stats in template_stats.items():
        results.append({
            'template': template,
            'queries_with_3plus_patterns': stats['queries_with_3plus_patterns'],
            'max_patterns_in_query': stats['max_patterns'],
            'avg_patterns_in_multi_queries': stats['total_patterns'] / stats['queries_with_3plus_patterns']
        })
    
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values('queries_with_3plus_patterns', ascending=False).reset_index(drop=True)
    
    return results_df

def export_template_stats(results, output_dir):
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = csv_dir / f'templates_with_multi_patterns_{timestamp}.csv'
    results.to_csv(output_file, sep=';', index=False)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(1)
    analyze_multi_pattern_queries_workflow(sys.argv[1], sys.argv[2])
