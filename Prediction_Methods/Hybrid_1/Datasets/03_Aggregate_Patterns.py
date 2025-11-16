#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import re


# ORCHESTRATOR
def aggregate_patterns_workflow(patterns_base_dir: str) -> None:
    pattern_folders = get_pattern_folders(patterns_base_dir)
    for pattern_folder in pattern_folders:
        process_pattern_folder(pattern_folder)


# FUNCTIONS

# Get all pattern folders
def get_pattern_folders(patterns_base_dir: str) -> list:
    base_path = Path(patterns_base_dir)
    return [d for d in base_path.iterdir() if d.is_dir() and d.name != 'verification']

# Build map of direct children for each node
def build_children_map(df):
    children_map = {}
    
    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=False)
        
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
                        'df_index': next_row['index']
                    })
                elif next_row['depth'] <= current_depth:
                    break
            
            children_map[current_node_id] = children
    
    return children_map

# Clean node type for column naming
def clean_node_type(node_type):
    return node_type.replace(' ', '')

# Parse pattern structure from folder name
def parse_pattern_from_folder_name(folder_name):
    parts = folder_name.split('_')
    
    operators = []
    i = 0
    while i < len(parts):
        if i + 1 < len(parts) and parts[i + 1] in ['Outer', 'Inner', 'Unknown']:
            node_type = parts[i]
            relationship = parts[i + 1]
            operators.append((node_type, relationship))
            i += 2
        else:
            if i + 3 < len(parts) and parts[i] + ' ' + parts[i + 1] + ' ' + parts[i + 2] in ['Index Only Scan']:
                node_type = parts[i] + ' ' + parts[i + 1] + ' ' + parts[i + 2]
                i += 3
            elif i + 2 < len(parts) and parts[i] + ' ' + parts[i + 1] in ['Hash Join', 'Seq Scan', 'Index Scan', 'Nested Loop', 'Incremental Sort', 'Merge Join']:
                node_type = parts[i] + ' ' + parts[i + 1]
                i += 2
            else:
                node_type = parts[i]
                i += 1
            
            if i < len(parts) and parts[i] in ['Outer', 'Inner', 'Unknown']:
                relationship = parts[i]
                i += 1
            else:
                relationship = None
            
            operators.append((node_type, relationship))
    
    parent = operators[0]
    children = operators[1:]
    
    return parent, children

# Check if node and its children match pattern
def match_pattern(parent_row, children, parent_pattern, children_patterns):
    if parent_row['node_type'] != parent_pattern[0]:
        return False
    
    if len(children) != len(children_patterns):
        return False
    
    children_sorted = sorted(children, key=lambda x: (0 if x['relationship'] == 'Outer' else 1 if x['relationship'] == 'Inner' else 2, x['node_type']))
    patterns_sorted = sorted(children_patterns, key=lambda x: (0 if x[1] == 'Outer' else 1 if x[1] == 'Inner' else 2, x[0]))
    
    for child, (expected_type, expected_rel) in zip(children_sorted, patterns_sorted):
        if child['node_type'] != expected_type:
            return False
        if child['relationship'] != expected_rel:
            return False
    
    return True

# Aggregate pattern rows into single row
def aggregate_rows(parent_row, children, df):
    aggregated = {}
    
    aggregated['query_file'] = parent_row['query_file']
    
    parent_prefix = clean_node_type(parent_row['node_type']) + '_'
    for col in parent_row.index:
        if col != 'query_file':
            aggregated[parent_prefix + col] = parent_row[col]
    
    children_sorted = sorted(children, key=lambda x: (0 if x['relationship'] == 'Outer' else 1 if x['relationship'] == 'Inner' else 2, x['node_type']))
    
    for child in children_sorted:
        child_row = df.loc[child['df_index']]
        child_prefix = clean_node_type(child['node_type']) + '_' + child['relationship'] + '_'
        for col in child_row.index:
            if col != 'query_file':
                aggregated[child_prefix + col] = child_row[col]
    
    return aggregated

# Process single pattern folder
def process_pattern_folder(pattern_folder):
    training_file = pattern_folder / 'training.csv'
    
    if not training_file.exists():
        return
    
    df = pd.read_csv(training_file, delimiter=';')
    
    parent_pattern, children_patterns = parse_pattern_from_folder_name(pattern_folder.name)
    children_map = build_children_map(df)
    
    aggregated_rows = []
    processed_nodes = set()
    
    for idx, row in df.iterrows():
        node_id = row['node_id']
        
        if node_id in processed_nodes:
            continue
        
        if row['depth'] < 1:
            continue
        
        children = children_map.get(node_id, [])
        
        if match_pattern(row, children, parent_pattern, children_patterns):
            aggregated_row = aggregate_rows(row, children, df)
            aggregated_rows.append(aggregated_row)
            
            processed_nodes.add(node_id)
            for child in children:
                processed_nodes.add(child['node_id'])
    
    if aggregated_rows:
        result_df = pd.DataFrame(aggregated_rows)
        output_file = pattern_folder / 'training_aggregated.csv'
        result_df.to_csv(output_file, sep=';', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("patterns_dir", help="Base directory containing extracted pattern folders")
    args = parser.parse_args()

    aggregate_patterns_workflow(args.patterns_dir)
