import argparse
import pandas as pd
from pathlib import Path

# INFRASTRUCTURE

OCCURRENCE_BINS = [0, 10, 50, 100, 200, float('inf')]
OCCURRENCE_LABELS = ['occ_001_010', 'occ_011_050', 'occ_051_100', 'occ_101_200', 'occ_200_plus']

# ORCHESTRATOR

def analyze_occurrence(selection_log: str, patterns_metadata: str, output_dir: str) -> None:
    df_log = load_selection_log(selection_log)
    df_meta = load_patterns_metadata(patterns_metadata)
    df_joined = join_data(df_log, df_meta)
    df_joined = assign_occurrence_class(df_joined)
    results = compute_class_statistics(df_joined)
    export_results(results, output_dir)

# FUNCTIONS

# Load selection log CSV
def load_selection_log(path: str) -> pd.DataFrame:
    return pd.read_csv(path, delimiter=';')

# Load patterns metadata CSV
def load_patterns_metadata(path: str) -> pd.DataFrame:
    return pd.read_csv(path, delimiter=';')[['pattern_hash', 'occurrence_count']]

# Join selection log with patterns metadata
def join_data(df_log: pd.DataFrame, df_meta: pd.DataFrame) -> pd.DataFrame:
    return df_log.merge(df_meta, on='pattern_hash', how='left')

# Assign occurrence class based on bins
def assign_occurrence_class(df: pd.DataFrame) -> pd.DataFrame:
    df['occurrence_class'] = pd.cut(
        df['occurrence_count'],
        bins=OCCURRENCE_BINS,
        labels=OCCURRENCE_LABELS,
        right=True
    )
    return df

# Compute statistics per occurrence class
def compute_class_statistics(df: pd.DataFrame) -> list:
    max_occurrence = int(df['occurrence_count'].max())
    results = []
    for i, label in enumerate(OCCURRENCE_LABELS):
        class_df = df[df['occurrence_class'] == label]
        selected_df = class_df[class_df['status'] == 'SELECTED']
        patterns_total = len(class_df)
        patterns_selected = len(selected_df)
        patterns_rejected = patterns_total - patterns_selected
        selection_rate = patterns_selected / patterns_total if patterns_total > 0 else 0
        total_delta = selected_df['delta'].sum() if len(selected_df) > 0 else 0
        avg_delta = selected_df['delta'].mean() if len(selected_df) > 0 else 0
        occ_max = int(OCCURRENCE_BINS[i + 1]) if OCCURRENCE_BINS[i + 1] != float('inf') else max_occurrence
        results.append({
            'occurrence_class': label,
            'occ_min': int(OCCURRENCE_BINS[i]) + 1 if i > 0 else 1,
            'occ_max': occ_max,
            'patterns_total': patterns_total,
            'patterns_selected': patterns_selected,
            'patterns_rejected': patterns_rejected,
            'selection_rate': round(selection_rate, 4),
            'total_delta': round(total_delta, 6),
            'avg_delta': round(avg_delta, 6)
        })
    return results

# Export results to CSV
def export_results(results: list, output_dir: str) -> None:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(results)
    df.to_csv(out_path / 'A_02c_occurrence.csv', sep=';', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("selection_log", help="Path to selection_log.csv")
    parser.add_argument("patterns_metadata", help="Path to 07_patterns_by_frequency.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()
    analyze_occurrence(args.selection_log, args.patterns_metadata, args.output_dir)
