#!/usr/bin/env python3

# Infrastructure
import pandas as pd
from pathlib import Path
from datetime import datetime
import sys

REQUIRED_OPERATORS = {'Gather', 'Hash', 'Hash Join', 'Nested Loop', 'Seq Scan'}

# Orchestrator
def analyze_q9_pattern_structure_workflow(input_file, output_dir):
    df = load_q9_data(input_file)
    query_plans = identify_unique_plans(df)
    
    for plan_id, example_query in enumerate(query_plans, start=1):
        pattern_structure = extract_pattern_structure(df, example_query)
        export_pattern_structure(pattern_structure, output_dir, plan_id)

# Load Q9 queries from dataset and filter to main plan
def load_q9_data(input_file):
    df = pd.read_csv(input_file, delimiter=';')
    df['template'] = df['query_file'].str.extract(r'^(Q\d+)_')[0]
    df_q9 = df[df['template'] == 'Q9']
    return df_q9[df_q9['subplan_name'].isna() | (df_q9['subplan_name'] == '')]

# Identify unique query plans based on pattern signatures
def identify_unique_plans(df):
    plan_signatures = {}
    
    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        children_map = build_children_map(query_ops)
        patterns = extract_patterns_for_query(query_ops, children_map)
        
        pattern_string = ', '.join(patterns)
        
        if pattern_string not in plan_signatures:
            plan_signatures[pattern_string] = query_file
    
    return list(plan_signatures.values())

# Extract pattern structure with depth information for specific query
def extract_pattern_structure(df, query_file):
    query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
    children_map = build_children_map(query_ops)
    
    pattern_rows = []
    pattern_occurrence = {}
    
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
        
        is_leaf = any(len(children_map[child['node_id']]) == 0 for child in children)
        pattern_key = format_pattern_key(parent_type, children)
        
        if pattern_key not in pattern_occurrence:
            pattern_occurrence[pattern_key] = 0
        pattern_occurrence[pattern_key] += 1
        occurrence = pattern_occurrence[pattern_key]
        
        pattern_instance = f"{pattern_key} (#{occurrence})"
        leaf_status = 'Leaf' if is_leaf else 'Non-Leaf'
        
        pattern_rows.append({
            'pattern': pattern_instance,
            'is_leaf': leaf_status,
            'node_type': parent_type,
            'depth': parent_depth
        })
        
        for child in children:
            pattern_rows.append({
                'pattern': pattern_instance,
                'is_leaf': leaf_status,
                'node_type': child['node_type'],
                'depth': child['depth']
            })
    
    return pd.DataFrame(pattern_rows)

# Extract patterns from single query
def extract_patterns_for_query(query_ops, children_map):
    patterns = []
    
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
        
        pattern_key = format_pattern_key(parent_type, children)
        patterns.append(pattern_key)
    
    return patterns

# Build map of direct children for each node in query
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
                    'relationship': next_row['parent_relationship'],
                    'depth': next_row['depth']
                })
            elif next_row['depth'] <= current_depth:
                break
        
        children_map[current_node_id] = children
    
    return children_map

# Format pattern key with parent and sorted children
def format_pattern_key(parent_type, children):
    children_info = [(child['node_type'], child['relationship']) for child in children]
    children_sorted = sorted(children_info, key=lambda x: (0 if x[1] == 'Outer' else 1 if x[1] == 'Inner' else 2, x[0]))
    
    if len(children_sorted) == 1:
        return f"{parent_type} → {children_sorted[0][0]} ({children_sorted[0][1]})"
    else:
        children_str = ', '.join([f"{ct} ({rel})" for ct, rel in children_sorted])
        return f"{parent_type} → [{children_str}]"

# Export pattern structure to CSV with timestamp
def export_pattern_structure(pattern_structure, output_dir, plan_id):
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = csv_dir / f'q9_plan{plan_id}_pattern_structure_{timestamp}.csv'
    pattern_structure.to_csv(output_file, sep=';', index=False)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(1)
    analyze_q9_pattern_structure_workflow(sys.argv[1], sys.argv[2])
