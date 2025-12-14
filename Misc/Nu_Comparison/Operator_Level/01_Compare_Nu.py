#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path
import pandas as pd


# ORCHESTRATOR

# Compare FFS results between nu=0.65 (baseline) and nu=0.5 (alternative)
def compare_nu_workflow(baseline_file: Path, alternative_file: Path, output_dir: Path) -> None:
    df_baseline = load_overview(baseline_file)
    df_alternative = load_overview(alternative_file)
    df_comparison = compute_comparison(df_baseline, df_alternative)
    export_comparison(df_comparison, output_dir)


# FUNCTIONS

# Load two_step_evaluation_overview.csv
def load_overview(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')


# Compute delta MRE: baseline - alternative (positive = alternative better)
def compute_comparison(df_baseline: pd.DataFrame, df_alternative: pd.DataFrame) -> pd.DataFrame:
    df = df_baseline[['operator', 'target']].copy()

    df['mre_ffs_0.65'] = df_baseline['mre_ffs']
    df['mre_ffs_0.5'] = df_alternative['mre_ffs']
    df['delta_mre_ffs'] = df['mre_ffs_0.65'] - df['mre_ffs_0.5']

    df['mre_final_0.65'] = df_baseline['mre_final']
    df['mre_final_0.5'] = df_alternative['mre_final']
    df['delta_mre_final'] = df['mre_final_0.65'] - df['mre_final_0.5']

    df['better_ffs'] = df['delta_mre_ffs'].apply(lambda x: 'nu=0.5' if x > 0 else 'nu=0.65')
    df['better_final'] = df['delta_mre_final'].apply(lambda x: 'nu=0.5' if x > 0 else 'nu=0.65')

    return df


# Export comparison results
def export_comparison(df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / '01_nu_comparison.csv'
    df.to_csv(output_file, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare FFS results between nu=0.65 and nu=0.5")
    parser.add_argument("--baseline", default="nu_0.65_overview.csv", help="Baseline overview (nu=0.65)")
    parser.add_argument("--alternative", default="nu_0.5_overview.csv", help="Alternative overview (nu=0.5)")
    parser.add_argument("--output-dir", default=".", help="Output directory")

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    baseline_path = script_dir / args.baseline
    alternative_path = script_dir / args.alternative
    output_path = Path(args.output_dir)

    compare_nu_workflow(baseline_path, alternative_path, output_path)
