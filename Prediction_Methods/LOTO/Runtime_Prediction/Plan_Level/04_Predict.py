#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pickle
from pathlib import Path

import numpy as np
import pandas as pd

TARGET = 'runtime'

# ORCHESTRATOR

def predict_workflow(dataset_dir: str, model_dir: str, output_dir: str) -> None:
    dataset_path = Path(dataset_dir)
    model_path = Path(model_dir)
    output_path = Path(output_dir)

    for template_dir in sorted(model_path.iterdir()):
        if not template_dir.is_dir():
            continue

        template_name = template_dir.name
        predict_template(template_name, dataset_path, model_path, output_path)


def predict_template(template_name: str, dataset_path: Path, model_path: Path, output_path: Path) -> None:
    test_file = dataset_path / template_name / 'test.csv'
    model_file = model_path / template_name / 'model.pkl'

    if not test_file.exists() or not model_file.exists():
        return

    df_test = load_dataset(test_file)
    model_data = load_model(model_file)

    model = model_data['model']
    features = model_data['features']

    X_test = df_test[features]
    y_test = df_test[TARGET]

    y_pred = model.predict(X_test)
    export_predictions(df_test, y_test, y_pred, output_path / template_name)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Load model and features from pickle
def load_model(model_path: Path) -> dict:
    with open(model_path, 'rb') as f:
        return pickle.load(f)


# Export predictions to CSV
def export_predictions(df_test: pd.DataFrame, y_test: pd.Series, y_pred: np.ndarray, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    results_df = pd.DataFrame({
        'query_file': df_test['query_file'],
        'actual_ms': y_test,
        'predicted_ms': y_pred,
        'error_ms': y_test - y_pred,
        'abs_error_ms': np.abs(y_test - y_pred),
        'relative_error': np.abs((y_test - y_pred) / y_test)
    })

    results_df.to_csv(output_dir / 'predictions.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_dir", help="Path to Dataset/ containing template folders")
    parser.add_argument("model_dir", help="Path to Model/ containing trained models")
    parser.add_argument("--output-dir", required=True, help="Output directory for predictions")

    args = parser.parse_args()

    predict_workflow(args.dataset_dir, args.model_dir, args.output_dir)
