#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import importlib
from datetime import datetime
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))  # Plan_Level_1
# From mapping_config.py: Metadata column names and target column
from mapping_config import PLAN_METADATA, PLAN_TARGET
# From ffs_config.py: Model registry
from ffs_config import MODEL_REGISTRY


# ORCHESTRATOR

# Train model pipeline and generate predictions on test set
def train_model_workflow(train_csv: Path, test_csv: Path, ffs_csv: Path, output_dir: Path, model_key: str, seed: int = 42) -> None:
    model_config = MODEL_REGISTRY[model_key]
    selected_features = load_selected_features(ffs_csv, seed)

    df_train = load_dataset(train_csv)
    df_test = load_dataset(test_csv)
    X_train, y_train = prepare_features(df_train, selected_features)
    X_test, y_test = prepare_features(df_test, selected_features)
    trained_model = train_model(X_train, y_train, model_config)
    save_model(trained_model, output_dir)
    y_pred = trained_model.predict(X_test)
    export_predictions(df_test, y_test, y_pred, output_dir)


# FUNCTIONS

# Load selected features from FFS CSV output
def load_selected_features(ffs_csv_path: Path, seed: int = 42) -> list:
    df = pd.read_csv(ffs_csv_path, sep=';')

    seed_row = df[df['seed'] == seed]

    if len(seed_row) == 0:
        raise ValueError(f"Seed {seed} not found in FFS results. Available seeds: {df['seed'].tolist()}")

    features_str = seed_row.iloc[0]['selected_features']
    features = [f.strip() for f in features_str.split(',')]

    return features


# Load dataset from CSV with semicolon delimiter
def load_dataset(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Prepare feature matrix and target vector
def prepare_features(df: pd.DataFrame, selected_features: list) -> tuple:
    X = df[selected_features]
    y = df[PLAN_TARGET]
    return X, y


# Train model with optional scaler pipeline
def train_model(X_train: pd.DataFrame, y_train: pd.Series, model_config: dict):
    model_module = importlib.import_module(model_config['module'])
    model_class = getattr(model_module, model_config['class_name'])
    model = model_class(**model_config['params'])

    if model_config['use_scaler']:
        scaler_module = importlib.import_module(model_config['scaler_module'])
        scaler_class = getattr(scaler_module, model_config['scaler_class'])
        estimator = Pipeline([
            ('scaler', scaler_class()),
            ('model', model)
        ])
    else:
        estimator = model

    estimator.fit(X_train, y_train)
    return estimator


# Save trained model to pickle file
def save_model(model, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    model_file = output_dir / f'02_model_{timestamp}.pkl'
    joblib.dump(model, model_file)


# Export predictions to CSV with semicolon delimiter
def export_predictions(df_test: pd.DataFrame, y_test: pd.Series, y_pred: np.ndarray, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    results_df = pd.DataFrame({
        PLAN_METADATA[0]: df_test[PLAN_METADATA[0]],
        'actual_ms': y_test,
        'predicted_ms': y_pred,
        'error_ms': y_test - y_pred,
        'abs_error_ms': np.abs(y_test - y_pred),
        'relative_error': np.abs((y_test - y_pred) / y_test)
    })

    predictions_file = output_dir / f'02_predictions_{timestamp}.csv'
    results_df.to_csv(predictions_file, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train model and generate predictions")
    parser.add_argument("train_csv", help="Training dataset CSV file")
    parser.add_argument("test_csv", help="Test dataset CSV file")
    parser.add_argument("--model", choices=['svm', 'random_forest', 'xgboost'], required=True, help="Model to use for training")
    parser.add_argument("--ffs-csv", default=None, help="FFS results CSV (default: Baseline_<model>/<output_folder>/01_multi_seed_summary.csv)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed to select features for (default: 42)")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: Baseline_<model>/<output_folder>)")

    args = parser.parse_args()

    train_path = Path(args.train_csv)
    test_path = Path(args.test_csv)

    model_output_folder = MODEL_REGISTRY[args.model]['output_folder']
    baseline_dir = Path(__file__).parent / f'Baseline_{MODEL_REGISTRY[args.model]["name"]}'

    if args.ffs_csv:
        ffs_csv_path = Path(args.ffs_csv)
    else:
        ffs_csv_path = baseline_dir / model_output_folder / '01_multi_seed_summary.csv'

    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = baseline_dir / model_output_folder

    train_model_workflow(train_path, test_path, ffs_csv_path, output_path, args.model, args.seed)
