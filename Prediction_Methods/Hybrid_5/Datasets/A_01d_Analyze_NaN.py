#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

# From mapping_config.py: Pattern definitions and feature exclusions
from mapping_config import PATTERNS, NON_FEATURE_SUFFIXES


# ORCHESTRATOR
def analyze_all_patterns(dataset_base_dir: str, output_dir: str) -> None:
    analysis_results = []

    for pattern_hash in PATTERNS:
        result = analyze_pattern_nan(dataset_base_dir, pattern_hash)
        if result:
            analysis_results.append(result)

    export_nan_report(analysis_results, output_dir)


# FUNCTIONS

# Analyze single pattern for NaN values
def analyze_pattern_nan(dataset_base_dir: str, pattern_hash: str) -> dict:
    pattern_dir = Path(dataset_base_dir) / pattern_hash
    cleaned_file = pattern_dir / 'training_cleaned.csv'

    if not cleaned_file.exists():
        return None

    df = load_cleaned_data(cleaned_file)
    nan_columns = identify_nan_columns(df)

    if not nan_columns:
        return None

    return {
        'pattern_hash': pattern_hash,
        'nan_columns': nan_columns,
        'total_rows': len(df)
    }

# Load cleaned pattern dataset
def load_cleaned_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')

# Extract FFS-relevant features using same logic as Feature Selection
def extract_ffs_features(df: pd.DataFrame) -> list:
    non_feature_cols = ['query_file']

    ffs_features = []
    for col in df.columns:
        if col in non_feature_cols:
            continue
        if any(col.endswith(suffix) for suffix in NON_FEATURE_SUFFIXES):
            continue
        ffs_features.append(col)

    return ffs_features

# Identify NaN values in FFS-relevant features only
def identify_nan_columns(df: pd.DataFrame) -> dict:
    ffs_features = extract_ffs_features(df)
    nan_columns = {}

    for col in ffs_features:
        nan_count = df[col].isna().sum()
        if nan_count > 0:
            nan_columns[col] = nan_count

    return nan_columns

# Export NaN analysis report to markdown
def export_nan_report(analysis_results: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    report_file = output_path / 'A_01d_nan_analysis.md'

    with open(report_file, 'w') as f:
        f.write('# NaN Value Analysis - FFS-Relevant Features Only\n\n')
        f.write('Analyzing only features used by Forward Feature Selection.\n')
        f.write('Excludes: query_file, metadata columns (*_node_id, *_node_type, *_depth, *_parent_relationship, *_subplan_name, *_actual_startup_time, *_actual_total_time)\n\n')

        if not analysis_results:
            f.write('No NaN values found in any pattern datasets.\n')
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
