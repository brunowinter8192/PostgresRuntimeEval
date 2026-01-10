#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path


# ORCHESTRATOR
def analyze_pattern_usage(evaluation_dir: str, selection_dir: str, output_dir: str) -> None:
    pattern_templates = load_pattern_templates(selection_dir)
    for strategy in ['Size', 'Frequency', 'Error']:
        for config in ['Baseline', 'Epsilon']:
            usage_df = build_usage_for_config(evaluation_dir, selection_dir, strategy, config, pattern_templates)
            export_usage(usage_df, output_dir, strategy, config)


# FUNCTIONS

# Load pattern to templates mapping from test occurrences
def load_pattern_templates(selection_dir: str) -> dict:
    occ_file = Path(selection_dir) / '06_test_pattern_occurrences.csv'
    if not occ_file.exists():
        return {}

    df = pd.read_csv(occ_file, delimiter=';')
    templates = {}
    for _, row in df.iterrows():
        h = row['pattern_hash']
        t = row['template']
        if h not in templates:
            templates[h] = set()
        templates[h].add(t)

    return templates


# Build usage table for one strategy/config combination
def build_usage_for_config(evaluation_dir: str, selection_dir: str, strategy: str, config: str, pattern_templates: dict) -> pd.DataFrame:
    selected = load_selected_patterns(selection_dir, strategy, config)
    used_hashes = load_used_hashes(evaluation_dir, strategy, config)

    rows = []
    for _, row in selected.iterrows():
        pattern_hash = row['pattern_hash']
        pattern_string = row['pattern_string']
        status = 'genutzt' if pattern_hash in used_hashes else 'beifang'
        templates = sorted(pattern_templates.get(pattern_hash, set()), key=lambda x: int(x[1:]))
        rows.append({
            'pattern_hash': pattern_hash,
            'pattern_string': pattern_string,
            'status': status,
            'templates': ','.join(templates)
        })

    return pd.DataFrame(rows)


# Load selected patterns from Pattern_Selection directory
def load_selected_patterns(selection_dir: str, strategy: str, config: str) -> pd.DataFrame:
    sel_file = Path(selection_dir) / strategy / config / 'selected_patterns.csv'
    if sel_file.exists():
        return pd.read_csv(sel_file, delimiter=';')[['pattern_hash', 'pattern_string']]
    return pd.DataFrame(columns=['pattern_hash', 'pattern_string'])


# Load used pattern hashes from predictions
def load_used_hashes(evaluation_dir: str, strategy: str, config: str) -> set:
    pred_file = Path(evaluation_dir) / strategy / config / '12_predictions.csv'
    if pred_file.exists():
        df = pd.read_csv(pred_file, delimiter=';')
        pattern_preds = df[df['prediction_type'] == 'pattern']
        return set(pattern_preds['pattern_hash'].dropna().unique())
    return set()


# Export usage table for one strategy/config
def export_usage(usage_df: pd.DataFrame, output_dir: str, strategy: str, config: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    filename = f'A_02c_{strategy}_{config}.csv'
    usage_df.to_csv(output_path / filename, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('evaluation_dir', help='Path to Evaluation directory')
    parser.add_argument('--selection-dir', required=True, help='Path to Pattern_Selection directory')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    args = parser.parse_args()

    analyze_pattern_usage(args.evaluation_dir, args.selection_dir, args.output_dir)
