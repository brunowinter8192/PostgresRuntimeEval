#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def operator_prediction_workflow(dataset_dir: Path, output_dir: Path) -> None:
    for template in TEMPLATES:
        train_df = load_csv(dataset_dir / template / 'training.csv')
        test_df = load_csv(dataset_dir / template / 'test.csv')
        model = train_linear_regression(train_df)
        predictions = predict(model, test_df)
        export_predictions(predictions, output_dir / template)


# FUNCTIONS

# Load CSV file
def load_csv(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Train linear regression on root operator total_cost
def train_linear_regression(train_df: pd.DataFrame) -> LinearRegression:
    root_train = train_df[train_df['depth'] == 0].copy()
    X = root_train[['total_cost']]
    y = root_train['actual_total_time']
    model = LinearRegression()
    model.fit(X, y)
    return model


# Predict on test data (root operators only)
def predict(model: LinearRegression, test_df: pd.DataFrame) -> pd.DataFrame:
    root_test = test_df[test_df['depth'] == 0].copy()
    X = root_test[['total_cost']]
    predictions = model.predict(X)
    predictions = np.maximum(predictions, 0)

    root_test['template'] = root_test['query_file'].apply(lambda x: x.split('_')[0])

    result = pd.DataFrame({
        'query_file': root_test['query_file'],
        'template': root_test['template'],
        'actual_runtime': root_test['actual_total_time'],
        'predicted_runtime': predictions,
        'total_cost': root_test['total_cost']
    })
    return result


# Export predictions to CSV
def export_predictions(predictions: pd.DataFrame, output_path: Path) -> None:
    output_path.mkdir(parents=True, exist_ok=True)
    predictions.to_csv(output_path / 'predictions.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-dir", required=True, help="Path to Dataset_Operator")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    operator_prediction_workflow(Path(args.dataset_dir), Path(args.output_dir))
