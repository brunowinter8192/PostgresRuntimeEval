#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
# From plot_config.py: Central plot configuration
from plot_config import PRIMARY_COLOR, ACCENT_COLOR, DPI, PLOTS_PER_PAGE, SUBPLOT_ROWS, SUBPLOT_COLS


# ORCHESTRATOR

# Create and save runtime histograms for each template
def create_histograms_workflow(dataset_csv: Path, predictions_csv: Path, output_dir: Path) -> None:
    df = load_dataset(dataset_csv)
    predictions = load_predictions(predictions_csv)
    figures = create_histogram_pages(df, predictions)
    save_plots(figures, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=';')


# Load predictions and extract template from query_file
def load_predictions(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, delimiter=';')
    df['template'] = df['query_file'].str.extract(r'^(Q\d+)_')[0]
    return df.groupby('template')['predicted_ms'].mean().to_dict()


# Create multiple pages of histograms (2x2 grid per page)
def create_histogram_pages(df: pd.DataFrame, predictions: dict) -> list:
    templates = sorted(df['template'].unique())
    figures = []

    for page_idx in range(0, len(templates), PLOTS_PER_PAGE):
        page_templates = templates[page_idx:page_idx + PLOTS_PER_PAGE]
        fig = create_single_page(df, predictions, page_templates)
        figures.append(fig)

    return figures


# Create single page with up to 4 histograms
def create_single_page(df: pd.DataFrame, predictions: dict, templates: list):
    fig, axes = plt.subplots(SUBPLOT_ROWS, SUBPLOT_COLS, figsize=(12, 10))
    axes = axes.flatten()

    for i, template in enumerate(templates):
        ax = axes[i]
        template_data = df[df['template'] == template]['runtime']

        ax.hist(template_data, bins=15, color=PRIMARY_COLOR, alpha=0.8, edgecolor='black')
        ax.set_title(f'{template}', fontsize=11, loc='left')
        ax.set_xlabel('Runtime (ms)', fontsize=10)
        ax.set_ylabel('Count', fontsize=10)

        mean_val = template_data.mean()
        std_val = template_data.std()
        cv = (std_val / mean_val) * 100

        ax.text(0.95, 0.95, f'CV: {cv:.1f}%', transform=ax.transAxes,
                ha='right', va='top', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        template_key = f'Q{template}' if not str(template).startswith('Q') else str(template)
        if template_key in predictions:
            ax.axvline(predictions[template_key], color=ACCENT_COLOR, linestyle='--', linewidth=2)

        ax.grid(axis='y', alpha=0.3, linestyle='--')

    for j in range(len(templates), len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()

    return fig


# Save multiple plots to files
def save_plots(figures: list, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for i, fig in enumerate(figures, start=1):
        plot_file = output_dir / f'A_01k_runtime_histograms_{i}.png'
        fig.savefig(plot_file, dpi=DPI, bbox_inches='tight')
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
