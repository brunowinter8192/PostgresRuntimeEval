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

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import METHOD_COLORS, DPI, TAB20_RED


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
        'method': ['Plan-Level Methode', 'Optimizer Cost Model'],
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

    y_limit = 100
    ml_values = template_df['mre_ml_pct'].values
    opt_values = template_df['mre_optimizer_pct'].values
    ml_display = np.minimum(ml_values, y_limit)
    opt_display = np.minimum(opt_values, y_limit)

    bars_ml = ax.bar(x - width/2, ml_display, width,
                     label=f"Plan-Level Methode (Overall: {results['overall_ml']*100:.1f}%)",
                     color=METHOD_COLORS['Plan_Level_SVM'], alpha=0.8)
    bars_opt = ax.bar(x + width/2, opt_display, width,
                      label=f"Optimizer Cost Model (Overall: {results['overall_optimizer']*100:.1f}%)",
                      color=METHOD_COLORS['Optimizer'], alpha=0.8)

    for i, bar in enumerate(bars_ml):
        actual = ml_values[i]
        color = TAB20_RED if actual > y_limit else 'black'
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                f'{actual:.1f}%', ha='center', va='bottom', fontsize=7, color=color)

    for i, bar in enumerate(bars_opt):
        actual = opt_values[i]
        template = templates[i]
        color = TAB20_RED if actual > y_limit else 'black'
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
    plt.savefig(output_dir / 'A_01i_optimizer_baseline_plot.png', dpi=DPI)
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
