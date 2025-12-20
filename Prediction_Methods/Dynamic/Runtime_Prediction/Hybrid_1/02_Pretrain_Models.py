#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import argparse
import pickle
from pathlib import Path
from multiprocessing import Pool

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
ALL_APPROACHES = ['approach_3']

SCRIPT_DIR = Path(__file__).resolve().parent
DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Hybrid_1'
OPERATOR_DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Operator'
OUTPUT_DIR = SCRIPT_DIR


# ORCHESTRATOR
def batch_pretrain(templates: list, approaches: list) -> None:
    tasks = [(template, approach) for template in templates for approach in approaches]
    with Pool(6) as pool:
        pool.map(process_task, tasks)


# FUNCTIONS

# Process single template-approach combination
def process_task(task: tuple) -> None:
    template, approach = task
    print(f"{template}/{approach}...")

    template_output = OUTPUT_DIR / template / approach
    template_output.mkdir(exist_ok=True, parents=True)

    pattern_dataset = DATASET_DIR / template / approach
    used_patterns_file = pattern_dataset / 'used_patterns.csv'

    if not used_patterns_file.exists():
        print(f"  Skipping: no used_patterns.csv")
        return

    train_operators(template, template_output)
    train_patterns(template, approach, pattern_dataset, template_output)


# Train all operator models for a template
def train_operators(template: str, output_dir: Path) -> None:
    training_file = OPERATOR_DATASET_DIR / template / 'training.csv'
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
            model_dir = output_dir / 'Model' / 'Operators' / target_type / op_name
            model_dir.mkdir(parents=True, exist_ok=True)

            with open(model_dir / 'model.pkl', 'wb') as f:
                pickle.dump({'model': model, 'features': available_features}, f)


# Train pattern models for used_patterns
def train_patterns(template: str, approach: str, pattern_dataset: Path, output_dir: Path) -> None:
    used_patterns_file = pattern_dataset / 'used_patterns.csv'
    used_patterns_df = pd.read_csv(used_patterns_file, delimiter=';')
    if used_patterns_df.empty:
        return
    used_hashes = set(used_patterns_df['pattern_hash'].tolist())

    patterns_dir = pattern_dataset / 'patterns'

    for pattern_hash in used_hashes:
        pattern_dir = patterns_dir / pattern_hash
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

            model_dir = output_dir / 'Model' / target_type / pattern_hash
            model_dir.mkdir(parents=True, exist_ok=True)

            with open(model_dir / 'model.pkl', 'wb') as f:
                pickle.dump({'model': model, 'features': feature_cols}, f)


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
    parser.add_argument("--templates", nargs="+", default=ALL_TEMPLATES, help="Templates to process")
    parser.add_argument("--approaches", nargs="+", default=ALL_APPROACHES, help="Approaches to process")
    args = parser.parse_args()
    batch_pretrain(args.templates, args.approaches)
