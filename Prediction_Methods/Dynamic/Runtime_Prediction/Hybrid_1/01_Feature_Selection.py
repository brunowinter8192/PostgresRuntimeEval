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
from multiprocessing import Pool

ALL_TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
ALL_APPROACHES = ['approach_3']
TARGET_TYPES = ['execution_time', 'start_time']
NON_FEATURE_SUFFIXES = [
    '_node_id',
    '_node_type',
    '_depth',
    '_parent_relationship',
    '_subplan_name',
    '_template',
    'actual_startup_time',
    'actual_total_time'
]
FFS_SEED = 42
FFS_MIN_FEATURES = 1

SCRIPT_DIR = Path(__file__).resolve().parent
DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Hybrid_1'


# ORCHESTRATOR
def batch_feature_selection(templates: list, approaches: list) -> None:
    tasks = [(template, approach) for template in templates for approach in approaches]
    with Pool(6) as pool:
        pool.map(process_template, tasks)


# FUNCTIONS

# Process single template-approach combination
def process_template(task: tuple) -> None:
    template, approach = task
    print(f"{template}/{approach}...")

    pattern_dataset = DATASET_DIR / template / approach
    output_dir = SCRIPT_DIR / template / approach

    used_patterns_file = pattern_dataset / 'used_patterns.csv'
    if not used_patterns_file.exists():
        print(f"  Skipping: no used_patterns.csv")
        return

    run_two_step_workflow(pattern_dataset, output_dir, used_patterns_file)


# Run two-step feature selection workflow for all used patterns
def run_two_step_workflow(dataset_dir: Path, output_dir: Path, filter_file: Path) -> None:
    allowed_hashes = load_pattern_filter(filter_file)
    patterns = discover_patterns(dataset_dir, allowed_hashes)

    if not patterns:
        print(f"  No patterns found")
        return

    ffs_results = {}
    for pattern in patterns:
        for target in TARGET_TYPES:
            selected_features = run_ffs_for_pattern(pattern, target, dataset_dir, output_dir)
            ffs_results[(pattern['hash'], target)] = selected_features

    overview_data = process_all_patterns_two_step(patterns, ffs_results, dataset_dir, output_dir)
    export_overview(overview_data, output_dir)


# Load allowed pattern hashes from filter CSV
def load_pattern_filter(filter_path: Path) -> set:
    df = pd.read_csv(filter_path, delimiter=';')
    return set(df['pattern_hash'].tolist())


# Discover patterns from patterns folder
def discover_patterns(dataset_dir: Path, allowed_hashes: set) -> list:
    patterns_path = dataset_dir / 'patterns'
    patterns = []

    if not patterns_path.exists():
        return patterns

    for folder in patterns_path.iterdir():
        if folder.is_dir() and folder.name in allowed_hashes:
            training_file = folder / 'training_cleaned.csv'
            if training_file.exists():
                patterns.append({
                    'hash': folder.name,
                    'folder_name': folder.name
                })

    return patterns


# Run forward feature selection and return selected features
def run_ffs_for_pattern(pattern: dict, target: str, dataset_dir: Path, output_dir: Path) -> list:
    df = load_pattern_data(dataset_dir, pattern['hash'])
    if df is None or df.empty:
        return []

    X, y, template_ids = prepare_features_and_target(df, target)
    if X is None or X.empty or y is None:
        return []

    cv = create_cv_splitter()
    selected_features, results_df = perform_forward_selection(X, y, template_ids, cv)
    export_ffs_results(selected_features, results_df, pattern['hash'], target, output_dir)
    return selected_features


# Load cleaned training data for pattern using hash
def load_pattern_data(dataset_dir: Path, pattern_hash: str) -> pd.DataFrame:
    pattern_dir = dataset_dir / 'patterns' / pattern_hash
    training_file = pattern_dir / 'training_cleaned.csv'
    if not training_file.exists():
        return None
    return pd.read_csv(training_file, delimiter=';')


# Extract features target and template IDs from dataframe
def prepare_features_and_target(df: pd.DataFrame, target: str) -> tuple:
    available_features = extract_available_features(df)
    target_column = identify_target_column(df, target)

    if not target_column or target_column not in df.columns:
        return None, None, None

    X = df[available_features].fillna(0)
    y = df[target_column]
    template_ids = df['query_file'].apply(extract_template_id).values

    return X, y, template_ids


# Extract available features excluding non-feature columns
def extract_available_features(df: pd.DataFrame) -> list:
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
def identify_target_column(df: pd.DataFrame, target: str) -> str:
    unprefixed = 'actual_startup_time' if target == 'start_time' else 'actual_total_time'
    if unprefixed in df.columns:
        return unprefixed

    target_suffix = '_actual_startup_time' if target == 'start_time' else '_actual_total_time'
    for col in df.columns:
        if col.endswith(target_suffix) and '_Outer_' not in col and '_Inner_' not in col:
            return col

    return None


# Create stratified K-fold cross-validator
def create_cv_splitter() -> StratifiedKFold:
    return StratifiedKFold(n_splits=5, shuffle=True, random_state=FFS_SEED)


# Perform forward feature selection with cross-validation
def perform_forward_selection(X: pd.DataFrame, y: pd.Series, template_ids: np.ndarray, cv: StratifiedKFold) -> tuple:
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
            improvement = (best_score - best_new_score) / best_score if best_score > 0 else 0
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
def evaluate_feature_set(X: pd.DataFrame, y: pd.Series, features: list, template_ids: np.ndarray, cv: StratifiedKFold) -> float:
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
def calculate_mean_relative_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    epsilon = 1e-6
    relative_errors = np.abs((y_true - y_pred) / (y_true + epsilon))
    return np.mean(relative_errors)


# Extract template ID number from query filename
def extract_template_id(query_file: str) -> int:
    filename = str(query_file).lower()
    match = re.search(r'q(\d+)_', filename)
    if match:
        return int(match.group(1))
    return 0


# Save FFS selected features to CSV file
def export_ffs_results(selected_features: list, results_df: pd.DataFrame, pattern_hash: str, target: str, output_dir: Path) -> None:
    output_path = output_dir / 'SVM' / target / f'{pattern_hash}_csv'
    output_path.mkdir(parents=True, exist_ok=True)

    results_file = output_path / f'ffs_results_seed{FFS_SEED}.csv'
    results_df.to_csv(results_file, index=False, sep=';')

    selected_df = pd.DataFrame({
        'feature': selected_features,
        'order': range(1, len(selected_features) + 1)
    })
    selected_file = output_path / f'selected_features_seed{FFS_SEED}.csv'
    selected_df.to_csv(selected_file, index=False, sep=';')


# Process all patterns with two-step evaluation
def process_all_patterns_two_step(patterns: list, ffs_results: dict, dataset_dir: Path, output_dir: Path) -> list:
    overview_data = []

    for pattern in patterns:
        for target in TARGET_TYPES:
            result = evaluate_pattern_two_step(pattern, target, ffs_results, dataset_dir, output_dir)
            if result:
                overview_data.append(result)

    return overview_data


# Evaluate single pattern with two-step approach
def evaluate_pattern_two_step(pattern: dict, target: str, ffs_results: dict, dataset_dir: Path, output_dir: Path) -> dict:
    ffs_selected = ffs_results.get((pattern['hash'], target), [])

    if not ffs_selected:
        return None

    df = load_pattern_data(dataset_dir, pattern['hash'])
    if df is None:
        return None

    X, y, template_ids = prepare_features_and_target(df, target)
    if X is None:
        return None

    cv = create_cv_splitter()

    mre_ffs = evaluate_feature_set(X, y, ffs_selected, template_ids, cv)

    dataset_child_features = identify_child_features_in_dataset(df)
    missing_child_features = identify_missing_child_features(ffs_selected, dataset_child_features)

    final_features = list(ffs_selected) + list(missing_child_features)

    if missing_child_features:
        mre_final = evaluate_feature_set(X, y, final_features, template_ids, cv)
    else:
        mre_final = mre_ffs

    export_final_features(final_features, pattern['hash'], target, output_dir)

    return {
        'pattern_hash': pattern['hash'],
        'target': target,
        'ffs_feature_count': len(ffs_selected),
        'missing_child_count': len(missing_child_features),
        'final_feature_count': len(final_features),
        'mre_ffs': f'{mre_ffs:.4f}',
        'mre_final': f'{mre_final:.4f}',
        'mre_delta': f'{mre_final - mre_ffs:.4f}',
        'final_features': ', '.join(sorted(final_features))
    }


# Identify all child features present in dataset
def identify_child_features_in_dataset(df: pd.DataFrame) -> set:
    child_features = set()
    for col in df.columns:
        if ('_Outer_' in col or '_Inner_' in col) and col.endswith(('_st1', '_rt1', '_st2', '_rt2')):
            child_features.add(col)
    return child_features


# Identify child features missing from FFS selection
def identify_missing_child_features(ffs_selected: list, dataset_child_features: set) -> set:
    ffs_selected_set = set(ffs_selected)
    return dataset_child_features - ffs_selected_set


# Export final feature set to CSV
def export_final_features(final_features: list, pattern_hash: str, target: str, output_dir: Path) -> None:
    output_path = output_dir / 'SVM' / target / f'{pattern_hash}_csv'
    output_path.mkdir(parents=True, exist_ok=True)

    final_df = pd.DataFrame({
        'feature': sorted(final_features),
        'order': range(1, len(final_features) + 1)
    })
    final_file = output_path / 'final_features.csv'
    final_df.to_csv(final_file, index=False, sep=';')


# Export two-step evaluation overview to CSV
def export_overview(overview_data: list, output_dir: Path) -> None:
    output_path = output_dir / 'SVM'
    output_path.mkdir(parents=True, exist_ok=True)

    overview_df = pd.DataFrame(overview_data)
    overview_file = output_path / 'two_step_evaluation_overview.csv'
    overview_df.to_csv(overview_file, index=False, sep=';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--templates", nargs="+", default=ALL_TEMPLATES, help="Templates to process")
    parser.add_argument("--approaches", nargs="+", default=ALL_APPROACHES, help="Approaches to process")
    args = parser.parse_args()
    batch_feature_selection(args.templates, args.approaches)
