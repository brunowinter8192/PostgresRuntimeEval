#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from collections import Counter


# ORCHESTRATOR
def check_node_types(training_file: str, expected_types: list, output_dir: str) -> None:
    df = load_training_data(training_file)
    node_type_analysis = analyze_node_types(df, expected_types)
    export_node_types_report(node_type_analysis, training_file, output_dir)


# FUNCTIONS

# Load training pattern dataset
def load_training_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')

# Analyze node type + parent relationship combinations in dataset
def analyze_node_types(df: pd.DataFrame, expected_types: list) -> dict:
    df['combination'] = df.apply(
        lambda row: f"{row['node_type']} | {row['parent_relationship']}"
        if pd.notna(row['parent_relationship'])
        else f"{row['node_type']} | None",
        axis=1
    )

    actual_combinations = df['combination'].value_counts().to_dict()
    expected_set = set(expected_types)
    actual_set = set(actual_combinations.keys())

    unexpected_combinations = actual_set - expected_set
    missing_combinations = expected_set - actual_set

    return {
        'expected_types': expected_types,
        'actual_types': actual_combinations,
        'unexpected_types': list(unexpected_combinations),
        'missing_types': list(missing_combinations),
        'has_unexpected': len(unexpected_combinations) > 0,
        'has_missing': len(missing_combinations) > 0,
        'total_rows': len(df)
    }

# Export node types report to markdown
def export_node_types_report(analysis: dict, training_file: str, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    pattern_hash = Path(training_file).parent.name
    report_file = output_path / f'A_01i_node_types_{pattern_hash}.md'

    with open(report_file, 'w') as f:
        f.write(f'# Node Type + Parent Relationship Analysis - Pattern `{pattern_hash}`\n\n')
        f.write(f'**Total rows:** {analysis["total_rows"]}\n\n')

        f.write('## Expected Combinations\n\n')
        for combo in analysis['expected_types']:
            f.write(f'- {combo}\n')
        f.write('\n')

        f.write('## Actual Combinations\n\n')
        f.write('| Node Type + Relationship | Count | Percentage |\n')
        f.write('|--------------------------|-------|------------|\n')
        for combo, count in sorted(analysis['actual_types'].items(), key=lambda x: -x[1]):
            percentage = (count / analysis['total_rows']) * 100
            f.write(f'| {combo} | {count} | {percentage:.2f}% |\n')
        f.write('\n')

        if analysis['has_unexpected']:
            f.write('## PROBLEM: Unexpected Combinations Found!\n\n')
            f.write('These combinations were NOT expected but are present in the dataset:\n\n')
            for combo in analysis['unexpected_types']:
                count = analysis['actual_types'][combo]
                f.write(f'- **{combo}**: {count} occurrences\n')
            f.write('\n')
            f.write('This explains the NaN values! Different pattern instances have different operator structures.\n\n')
        else:
            f.write('## Result: All Combinations Match Expected\n\n')
            f.write('No unexpected combinations found. All instances use the same structure.\n\n')

        if analysis['has_missing']:
            f.write('## Warning: Missing Expected Combinations\n\n')
            f.write('These combinations were expected but NOT found:\n\n')
            for combo in analysis['missing_types']:
                f.write(f'- {combo}\n')
            f.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("training_file", help="Path to training.csv file")
    parser.add_argument("--expected-types", nargs='+', required=True, help="Expected node types (space-separated)")
    parser.add_argument("--output-dir", required=True, help="Output directory for markdown report")
    args = parser.parse_args()

    check_node_types(args.training_file, args.expected_types, args.output_dir)
