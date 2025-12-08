# INFRASTRUCTURE

import json
import pandas as pd
import joblib
from pathlib import Path


# FUNCTIONS

# Load test data from CSV
def load_test_data(test_file: str) -> pd.DataFrame:
    return pd.read_csv(test_file, delimiter=';')


# Load pattern features from overview CSV with hash mapping
def load_pattern_features(overview_file: str, dataset_dir: str) -> dict:
    df = pd.read_csv(overview_file, delimiter=';')
    folder_to_hash = build_folder_to_hash_mapping(dataset_dir)

    pattern_dict = {}

    for _, row in df.iterrows():
        folder_name = row['pattern']
        pattern_hash = folder_to_hash.get(folder_name)

        if pattern_hash is None:
            continue

        if pattern_hash not in pattern_dict:
            pattern_dict[pattern_hash] = {'folder_name': folder_name}

        target = row['target']
        final_features = [f.strip() for f in row['final_features'].split(',')]
        missing_child = []
        if pd.notna(row['missing_child_features']) and row['missing_child_features'].strip():
            missing_child = [f.strip() for f in row['missing_child_features'].split(',')]

        pattern_dict[pattern_hash][target] = {
            'final_features': final_features,
            'missing_child_features': missing_child
        }

    return pattern_dict


# Build folder_name to hash mapping from pattern_info.json files
def build_folder_to_hash_mapping(dataset_dir: str) -> dict:
    patterns_path = Path(dataset_dir) / 'patterns'
    mapping = {}

    if not patterns_path.exists():
        return mapping

    for folder in patterns_path.iterdir():
        if folder.is_dir():
            info_file = folder / 'pattern_info.json'
            if info_file.exists():
                with open(info_file, 'r') as f:
                    info = json.load(f)
                mapping[info['folder_name']] = folder.name

    return mapping


# Load operator features from overview CSV
def load_operator_features(operator_file: str) -> dict:
    df = pd.read_csv(operator_file, delimiter=';')
    operator_dict = {}

    for _, row in df.iterrows():
        operator = row['operator']

        if operator not in operator_dict:
            operator_dict[operator] = {}

        target = row['target']
        final_features = [f.strip() for f in row['final_features'].split(',')]

        operator_dict[operator][target] = {
            'final_features': final_features
        }

    return operator_dict


# Load pattern models from directory (stored by folder_name)
def load_pattern_models(model_dir: str, pattern_features: dict) -> dict:
    models = {'execution_time': {}, 'start_time': {}}
    model_path = Path(model_dir)

    for pattern_hash, data in pattern_features.items():
        folder_name = data['folder_name']

        for target in ['execution_time', 'start_time']:
            model_file = model_path / target / folder_name / 'model.pkl'
            if model_file.exists():
                models[target][pattern_hash] = joblib.load(model_file)

    return models


# Load operator models from directory
def load_operator_models(model_dir: str) -> dict:
    models = {'execution_time': {}, 'start_time': {}}
    model_path = Path(model_dir)

    for target in ['execution_time', 'start_time']:
        operators_dir = model_path / target / 'operators'
        if not operators_dir.exists():
            continue

        for operator_dir in operators_dir.iterdir():
            if operator_dir.is_dir():
                model_file = operator_dir / 'model.pkl'
                if model_file.exists():
                    models[target][operator_dir.name] = joblib.load(model_file)

    return models


# Create prediction result dictionary
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


# Export predictions to CSV
def export_predictions(predictions: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    df_predictions = pd.DataFrame(predictions)
    df_predictions.to_csv(output_path / 'predictions.csv', sep=';', index=False)
