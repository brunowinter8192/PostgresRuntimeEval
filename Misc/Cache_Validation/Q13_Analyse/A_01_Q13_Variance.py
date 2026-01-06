# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path

# ORCHESTRATOR
def main(plan_level_csv: str, operator_csv: str, output_dir: str) -> None:
    plan_df = load_plan_level(plan_level_csv)
    op_df = load_operator_level(operator_csv)

    row_count_stats = analyze_row_count(plan_df)
    seq_scan_stats = analyze_seq_scan(op_df)

    export_results(row_count_stats, seq_scan_stats, output_dir)

# FUNCTIONS
# Load Plan-Level dataset
def load_plan_level(path: str) -> pd.DataFrame:
    return pd.read_csv(path, delimiter=';')

# Load Operator-Level dataset
def load_operator_level(path: str) -> pd.DataFrame:
    return pd.read_csv(path, delimiter=';')

# Analyze Q13 row_count variance
def analyze_row_count(df: pd.DataFrame) -> dict:
    q13 = df[df['template'] == 'Q13']
    mean = q13['row_count'].mean()
    std = q13['row_count'].std()
    cv = (std / mean) * 100
    return {
        'metric': 'row_count',
        'n': len(q13),
        'mean': mean,
        'std': std,
        'cv_percent': cv,
        'min': q13['row_count'].min(),
        'max': q13['row_count'].max()
    }

# Analyze Q13 Seq Scan runtime variance
def analyze_seq_scan(df: pd.DataFrame) -> dict:
    q13 = df[df['query_file'].str.startswith('Q13_')]
    seq_scan = q13[q13['node_type'] == 'Seq Scan']
    mean = seq_scan['actual_total_time'].mean()
    std = seq_scan['actual_total_time'].std()
    cv = (std / mean) * 100
    return {
        'metric': 'seq_scan_runtime',
        'n': len(seq_scan),
        'mean': mean,
        'std': std,
        'cv_percent': cv,
        'min': seq_scan['actual_total_time'].min(),
        'max': seq_scan['actual_total_time'].max()
    }

# Export results to CSV
def export_results(row_count: dict, seq_scan: dict, output_dir: str) -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    results = pd.DataFrame([row_count, seq_scan])
    results.to_csv(f'{output_dir}/A_01_q13_variance.csv', sep=';', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("plan_level_csv", help="Path to Plan-Level complete_dataset.csv")
    parser.add_argument("operator_csv", help="Path to Operator-Level operator_dataset_cleaned.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")

    args = parser.parse_args()
    main(args.plan_level_csv, args.operator_csv, args.output_dir)
