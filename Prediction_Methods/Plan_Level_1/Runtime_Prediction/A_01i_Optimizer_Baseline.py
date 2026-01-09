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

# Train linear regression on optimizer costs and compare with ML predictions
def optimizer_baseline_workflow(train_csv: Path, test_csv: Path, predictions_csv: Path, output_dir: Path) -> None:
    train_df = load_csv(train_csv)
    test_df = load_csv(test_csv)
    pred_df = load_csv(predictions_csv)
    model = train_linear_regression(train_df)
    results = evaluate_comparison(model, test_df, pred_df)
    export_results(results, output_dir)
    create_comparison_plot(results, output_dir)


# FUNCTIONS

# Load CSV file
def load_csv(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Train linear regression on p_tot_cost
def train_linear_regression(train_df: pd.DataFrame) -> LinearRegression:
    X_train = train_df[['p_tot_cost']]
    y_train = train_df[PLAN_TARGET]
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


# Evaluate both optimizer baseline and ML predictions
def evaluate_comparison(model: LinearRegression, test_df: pd.DataFrame, pred_df: pd.DataFrame) -> dict:
    test_df = test_df.copy()
    test_df['template'] = test_df[PLAN_METADATA[1]].apply(lambda x: x.replace('.sql', ''))

    X_test = test_df[['p_tot_cost']]
    optimizer_pred = model.predict(X_test)
    optimizer_pred = np.maximum(optimizer_pred, 0)
    test_df['optimizer_pred'] = optimizer_pred

    pred_df = pred_df.copy()
    pred_df['query_file_clean'] = pred_df['query_file'].str.replace('.sql', '', regex=False)
    test_df['query_file_clean'] = test_df[PLAN_METADATA[0]].str.replace('.sql', '', regex=False)

    test_df = test_df.merge(
        pred_df[['query_file_clean', 'predicted_ms']],
        on='query_file_clean',
        how='left'
    )

    test_df['mre_optimizer'] = np.abs(test_df['optimizer_pred'] - test_df[PLAN_TARGET]) / test_df[PLAN_TARGET]
    test_df['mre_ml'] = np.abs(test_df['predicted_ms'] - test_df[PLAN_TARGET]) / test_df[PLAN_TARGET]

    overall_optimizer = test_df['mre_optimizer'].mean()
    overall_ml = test_df['mre_ml'].mean()

    template_comparison = test_df.groupby('template').agg({
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
def export_results(results: dict, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    overall_df = pd.DataFrame({
        'method': ['ML (SVM)', 'Optimizer Cost (LinReg)'],
        'mre': [results['overall_ml'], results['overall_optimizer']],
        'mre_pct': [results['overall_ml'] * 100, results['overall_optimizer'] * 100]
    })
    overall_df.to_csv(output_dir / 'A_01i_optimizer_baseline_overall.csv', sep=';', index=False)

    results['template_comparison'].to_csv(output_dir / 'A_01i_optimizer_baseline_template.csv', sep=';')


# Create bar plot comparing ML vs Optimizer
def create_comparison_plot(results: dict, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    template_df = results['template_comparison']
    templates = template_df.index.tolist()
    x = np.arange(len(templates))
    width = 0.35

    fig, ax = plt.subplots(figsize=(14, 7))

    bars_ml = ax.bar(x - width/2, template_df['mre_ml_pct'], width,
                     label=f"ML (Overall: {results['overall_ml']*100:.1f}%)",
                     color='steelblue', alpha=0.8)
    bars_opt = ax.bar(x + width/2, template_df['mre_optimizer_pct'], width,
                      label=f"Optimizer LinReg (Overall: {results['overall_optimizer']*100:.1f}%)",
                      color='coral', alpha=0.8)

    ax.bar_label(bars_ml, fmt='%.1f%%', padding=3, fontsize=8, rotation=0)
    ax.bar_label(bars_opt, fmt='%.1f%%', padding=3, fontsize=8, rotation=0)

    ax.set_xlabel('Template', fontsize=12)
    ax.set_ylabel('Mean Relative Error (%)', fontsize=12)
    ax.set_title('ML Prediction vs. Optimizer Cost Baseline (Plan-Level)', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(templates, fontsize=10)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    y_max = max(template_df['mre_ml_pct'].max(), template_df['mre_optimizer_pct'].max())
    ax.set_ylim(0, y_max * 1.35)

    plt.tight_layout()
    plt.savefig(output_dir / 'A_01i_optimizer_baseline_plot.png', dpi=150)
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimizer cost baseline vs ML comparison")
    parser.add_argument("train_csv", help="Training dataset CSV")
    parser.add_argument("test_csv", help="Test dataset CSV")
    parser.add_argument("predictions_csv", help="ML predictions CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")

    args = parser.parse_args()

    optimizer_baseline_workflow(
        Path(args.train_csv),
        Path(args.test_csv),
        Path(args.predictions_csv),
        Path(args.output_dir)
    )
