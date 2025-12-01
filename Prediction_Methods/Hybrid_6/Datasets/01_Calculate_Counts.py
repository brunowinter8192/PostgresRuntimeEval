#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))


# ORCHESTRATOR
def calculate_operator_counts(patterns_csv: str, datasets_dir: str, output_dir: str) -> None:
    pattern_info = load_pattern_info(patterns_csv)
    operator_counts = compute_operator_counts_from_datasets(pattern_info, datasets_dir)
    export_to_csv(operator_counts, output_dir)


# FUNCTIONS

# Load pattern information from mining CSV
def load_pattern_info(patterns_csv: str) -> pd.DataFrame:
    df = pd.read_csv(patterns_csv, delimiter=';')
    return df[['pattern_hash', 'pattern_string', 'occurrence_count']]

# Compute operator counts using formula: operator_count = actual_rows / occurrence_count
def compute_operator_counts_from_datasets(pattern_info: pd.DataFrame, datasets_dir: str) -> pd.DataFrame:
    results = []
    baseline_dir = Path(datasets_dir) / 'Baseline'

    for _, row in pattern_info.iterrows():
        pattern_hash = row['pattern_hash']
        pattern_string = row['pattern_string']
        occurrence_count = row['occurrence_count']

        pattern_file = baseline_dir / pattern_hash / 'training.csv'

        if not pattern_file.exists():
            continue

        df = pd.read_csv(pattern_file, delimiter=';')
        actual_rows = len(df)

        operator_count = actual_rows // occurrence_count

        results.append({
            'pattern_hash': pattern_hash,
            'pattern_string': pattern_string,
            'operator_count': operator_count
        })

    return pd.DataFrame(results)

# Export operator counts to CSV
def export_to_csv(operator_counts_df: pd.DataFrame, output_dir: str) -> None:
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = csv_dir / f'01_operator_counts_{timestamp}.csv'
    operator_counts_df.to_csv(output_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("patterns_csv", help="Path to patterns CSV from Data_Generation")
    parser.add_argument("datasets_dir", help="Path to Datasets directory")
    parser.add_argument("--output-dir", required=True, help="Output directory for CSV export")
    args = parser.parse_args()

    calculate_operator_counts(args.patterns_csv, args.datasets_dir, args.output_dir)
