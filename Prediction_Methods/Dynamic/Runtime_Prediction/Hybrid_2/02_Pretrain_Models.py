#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import json
import argparse
from pathlib import Path
from multiprocessing import Pool

import joblib
import pandas as pd
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

# From mapping_config.py: Configuration constants
from mapping_config import (
    SVM_PARAMS, TARGET_TYPES, TARGET_NAME_MAP,
    get_operator_features, csv_name_to_folder_name
)

ALL_TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']

SCRIPT_DIR = Path(__file__).resolve().parent
DATASET_BASE = SCRIPT_DIR.parent.parent / 'Dataset'
OUTPUT_BASE = SCRIPT_DIR / 'Model'

SPLIT_CONFIG = {
    'Training_Training': {
        'operator_data': DATASET_BASE / 'Dataset_Hybrid_2' / 'Training_Training',
        'operator_file': 'Training_Training.csv',
        'pattern_data': DATASET_BASE / 'Dataset_Hybrid_2' / 'Training_Training',
    },
    'Training': {
        'operator_data': DATASET_BASE / 'Dataset_Operator',
        'operator_file': 'training.csv',
        'pattern_data': DATASET_BASE / 'Dataset_Hybrid_1',
        'pattern_subdir': 'approach_3',
    }
}


# ORCHESTRATOR
def batch_pretrain(templates: list, split: str) -> None:
    config = SPLIT_CONFIG[split]
    output_dir = OUTPUT_BASE / split
    tasks = [(t, config, output_dir) for t in templates]
    with Pool(6) as pool:
        pool.map(process_template, tasks)


# FUNCTIONS

# Process single template
def process_template(task: tuple) -> None:
    template, config, output_dir = task
    print(f"{template}...")

    operator_dir = config['operator_data'] / template
    operator_file = operator_dir / config['operator_file']

    if not operator_file.exists():
        print(f"  Skipping: no {config['operator_file']}")
        return

    pattern_dir = config['pattern_data'] / template
    if 'pattern_subdir' in config:
        pattern_dir = pattern_dir / config['pattern_subdir']

    train_operators(template, operator_file, output_dir)
    train_patterns(template, pattern_dir, output_dir)


# Train all operator models for a template
def train_operators(template: str, training_file: Path, output_dir: Path) -> None:
    df = pd.read_csv(training_file, delimiter=';')

    operator_types = df['node_type'].unique()

    for op_type in operator_types:
        op_data = df[df['node_type'] == op_type]

        features = get_operator_features(op_type)
        available_features = [f for f in features if f in op_data.columns]

        if not available_features or len(op_data) < 10:
            continue

        X = op_data[available_features].fillna(0)

        for target_type in TARGET_TYPES:
            target_col = TARGET_NAME_MAP[target_type]
            y = op_data[target_col]

            if y.std() == 0:
                continue

            model = Pipeline([
                ('scaler', MaxAbsScaler()),
                ('model', NuSVR(**SVM_PARAMS))
            ])
            model.fit(X, y)

            op_name = csv_name_to_folder_name(op_type)
            model_dir = output_dir / template / 'Operator' / target_type / op_name
            model_dir.mkdir(parents=True, exist_ok=True)

            joblib.dump(model, model_dir / 'model.pkl')


# Train all pattern models for a template
def train_patterns(template: str, pattern_base_dir: Path, output_dir: Path) -> None:
    patterns_dir = pattern_base_dir / 'patterns'

    if not patterns_dir.exists():
        return

    for pattern_dir in patterns_dir.iterdir():
        if not pattern_dir.is_dir():
            continue

        pattern_hash = pattern_dir.name
        training_file = pattern_dir / 'training_cleaned.csv'

        if not training_file.exists():
            continue

        df = pd.read_csv(training_file, delimiter=';')

        if len(df) < 10:
            continue

        feature_cols = get_pattern_features(df)

        if not feature_cols:
            continue

        X = df[feature_cols].fillna(0)

        models_trained = {}
        features_used = {}

        for target_type in TARGET_TYPES:
            target_col = TARGET_NAME_MAP[target_type]

            if target_col not in df.columns:
                continue

            y = df[target_col]

            if y.std() == 0:
                continue

            model = Pipeline([
                ('scaler', MaxAbsScaler()),
                ('model', NuSVR(**SVM_PARAMS))
            ])
            model.fit(X, y)

            models_trained[target_type] = model
            features_used[target_type] = feature_cols

        if len(models_trained) != 2:
            continue

        model_dir = output_dir / template / 'Pattern' / pattern_hash
        model_dir.mkdir(parents=True, exist_ok=True)

        joblib.dump(models_trained['execution_time'], model_dir / 'model_execution_time.pkl')
        joblib.dump(models_trained['start_time'], model_dir / 'model_start_time.pkl')

        with open(model_dir / 'features.json', 'w') as f:
            json.dump({
                'features_exec': features_used['execution_time'],
                'features_start': features_used['start_time']
            }, f)


# Get feature columns for pattern training
def get_pattern_features(df: pd.DataFrame) -> list:
    exclude_cols = {'query_file', 'actual_startup_time', 'actual_total_time'}
    feature_cols = []

    for col in df.columns:
        if col in exclude_cols:
            continue
        if any(meta in col for meta in ['node_id', 'node_type', 'depth', 'parent_relationship', 'subplan_name']):
            continue
        feature_cols.append(col)

    return feature_cols


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", choices=['Training_Training', 'Training'], required=True,
                        help="Training_Training (80%%) or Training (100%%)")
    parser.add_argument("--templates", nargs="+", default=ALL_TEMPLATES, help="Templates to process")
    args = parser.parse_args()
    batch_pretrain(args.templates, args.split)
