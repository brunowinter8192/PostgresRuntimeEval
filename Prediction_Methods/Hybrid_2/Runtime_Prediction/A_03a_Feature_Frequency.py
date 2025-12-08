import argparse
import pandas as pd
from pathlib import Path
from collections import Counter

# INFRASTRUCTURE

OPERATOR_PREFIXES = [
    'GatherMerge_', 'HashJoin_', 'NestedLoop_', 'MergeJoin_', 'IncrementalSort_',
    'IndexOnlyScan_', 'IndexScan_', 'SeqScan_',
    'Aggregate_', 'Gather_', 'Limit_', 'Sort_', 'Hash_'
]
EXCLUDE_FEATURES = ['actual_total_time', 'actual_startup_time']

# ORCHESTRATOR

def analyze_features(ffs_overview: str, output_dir: str) -> None:
    df = load_data(ffs_overview)
    for target in ['execution_time', 'start_time']:
        df_target = df[df['target'] == target]
        feature_counts = count_base_features(df_target)
        export_frequency(feature_counts, target, output_dir)

# FUNCTIONS

# Load pattern FFS overview
def load_data(ffs_overview: str) -> pd.DataFrame:
    return pd.read_csv(ffs_overview, delimiter=';')

# Strip operator and position prefixes from feature name
def strip_operator_prefix(feature: str) -> str:
    for prefix in OPERATOR_PREFIXES:
        if feature.startswith(prefix):
            feature = feature[len(prefix):]
            break
    if feature.startswith('Outer_'):
        feature = feature[6:]
    elif feature.startswith('Inner_'):
        feature = feature[6:]
    return feature

# Count base feature occurrences across all patterns
def count_base_features(df: pd.DataFrame) -> Counter:
    counter = Counter()
    for features_str in df['final_features'].dropna():
        features = [f.strip() for f in features_str.split(',')]
        features = [f for f in features if f not in EXCLUDE_FEATURES]
        base_features = [strip_operator_prefix(f) for f in features]
        counter.update(base_features)
    return counter

# Export feature frequency to CSV
def export_frequency(counter: Counter, target: str, output_dir: str) -> None:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    rows = []
    for feature, count in counter.most_common():
        rows.append({'feature': feature, 'count': count})
    df = pd.DataFrame(rows)
    df.to_csv(out_path / f'A_03a_feature_frequency_{target}.csv', sep=';', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ffs_overview", help="Path to pattern_ffs_overview.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()
    analyze_features(args.ffs_overview, args.output_dir)
