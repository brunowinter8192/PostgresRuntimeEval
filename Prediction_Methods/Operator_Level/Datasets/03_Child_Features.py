#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path

# ORCHESTRATOR

# Coordinate workflow to add child operator features to dataset
def add_children_workflow(input_file, output_dir):
    df = load_data(input_file)
    df_with_children = compute_child_features(df)
    export_data(df_with_children, output_dir)

# FUNCTIONS

# Load cleaned operator dataset from CSV file
def load_data(input_file):
    return pd.read_csv(input_file, delimiter=';')


# Compute st1, rt1, st2, rt2 for each operator based on child operators
def compute_child_features(df):
    st1_list = []
    rt1_list = []
    st2_list = []
    rt2_list = []
    
    for idx in range(len(df)):
        current_row = df.iloc[idx]
        current_depth = current_row['depth']
        current_query = current_row['query_file']
        
        st1, rt1 = 0.0, 0.0
        st2, rt2 = 0.0, 0.0
        
        for j in range(idx + 1, len(df)):
            next_row = df.iloc[j]
            
            if next_row['query_file'] != current_query:
                break
            
            if next_row['depth'] == current_depth + 1:
                if next_row['parent_relationship'] == 'Outer':
                    st1 = next_row['actual_startup_time']
                    rt1 = next_row['actual_total_time']
                elif next_row['parent_relationship'] == 'Inner':
                    st2 = next_row['actual_startup_time']
                    rt2 = next_row['actual_total_time']
            elif next_row['depth'] <= current_depth:
                break
        
        st1_list.append(st1)
        rt1_list.append(rt1)
        st2_list.append(st2)
        rt2_list.append(rt2)
    
    df = df.copy()
    df['st1'] = st1_list
    df['rt1'] = rt1_list
    df['st2'] = st2_list
    df['rt2'] = rt2_list
    
    return df


# Save dataset with child features to CSV file
def export_data(df, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    csv_path = output_path / '03_operator_dataset_with_children.csv'
    df.to_csv(csv_path, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to cleaned operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for dataset with child features")

    args = parser.parse_args()

    add_children_workflow(args.input_file, args.output_dir)
