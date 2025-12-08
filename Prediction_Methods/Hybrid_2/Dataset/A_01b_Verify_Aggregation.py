#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime


# ORCHESTRATOR
def verify_aggregation(patterns_csv: str, patterns_dir: str, output_dir: str) -> None:
    pattern_info = load_pattern_info(patterns_csv)
    verification_results = verify_all_patterns(pattern_info, patterns_dir)
    export_results(verification_results, output_dir)


# FUNCTIONS

# Load pattern information from mining CSV
def load_pattern_info(patterns_csv: str) -> pd.DataFrame:
    df = pd.read_csv(patterns_csv, delimiter=';')
    return df[['pattern_hash', 'pattern_string', 'pattern_length', 'occurrence_count']]


# Verify all patterns against expected row counts
def verify_all_patterns(pattern_info: pd.DataFrame, patterns_dir: str) -> pd.DataFrame:
    results = []
    base_dir = Path(patterns_dir)

    for _, row in pattern_info.iterrows():
        pattern_hash = row['pattern_hash']
        pattern_string = row['pattern_string']
        pattern_length = row['pattern_length']
        occurrence_count = row['occurrence_count']

        expected_rows = occurrence_count

        pattern_file = base_dir / pattern_hash / 'training_aggregated.csv'
        actual_rows = count_csv_rows(pattern_file)

        if actual_rows is None:
            status = 'MISSING'
        elif actual_rows == expected_rows:
            status = 'OK'
        else:
            status = 'MISMATCH'

        results.append({
            'pattern_hash': pattern_hash,
            'pattern_string': pattern_string,
            'pattern_length': pattern_length,
            'occurrence_count': occurrence_count,
            'expected_rows': expected_rows,
            'actual_rows': actual_rows if actual_rows is not None else 0,
            'status': status
        })

    return pd.DataFrame(results)


# Count rows in CSV file excluding header
def count_csv_rows(csv_file: Path) -> int:
    if not csv_file.exists():
        return None

    df = pd.read_csv(csv_file, delimiter=';')
    return len(df)


# Export verification results to CSV
def export_results(results: pd.DataFrame, output_dir: str) -> None:
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = csv_dir / f'A_01b_aggregation_verification_{timestamp}.csv'
    results.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("patterns_csv", help="Path to 01_patterns_*.csv from Data_Generation")
    parser.add_argument("patterns_dir", help="Path to Patterns directory")
    parser.add_argument("--output-dir", required=True, help="Output directory for verification results")
    args = parser.parse_args()

    verify_aggregation(args.patterns_csv, args.patterns_dir, args.output_dir)
