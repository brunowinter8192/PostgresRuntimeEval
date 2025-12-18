#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Target and metadata columns
from mapping_config import PLAN_TARGET, PLAN_METADATA


# ORCHESTRATOR

# Train linear regression on optimizer costs and evaluate
def optimizer_baseline_workflow(train_csv: Path, test_csv: Path, output_dir: Path) -> None:
    train_df, test_df = load_datasets(train_csv, test_csv)
    model = train_linear_regression(train_df)
    results_df, overall_mre = predict_and_evaluate(model, test_df)
    fig = create_mre_plot(results_df)
    export_results(results_df, overall_mre, len(train_df), len(test_df), fig, output_dir)


# FUNCTIONS

# Load train and test datasets
def load_datasets(train_csv: Path, test_csv: Path) -> tuple:
    train_df = pd.read_csv(train_csv, delimiter=';')
    test_df = pd.read_csv(test_csv, delimiter=';')
    return train_df, test_df


# Train linear regression on p_tot_cost
def train_linear_regression(train_df: pd.DataFrame) -> LinearRegression:
    X_train = train_df[['p_tot_cost']]
    y_train = train_df[PLAN_TARGET]
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


# Generate predictions and calculate MRE
def predict_and_evaluate(model: LinearRegression, test_df: pd.DataFrame) -> tuple:
    X_test = test_df[['p_tot_cost']]
    y_test = test_df[PLAN_TARGET]

    predictions = model.predict(X_test)
    predictions = np.maximum(predictions, 0)

    relative_errors = np.abs(y_test - predictions) / y_test
    overall_mre = relative_errors.mean()

    results_df = pd.DataFrame({
        PLAN_METADATA[0]: test_df[PLAN_METADATA[0]],
        PLAN_METADATA[1]: test_df[PLAN_METADATA[1]],
        'actual_ms': y_test,
        'predicted_ms': predictions,
        'relative_error': relative_errors
    })

    return results_df, overall_mre


# Create MRE bar plot by template
def create_mre_plot(results_df: pd.DataFrame):
    template_mre = results_df.groupby(PLAN_METADATA[1])['relative_error'].mean().reset_index()
    template_mre['sort_key'] = template_mre[PLAN_METADATA[1]].str.extract(r'(\d+)').astype(int)
    template_mre = template_mre.sort_values('sort_key').drop(columns=['sort_key'])

    fig, ax = plt.subplots(figsize=(16, 8))

    templates = template_mre[PLAN_METADATA[1]].tolist()
    mre_values = template_mre['relative_error'].values * 100

    x = np.arange(len(templates))
    bars = ax.bar(x, mre_values, width=0.5, color='indianred', alpha=0.8,
                  edgecolor='black', linewidth=0.8)

    ax.set_xlabel('Template', fontsize=13, fontweight='bold')
    ax.set_ylabel('Mean Relative Error (%)', fontsize=13, fontweight='bold')
    ax.set_title('Optimizer Cost Baseline - Runtime Prediction Error by Template',
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(templates, rotation=0, fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    return fig


# Export predictions, summary, and plot
def export_results(results_df: pd.DataFrame, overall_mre: float,
                   n_train: int, n_test: int, fig, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    predictions_file = output_dir / 'A_01i_optimizer_predictions.csv'
    results_df.to_csv(predictions_file, sep=';', index=False)

    summary_df = pd.DataFrame({
        'metric': ['overall_mre', 'train_samples', 'test_samples', 'feature', 'model'],
        'value': [f'{overall_mre:.4f}', str(n_train), str(n_test), 'p_tot_cost', 'LinearRegression']
    })
    summary_file = output_dir / 'A_01i_optimizer_summary.csv'
    summary_df.to_csv(summary_file, sep=';', index=False)

    plot_file = output_dir / 'A_01i_optimizer_mre_plot.png'
    fig.savefig(plot_file, dpi=300, bbox_inches='tight')
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimizer cost baseline for runtime prediction")
    parser.add_argument("train_csv", help="Training dataset CSV")
    parser.add_argument("test_csv", help="Test dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")

    args = parser.parse_args()

    optimizer_baseline_workflow(
        Path(args.train_csv),
        Path(args.test_csv),
        Path(args.output_dir)
    )
