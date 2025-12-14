# INFRASTRUCTURE

import json
import numpy as np
import pandas as pd
from pathlib import Path
import joblib


# FUNCTIONS

# Load operator models from directory
def load_operator_models(model_dir: str) -> dict:
    models = {'execution_time': {}, 'start_time': {}}
    model_path = Path(model_dir)

    for target in ['execution_time', 'start_time']:
        target_dir = model_path / target

        if not target_dir.exists():
            continue

        for op_dir in target_dir.iterdir():
            if op_dir.is_dir():
                model_file = op_dir / 'model.pkl'

                if model_file.exists():
                    models[target][op_dir.name] = joblib.load(model_file)

    return models


# Load operator FFS features from directory (preserving order)
def load_operator_ffs(ffs_dir: str) -> dict:
    features = {'execution_time': {}, 'start_time': {}}
    ffs_path = Path(ffs_dir)

    for target in ['execution_time', 'start_time']:
        target_dir = ffs_path / target

        if not target_dir.exists():
            continue

        for op_folder in target_dir.iterdir():
            if op_folder.is_dir() and op_folder.name.endswith('_csv'):
                op_name = op_folder.name.replace('_csv', '')
                ffs_file = op_folder / 'final_features.csv'

                if ffs_file.exists():
                    df = pd.read_csv(ffs_file, delimiter=';')
                    df = df.sort_values('order')
                    features[target][op_name] = df['feature'].tolist()

    return features


# Load pattern FFS features from overview CSV
def load_pattern_ffs(pattern_ffs_file: str) -> dict:
    df = pd.read_csv(pattern_ffs_file, delimiter=';')
    features = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']
        target = row['target']

        if pattern_hash not in features:
            features[pattern_hash] = {}

        if pd.isna(row['final_features']) or row['final_features'] == '':
            features[pattern_hash][target] = []
        else:
            features[pattern_hash][target] = [f.strip() for f in row['final_features'].split(',')]

    return features


# Load sorted patterns from CSV
def load_sorted_patterns(sorted_patterns_file: str) -> pd.DataFrame:
    return pd.read_csv(sorted_patterns_file, delimiter=';')


# Load pattern occurrences from CSV (for error strategy)
def load_pattern_occurrences(pattern_occurrences_file: str) -> pd.DataFrame:
    return pd.read_csv(pattern_occurrences_file, delimiter=';')


# Count unique templates per pattern from occurrences
def count_templates_per_pattern(pattern_occurrences: pd.DataFrame) -> dict:
    df = pattern_occurrences.copy()
    df['template'] = df['query_file'].str.split('_').str[0]
    return df.groupby('pattern_hash')['template'].nunique().to_dict()


# Load training data filtered to main plan
def load_training_data(training_file: str) -> pd.DataFrame:
    df = pd.read_csv(training_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load test data filtered to main plan
def load_test_data(test_file: str) -> pd.DataFrame:
    df = pd.read_csv(test_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load pretrained model from disk
def load_pretrained_model(pretrained_dir: str, pattern_hash: str) -> dict:
    pattern_path = Path(pretrained_dir) / pattern_hash

    if not pattern_path.exists():
        return None

    model_exec_file = pattern_path / 'model_execution_time.pkl'
    model_start_file = pattern_path / 'model_start_time.pkl'
    features_file = pattern_path / 'features.json'

    if not all(f.exists() for f in [model_exec_file, model_start_file, features_file]):
        return None

    with open(features_file, 'r') as f:
        features = json.load(f)

    return {
        'execution_time': joblib.load(model_exec_file),
        'start_time': joblib.load(model_start_file),
        'features_exec': features['features_exec'],
        'features_start': features['features_start']
    }


# Create log entry dict
def create_log_entry(
    pattern_hash: str,
    pattern_string: str,
    baseline_mre: float,
    new_mre: float,
    delta: float,
    status: str,
    iteration: int
) -> dict:
    return {
        'iteration': iteration,
        'pattern_hash': pattern_hash,
        'pattern_string': pattern_string,
        'baseline_mre': baseline_mre,
        'new_mre': new_mre,
        'delta': delta,
        'status': status
    }


# Create prediction result dict
def create_prediction_result(row, pred_start: float, pred_exec: float, prediction_type: str) -> dict:
    return {
        'query_file': row['query_file'],
        'node_id': row['node_id'],
        'node_type': row['node_type'],
        'depth': row['depth'],
        'parent_relationship': row['parent_relationship'],
        'subplan_name': row['subplan_name'],
        'actual_startup_time': row['actual_startup_time'],
        'actual_total_time': row['actual_total_time'],
        'predicted_startup_time': pred_start,
        'predicted_total_time': pred_exec,
        'prediction_type': prediction_type
    }


# Calculate MRE on root operators
def calculate_mre(predictions: list) -> float:
    root_preds = [p for p in predictions if p['depth'] == 0]

    if not root_preds:
        return float('inf')

    mre_values = []

    for p in root_preds:
        if p['actual_total_time'] > 0:
            mre = abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time']
            mre_values.append(mre)

    return np.mean(mre_values) if mre_values else float('inf')


# Export per-pattern results
def export_pattern_results(
    output_dir: str,
    pattern_hash: str,
    pattern_string: str,
    predictions: list,
    mre: float,
    status: str
) -> None:
    pattern_dir = Path(output_dir) / pattern_hash
    pattern_dir.mkdir(parents=True, exist_ok=True)

    df_preds = pd.DataFrame(predictions)
    df_preds.to_csv(pattern_dir / 'predictions.csv', sep=';', index=False)

    mre_df = pd.DataFrame({
        'pattern_hash': [pattern_hash],
        'pattern_string': [pattern_string],
        'mre': [mre],
        'mre_pct': [mre * 100],
        'status': [status]
    })
    mre_df.to_csv(pattern_dir / 'mre.csv', sep=';', index=False)

    with open(pattern_dir / 'status.txt', 'w') as f:
        f.write(status)


# Export selection summary
def export_selection_summary(output_dir: str, selection_log: list) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    log_df = pd.DataFrame(selection_log)
    log_df.to_csv(output_path / 'selection_log.csv', sep=';', index=False)

    selected_df = log_df[log_df['status'] == 'SELECTED']
    selected_df.to_csv(output_path / 'selected_patterns.csv', sep=';', index=False)

    summary = {
        'total_patterns': len(selection_log),
        'selected': len([s for s in selection_log if s['status'] == 'SELECTED']),
        'rejected': len([s for s in selection_log if s['status'] == 'REJECTED']),
        'skipped_no_ffs': len([s for s in selection_log if s['status'] == 'SKIPPED_NO_FFS']),
        'skipped_train_failed': len([s for s in selection_log if s['status'] == 'SKIPPED_TRAIN_FAILED']),
        'skipped_low_template_count': len([s for s in selection_log if s['status'] == 'SKIPPED_LOW_TEMPLATE_COUNT']),
        'final_mre': selection_log[-1]['baseline_mre'] if selection_log else None
    }
    summary_df = pd.DataFrame([summary])
    summary_df.to_csv(output_path / 'selection_summary.csv', sep=';', index=False)
