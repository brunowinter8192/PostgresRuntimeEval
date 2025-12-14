#!/usr/bin/env python3
"""
Local copy for Dynamic LOTO workflow.

DIFFERENCE FROM ORIGINAL (Operator_Level/Runtime_Prediction/01_Forward_Selection.py):
- Iterates over AVAILABLE operator folders instead of fixed OPERATORS_FOLDER_NAMES list
- Required because LOTO splits may not contain all 13 operators (e.g., Index_Only_Scan only in Q13)
"""

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
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'Operator_Level'))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'Operator_Level' / 'Runtime_Prediction'))

# From mapping_config.py: Get target types child features and leaf operators
from mapping_config import (
    TARGET_TYPES, TARGET_NAME_MAP,
    CHILD_FEATURES, LEAF_OPERATORS, csv_name_to_folder_name,
    OPERATOR_METADATA, OPERATOR_TARGETS
)

# From ffs_config.py: Get FFS parameters and SVM configuration
from ffs_config import SEED, MIN_FEATURES, SVM_PARAMS

NO_CHILD_OPERATORS = set(csv_name_to_folder_name(op) for op in LEAF_OPERATORS)

CHILD_FEATURES_SET = set(CHILD_FEATURES)


# ORCHESTRATOR
def run_ffs_workflow(dataset_dir, output_dir):
    overview_data = collect_operator_results(dataset_dir, output_dir)
    overview_df = generate_two_step_overview(overview_data)
    export_two_step_overview(overview_df, output_dir)


# FUNCTIONS

# Get available operator folders from dataset directory
def get_available_operators(dataset_dir):
    dataset_path = Path(dataset_dir)
    operators = []
    for folder in sorted(dataset_path.iterdir()):
        if folder.is_dir() and folder.name.startswith('04a_'):
            operator_name = folder.name[4:]
            csv_file = folder / f'04a_{operator_name}.csv'
            if csv_file.exists():
                df = pd.read_csv(csv_file, delimiter=';', nrows=1)
                if len(df) > 0:
                    operators.append(operator_name)
    return operators


# Collect feature selection results from all operator-target combinations
def collect_operator_results(dataset_dir, output_dir):
    available_operators = get_available_operators(dataset_dir)
    overview_data = []
    for operator in available_operators:
        for target in TARGET_TYPES:
            result = process_operator_target(operator, target, dataset_dir, output_dir)
            if result:
                overview_data.append(result)
    return overview_data


# Process forward feature selection for single operator-target combination
def process_operator_target(operator, target, dataset_dir, output_dir):
    df = load_operator_data(dataset_dir, operator)
    X, y, template_ids = prepare_features_and_target(df, operator, target)
    cv = create_cv_splitter()
    selected_features, results_df = perform_forward_selection(X, y, template_ids, cv)
    export_results(selected_features, results_df, operator, target, output_dir)

    two_step_result = evaluate_operator_two_step(df, operator, target, template_ids, cv, selected_features)
    export_final_features(two_step_result['final_features'], operator, target, output_dir)

    return {
        'operator': operator,
        'target': target,
        'ffs_features': two_step_result['ffs_features'],
        'missing_child_features': two_step_result['missing_child_features'],
        'final_features': two_step_result['final_features'],
        'ffs_feature_count': two_step_result['ffs_feature_count'],
        'missing_child_count': two_step_result['missing_child_count'],
        'final_feature_count': two_step_result['final_feature_count'],
        'mre_ffs': two_step_result['mre_ffs'],
        'mre_final': two_step_result['mre_final']
    }


# Load training data for specified operator
def load_operator_data(dataset_dir, operator):
    operator_dir = Path(dataset_dir) / f'04a_{operator}'
    training_file = operator_dir / f'04a_{operator}.csv'
    return pd.read_csv(training_file, delimiter=';')


# Extract features, target, and template IDs from dataframe
def prepare_features_and_target(df, operator, target):
    available_features = extract_available_features(df, operator)

    X = df[available_features]
    y = df[TARGET_NAME_MAP[target]]

    template_ids = df['query_file'].apply(extract_template_id).values

    return X, y, template_ids


# Extract available features excluding metadata and target columns
def extract_available_features(df, operator):
    non_feature_cols = OPERATOR_METADATA + OPERATOR_TARGETS
    available_features = [col for col in df.columns if col not in non_feature_cols]
    return available_features


# Create stratified K-fold cross-validator
def create_cv_splitter():
    return StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)


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

        if iteration <= MIN_FEATURES:
            should_add = True
        else:
            improvement = (best_score - best_new_score) / best_score
            should_add = improvement >= 0

        if should_add:
            selected.append(best_feature)
            best_score = best_new_score
            remaining.remove(best_feature)

            results.append({
                'iteration': iteration,
                'feature_added': best_feature,
                'mre': best_new_score,
                'n_features': len(selected),
                'features': ', '.join(selected)
            })
        else:
            break

    return selected, pd.DataFrame(results)


# Evaluate feature set using cross-validated mean relative error
def evaluate_feature_set(X, y, features, template_ids, cv):
    pipeline = Pipeline([
        ('scaler', MaxAbsScaler()),
        ('model', NuSVR(**SVM_PARAMS))
    ])

    scorer = make_scorer(calculate_mean_relative_error, greater_is_better=False)

    scores = cross_val_score(
        pipeline,
        X[features],
        y,
        cv=cv.split(X[features], template_ids),
        scoring=scorer,
        n_jobs=-1
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


# Save selected features and iteration trace to CSV files
def export_results(selected_features, results_df, operator, target, output_dir):
    output_path = Path(output_dir) / 'SVM' / target / f'{operator}_csv'
    output_path.mkdir(parents=True, exist_ok=True)

    results_file = output_path / f'ffs_results_seed{SEED}.csv'
    results_df.to_csv(results_file, index=False, sep=';')

    selected_df = pd.DataFrame({
        'feature': selected_features,
        'order': range(1, len(selected_features) + 1)
    })
    selected_file = output_path / f'selected_features_seed{SEED}.csv'
    selected_df.to_csv(selected_file, index=False, sep=';')


# Identify child features missing from FFS selection
def identify_missing_child_features(ffs_features, operator):
    if operator in NO_CHILD_OPERATORS:
        return set()

    ffs_set = set(ffs_features)
    missing = CHILD_FEATURES_SET - ffs_set
    return missing


# Evaluate operator with two-step approach
def evaluate_operator_two_step(df, operator, target, template_ids, cv, ffs_features):
    available_features = extract_available_features(df, operator)

    X = df[available_features]
    y = df[TARGET_NAME_MAP[target]]

    mre_ffs = evaluate_feature_set(X, y, ffs_features, template_ids, cv)

    missing_child = identify_missing_child_features(ffs_features, operator)
    final_features = ffs_features + list(missing_child)

    mre_final = evaluate_feature_set(X, y, final_features, template_ids, cv)

    return {
        'ffs_features': ffs_features,
        'missing_child_features': list(missing_child),
        'final_features': final_features,
        'mre_ffs': mre_ffs,
        'mre_final': mre_final,
        'ffs_feature_count': len(ffs_features),
        'missing_child_count': len(missing_child),
        'final_feature_count': len(final_features)
    }


# Save final features to CSV file
def export_final_features(final_features, operator, target, output_dir):
    output_path = Path(output_dir) / 'SVM' / target / f'{operator}_csv'
    output_path.mkdir(parents=True, exist_ok=True)

    final_df = pd.DataFrame({
        'feature': final_features,
        'order': range(1, len(final_features) + 1)
    })
    final_file = output_path / 'final_features.csv'
    final_df.to_csv(final_file, index=False, sep=';')


# Create overview dataframe from two-step evaluation results
def generate_two_step_overview(overview_data):
    df = pd.DataFrame(overview_data)

    df['ffs_features'] = df['ffs_features'].apply(lambda x: ', '.join(sorted(x)))
    df['missing_child_features'] = df['missing_child_features'].apply(lambda x: ', '.join(sorted(x)) if x else '')
    df['final_features'] = df['final_features'].apply(lambda x: ', '.join(sorted(x)))

    columns_order = [
        'operator', 'target',
        'ffs_feature_count', 'missing_child_count', 'final_feature_count',
        'mre_ffs', 'mre_final',
        'ffs_features', 'missing_child_features', 'final_features'
    ]

    return df[columns_order]


# Save two-step evaluation overview to CSV
def export_two_step_overview(overview_df, output_dir):
    overview_path = Path(output_dir) / 'SVM' / 'two_step_evaluation_overview.csv'
    overview_path.parent.mkdir(parents=True, exist_ok=True)
    overview_df.to_csv(overview_path, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_dir", help="Path to dataset directory containing operator folders")
    parser.add_argument("--output-dir", required=True, help="Output directory for FFS results")

    args = parser.parse_args()

    run_ffs_workflow(args.dataset_dir, args.output_dir)
