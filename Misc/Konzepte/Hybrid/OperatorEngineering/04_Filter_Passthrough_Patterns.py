#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime

PASSTHROUGH_THRESHOLD = 0.99

# ORCHESTRATOR

# Filter patterns containing pass-through operators
def filter_passthrough_patterns_workflow(operator_analysis, execution_time_file, start_time_file, output_dir):
    passthrough_ops = load_passthrough_operators(operator_analysis)
    all_ops = load_all_operator_names(operator_analysis)
    df_execution = filter_mre_file(execution_time_file, passthrough_ops, all_ops)
    df_start = filter_mre_file(start_time_file, passthrough_ops, all_ops)
    export_results(df_execution, df_start, output_dir)

# FUNCTIONS

# Load pass-through operators from runtime analysis
def load_passthrough_operators(operator_analysis):
    df = pd.read_csv(operator_analysis, delimiter=';')
    passthrough = df[df['startup_total_ratio'] >= PASSTHROUGH_THRESHOLD]
    return set(passthrough['node_type'].str.strip().tolist())

# Load all operator names for compound operator matching
def load_all_operator_names(operator_analysis):
    df = pd.read_csv(operator_analysis, delimiter=';')
    return set(df['node_type'].str.strip().tolist())

# Parse pattern name into components
def parse_pattern_components(pattern_name, all_ops):
    parts = pattern_name.split('_')

    parent = None
    outer_child = None
    inner_child = None

    if 'Outer' not in parts and 'Inner' not in parts:
        parent = pattern_name.replace('_', ' ')
        return {'parent': parent, 'outer_child': None, 'inner_child': None}

    outer_idx = parts.index('Outer') if 'Outer' in parts else None
    inner_idx = parts.index('Inner') if 'Inner' in parts else None

    parent_end_idx = 1
    for i in range(2, len(parts)):
        if parts[i] in ['Outer', 'Inner']:
            break
        candidate = ' '.join(parts[:i])
        if candidate in all_ops:
            parent_end_idx = i

    parent = ' '.join(parts[:parent_end_idx])

    if outer_idx is not None:
        outer_parts = parts[parent_end_idx:outer_idx]
        outer_child = ' '.join(outer_parts)

    if inner_idx is not None:
        if outer_idx is not None:
            inner_parts = parts[outer_idx + 1:inner_idx]
        else:
            inner_parts = parts[parent_end_idx:inner_idx]
        inner_child = ' '.join(inner_parts)

    return {'parent': parent, 'outer_child': outer_child, 'inner_child': inner_child}

# Check if pattern has non-passthrough parent AND passthrough child
def has_passthrough_component(pattern_name, passthrough_ops, all_ops):
    components = parse_pattern_components(pattern_name, all_ops)

    if components['parent'] in passthrough_ops:
        return False

    has_passthrough_child = False

    if components['outer_child'] and components['outer_child'] in passthrough_ops:
        has_passthrough_child = True

    if components['inner_child'] and components['inner_child'] in passthrough_ops:
        has_passthrough_child = True

    return has_passthrough_child

# Filter MRE file to keep only pass-through patterns
def filter_mre_file(mre_file, passthrough_ops, all_ops):
    df = pd.read_csv(mre_file, delimiter=';')

    mask = df['pattern_name'].apply(lambda p: has_passthrough_component(p, passthrough_ops, all_ops))
    return df[mask]

# Export filtered results to CSV
def export_results(df_execution, df_start, output_dir):
    output_path = Path(output_dir) / 'csv'
    output_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    filename_execution = f'04_filtered_execution_time_passthrough_{timestamp}.csv'
    df_execution.to_csv(output_path / filename_execution, sep=';', index=False)

    filename_start = f'04_filtered_start_time_passthrough_{timestamp}.csv'
    df_start.to_csv(output_path / filename_start, sep=';', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('operator_analysis', help='Path to operator runtime analysis CSV')
    parser.add_argument('execution_time_file', help='Path to pattern execution_time MRE CSV')
    parser.add_argument('start_time_file', help='Path to pattern start_time MRE CSV')
    parser.add_argument('--output-dir', required=True, help='Output directory for filtered results')
    args = parser.parse_args()

    filter_passthrough_patterns_workflow(args.operator_analysis, args.execution_time_file, args.start_time_file, args.output_dir)
