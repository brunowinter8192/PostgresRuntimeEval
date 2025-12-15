#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path
import pandas as pd


# ORCHESTRATOR

# Compare FFS results between nu=0.5 (baseline) and nu=0.65 (alternative)
def compare_nu_workflow(baseline_file: Path, alternative_file: Path, output_dir: Path) -> None:
    df_baseline = load_summary(baseline_file)
    df_alternative = load_summary(alternative_file)
    df_comparison = compute_comparison(df_baseline, df_alternative)
    export_comparison(df_comparison, output_dir)


# FUNCTIONS

# Load 01_ffs_summary.csv
def load_summary(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')


# Compute delta MRE: baseline - alternative (positive = alternative better)
def compute_comparison(df_baseline: pd.DataFrame, df_alternative: pd.DataFrame) -> pd.DataFrame:
    data = {
        'mre_0.5': df_baseline['final_mre'].iloc[0],
        'mre_0.65': df_alternative['final_mre'].iloc[0],
        'delta_mre': df_baseline['final_mre'].iloc[0] - df_alternative['final_mre'].iloc[0],
        'n_features_0.5': df_baseline['n_features'].iloc[0],
        'n_features_0.65': df_alternative['n_features'].iloc[0],
        'features_0.5': df_baseline['selected_features'].iloc[0],
        'features_0.65': df_alternative['selected_features'].iloc[0]
    }

    data['better'] = 'nu=0.65' if data['delta_mre'] > 0 else 'nu=0.5'

    return pd.DataFrame([data])


# Export comparison results
def export_comparison(df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / '01_nu_comparison.csv'
    df.to_csv(output_file, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare FFS results between nu=0.5 and nu=0.65")
    parser.add_argument("--baseline", default="nu_0.5_summary.csv", help="Baseline summary (nu=0.5)")
    parser.add_argument("--alternative", default="nu_0.65_summary.csv", help="Alternative summary (nu=0.65)")
    parser.add_argument("--output-dir", default=".", help="Output directory")

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    baseline_path = script_dir / args.baseline
    alternative_path = script_dir / args.alternative
    output_path = Path(args.output_dir)

    compare_nu_workflow(baseline_path, alternative_path, output_path)
