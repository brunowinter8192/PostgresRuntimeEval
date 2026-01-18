#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# ORCHESTRATOR

# Create and save runtime histograms for each template
def create_histograms_workflow(dataset_csv: Path, predictions_csv: Path, output_dir: Path) -> None:
    df = load_dataset(dataset_csv)
    pred_df = load_predictions(predictions_csv)
    fig = create_histogram_grid(df, pred_df)
    save_plot(fig, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Load predictions and extract template from query_file
def load_predictions(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    df['template'] = df['query_file'].str.extract(r'^(Q\d+)_')[0]
    return df.groupby('template')['predicted_ms'].mean().to_dict()


# Create grid of histograms showing runtime distribution per template
def create_histogram_grid(df: pd.DataFrame, predictions: dict):
    templates = sorted(df['template'].unique())
    n_templates = len(templates)

    n_cols = 5
    n_rows = (n_templates + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 4 * n_rows))
    axes = axes.flatten()

    for i, template in enumerate(templates):
        ax = axes[i]
        template_data = df[df['template'] == template]['runtime']

        ax.hist(template_data, bins=15, color='steelblue', alpha=0.8, edgecolor='black')
        ax.text(0.05, 0.95, f'{template}', transform=ax.transAxes,
                ha='left', va='top', fontsize=11, fontweight='bold')
        ax.set_xlabel('Runtime (ms)', fontsize=10)
        ax.set_ylabel('Count', fontsize=10)

        mean_val = template_data.mean()
        std_val = template_data.std()
        cv = (std_val / mean_val) * 100

        ax.text(0.95, 0.95, f'CV: {cv:.1f}%', transform=ax.transAxes,
                ha='right', va='top', fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        template_key = f'Q{template}' if not str(template).startswith('Q') else str(template)
        if template_key in predictions:
            ax.axvline(predictions[template_key], color='red', linestyle='--', linewidth=2)

        ax.grid(axis='y', alpha=0.3, linestyle='--')

    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()

    return fig


# Save plot to file
def save_plot(fig, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_file = output_dir / 'A_01k_runtime_histograms.png'
    fig.savefig(plot_file, dpi=300, bbox_inches='tight')
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create runtime histograms per template")
    parser.add_argument("dataset_csv", help="Complete dataset CSV file")
    parser.add_argument("--predictions-csv", required=True, help="Predictions CSV file")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: script_dir/Baseline_SVM/Evaluation)")

    args = parser.parse_args()

    dataset_path = Path(args.dataset_csv)
    predictions_path = Path(args.predictions_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'Baseline_SVM' / 'Evaluation'

    create_histograms_workflow(dataset_path, predictions_path, output_path)
