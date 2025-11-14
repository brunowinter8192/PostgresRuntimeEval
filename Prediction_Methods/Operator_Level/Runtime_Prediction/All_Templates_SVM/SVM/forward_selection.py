#!/usr/bin/env python3

import sys
import re
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import make_scorer


OPERATORS = [
    'Aggregate', 'Gather', 'Gather_Merge', 'Hash', 'Hash_Join',
    'Incremental_Sort', 'Index_Only_Scan', 'Index_Scan', 'Limit',
    'Merge_Join', 'Nested_Loop', 'Seq_Scan', 'Sort'
]

TARGETS = ['execution_time', 'start_time']

SEED = 42
MIN_FEATURES = 1

SPARSE_FEATURES_MAP = {
    'Seq_Scan': ['nt1', 'nt2', 'startup_cost', 'parallel_workers', 'st1', 'rt1', 'st2', 'rt2'],
    'Index_Scan': ['nt1', 'nt2', 'parallel_workers', 'st1', 'rt1', 'st2', 'rt2']
}


def run_ffs_workflow(dataset_dir, output_dir):
    for operator in OPERATORS:
        for target in TARGETS:
            process_operator_target(operator, target, dataset_dir, output_dir)


# Process forward feature selection for single operator-target combination
def process_operator_target(operator, target, dataset_dir, output_dir):
    df = load_operator_data(dataset_dir, operator)
    X, y, template_ids = prepare_features_and_target(df, operator, target)
    cv = create_cv_splitter()
    selected_features, results_df = perform_forward_selection(X, y, template_ids, cv)
    export_results(selected_features, results_df, operator, target, output_dir)


# Load training data for specified operator
def load_operator_data(dataset_dir, operator):
    operator_dir = Path(dataset_dir) / operator
    training_file = operator_dir / f'{operator}.csv'
    return pd.read_csv(training_file, delimiter=';')


# Extract features, target, and template IDs from dataframe
def prepare_features_and_target(df, operator, target):
    available_features = extract_available_features(df, operator)
    
    X = df[available_features]
    
    target_columns = {
        'execution_time': 'actual_total_time',
        'start_time': 'actual_startup_time'
    }
    y = df[target_columns[target]]
    
    template_ids = df['query_file'].apply(extract_template_id).values
    
    return X, y, template_ids


# Extract available features excluding non-feature and sparse columns
def extract_available_features(df, operator):
    non_feature_cols = [
        'query_file', 'node_id', 'node_type', 'depth',
        'parent_relationship', 'subplan_name',
        'actual_startup_time', 'actual_total_time'
    ]
    
    available_features = [col for col in df.columns if col not in non_feature_cols]
    
    if operator in SPARSE_FEATURES_MAP:
        sparse_features = SPARSE_FEATURES_MAP[operator]
        available_features = [f for f in available_features if f not in sparse_features]
    
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
    output_path = Path(output_dir) / target / f'{operator}_csv'
    output_path.mkdir(parents=True, exist_ok=True)
    
    results_file = output_path / f'ffs_results_seed{SEED}.csv'
    results_df.to_csv(results_file, index=False, sep=';')
    
    selected_df = pd.DataFrame({
        'feature': selected_features,
        'order': range(1, len(selected_features) + 1)
    })
    selected_file = output_path / f'selected_features_seed{SEED}.csv'
    selected_df.to_csv(selected_file, index=False, sep=';')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    
    dataset_directory = sys.argv[1]
    output_directory = sys.argv[2]
    
    run_ffs_workflow(dataset_directory, output_directory)
