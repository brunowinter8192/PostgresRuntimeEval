#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Pattern discovery constants
from mapping_config import REQUIRED_OPERATORS


# ORCHESTRATOR
def analyze_patterns(input_file: str, output_dir: str) -> None:
    df = load_and_filter_data(input_file)
    pattern_data = extract_all_patterns(df)
    results = create_pattern_matrix(pattern_data, df)
    export_results(results, output_dir)


# FUNCTIONS

# Load training data and filter to main plan with template extraction
def load_and_filter_data(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file, delimiter=';')
    df['template'] = df['query_file'].str.extract(r'^(Q\d+)_')[0]
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]

# Extract all patterns from training data with occurrence counts per template
def extract_all_patterns(df):
    pattern_data = {}
    
    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        template = query_ops.iloc[0]['template']
        
        children_map = build_children_map(query_ops)
        
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
            
            is_leaf_pattern = all(len(children_map[child['node_id']]) == 0 for child in children)
            
            pattern_key = format_pattern_key(parent_type, children)
            
            if pattern_key not in pattern_data:
                pattern_data[pattern_key] = {
                    'leaf_pattern': is_leaf_pattern,
                    'templates': {}
                }
            
            if template not in pattern_data[pattern_key]['templates']:
                pattern_data[pattern_key]['templates'][template] = 0
            
            pattern_data[pattern_key]['templates'][template] += 1
    
    return pattern_data

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
                    'relationship': next_row['parent_relationship']
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

# Create pattern matrix with template occurrence columns
def create_pattern_matrix(pattern_data, df):
    all_templates = sorted(df['template'].unique())
    
    rows = []
    for pattern_key, data in pattern_data.items():
        row = {
            'pattern': pattern_key,
            'leaf_pattern': data['leaf_pattern']
        }
        
        for template in all_templates:
            row[template] = data['templates'].get(template, 0)
        
        row['total'] = sum(data['templates'].values())
        rows.append(row)
    
    results_df = pd.DataFrame(rows)
    results_df = results_df.sort_values('total', ascending=False).reset_index(drop=True)
    
    cols = ['pattern', 'leaf_pattern', 'total'] + all_templates
    return results_df[cols]

# Save pattern matrix to CSV with timestamp
def export_results(results, output_dir):
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = csv_dir / f'baseline_patterns_depth1plus_{timestamp}.csv'
    results.to_csv(output_file, sep=';', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for pattern analysis")
    args = parser.parse_args()

    analyze_patterns(args.input_file, args.output_dir)
