#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def plan_prediction_workflow(dataset_dir: Path, output_dir: Path) -> None:
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


# Train linear regression on p_tot_cost
def train_linear_regression(train_df: pd.DataFrame) -> LinearRegression:
    X = train_df[['p_tot_cost']]
    y = train_df['runtime']
    model = LinearRegression()
    model.fit(X, y)
    return model


# Predict on test data
def predict(model: LinearRegression, test_df: pd.DataFrame) -> pd.DataFrame:
    X = test_df[['p_tot_cost']]
    predictions = model.predict(X)
    predictions = np.maximum(predictions, 0)

    result = pd.DataFrame({
        'query_file': test_df['query_file'],
        'template': test_df['template'],
        'actual_runtime': test_df['runtime'],
        'predicted_runtime': predictions,
        'p_tot_cost': test_df['p_tot_cost']
    })
    return result


# Export predictions to CSV
def export_predictions(predictions: pd.DataFrame, output_path: Path) -> None:
    output_path.mkdir(parents=True, exist_ok=True)
    predictions.to_csv(output_path / 'predictions.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-dir", required=True, help="Path to Dataset_Plan")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    plan_prediction_workflow(Path(args.dataset_dir), Path(args.output_dir))
