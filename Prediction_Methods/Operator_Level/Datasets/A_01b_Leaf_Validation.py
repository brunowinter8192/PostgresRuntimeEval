#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import argparse
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

# From mapping_config.py: Get leaf operator types for validation
from mapping_config import LEAF_OPERATORS

# ORCHESTRATOR
def verify_workflow(input_file, output_dir):
    df = load_data(input_file)
    issues_df = verify_scan_leaf_structure(df)
    export_results(issues_df, output_dir)

# FUNCTIONS

# Load operator dataset from CSV file
def load_data(input_file):
    return pd.read_csv(input_file, delimiter=';')


# Verify that all scans are leafs and all leafs are scans
def verify_scan_leaf_structure(df):
    scan_types = LEAF_OPERATORS
    issues = []
    
    for query_file in df['query_file'].unique():
        query_df = df[df['query_file'] == query_file].reset_index(drop=True)
        
        for i in range(len(query_df) - 1):
            current = query_df.iloc[i]
            next_row = query_df.iloc[i + 1]
            
            current_depth = current['depth']
            next_depth = next_row['depth']
            current_type = current['node_type']
            template = query_file.split('_')[0]
            
            if next_depth > current_depth:
                if current_type in scan_types:
                    issues.append({
                        'template': template,
                        'issue_type': 'Scan with child'
                    })
            elif next_depth < current_depth:
                if current_type not in scan_types:
                    issues.append({
                        'template': template,
                        'issue_type': 'Non-scan leaf'
                    })
    
    if len(issues) == 0:
        return pd.DataFrame(columns=['template', 'scan_with_child_count', 'non_scan_leaf_count'])
    
    issues_df = pd.DataFrame(issues)
    
    scan_child_counts = issues_df[issues_df['issue_type'] == 'Scan with child'].groupby('template').size().to_dict()
    non_scan_leaf_counts = issues_df[issues_df['issue_type'] == 'Non-scan leaf'].groupby('template').size().to_dict()
    
    all_templates = sorted(set(scan_child_counts.keys()) | set(non_scan_leaf_counts.keys()))
    
    summary = []
    for template in all_templates:
        summary.append({
            'template': template,
            'scan_with_child_count': scan_child_counts.get(template, 0),
            'non_scan_leaf_count': non_scan_leaf_counts.get(template, 0)
        })
    
    return pd.DataFrame(summary)


# Save verification issues to CSV file
def export_results(issues_df, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    csv_path = output_path / 'A_01b_scan_leaf_issues.csv'
    issues_df.to_csv(csv_path, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for validation results")

    args = parser.parse_args()

    verify_workflow(args.input_file, args.output_dir)
