#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pickle
from pathlib import Path

import pandas as pd
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline

TARGET = 'runtime'

SVM_PARAMS = {
    'kernel': 'rbf',
    'nu': 0.5,
    'C': 5.0,
    'gamma': 'scale',
    'cache_size': 500
}

# ORCHESTRATOR

def train_workflow(dataset_dir: str, svm_dir: str, output_dir: str) -> None:
    dataset_path = Path(dataset_dir)
    svm_path = Path(svm_dir)
    output_path = Path(output_dir)

    for template_dir in sorted(svm_path.iterdir()):
        if not template_dir.is_dir():
            continue

        template_name = template_dir.name
        train_template(template_name, dataset_path, svm_path, output_path)


def train_template(template_name: str, dataset_path: Path, svm_path: Path, output_path: Path) -> None:
    training_file = dataset_path / template_name / 'training.csv'
    ffs_file = svm_path / template_name / 'ffs_summary.csv'

    if not training_file.exists() or not ffs_file.exists():
        return

    df_train = load_dataset(training_file)
    selected_features = load_selected_features(ffs_file)

    X_train = df_train[selected_features]
    y_train = df_train[TARGET]

    model = train_model(X_train, y_train)
    save_model(model, selected_features, output_path / template_name)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Load selected features from FFS summary
def load_selected_features(ffs_path: Path) -> list:
    df = pd.read_csv(ffs_path, delimiter=';')
    features_str = df.iloc[0]['selected_features']
    return [f.strip() for f in features_str.split(',')]


# Train SVM model with scaler
def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
    pipeline = Pipeline([
        ('scaler', MaxAbsScaler()),
        ('model', NuSVR(**SVM_PARAMS))
    ])
    pipeline.fit(X_train, y_train)
    return pipeline


# Save model and feature list
def save_model(model: Pipeline, features: list, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / 'model.pkl', 'wb') as f:
        pickle.dump({'model': model, 'features': features}, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_dir", help="Path to Dataset/ containing template folders")
    parser.add_argument("svm_dir", help="Path to SVM/ containing ffs_summary.csv per template")
    parser.add_argument("--output-dir", required=True, help="Output directory for models")

    args = parser.parse_args()

    train_workflow(args.dataset_dir, args.svm_dir, args.output_dir)
