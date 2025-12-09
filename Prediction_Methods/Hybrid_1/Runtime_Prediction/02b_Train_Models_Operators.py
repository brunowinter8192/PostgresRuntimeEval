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
# From mapping_config.py: Target types
from mapping_config import TARGET_TYPES


# ORCHESTRATOR

# Train models for all operator-target combinations
def train_all_operators(dataset_dir, overview_file, output_dir):
    overview_df = load_overview(overview_file)

    for _, row in overview_df.iterrows():
        operator = row['operator']
        target = row['target']
        train_single_model(operator, target, dataset_dir, overview_df, output_dir)


# FUNCTIONS

# Load feature selection overview from CSV
def load_overview(overview_file):
    return pd.read_csv(overview_file, delimiter=';')


# Train model for single operator-target combination
def train_single_model(operator, target, dataset_dir, overview_df, output_dir):
    features = get_selected_features(overview_df, operator, target)
    if not features:
        return
    df_train = load_training_data(dataset_dir, operator)
    X, y = prepare_training_data(df_train, features, target)
    pipeline = create_and_train_pipeline(X, y)
    save_model(pipeline, operator, target, output_dir)


# Extract selected features from overview for operator-target combination
def get_selected_features(overview_df, operator, target):
    row = overview_df[(overview_df['operator'] == operator) & (overview_df['target'] == target)]
    if row.empty:
        return []
    features_str = row.iloc[0]['final_features']
    if pd.isna(features_str) or features_str.strip() == '':
        return []
    return [f.strip() for f in features_str.split(',')]


# Load training data for operator from CSV
def load_training_data(dataset_dir, operator):
    operator_dir = Path(dataset_dir) / operator
    training_file = operator_dir / 'training.csv'
    return pd.read_csv(training_file, delimiter=';')


# Prepare features and target from training dataframe
def prepare_training_data(df_train, features, target):
    X = df_train[features]
    target_column = 'actual_startup_time' if target == 'start_time' else 'actual_total_time'
    y = df_train[target_column]
    return X, y


# Create and train SVM pipeline with scaling
def create_and_train_pipeline(X, y):
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
    pipeline.fit(X, y)
    return pipeline


# Save trained model pipeline to disk
def save_model(pipeline, operator, target, output_dir):
    model_dir = Path(output_dir) / 'Model' / target / 'operators' / operator
    model_dir.mkdir(parents=True, exist_ok=True)
    model_file = model_dir / 'model.pkl'
    joblib.dump(pipeline, model_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train operator-level SVM models')
    parser.add_argument('dataset_dir', help='Path to directory containing operators/')
    parser.add_argument('overview_file', help='Path to operator_overview.csv')
    parser.add_argument('--output-dir', required=True, help='Path to output directory')
    args = parser.parse_args()

    train_all_operators(args.dataset_dir, args.overview_file, args.output_dir)
