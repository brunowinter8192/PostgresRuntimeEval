# INFRASTRUCTURE

import pandas as pd
import joblib
from pathlib import Path


# FUNCTIONS

# Load test data from CSV
def load_test_data(test_file: str) -> pd.DataFrame:
    df = pd.read_csv(test_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load pattern info from patterns.csv sorted by length descending
def load_pattern_info(patterns_csv: str) -> tuple:
    df = pd.read_csv(patterns_csv, delimiter=';')
    df_sorted = df.sort_values(['pattern_length', 'occurrence_count'], ascending=[False, False])
    pattern_order = df_sorted['pattern_hash'].tolist()

    info = {}
    for _, row in df_sorted.iterrows():
        info[row['pattern_hash']] = {
            'length': int(row['pattern_length']),
            'pattern_string': row['pattern_string']
        }

    return info, pattern_order


# Load pattern features from FFS overview for given patterns
def load_pattern_features(overview_file: str, pattern_hashes: list) -> dict:
    df = pd.read_csv(overview_file, delimiter=';')
    pattern_set = set(pattern_hashes)
    features = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']

        if pattern_hash not in pattern_set:
            continue

        if pattern_hash not in features:
            features[pattern_hash] = {}

        target = row['target']
        features_str = row['final_features']

        if pd.isna(features_str) or features_str.strip() == '':
            features[pattern_hash][target] = []
        else:
            features[pattern_hash][target] = [f.strip() for f in features_str.split(',')]

    return features


# Load pattern models from Model/Patterns/{target}/{hash}/model.pkl
def load_pattern_models(model_dir: str, pattern_hashes: list) -> dict:
    models = {'execution_time': {}, 'start_time': {}}
    model_path = Path(model_dir) / 'Patterns'

    for pattern_hash in pattern_hashes:
        for target in ['execution_time', 'start_time']:
            model_file = model_path / target / pattern_hash / 'model.pkl'

            if model_file.exists():
                models[target][pattern_hash] = joblib.load(model_file)

    return models


# Load operator features from overview CSV
def load_operator_features(operator_file: str) -> dict:
    df = pd.read_csv(operator_file, delimiter=';')
    features = {'execution_time': {}, 'start_time': {}}

    for _, row in df.iterrows():
        operator = row['operator']
        target = row['target']
        features_str = row['final_features']

        if pd.isna(features_str) or features_str.strip() == '':
            continue

        features[target][operator] = [f.strip() for f in features_str.split(',')]

    return features


# Load operator models from directory structure
def load_operator_models(model_dir: str) -> dict:
    models = {'execution_time': {}, 'start_time': {}}
    model_path = Path(model_dir)

    for target in ['execution_time', 'start_time']:
        target_dir = model_path / 'Operators' / target / 'operators'

        if not target_dir.exists():
            continue

        for op_dir in target_dir.iterdir():
            if op_dir.is_dir():
                model_file = op_dir / 'model.pkl'

                if model_file.exists():
                    models[target][op_dir.name] = joblib.load(model_file)

    return models


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
