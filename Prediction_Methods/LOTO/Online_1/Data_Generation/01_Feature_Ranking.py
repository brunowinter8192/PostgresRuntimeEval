# INFRASTRUCTURE

import argparse
from pathlib import Path
from collections import Counter, defaultdict
import pandas as pd

# ORCHESTRATOR

def ranking_workflow(svm_base_dir: Path, output_dir: Path) -> None:
    ffs_counts, added_counts, feature_operator_counts, dataset_count, rows_per_dataset = collect_feature_counts(svm_base_dir)
    max_total = dataset_count * rows_per_dataset
    export_ranking(ffs_counts, added_counts, feature_operator_counts, max_total, output_dir)

# FUNCTIONS

# Collect feature counts from all two_step_evaluation_overview.csv files
def collect_feature_counts(svm_base_dir: Path) -> tuple[Counter, Counter, dict, int, int]:
    ffs_counter = Counter()
    added_counter = Counter()
    feature_operator_counts = defaultdict(Counter)
    dataset_count = 0
    rows_per_dataset = 0

    for template_dir in sorted(svm_base_dir.iterdir()):
        if not template_dir.is_dir() or not template_dir.name.startswith('Q'):
            continue

        overview_file = template_dir / 'two_step_evaluation_overview.csv'
        if not overview_file.exists():
            continue

        df = pd.read_csv(overview_file, delimiter=';')
        dataset_count += 1
        rows_per_dataset = len(df)

        for _, row in df.iterrows():
            operator = row['operator']
            ffs_features = parse_features(row['ffs_features'])
            missing_features = parse_features(row['missing_child_features'])
            final_features = parse_features(row['final_features'])

            for feature in ffs_features:
                ffs_counter[feature] += 1
            for feature in missing_features:
                added_counter[feature] += 1
            for feature in final_features:
                feature_operator_counts[feature][operator] += 1

    return ffs_counter, added_counter, feature_operator_counts, dataset_count, rows_per_dataset

# Parse comma-separated feature string
def parse_features(features_str: str) -> list:
    if pd.isna(features_str) or not features_str.strip():
        return []
    return [f.strip() for f in features_str.split(',') if f.strip()]

# Find top operator for a feature
def get_top_operator(feature: str, feature_operator_counts: dict) -> str:
    if feature not in feature_operator_counts:
        return ''
    op_counts = feature_operator_counts[feature]
    top_op = max(op_counts, key=op_counts.get)
    return f'{top_op} ({op_counts[top_op]})'

# Export ranking to CSV
def export_ranking(ffs_counts: Counter, added_counts: Counter, feature_operator_counts: dict, max_total: int, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    all_features = set(ffs_counts.keys()) | set(added_counts.keys())

    rows = []
    for feature in all_features:
        ffs = ffs_counts.get(feature, 0)
        added = added_counts.get(feature, 0)
        total = ffs + added
        top_operator = get_top_operator(feature, feature_operator_counts)
        rows.append({
            'feature': feature,
            'ffs_selected': ffs,
            'added_as_child': added,
            'total': total,
            'max_possible': max_total,
            'percentage': round(total / max_total * 100, 2),
            'top_operator': top_operator
        })

    df = pd.DataFrame(rows)
    df = df.sort_values('total', ascending=False)
    df.to_csv(output_dir / 'feature_ranking.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("svm_base_dir", help="Base directory containing Q1/, Q3/, ... folders with two_step_evaluation_overview.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for ranking CSV")

    args = parser.parse_args()

    ranking_workflow(Path(args.svm_base_dir), Path(args.output_dir))
