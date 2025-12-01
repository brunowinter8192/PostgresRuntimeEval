#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

# From mapping_config.py: Pattern definitions and expected operator counts
from mapping_config import PATTERNS, PATTERN_OPERATOR_COUNT


# ORCHESTRATOR
def check_all_patterns(dataset_base_dir: str, output_dir: str) -> None:
    check_results = []

    for pattern_hash in PATTERNS:
        result = check_pattern_multiples(dataset_base_dir, pattern_hash)
        if result:
            check_results.append(result)

    export_multiples_report(check_results, output_dir)


# FUNCTIONS

# Check if all query instances are multiples of expected operator count
def check_pattern_multiples(dataset_base_dir: str, pattern_hash: str) -> dict:
    pattern_dir = Path(dataset_base_dir) / pattern_hash
    training_file = pattern_dir / 'training.csv'

    if not training_file.exists():
        return None

    df = load_training_data(training_file)
    operator_counts = count_operators_per_query(df)
    expected_count = PATTERN_OPERATOR_COUNT.get(pattern_hash)

    valid_queries = []
    invalid_queries = []

    for query_file, count in operator_counts.items():
        if count % expected_count == 0:
            valid_queries.append((query_file, count, count // expected_count))
        else:
            invalid_queries.append((query_file, count, count % expected_count))

    has_invalid = len(invalid_queries) > 0

    return {
        'pattern_hash': pattern_hash,
        'expected_count': expected_count,
        'total_queries': len(operator_counts),
        'valid_queries': len(valid_queries),
        'invalid_queries': len(invalid_queries),
        'invalid_details': invalid_queries,
        'has_invalid': has_invalid
    }

# Load training pattern dataset
def load_training_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')

# Count operators per query file
def count_operators_per_query(df: pd.DataFrame) -> dict:
    operator_counts = df.groupby('query_file').size().to_dict()
    return operator_counts

# Export multiples check report to markdown
def export_multiples_report(check_results: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    report_file = output_path / 'A_01h_multiples_check.md'

    patterns_with_invalid = [r for r in check_results if r['has_invalid']]
    patterns_all_valid = [r for r in check_results if not r['has_invalid']]

    with open(report_file, 'w') as f:
        f.write('# Operator Count Multiples Check\n\n')
        f.write('Checking if all query instances have operator counts that are multiples of PATTERN_OPERATOR_COUNT.\n\n')

        f.write(f'**Total patterns analyzed:** {len(check_results)}\n')
        f.write(f'**Patterns with non-multiples:** {len(patterns_with_invalid)}\n')
        f.write(f'**Patterns with all valid multiples:** {len(patterns_all_valid)}\n\n')

        if patterns_with_invalid:
            f.write('---\n\n')
            f.write('## Patterns with Non-Multiple Queries\n\n')

            for result in patterns_with_invalid:
                f.write(f'### Pattern: `{result["pattern_hash"]}`\n\n')
                f.write(f'- **Expected operator count:** {result["expected_count"]}\n')
                f.write(f'- **Total queries:** {result["total_queries"]}\n')
                f.write(f'- **Valid queries:** {result["valid_queries"]}\n')
                f.write(f'- **Invalid queries:** {result["invalid_queries"]}\n\n')

                if result['invalid_details']:
                    f.write('**Problematic queries:**\n\n')
                    f.write('| Query File | Operator Count | Remainder |\n')
                    f.write('|------------|----------------|----------|\n')
                    for query, count, remainder in result['invalid_details'][:10]:
                        f.write(f'| {query} | {count} | {remainder} |\n')

                    if len(result['invalid_details']) > 10:
                        f.write(f'\n... and {len(result["invalid_details"]) - 10} more\n')

                    f.write('\n')

        if patterns_all_valid:
            f.write('---\n\n')
            f.write('## Patterns with All Valid Multiples\n\n')

            for result in patterns_all_valid:
                f.write(f'- `{result["pattern_hash"]}`: {result["expected_count"]} operators ({result["total_queries"]} queries)\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_base_dir", help="Base directory containing pattern subdirectories (e.g., Baseline/)")
    parser.add_argument("--output-dir", required=True, help="Output directory for markdown report")
    args = parser.parse_args()

    check_all_patterns(args.dataset_base_dir, args.output_dir)
