#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import re
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import make_scorer
from joblib import Parallel, delayed
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Target types and FFS configuration
from mapping_config import TARGET_TYPES, FFS_SEED, FFS_MIN_FEATURES, CHILD_FEATURES_TIMING


# ORCHESTRATOR

# Run two-step feature selection workflow for all operators
def run_two_step_workflow(dataset_dir: str, output_dir: str) -> None:
    operators = discover_operators(dataset_dir)

    tasks = [(operator, target) for operator in operators for target in TARGET_TYPES]

    results = Parallel(n_jobs=-1)(
        delayed(run_ffs_for_operator)(operator, target, dataset_dir, output_dir)
        for operator, target in tasks
    )

    ffs_results = {}
    for (operator, target), selected_features in zip(tasks, results):
        ffs_results[(operator, target)] = selected_features

    overview_data = process_all_operators_two_step(operators, ffs_results, dataset_dir, output_dir)
    export_overview(overview_data, output_dir)


# FUNCTIONS

# Discover operators from operators folder
def discover_operators(dataset_dir: str) -> list:
    operators_path = Path(dataset_dir)
    operators = []

    if not operators_path.exists():
        return operators

    for folder in operators_path.iterdir():
        if folder.is_dir():
            training_file = folder / 'training.csv'
            if training_file.exists():
                operators.append(folder.name)

    return sorted(operators)


# Run forward feature selection and return selected features
def run_ffs_for_operator(operator: str, target: str, dataset_dir: str, output_dir: str) -> list:
    df = load_operator_data(dataset_dir, operator)
    X, y, template_ids = prepare_features_and_target(df, target)
    cv = create_cv_splitter()
    selected_features, results_df = perform_forward_selection(X, y, template_ids, cv)
    export_ffs_results(selected_features, results_df, operator, target, output_dir)
    return selected_features


# Load training data for operator
def load_operator_data(dataset_dir, operator):
    operator_dir = Path(dataset_dir) / operator
    training_file = operator_dir / 'training.csv'
    return pd.read_csv(training_file, delimiter=';')


# Extract features target and template IDs from dataframe
def prepare_features_and_target(df, target):
    available_features = extract_available_features(df)
    target_column = 'actual_startup_time' if target == 'start_time' else 'actual_total_time'

    X = df[available_features]
    y = df[target_column]
    template_ids = df['query_file'].apply(extract_template_id).values

    return X, y, template_ids


# Extract available features excluding non-feature columns
def extract_available_features(df):
    non_feature_cols = [
        'query_file', 'node_id', 'node_type', 'depth', 'parent_relationship',
        'subplan_name', 'actual_startup_time', 'actual_total_time', 'template'
    ]

    available_features = []
    for col in df.columns:
        if col in non_feature_cols:
            continue
        available_features.append(col)

    return available_features


# Create stratified K-fold cross-validator
def create_cv_splitter():
    return StratifiedKFold(n_splits=5, shuffle=True, random_state=FFS_SEED)


# Perform forward feature selection with cross-validation
def perform_forward_selection(X, y, template_ids, cv):
    selected = []
    remaining = list(X.columns)
    results = []
    best_score = float('inf')
    iteration = 0

    while remaining:
        iteration += 1
        scores = {}

        for feature in remaining:
            test_features = selected + [feature]
            score = evaluate_feature_set(X, y, test_features, template_ids, cv)
            scores[feature] = score

        best_feature = min(scores, key=scores.get)
        best_new_score = scores[best_feature]

        if iteration <= FFS_MIN_FEATURES:
            should_add = True
        else:
            improvement = (best_score - best_new_score) / best_score
            should_add = improvement >= 0

        if should_add:
            selected.append(best_feature)
            best_score = best_new_score

            results.append({
                'iteration': iteration,
                'feature_tested': best_feature,
                'was_selected': True,
                'mre': best_new_score,
                'n_features_selected': len(selected),
                'selected_features': ', '.join(selected)
            })
        else:
            results.append({
                'iteration': iteration,
                'feature_tested': best_feature,
                'was_selected': False,
                'mre': best_new_score,
                'n_features_selected': len(selected),
                'selected_features': ', '.join(selected) if selected else ''
            })

        remaining.remove(best_feature)

    return selected, pd.DataFrame(results)


# Evaluate feature set using cross-validated mean relative error
def evaluate_feature_set(X, y, features, template_ids, cv):
    pipeline = Pipeline([
        ('scaler', MaxAbsScaler()),
        ('model', NuSVR(
            kernel='rbf',
            nu=0.65,
            C=1.5,
            gamma='scale',
            cache_size=500
        ))
    ])

    scorer = make_scorer(calculate_mean_relative_error, greater_is_better=False)

    scores = cross_val_score(
        pipeline,
        X[features],
        y,
        cv=cv.split(X[features], template_ids),
        scoring=scorer,
        n_jobs=1
    )

    return -scores.mean()


# Calculate mean relative error between true and predicted values
def calculate_mean_relative_error(y_true, y_pred):
    epsilon = 1e-6
    relative_errors = np.abs((y_true - y_pred) / (y_true + epsilon))
    return np.mean(relative_errors)


# Extract template ID number from query filename
def extract_template_id(query_file):
    filename = str(query_file).lower()
    match = re.search(r'q(\d+)_', filename)
    if match:
        return int(match.group(1))
    return 0


# Save FFS selected features to CSV file
def export_ffs_results(selected_features, results_df, operator, target, output_dir):
    output_path = Path(output_dir) / 'SVM' / target / 'operators' / f'{operator}_csv'
    output_path.mkdir(parents=True, exist_ok=True)

    results_file = output_path / f'ffs_results_seed{FFS_SEED}.csv'
    results_df.to_csv(results_file, index=False, sep=';')

    selected_df = pd.DataFrame({
        'feature': selected_features,
        'order': range(1, len(selected_features) + 1)
    })
    selected_file = output_path / f'selected_features_seed{FFS_SEED}.csv'
    selected_df.to_csv(selected_file, index=False, sep=';')


# Process all operators with two-step evaluation
def process_all_operators_two_step(operators, ffs_results, dataset_dir, output_dir):
    overview_data = []

    for operator in operators:
        for target in TARGET_TYPES:
            result = evaluate_operator_two_step(operator, target, ffs_results, dataset_dir, output_dir)
            if result:
                overview_data.append(result)

    return overview_data


# Evaluate single operator with two-step approach
def evaluate_operator_two_step(operator, target, ffs_results, dataset_dir, output_dir):
    ffs_selected = ffs_results.get((operator, target), [])

    if not ffs_selected:
        return None

    df = load_operator_data(dataset_dir, operator)
    X, y, template_ids = prepare_features_and_target(df, target)
    cv = create_cv_splitter()

    mre_ffs = evaluate_feature_set(X, y, ffs_selected, template_ids, cv)

    missing_child_features = identify_missing_child_features(ffs_selected, X.columns)

    final_features = list(ffs_selected) + list(missing_child_features)

    if missing_child_features:
        mre_final = evaluate_feature_set(X, y, final_features, template_ids, cv)
    else:
        mre_final = mre_ffs

    export_final_features(final_features, operator, target, output_dir)

    return {
        'operator': operator,
        'target': target,
        'ffs_feature_count': len(ffs_selected),
        'missing_child_count': len(missing_child_features),
        'final_feature_count': len(final_features),
        'mre_ffs': f'{mre_ffs:.4f}',
        'mre_final': f'{mre_final:.4f}',
        'mre_delta': f'{mre_final - mre_ffs:.4f}',
        'ffs_features': ', '.join(sorted(ffs_selected)),
        'missing_child_features': ', '.join(sorted(missing_child_features)) if missing_child_features else '',
        'final_features': ', '.join(sorted(final_features))
    }


# Identify child features missing from FFS selection
def identify_missing_child_features(ffs_selected, available_columns):
    ffs_selected_set = set(ffs_selected)
    missing = []
    for feat in CHILD_FEATURES_TIMING:
        if feat in available_columns and feat not in ffs_selected_set:
            missing.append(feat)
    return missing


# Export final feature set to CSV
def export_final_features(final_features, operator, target, output_dir):
    output_path = Path(output_dir) / 'SVM' / target / 'operators' / f'{operator}_csv'
    output_path.mkdir(parents=True, exist_ok=True)

    final_df = pd.DataFrame({
        'feature': sorted(final_features),
        'order': range(1, len(final_features) + 1)
    })
    final_file = output_path / 'final_features.csv'
    final_df.to_csv(final_file, index=False, sep=';')


# Export two-step evaluation overview to CSV
def export_overview(overview_data, output_dir):
    output_path = Path(output_dir) / 'SVM'
    output_path.mkdir(parents=True, exist_ok=True)

    overview_df = pd.DataFrame(overview_data)
    overview_file = output_path / 'operator_overview.csv'
    overview_df.to_csv(overview_file, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_dir", help="Directory containing operator training datasets")
    parser.add_argument("--output-dir", required=True, help="Output directory for FFS results and overview")
    args = parser.parse_args()

    run_two_step_workflow(args.dataset_dir, args.output_dir)
