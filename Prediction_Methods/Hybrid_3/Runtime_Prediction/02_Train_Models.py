#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import sys
import pandas as pd
from pathlib import Path
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
import joblib

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Pattern definitions and target types
from mapping_config import PATTERNS, TARGET_TYPES
# From ffs_config.py: SVM parameters
from ffs_config import SVM_PARAMS

# ORCHESTRATOR

# Train models for all pattern-target combinations
def train_all_patterns(dataset_dir, overview_file, output_dir):
    overview_df = load_overview(overview_file)
    for pattern in PATTERNS:
        for target in TARGET_TYPES:
            train_single_model(pattern, target, dataset_dir, overview_df, output_dir)

# FUNCTIONS

# Load feature selection overview from CSV
def load_overview(overview_file):
    return pd.read_csv(overview_file, delimiter=';')

# Train model for single pattern-target combination
def train_single_model(pattern, target, dataset_dir, overview_df, output_dir):
    features = get_selected_features(overview_df, pattern, target)
    if not features:
        return
    df_train = load_training_data(dataset_dir, pattern)
    X, y = prepare_training_data(df_train, features, target)
    pipeline = create_and_train_pipeline(X, y)
    save_model(pipeline, pattern, target, output_dir)

# Extract selected features from overview for pattern-target combination
def get_selected_features(overview_df, pattern, target):
    row = overview_df[(overview_df['pattern'] == pattern) & (overview_df['target'] == target)]
    if row.empty:
        return []
    features_str = row.iloc[0]['final_features']
    if pd.isna(features_str) or features_str.strip() == '':
        return []
    return [f.strip() for f in features_str.split(',')]

# Load cleaned training data for pattern from CSV
def load_training_data(dataset_dir, pattern):
    pattern_dir = Path(dataset_dir) / pattern
    training_file = pattern_dir / 'training_cleaned.csv'
    return pd.read_csv(training_file, delimiter=';')

# Prepare features and target from training dataframe
def prepare_training_data(df_train, features, target):
    X = df_train[features]
    target_column = identify_target_column(df_train, target)
    y = df_train[target_column]
    return X, y

# Identify target column based on target type
def identify_target_column(df, target):
    target_suffix = '_actual_startup_time' if target == 'start_time' else '_actual_total_time'
    for col in df.columns:
        if col.endswith(target_suffix) and '_Outer_' not in col and '_Inner_' not in col:
            return col
    return None

# Create and train SVM pipeline with scaling
def create_and_train_pipeline(X, y):
    pipeline = Pipeline([
        ('scaler', MaxAbsScaler()),
        ('model', NuSVR(**SVM_PARAMS))
    ])
    pipeline.fit(X, y)
    return pipeline

# Save trained model pipeline to disk
def save_model(pipeline, pattern, target, output_dir):
    model_dir = Path(output_dir) / 'Model' / target / pattern
    model_dir.mkdir(parents=True, exist_ok=True)
    model_file = model_dir / 'model.pkl'
    joblib.dump(pipeline, model_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train pattern-level SVM models')
    parser.add_argument('dataset_dir', help='Path to Patterns directory')
    parser.add_argument('overview_file', help='Path to two_step_evaluation_overview.csv')
    parser.add_argument('--output-dir', required=True, help='Path to Model/Hybrid output directory')
    args = parser.parse_args()

    train_all_patterns(args.dataset_dir, args.overview_file, args.output_dir)
