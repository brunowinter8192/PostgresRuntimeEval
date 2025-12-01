#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

# From mapping_config.py: Pattern definitions
from mapping_config import PATTERNS


# ORCHESTRATOR
def analyze_all_patterns(dataset_base_dir: str, output_dir: str) -> None:
    analysis_results = []

    for pattern_hash in PATTERNS:
        result = analyze_pattern_nan(dataset_base_dir, pattern_hash)
        if result:
            analysis_results.append(result)

    export_nan_report(analysis_results, output_dir)


# FUNCTIONS

# Analyze single pattern for NaN values in training.csv
def analyze_pattern_nan(dataset_base_dir: str, pattern_hash: str) -> dict:
    pattern_dir = Path(dataset_base_dir) / pattern_hash
    training_file = pattern_dir / 'training.csv'

    if not training_file.exists():
        return None

    df = load_training_data(training_file)
    nan_columns = identify_nan_columns(df)

    if not nan_columns:
        return None

    return {
        'pattern_hash': pattern_hash,
        'nan_columns': nan_columns,
        'total_rows': len(df)
    }

# Load training pattern dataset
def load_training_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')

# Identify columns containing NaN values
def identify_nan_columns(df: pd.DataFrame) -> dict:
    nan_columns = {}

    for col in df.columns:
        nan_count = df[col].isna().sum()
        if nan_count > 0:
            nan_columns[col] = nan_count

    return nan_columns

# Export NaN analysis report to markdown
def export_nan_report(analysis_results: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    report_file = output_path / 'A_01e_training_nan_analysis.md'

    with open(report_file, 'w') as f:
        f.write('# NaN Value Analysis - training.csv (Before Aggregation)\n\n')
        f.write('Analyzing raw training data BEFORE aggregation to determine if NaN values exist in source data.\n\n')

        if not analysis_results:
            f.write('No NaN values found in any pattern training datasets.\n')
            return

        f.write(f'**Total patterns analyzed:** {len(PATTERNS)}\n')
        f.write(f'**Patterns with NaN values:** {len(analysis_results)}\n\n')
        f.write('---\n\n')

        for result in analysis_results:
            pattern_hash = result['pattern_hash']
            nan_columns = result['nan_columns']
            total_rows = result['total_rows']

            f.write(f'## Pattern: `{pattern_hash}`\n\n')
            f.write(f'**Total rows:** {total_rows}\n\n')
            f.write(f'**Columns with NaN values:** {len(nan_columns)}\n\n')

            for col, count in sorted(nan_columns.items()):
                percentage = (count / total_rows) * 100
                f.write(f'- `{col}`: {count} NaN values ({percentage:.2f}%)\n')

            f.write('\n---\n\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_base_dir", help="Base directory containing pattern subdirectories (e.g., Baseline/)")
    parser.add_argument("--output-dir", required=True, help="Output directory for markdown report")
    args = parser.parse_args()

    analyze_all_patterns(args.dataset_base_dir, args.output_dir)
