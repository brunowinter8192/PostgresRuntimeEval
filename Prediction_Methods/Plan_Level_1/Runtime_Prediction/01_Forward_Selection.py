#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import importlib
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import make_scorer
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))  # Plan_Level_1
# From mapping_config.py: Metadata columns, target column, and template column
from mapping_config import METADATA_COLUMNS, PLAN_TARGET, PLAN_METADATA
# From ffs_config.py: Forward feature selection parameters and model registry
from ffs_config import FFS_CONFIG, MODEL_REGISTRY


# ORCHESTRATOR

# Perform multi-seed forward feature selection with specified model
def forward_selection_workflow(input_csv: Path, output_dir: Path, model_key: str) -> None:
    model_config = MODEL_REGISTRY[model_key]
    df = load_dataset(input_csv)
    feature_cols = get_feature_columns(df)
    X = df[feature_cols]
    y = df[PLAN_TARGET]
    template_ids = extract_template_ids(df)

    all_seed_results, feature_counter = run_multi_seed_selection(X, y, feature_cols, template_ids, model_config)
    export_results(all_seed_results, feature_counter, output_dir)


# FUNCTIONS

# Load dataset from CSV with semicolon delimiter
def load_dataset(input_csv: Path) -> pd.DataFrame:
    return pd.read_csv(input_csv, delimiter=';')


# Get feature columns excluding metadata
def get_feature_columns(df: pd.DataFrame) -> list:
    return [col for col in df.columns if col not in METADATA_COLUMNS]


# Extract template IDs from template column
def extract_template_ids(df: pd.DataFrame) -> np.ndarray:
    template_column = PLAN_METADATA[1]
    return df[template_column].apply(extract_template_id).values


# Extract numeric template ID from template string
def extract_template_id(template_str) -> int:
    match = re.search(r'q(\d+)', str(template_str).lower())
    if match:
        return int(match.group(1))
    return 0


# Run forward selection across multiple seeds
def run_multi_seed_selection(X: pd.DataFrame, y: pd.Series, feature_cols: list, template_ids: np.ndarray, model_config: dict) -> tuple:
    all_seed_results = []
    feature_counter = {}

    for seed in FFS_CONFIG['seeds']:
        cv = StratifiedKFold(n_splits=FFS_CONFIG['n_splits'], shuffle=True, random_state=seed)
        selected_features, results_df = forward_selection(X, y, feature_cols, template_ids, cv, model_config)

        final_mre = results_df.iloc[-1]['mre']
        n_features = len(selected_features)

        seed_result = {
            'seed': seed,
            'n_features': n_features,
            'final_mre': final_mre,
            'selected_features': ', '.join(selected_features)
        }
        all_seed_results.append(seed_result)

        for feature in selected_features:
            feature_counter[feature] = feature_counter.get(feature, 0) + 1

    return all_seed_results, feature_counter


# Forward selection algorithm with minimum features constraint
def forward_selection(X: pd.DataFrame, y: pd.Series, feature_cols: list, template_ids: np.ndarray, cv, model_config: dict) -> tuple:
    selected = []
    remaining = list(feature_cols)
    results = []
    best_score = float('inf')
    iteration = 0

    while remaining:
        iteration += 1
        scores = {}

        for feature in remaining:
            test_features = selected + [feature]
            score = evaluate_features(X, y, test_features, template_ids, cv, model_config)
            scores[feature] = score

        best_feature = min(scores, key=scores.get)
        best_new_score = scores[best_feature]

        if iteration <= FFS_CONFIG['min_features']:
            should_add = True
        else:
            improvement = (best_score - best_new_score) / best_score
            should_add = improvement >= 0

        if should_add:
            selected.append(best_feature)
            remaining.remove(best_feature)
            best_score = best_new_score

            results.append({
                'iteration': iteration,
                'feature_added': best_feature,
                'mre': best_score,
                'n_features': len(selected),
                'features': ', '.join(selected)
            })
        else:
            break

    return selected, pd.DataFrame(results)


# Evaluate feature set using cross-validation with configured model
def evaluate_features(X: pd.DataFrame, y: pd.Series, features: list, template_ids: np.ndarray, cv, model_config: dict) -> float:
    model_module = importlib.import_module(model_config['module'])
    model_class = getattr(model_module, model_config['class_name'])
    model = model_class(**model_config['params'])

    if model_config['use_scaler']:
        scaler_module = importlib.import_module(model_config['scaler_module'])
        scaler_class = getattr(scaler_module, model_config['scaler_class'])
        estimator = Pipeline([
            ('scaler', scaler_class()),
            ('model', model)
        ])
    else:
        estimator = model

    scorer = make_scorer(mean_relative_error, greater_is_better=False)
    scores = cross_val_score(
        estimator,
        X[features],
        y,
        cv=cv.split(X[features], template_ids),
        scoring=scorer,
        n_jobs=-1
    )

    return -scores.mean()


# Calculate mean relative error metric
def mean_relative_error(y_true, y_pred) -> float:
    epsilon = 1e-6
    relative_errors = np.abs((y_true - y_pred) / (y_true + epsilon))
    return np.mean(relative_errors)


# Export all results to CSV files with semicolon delimiter
def export_results(all_seed_results: list, feature_counter: dict, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)

    summary_df = pd.DataFrame(all_seed_results)
    summary_file = output_dir / '01_multi_seed_summary.csv'
    summary_df.to_csv(summary_file, sep=';', index=False)

    sorted_features = sorted(feature_counter.items(), key=lambda x: x[1], reverse=True)
    stability_data = [
        {
            'feature': feat,
            'count': cnt,
            'percentage': (cnt / len(FFS_CONFIG['seeds'])) * 100
        }
        for feat, cnt in sorted_features
    ]
    stability_df = pd.DataFrame(stability_data)
    stability_file = output_dir / '01_feature_stability.csv'
    stability_df.to_csv(stability_file, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Forward feature selection with configurable model")
    parser.add_argument("input_csv", help="Input CSV file with features and runtime")
    parser.add_argument("--model", choices=['svm', 'random_forest', 'xgboost'], required=True, help="Model to use for feature selection")
    parser.add_argument("--output-dir", default=None, help="Output directory for results (default: Baseline_<model>/<output_folder>)")

    args = parser.parse_args()

    input_path = Path(args.input_csv)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        model_output_folder = MODEL_REGISTRY[args.model]['output_folder']
        output_path = Path(__file__).parent / f'Baseline_{MODEL_REGISTRY[args.model]["name"]}' / model_output_folder

    forward_selection_workflow(input_path, output_path, args.model)
