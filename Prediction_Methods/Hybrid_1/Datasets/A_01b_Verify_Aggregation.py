#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Pattern to folder name conversion
from mapping_config import pattern_to_folder_name


# ORCHESTRATOR
def verify_aggregation(pattern_csv: str, patterns_base_dir: str, output_dir: str) -> None:
    pattern_data = load_pattern_data(pattern_csv)
    verification_results = verify_all_aggregated_patterns(pattern_data, patterns_base_dir)
    export_results(verification_results, output_dir)


# FUNCTIONS

# Load pattern data from find_all_patterns.py output
def load_pattern_data(pattern_csv: str) -> pd.DataFrame:
    df = pd.read_csv(pattern_csv, delimiter=';')
    return df[['pattern', 'leaf_pattern', 'total']]

# Count rows in aggregated CSV file
def count_aggregated_rows(pattern_folder):
    csv_file = pattern_folder / 'training_aggregated.csv'
    if not csv_file.exists():
        return None
    df = pd.read_csv(csv_file, delimiter=';')
    return len(df)

# Verify all aggregated patterns
def verify_all_aggregated_patterns(pattern_data, patterns_base_dir):
    results = []
    
    for _, row in pattern_data.iterrows():
        pattern_str = row['pattern']
        total_occurrences = row['total']
        leaf_pattern = row['leaf_pattern']
        
        folder_name = pattern_to_folder_name(pattern_str)
        pattern_folder = Path(patterns_base_dir) / folder_name
        
        actual_rows = count_aggregated_rows(pattern_folder)
        
        if actual_rows is None:
            match = False
            status = 'MISSING'
        elif actual_rows == total_occurrences:
            match = True
            status = 'OK'
        else:
            match = False
            status = 'MISMATCH'
        
        results.append({
            'pattern': pattern_str,
            'leaf_pattern': leaf_pattern,
            'total_occurrences': total_occurrences,
            'aggregated_rows': actual_rows if actual_rows is not None else 0,
            'match': match,
            'status': status
        })
    
    return pd.DataFrame(results)

# Export verification results to CSV
def export_results(results, output_dir):
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    output_file = csv_dir / 'A_01b_aggregation_verification.csv'
    results.to_csv(output_file, sep=';', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern_csv", help="Path to pattern analysis CSV from find_all_patterns.py")
    parser.add_argument("patterns_dir", help="Base directory containing aggregated pattern folders")
    parser.add_argument("--output-dir", required=True, help="Output directory for verification results")
    args = parser.parse_args()

    verify_aggregation(args.pattern_csv, args.patterns_dir, args.output_dir)
