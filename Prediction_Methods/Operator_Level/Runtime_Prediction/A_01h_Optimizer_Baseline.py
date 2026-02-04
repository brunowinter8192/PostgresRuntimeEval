#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LinearRegression

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from plot_config import METHOD_COLORS, DPI, DEEP_RED


# ORCHESTRATOR

def optimizer_baseline_workflow(train_csv, test_csv, predictions_csv, output_dir):
    train_df = load_csv(train_csv)
    test_df = load_csv(test_csv)
    pred_df = load_csv(predictions_csv)
    model = train_linear_regression(train_df)
    results = evaluate_comparison(model, test_df, pred_df)
    export_results(results, output_dir)
    create_comparison_plot(results, output_dir)


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


# Evaluate both optimizer baseline and ML predictions
def evaluate_comparison(model, test_df, pred_df):
    root_test = test_df[test_df['depth'] == 0].copy()
    root_test['template'] = root_test['query_file'].apply(lambda x: x.split('_')[0])

    X_test = root_test[['total_cost']]
    optimizer_pred = model.predict(X_test)
    optimizer_pred = np.maximum(optimizer_pred, 0)
    root_test['optimizer_pred'] = optimizer_pred

    pred_root = pred_df[pred_df['depth'] == 0][['query_file', 'predicted_total_time']]
    root_test = root_test.merge(pred_root, on='query_file', how='left')

    root_test['mre_optimizer'] = np.abs(root_test['optimizer_pred'] - root_test['actual_total_time']) / root_test['actual_total_time']
    root_test['mre_ml'] = np.abs(root_test['predicted_total_time'] - root_test['actual_total_time']) / root_test['actual_total_time']

    overall_optimizer = root_test['mre_optimizer'].mean()
    overall_ml = root_test['mre_ml'].mean()

    template_comparison = root_test.groupby('template').agg({
        'mre_optimizer': 'mean',
        'mre_ml': 'mean'
    }).round(4)
    template_comparison['mre_optimizer_pct'] = template_comparison['mre_optimizer'] * 100
    template_comparison['mre_ml_pct'] = template_comparison['mre_ml'] * 100
    template_comparison = template_comparison.reindex(sorted(template_comparison.index, key=lambda x: int(x[1:])))

    return {
        'overall_optimizer': overall_optimizer,
        'overall_ml': overall_ml,
        'template_comparison': template_comparison
    }


# Export comparison results to CSV
def export_results(results, output_dir):
    output_path = Path(output_dir) / 'Evaluation'
    output_path.mkdir(parents=True, exist_ok=True)

    overall_df = pd.DataFrame({
        'method': ['Operator-Level Methode', 'Optimizer Cost Model'],
        'mre': [results['overall_ml'], results['overall_optimizer']],
        'mre_pct': [results['overall_ml'] * 100, results['overall_optimizer'] * 100]
    })
    overall_df.to_csv(output_path / 'A_01h_optimizer_baseline_overall.csv', sep=';', index=False)

    results['template_comparison'].to_csv(output_path / 'A_01h_optimizer_baseline_template.csv', sep=';')


# Create bar plot comparing ML vs Optimizer
def create_comparison_plot(results, output_dir):
    output_path = Path(output_dir) / 'Evaluation'
    output_path.mkdir(parents=True, exist_ok=True)

    template_df = results['template_comparison']
    templates = template_df.index.tolist()
    x = np.arange(len(templates))
    width = 0.35
    y_limit = 100

    fig, ax = plt.subplots(figsize=(14, 7))

    ml_values = template_df['mre_ml_pct'].values
    opt_values = template_df['mre_optimizer_pct'].values
    ml_display = np.minimum(ml_values, y_limit)
    opt_display = np.minimum(opt_values, y_limit)

    bars_ml = ax.bar(x - width/2, ml_display, width,
                     label=f"Operator-Level Methode (Overall: {results['overall_ml']*100:.1f}%)",
                     color=METHOD_COLORS['Operator_Level'], alpha=0.8)
    bars_opt = ax.bar(x + width/2, opt_display, width,
                      label=f"Optimizer Cost Model (Overall: {results['overall_optimizer']*100:.1f}%)",
                      color=METHOD_COLORS['Optimizer'], alpha=0.8)

    for i, bar in enumerate(bars_ml):
        actual = ml_values[i]
        color = DEEP_RED if actual > y_limit else 'black'
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                f'{actual:.1f}%', ha='center', va='bottom', fontsize=7, color=color)

    for i, bar in enumerate(bars_opt):
        actual = opt_values[i]
        template = templates[i]
        color = DEEP_RED if actual > y_limit else 'black'
        if template in ['Q16', 'Q22'] and bar.get_height() > 90:
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() - 5,
                    f'{actual:.1f}%', ha='center', va='top', fontsize=7, color=color)
        else:
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                    f'{actual:.1f}%', ha='center', va='bottom', fontsize=7, color=color)

    ax.set_xlabel('Template', fontsize=12)
    ax.set_ylabel('Mean Relative Error (%)', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=10)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim(0, y_limit * 1.1)

    plt.tight_layout()
    plt.savefig(output_path / 'A_01h_optimizer_baseline_plot.png', dpi=DPI)
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("train_csv", help="Training dataset CSV")
    parser.add_argument("test_csv", help="Test dataset CSV")
    parser.add_argument("predictions_csv", help="ML predictions CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    optimizer_baseline_workflow(args.train_csv, args.test_csv, args.predictions_csv, args.output_dir)
