#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import sys
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent.parent))

# From mapping_config.py: Pattern definitions and expected operator counts
from mapping_config import PATTERNS, PATTERN_OPERATOR_COUNT


# ORCHESTRATOR
def verify_all_patterns(dataset_base_dir: str, output_dir: str) -> None:
    verification_results = []

    for pattern_hash in PATTERNS:
        result = verify_pattern_operator_count(dataset_base_dir, pattern_hash)
        if result:
            verification_results.append(result)

    export_verification_report(verification_results, output_dir)


# FUNCTIONS

# Verify operator count for single pattern
def verify_pattern_operator_count(dataset_base_dir: str, pattern_hash: str) -> dict:
    pattern_dir = Path(dataset_base_dir) / pattern_hash
    training_file = pattern_dir / 'training.csv'

    if not training_file.exists():
        return None

    df = load_training_data(training_file)
    operator_counts = count_operators_per_query(df)
    expected_count = PATTERN_OPERATOR_COUNT.get(pattern_hash)

    count_stats = analyze_operator_counts(operator_counts)
    has_mismatch = (count_stats['min'] != expected_count or
                    count_stats['max'] != expected_count)

    return {
        'pattern_hash': pattern_hash,
        'expected_count': expected_count,
        'actual_min': count_stats['min'],
        'actual_max': count_stats['max'],
        'actual_mode': count_stats['mode'],
        'unique_counts': count_stats['unique_counts'],
        'has_mismatch': has_mismatch,
        'total_instances': len(operator_counts)
    }

# Load training pattern dataset
def load_training_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')

# Count operators per query file
def count_operators_per_query(df: pd.DataFrame) -> dict:
    operator_counts = df.groupby('query_file').size().to_dict()
    return operator_counts

# Analyze operator count statistics
def analyze_operator_counts(operator_counts: dict) -> dict:
    counts = list(operator_counts.values())
    count_distribution = Counter(counts)

    return {
        'min': min(counts),
        'max': max(counts),
        'mode': count_distribution.most_common(1)[0][0],
        'unique_counts': dict(count_distribution)
    }

# Export verification report to markdown
def export_verification_report(verification_results: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    report_file = output_path / 'A_01f_operator_count_verification.md'

    mismatches = [r for r in verification_results if r['has_mismatch']]
    matches = [r for r in verification_results if not r['has_mismatch']]

    with open(report_file, 'w') as f:
        f.write('# Operator Count Verification\n\n')
        f.write('Verifying that actual operator counts match expected PATTERN_OPERATOR_COUNT values.\n\n')

        f.write(f'**Total patterns analyzed:** {len(verification_results)}\n')
        f.write(f'**Patterns with mismatches:** {len(mismatches)}\n')
        f.write(f'**Patterns matching expected:** {len(matches)}\n\n')

        if mismatches:
            f.write('---\n\n')
            f.write('## Patterns with Mismatches\n\n')

            for result in mismatches:
                f.write(f'### Pattern: `{result["pattern_hash"]}`\n\n')
                f.write(f'- **Expected count:** {result["expected_count"]}\n')
                f.write(f'- **Actual min:** {result["actual_min"]}\n')
                f.write(f'- **Actual max:** {result["actual_max"]}\n')
                f.write(f'- **Actual mode:** {result["actual_mode"]}\n')
                f.write(f'- **Total instances:** {result["total_instances"]}\n')
                f.write(f'- **Count distribution:**\n')
                for count, freq in sorted(result['unique_counts'].items()):
                    percentage = (freq / result['total_instances']) * 100
                    f.write(f'  - {count} operators: {freq} instances ({percentage:.2f}%)\n')
                f.write('\n')

        if matches:
            f.write('---\n\n')
            f.write('## Patterns Matching Expected Count\n\n')

            for result in matches:
                f.write(f'- `{result["pattern_hash"]}`: {result["expected_count"]} operators ({result["total_instances"]} instances)\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_base_dir", help="Base directory containing pattern subdirectories (e.g., Baseline/)")
    parser.add_argument("--output-dir", required=True, help="Output directory for markdown report")
    args = parser.parse_args()

    verify_all_patterns(args.dataset_base_dir, args.output_dir)
