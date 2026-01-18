# INFRASTRUCTURE

import argparse
import pandas as pd
from pathlib import Path

STRATEGIES = ['Size', 'Frequency', 'Error']


# ORCHESTRATOR

# Compare selected patterns between Baseline and Epsilon variants
def compare_epsilon_variants(base_dir: str, output_dir: str) -> None:
    comparison_rows = []
    summary_rows = []

    for strategy in STRATEGIES:
        baseline_path = Path(base_dir) / strategy / 'Baseline' / 'selected_patterns.csv'
        epsilon_path = Path(base_dir) / strategy / 'Epsilon' / 'selected_patterns.csv'

        if not baseline_path.exists() or not epsilon_path.exists():
            continue

        baseline_df = load_selected_patterns(baseline_path)
        epsilon_df = load_selected_patterns(epsilon_path)

        comparison, summary = compare_patterns(strategy, baseline_df, epsilon_df)
        comparison_rows.extend(comparison)
        summary_rows.append(summary)

    export_results(comparison_rows, summary_rows, output_dir)


# FUNCTIONS

# Load selected patterns from CSV
def load_selected_patterns(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, delimiter=';')


# Compare patterns between baseline and epsilon
def compare_patterns(strategy: str, baseline_df: pd.DataFrame, epsilon_df: pd.DataFrame) -> tuple:
    baseline_hashes = set(baseline_df['pattern_hash'])
    epsilon_hashes = set(epsilon_df['pattern_hash'])

    both = baseline_hashes & epsilon_hashes
    baseline_only = baseline_hashes - epsilon_hashes
    epsilon_only = epsilon_hashes - baseline_hashes

    comparison = []

    for h in both:
        row = baseline_df[baseline_df['pattern_hash'] == h].iloc[0]
        comparison.append({
            'strategy': strategy,
            'pattern_hash': h,
            'pattern_string': row['pattern_string'],
            'status': 'both',
            'baseline_delta': row['delta'] * 100,
            'epsilon_delta': epsilon_df[epsilon_df['pattern_hash'] == h].iloc[0]['delta'] * 100
        })

    for h in baseline_only:
        row = baseline_df[baseline_df['pattern_hash'] == h].iloc[0]
        comparison.append({
            'strategy': strategy,
            'pattern_hash': h,
            'pattern_string': row['pattern_string'],
            'status': 'baseline_only',
            'baseline_delta': row['delta'] * 100,
            'epsilon_delta': None
        })

    for h in epsilon_only:
        row = epsilon_df[epsilon_df['pattern_hash'] == h].iloc[0]
        comparison.append({
            'strategy': strategy,
            'pattern_hash': h,
            'pattern_string': row['pattern_string'],
            'status': 'epsilon_only',
            'baseline_delta': None,
            'epsilon_delta': row['delta'] * 100
        })

    summary = {
        'strategy': strategy,
        'baseline_count': len(baseline_hashes),
        'epsilon_count': len(epsilon_hashes),
        'both_count': len(both),
        'baseline_only_count': len(baseline_only),
        'epsilon_only_count': len(epsilon_only)
    }

    return comparison, summary


# Export comparison and summary CSVs
def export_results(comparison_rows: list, summary_rows: list, output_dir: str) -> None:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    comparison_df = pd.DataFrame(comparison_rows)
    comparison_df.to_csv(out_path / 'A_02e_epsilon_comparison.csv', sep=';', index=False)

    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(out_path / 'A_02e_epsilon_summary.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", required=True, help="Pattern_Selection directory")
    parser.add_argument("--output-dir", required=True, help="Output directory")

    args = parser.parse_args()

    compare_epsilon_variants(args.base_dir, args.output_dir)
