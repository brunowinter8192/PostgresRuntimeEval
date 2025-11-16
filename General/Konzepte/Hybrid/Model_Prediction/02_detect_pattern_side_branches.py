#!/usr/bin/env python3

import pandas as pd
from pathlib import Path
from datetime import datetime
import sys

REQUIRED_OPERATORS = {'Gather', 'Hash', 'Hash Join', 'Nested Loop', 'Seq Scan'}

def detect_side_branches_workflow(input_file, output_dir):
    df = load_and_filter_data(input_file)
    side_branch_data = find_all_side_branches(df)
    export_side_branches(side_branch_data, output_dir)

def load_and_filter_data(input_file):
    df = pd.read_csv(input_file, delimiter=';')
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

def build_parent_map(query_ops):
    parent_map = {}
    
    for idx in range(len(query_ops)):
        current_row = query_ops.iloc[idx]
        current_depth = current_row['depth']
        current_node_id = current_row['node_id']
        
        if current_depth == 0:
            parent_map[current_node_id] = None
            continue
        
        for j in range(idx - 1, -1, -1):
            prev_row = query_ops.iloc[j]
            
            if prev_row['depth'] == current_depth - 1:
                parent_map[current_node_id] = prev_row['node_id']
                break
    
    return parent_map

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
        
        is_leaf_pattern = any(len(children_map[child['node_id']]) == 0 for child in children)
        pattern_key = format_pattern_key(parent_type, children)
        
        pattern_info = {
            'pattern_key': pattern_key,
            'parent_node_id': parent_node_id,
            'parent_depth': parent_depth,
            'parent_type': parent_type,
            'child_node_ids': [child['node_id'] for child in children],
            'all_node_ids': [parent_node_id] + [child['node_id'] for child in children],
            'is_leaf': is_leaf_pattern
        }
        
        patterns.append(pattern_info)
    
    return patterns

def format_pattern_key(parent_type, children):
    children_info = [(child['node_type'], child['relationship']) for child in children]
    children_sorted = sorted(children_info, key=lambda x: (0 if x[1] == 'Outer' else 1 if x[1] == 'Inner' else 2, x[0]))
    
    if len(children_sorted) == 1:
        return f"{parent_type} → {children_sorted[0][0]} ({children_sorted[0][1]})"
    else:
        children_str = ', '.join([f"{ct} ({rel})" for ct, rel in children_sorted])
        return f"{parent_type} → [{children_str}]"

def find_all_side_branches(df):
    side_branch_records = []
    
    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        children_map = build_children_map(query_ops)
        parent_map = build_parent_map(query_ops)
        patterns = extract_patterns_for_query(query_ops, children_map)
        
        for pattern in patterns:
            pattern_parent_id = pattern['parent_node_id']
            pattern_parent_depth = pattern['parent_depth']
            
            grandparent_id = parent_map.get(pattern_parent_id)
            
            if grandparent_id is None:
                continue
            
            grandparent_children = children_map.get(grandparent_id, [])
            
            side_branch_nodes = []
            for sibling in grandparent_children:
                if sibling['node_id'] != pattern_parent_id:
                    sibling_row = query_ops[query_ops['node_id'] == sibling['node_id']].iloc[0]
                    side_branch_nodes.append({
                        'node_id': sibling['node_id'],
                        'node_type': sibling['node_type'],
                        'depth': sibling_row['depth'],
                        'relationship': sibling['relationship']
                    })
            
            if len(side_branch_nodes) > 0:
                grandparent_row = query_ops[query_ops['node_id'] == grandparent_id].iloc[0]
                
                side_branch_records.append({
                    'query_file': query_file,
                    'pattern': pattern['pattern_key'],
                    'pattern_parent_depth': pattern_parent_depth,
                    'merge_point_depth': grandparent_row['depth'],
                    'merge_point_node_id': grandparent_id,
                    'merge_point_node_type': grandparent_row['node_type'],
                    'side_branch_count': len(side_branch_nodes),
                    'side_branch_node_ids': ','.join([str(sb['node_id']) for sb in side_branch_nodes]),
                    'side_branch_node_types': ','.join([sb['node_type'] for sb in side_branch_nodes])
                })
    
    return side_branch_records

def export_side_branches(side_branch_data, output_dir):
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = csv_dir / f'pattern_side_branches_{timestamp}.csv'
    
    if len(side_branch_data) == 0:
        pd.DataFrame(columns=['query_file', 'pattern', 'pattern_parent_depth', 'merge_point_depth',
                              'merge_point_node_id', 'merge_point_node_type', 'side_branch_count',
                              'side_branch_node_ids', 'side_branch_node_types']).to_csv(output_file, sep=';', index=False)
    else:
        df_side_branches = pd.DataFrame(side_branch_data)
        df_side_branches.to_csv(output_file, sep=';', index=False)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(1)
    detect_side_branches_workflow(sys.argv[1], sys.argv[2])
