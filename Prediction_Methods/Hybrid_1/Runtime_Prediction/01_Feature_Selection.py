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
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Pattern definitions and feature suffixes
from mapping_config import PATTERNS, TARGET_TYPES, NON_FEATURE_SUFFIXES
# From ffs_config.py: Forward feature selection configuration
from ffs_config import SEED, MIN_FEATURES, SVM_PARAMS

# ORCHESTRATOR

# Run two-step feature selection workflow for all patterns
def run_two_step_workflow(dataset_dir: str, output_dir: str) -> None:
    ffs_results = {}

    for pattern in PATTERNS:
        for target in TARGET_TYPES:
            selected_features = run_ffs_for_pattern(pattern, target, dataset_dir, output_dir)
            ffs_results[(pattern, target)] = selected_features
    
    overview_data = process_all_patterns_two_step(ffs_results, dataset_dir, output_dir)
    export_overview(overview_data, output_dir)


# FUNCTIONS

# Run forward feature selection and return selected features
def run_ffs_for_pattern(pattern: str, target: str, dataset_dir: str, output_dir: str) -> list:
    df = load_pattern_data(dataset_dir, pattern)
    X, y, template_ids = prepare_features_and_target(df, target)
    cv = create_cv_splitter()
    selected_features, results_df = perform_forward_selection(X, y, template_ids, cv)
    export_ffs_results(selected_features, results_df, pattern, target, output_dir)
    return selected_features

# Load cleaned training data for pattern
def load_pattern_data(dataset_dir, pattern):
    pattern_dir = Path(dataset_dir) / pattern
    training_file = pattern_dir / 'training_cleaned.csv'
    return pd.read_csv(training_file, delimiter=';')

# Extract features target and template IDs from dataframe
def prepare_features_and_target(df, target):
    available_features = extract_available_features(df)
    target_column = identify_target_column(df, target)
    
    X = df[available_features]
    y = df[target_column]
    template_ids = df['query_file'].apply(extract_template_id).values
    
    return X, y, template_ids

# Extract available features excluding non-feature columns
def extract_available_features(df):
    non_feature_cols = ['query_file']
    
    available_features = []
    for col in df.columns:
        if col in non_feature_cols:
            continue
        if any(col.endswith(suffix) for suffix in NON_FEATURE_SUFFIXES):
            continue
        available_features.append(col)
    
    return available_features

# Identify target column based on target type
def identify_target_column(df, target):
    target_suffix = '_actual_startup_time' if target == 'start_time' else '_actual_total_time'
    
    for col in df.columns:
        if col.endswith(target_suffix) and '_Outer_' not in col and '_Inner_' not in col:
            return col
    
    return None

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

# Save FFS selected features to CSV file
def export_ffs_results(selected_features, results_df, pattern, target, output_dir):
    output_path = Path(output_dir) / 'SVM' / target / f'{pattern}_csv'
    output_path.mkdir(parents=True, exist_ok=True)
    
    results_file = output_path / f'ffs_results_seed{SEED}.csv'
    results_df.to_csv(results_file, index=False, sep=';')

    selected_df = pd.DataFrame({
        'feature': selected_features,
        'order': range(1, len(selected_features) + 1)
    })
    selected_file = output_path / f'selected_features_seed{SEED}.csv'
    selected_df.to_csv(selected_file, index=False, sep=';')

# Process all patterns with two-step evaluation
def process_all_patterns_two_step(ffs_results, dataset_dir, output_dir):
    overview_data = []
    
    for pattern in PATTERNS:
        for target in TARGET_TYPES:
            result = evaluate_pattern_two_step(pattern, target, ffs_results, dataset_dir, output_dir)
            if result:
                overview_data.append(result)
    
    return overview_data

# Evaluate single pattern with two-step approach
def evaluate_pattern_two_step(pattern, target, ffs_results, dataset_dir, output_dir):
    ffs_selected = ffs_results.get((pattern, target), [])
    
    if not ffs_selected:
        return None
    
    df = load_pattern_data(dataset_dir, pattern)
    X, y, template_ids = prepare_features_and_target(df, target)
    cv = create_cv_splitter()
    
    mre_ffs = evaluate_feature_set(X, y, ffs_selected, template_ids, cv)
    
    dataset_child_features = identify_child_features_in_dataset(df)
    missing_child_features = identify_missing_child_features(ffs_selected, dataset_child_features)
    
    final_features = list(ffs_selected) + list(missing_child_features)
    
    if missing_child_features:
        mre_final = evaluate_feature_set(X, y, final_features, template_ids, cv)
    else:
        mre_final = mre_ffs
    
    export_final_features(final_features, pattern, target, output_dir)
    
    return {
        'pattern': pattern,
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

# Identify all child features present in dataset
def identify_child_features_in_dataset(df):
    child_features = set()
    for col in df.columns:
        if ('_Outer_' in col or '_Inner_' in col) and col.endswith(('_st1', '_rt1', '_st2', '_rt2')):
            child_features.add(col)
    return child_features

# Identify child features missing from FFS selection
def identify_missing_child_features(ffs_selected, dataset_child_features):
    ffs_selected_set = set(ffs_selected)
    return dataset_child_features - ffs_selected_set

# Export final feature set to CSV
def export_final_features(final_features, pattern, target, output_dir):
    output_path = Path(output_dir) / 'SVM' / target / f'{pattern}_csv'
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
    overview_file = output_path / 'two_step_evaluation_overview.csv'
    overview_df.to_csv(overview_file, index=False, sep=';')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_dir", help="Directory containing pattern training datasets")
    parser.add_argument("--output-dir", required=True, help="Output directory for FFS results and overview")
    args = parser.parse_args()

    run_two_step_workflow(args.dataset_dir, args.output_dir)
