#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import hashlib
import json
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Pattern discovery constants and folder name conversion
from mapping_config import REQUIRED_OPERATORS, pattern_to_folder_name


# ORCHESTRATOR
def extract_patterns_workflow(input_file: str, output_base: str) -> None:
    df = load_training_data(input_file)
    pattern_occurrences, pattern_leaf_status = identify_pattern_occurrences(df)
    export_all_patterns(df, pattern_occurrences, pattern_leaf_status, output_base)


# FUNCTIONS

# Load training data and filter to main plan only
def load_training_data(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]

# Build map of direct children for each node
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
                    'df_index': next_row['index']
                })
            elif next_row['depth'] <= current_depth:
                break
        
        children_map[current_node_id] = children
    
    return children_map

# Compute MD5 hash for pattern structure
def compute_pattern_hash(parent_type: str, children: list) -> str:
    child_hashes = []
    for child in children:
        combined = f"{child[0]}:{child[1]}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = parent_type + '|' + '|'.join(child_hashes)

    return hashlib.md5(combined_string.encode()).hexdigest()


# Identify all pattern occurrences with their row indices
def identify_pattern_occurrences(df):
    pattern_rows = {}
    pattern_leaf_status = {}

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=False)
        children_map = build_children_map(query_ops)

        for idx, row in query_ops.iterrows():
            parent_depth = row['depth']
            parent_type = row['node_type']
            parent_node_id = row['node_id']
            parent_df_index = row['index']

            if parent_depth < 0:
                continue

            children = children_map[parent_node_id]

            if len(children) == 0:
                continue

            pattern_operators = {parent_type} | {child['node_type'] for child in children}
            if not pattern_operators.intersection(REQUIRED_OPERATORS):
                continue

            is_leaf_pattern = all(len(children_map.get(child['node_id'], [])) == 0 for child in children)

            children_info = [(child['node_type'], child['relationship']) for child in children]
            pattern_key = format_pattern_key(parent_type, children_info)
            pattern_hash = compute_pattern_hash(parent_type, children_info)

            composite_key = (pattern_hash, pattern_key)

            if composite_key not in pattern_rows:
                pattern_rows[composite_key] = []
                pattern_leaf_status[composite_key] = is_leaf_pattern

            children_df_indices = [child['df_index'] for child in children]
            pattern_rows[composite_key].append([parent_df_index] + children_df_indices)

    return pattern_rows, pattern_leaf_status

# Format pattern key based on parent type and children
def format_pattern_key(parent_type, children):
    children_sorted = sorted(children, key=lambda x: (0 if x[1] == 'Outer' else 1 if x[1] == 'Inner' else 2, x[0]))
    
    if len(children_sorted) == 1:
        return f"{parent_type} → {children_sorted[0][0]} ({children_sorted[0][1]})"
    else:
        children_str = ', '.join([f"{ct} ({rel})" for ct, rel in children_sorted])
        return f"{parent_type} → [{children_str}]"

# Export pattern dataset to dedicated folder
def export_pattern_dataset(df, pattern_hash, pattern_key, row_indices, is_leaf, output_base):
    pattern_dir = Path(output_base) / 'patterns' / pattern_hash
    pattern_dir.mkdir(parents=True, exist_ok=True)

    all_indices = [idx for occurrence in row_indices for idx in occurrence]
    pattern_df = df.loc[all_indices].sort_index()

    output_file = pattern_dir / 'training.csv'
    pattern_df.to_csv(output_file, sep=';', index=False)

    folder_name = pattern_to_folder_name(pattern_key)
    pattern_info = {
        'pattern_hash': pattern_hash,
        'pattern_string': pattern_key,
        'folder_name': folder_name,
        'leaf_pattern': is_leaf,
        'occurrence_count': len(row_indices)
    }
    info_file = pattern_dir / 'pattern_info.json'
    with open(info_file, 'w') as f:
        json.dump(pattern_info, f, indent=2)


# Export all patterns to their respective folders
def export_all_patterns(df, pattern_occurrences, pattern_leaf_status, output_base):
    for (pattern_hash, pattern_key), row_indices in pattern_occurrences.items():
        is_leaf = pattern_leaf_status.get((pattern_hash, pattern_key), False)
        export_pattern_dataset(df, pattern_hash, pattern_key, row_indices, is_leaf, output_base)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Base output directory for pattern folders")
    args = parser.parse_args()

    extract_patterns_workflow(args.input_file, args.output_dir)
