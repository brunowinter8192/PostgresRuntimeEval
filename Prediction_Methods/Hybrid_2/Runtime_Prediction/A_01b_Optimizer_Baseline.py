#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression


# ORCHESTRATOR

def optimizer_baseline_workflow(train_csv, test_csv, output_dir):
    train_df = load_csv(train_csv)
    test_df = load_csv(test_csv)
    model = train_linear_regression(train_df)
    results = evaluate_optimizer(model, test_df)
    export_results(results, output_dir)


# FUNCTIONS

# Load CSV file
def load_csv(csv_path):
    return pd.read_csv(csv_path, delimiter=';')


# Train linear regression on root operator total_cost
def train_linear_regression(train_df):
    root_train = train_df[train_df['depth'] == 0].copy()
    X = root_train[['total_cost']]
    y = root_train['actual_total_time']
    model = LinearRegression()
    model.fit(X, y)
    return model


# Evaluate optimizer on test set
def evaluate_optimizer(model, test_df):
    root_test = test_df[test_df['depth'] == 0].copy()
    root_test['template'] = root_test['query_file'].apply(lambda x: x.split('_')[0])

    X_test = root_test[['total_cost']]
    optimizer_pred = model.predict(X_test)
    optimizer_pred = np.maximum(optimizer_pred, 0)
    root_test['predicted_total_time'] = optimizer_pred

    root_test['mre'] = np.abs(root_test['predicted_total_time'] - root_test['actual_total_time']) / root_test['actual_total_time']

    overall_mre = root_test['mre'].mean()

    template_stats = root_test.groupby('template').agg({
        'mre': ['mean', 'std', 'count'],
        'predicted_total_time': 'mean',
        'actual_total_time': 'mean'
    }).round(4)

    template_stats.columns = ['mean_mre', 'std_mre', 'query_count', 'mean_predicted_ms', 'mean_actual_ms']
    template_stats['mean_mre_pct'] = template_stats['mean_mre'] * 100
    template_stats = template_stats[['mean_mre_pct', 'mean_mre', 'std_mre', 'query_count', 'mean_predicted_ms', 'mean_actual_ms']]
    template_stats = template_stats.reindex(
        sorted(template_stats.index, key=lambda x: int(x[1:]))
    )

    return {
        'overall_mre': overall_mre,
        'template_stats': template_stats
    }


# Export results to CSV
def export_results(results, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    overall_df = pd.DataFrame({
        'metric': ['mean_mre'],
        'value': [results['overall_mre']],
        'percentage': [results['overall_mre'] * 100]
    })
    overall_df.to_csv(output_path / 'A_01b_optimizer_overall_mre.csv', sep=';', index=False)

    results['template_stats'].to_csv(output_path / 'A_01b_optimizer_template_mre.csv', sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("train_csv", help="Training dataset CSV")
    parser.add_argument("test_csv", help="Test dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    optimizer_baseline_workflow(args.train_csv, args.test_csv, args.output_dir)
