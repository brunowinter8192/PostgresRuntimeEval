# INFRASTRUCTURE

import json
import pandas as pd
from pathlib import Path
import joblib
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

# From mapping_config.py: Convert CSV operator name to folder name, get operator features
from mapping_config import csv_name_to_folder_name, get_operator_features, LEAF_OPERATORS


# FUNCTIONS

# Load test dataset filtered to main plan only
def load_test_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load operator models from directory structure
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


# Load operator features from overview CSV or mapping_config fallback
def load_operator_features(overview_file: str) -> dict:
    features = {'execution_time': {}, 'start_time': {}}

    if overview_file and Path(overview_file).exists():
        df = pd.read_csv(overview_file, delimiter=';')

        for _, row in df.iterrows():
            operator = row['operator']
            target = row['target']
            features_str = row['final_features']

            if pd.isna(features_str) or features_str.strip() == '':
                continue

            features[target][operator] = [f.strip() for f in features_str.split(',')]

        return features

    all_operators = LEAF_OPERATORS + [
        'Hash Join', 'Merge Join', 'Nested Loop',
        'Hash', 'Sort', 'Aggregate', 'Materialize',
        'Limit', 'Result', 'Append', 'Subquery Scan',
        'Gather', 'Gather Merge', 'Group', 'Unique',
        'Hash Aggregate', 'Group Aggregate', 'WindowAgg',
        'Incremental Sort', 'Memoize', 'BitmapAnd', 'BitmapOr',
        'Bitmap Heap Scan', 'Bitmap Index Scan', 'CTE Scan'
    ]

    for op in all_operators:
        op_features = get_operator_features(op)
        features['execution_time'][op] = op_features
        features['start_time'][op] = op_features

    return features


# Load pattern models for selected hashes only
def load_pattern_models(model_dir: str, selected_hashes: list = None) -> dict:
    models = {}
    model_path = Path(model_dir)

    if not model_path.exists():
        return models

    hashes_to_load = selected_hashes if selected_hashes else []

    for pattern_hash in hashes_to_load:
        pattern_dir = model_path / pattern_hash

        if not pattern_dir.is_dir():
            continue

        exec_file = pattern_dir / 'model_execution_time.pkl'
        start_file = pattern_dir / 'model_start_time.pkl'
        features_file = pattern_dir / 'features.json'

        if not all(f.exists() for f in [exec_file, start_file, features_file]):
            continue

        with open(features_file, 'r') as f:
            features = json.load(f)

        models[pattern_hash] = {
            'execution_time': joblib.load(exec_file),
            'start_time': joblib.load(start_file),
            'features_exec': features['features_exec'],
            'features_start': features['features_start']
        }

    return models


# Load pattern features for loaded models
def load_pattern_features(ffs_file: str, pattern_models: dict) -> dict:
    df = pd.read_csv(ffs_file, delimiter=';')
    features = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']

        if pattern_hash not in pattern_models:
            continue

        if pattern_hash not in features:
            features[pattern_hash] = {}

        target = row['target']

        if pd.isna(row['final_features']) or row['final_features'] == '':
            features[pattern_hash][target] = []
        else:
            features[pattern_hash][target] = [f.strip() for f in row['final_features'].split(',')]

    return features


# Load pattern info from selected patterns and metadata
def load_pattern_info(selected_patterns_file: str, pattern_metadata_file: str) -> tuple:
    df_selected = pd.read_csv(selected_patterns_file, delimiter=';')
    df_metadata = pd.read_csv(pattern_metadata_file, delimiter=';')

    pattern_order = df_selected['pattern_hash'].tolist()

    df_merged = df_selected[['pattern_hash']].merge(
        df_metadata[['pattern_hash', 'pattern_string', 'pattern_length', 'operator_count']],
        on='pattern_hash',
        how='left'
    )

    info = {}

    for _, row in df_merged.iterrows():
        info[row['pattern_hash']] = {
            'length': int(row['pattern_length']),
            'operator_count': int(row['operator_count']),
            'pattern_string': row['pattern_string'] if pd.notna(row['pattern_string']) else 'N/A'
        }

    return info, pattern_order


# Create prediction result dictionary
def create_prediction_result(row, pred_start: float, pred_exec: float, prediction_type: str, pattern_hash: str = None) -> dict:
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
        'prediction_type': prediction_type,
        'pattern_hash': pattern_hash
    }


# Export predictions to CSV file
def export_predictions(predictions: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(predictions)
    df.to_csv(output_path / 'predictions.csv', sep=';', index=False)

    export_pattern_usage(df, output_path)


# Export pattern usage summary to separate CSV
def export_pattern_usage(df: pd.DataFrame, output_path: Path) -> None:
    pattern_df = df[df['pattern_hash'].notna()].copy()

    if pattern_df.empty:
        return

    usage = pattern_df.groupby('pattern_hash').agg(
        usage_count=('pattern_hash', 'count'),
        node_types=('node_type', lambda x: ', '.join(sorted(x.unique())))
    ).reset_index()

    usage = usage.sort_values('usage_count', ascending=False)
    usage.to_csv(output_path / 'patterns.csv', sep=';', index=False)
