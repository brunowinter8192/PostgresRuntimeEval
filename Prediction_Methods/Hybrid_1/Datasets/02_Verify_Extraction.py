#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime
import re


# ORCHESTRATOR
def verify_extraction(pattern_csv: str, patterns_base_dir: str, output_dir: str) -> None:
    pattern_data = load_pattern_data(pattern_csv)
    verification_results = verify_all_patterns(pattern_data, patterns_base_dir)
    export_results(verification_results, output_dir)


# FUNCTIONS

# Load pattern data from find_all_patterns.py output
def load_pattern_data(pattern_csv: str) -> pd.DataFrame:
    df = pd.read_csv(pattern_csv, delimiter=';')
    return df[['pattern', 'leaf_pattern', 'total']]

# Count operators in pattern string
def count_operators_in_pattern(pattern_str):
    if '[' in pattern_str:
        children = pattern_str.split('[')[1].split(']')[0]
        num_children = len([c for c in children.split(',') if c.strip()])
        return num_children + 1
    else:
        return 2

# Create folder name from pattern string
def pattern_to_folder_name(pattern_str):
    clean = pattern_str.replace(' → ', '_')
    clean = clean.replace('[', '').replace(']', '')
    clean = clean.replace('(', '').replace(')', '')
    clean = clean.replace(', ', '_')
    clean = clean.replace(' ', '_')
    clean = re.sub(r'_+', '_', clean)
    return clean

# Count rows in pattern CSV file
def count_pattern_rows(pattern_folder):
    csv_file = pattern_folder / 'training.csv'
    if not csv_file.exists():
        return None
    df = pd.read_csv(csv_file, delimiter=';')
    return len(df)

# Verify all patterns against extracted CSVs
def verify_all_patterns(pattern_data, patterns_base_dir):
    results = []
    
    for _, row in pattern_data.iterrows():
        pattern_str = row['pattern']
        total_occurrences = row['total']
        leaf_pattern = row['leaf_pattern']
        
        num_operators = count_operators_in_pattern(pattern_str)
        expected_rows = total_occurrences * num_operators
        
        folder_name = pattern_to_folder_name(pattern_str)
        pattern_folder = Path(patterns_base_dir) / folder_name
        
        actual_rows = count_pattern_rows(pattern_folder)
        
        if actual_rows is None:
            match = False
            status = 'MISSING'
        elif actual_rows == expected_rows:
            match = True
            status = 'OK'
        else:
            match = False
            status = 'MISMATCH'
        
        results.append({
            'pattern': pattern_str,
            'leaf_pattern': leaf_pattern,
            'total_occurrences': total_occurrences,
            'num_operators': num_operators,
            'expected_rows': expected_rows,
            'actual_rows': actual_rows if actual_rows is not None else 0,
            'match': match,
            'status': status
        })
    
    return pd.DataFrame(results)

# Export verification results to CSV
def export_results(results, output_dir):
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = csv_dir / f'pattern_extraction_verification_{timestamp}.csv'
    results.to_csv(output_file, sep=';', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern_csv", help="Path to pattern analysis CSV from find_all_patterns.py")
    parser.add_argument("patterns_dir", help="Base directory containing extracted pattern folders")
    parser.add_argument("--output-dir", required=True, help="Output directory for verification results")
    args = parser.parse_args()

    verify_extraction(args.pattern_csv, args.patterns_dir, args.output_dir)
