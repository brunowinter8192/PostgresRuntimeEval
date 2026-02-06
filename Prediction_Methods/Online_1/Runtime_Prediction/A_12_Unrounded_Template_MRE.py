#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
EVALUATION_DIR = SCRIPT_DIR / 'Evaluation'


# ORCHESTRATOR
def unrounded_mre_workflow(output_dir: str) -> None:
    strategy_mres = compute_all_strategies()
    combined = combine_strategies(strategy_mres)
    export_csv(combined, output_dir)


# FUNCTIONS

# Compute unrounded template MRE for all three strategies
def compute_all_strategies() -> dict:
    return {
        strategy: compute_template_mre(EVALUATION_DIR / strategy)
        for strategy in ['Size', 'Frequency', 'Error']
    }


# Load all predictions.csv and compute MRE per template without rounding
def compute_template_mre(strategy_dir: Path) -> pd.Series:
    csv_files = list(strategy_dir.glob('*/csv/predictions.csv'))
    dfs = [pd.read_csv(f, delimiter=';') for f in csv_files]
    df = pd.concat(dfs, ignore_index=True)

    roots = df[df['depth'] == 0].copy()
    roots['template'] = roots['query_file'].apply(lambda x: x.split('_')[0])
    roots['mre'] = np.abs(
        roots['predicted_total_time'] - roots['actual_total_time']
    ) / roots['actual_total_time']

    return roots.groupby('template')['mre'].mean() * 100


# Combine all strategies into single DataFrame
def combine_strategies(strategy_mres: dict) -> pd.DataFrame:
    combined = pd.DataFrame({
        f'{s.lower()}_mre_pct': mre for s, mre in strategy_mres.items()
    })
    combined.index.name = 'template'
    combined = combined.sort_index(
        key=lambda x: x.str.extract(r'Q(\d+)')[0].astype(int)
    )
    return combined


# Export to CSV
def export_csv(df: pd.DataFrame, output_dir: str) -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    df.to_csv(Path(output_dir) / 'A_12_unrounded_template_mre.csv', sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        default=str(SCRIPT_DIR / 'Evaluation' / 'Analysis' / 'Overall'),
        help="Output directory"
    )
    args = parser.parse_args()

    unrounded_mre_workflow(args.output_dir)
