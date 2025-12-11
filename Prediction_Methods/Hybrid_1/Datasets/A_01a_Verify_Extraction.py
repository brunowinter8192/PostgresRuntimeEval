#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime


# ORCHESTRATOR
def verify_extraction(pattern_csv: str, patterns_base_dir: str, output_dir: str) -> None:
    pattern_data = load_pattern_data(pattern_csv)
    verification_results = verify_all_patterns(pattern_data, patterns_base_dir)
    export_results(verification_results, output_dir)


# FUNCTIONS

# Load pattern data from 01_Find_Patterns.py output
def load_pattern_data(pattern_csv: str) -> pd.DataFrame:
    df = pd.read_csv(pattern_csv, delimiter=';')
    return df[['pattern_hash', 'pattern_string', 'operator_count', 'occurrence_count']]


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
    patterns_path = Path(patterns_base_dir) / 'patterns'

    for _, row in pattern_data.iterrows():
        pattern_hash = row['pattern_hash']
        pattern_str = row['pattern_string']
        total_occurrences = row['occurrence_count']
        num_operators = row['operator_count']

        expected_rows = total_occurrences * num_operators

        pattern_folder = patterns_path / pattern_hash

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
            'pattern_hash': pattern_hash,
            'pattern_string': pattern_str,
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
    output_file = csv_dir / f'A_01a_extraction_verification_{timestamp}.csv'
    results.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern_csv", help="Path to pattern analysis CSV from find_all_patterns.py")
    parser.add_argument("patterns_dir", help="Base directory containing patterns subfolder")
    parser.add_argument("--output-dir", required=True, help="Output directory for verification results")
    args = parser.parse_args()

    verify_extraction(args.pattern_csv, args.patterns_dir, args.output_dir)
