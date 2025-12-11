#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
from pathlib import Path
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
import joblib

# From mapping_config.py: Get operator names target types and target mapping
from mapping_config import OPERATORS_FOLDER_NAMES, TARGET_TYPES, TARGET_NAME_MAP

# From ffs_config.py: Get SVM hyperparameters
from ffs_config import SVM_PARAMS


# ORCHESTRATOR

def train_all_models_workflow(training_csv, overview_file, output_dir, template):
    df = load_training_data(training_csv)
    overview_df = load_overview(overview_file)
    for operator in OPERATORS_FOLDER_NAMES:
        for target in TARGET_TYPES:
            train_single_model(df, operator, target, overview_df, output_dir, template)


# FUNCTIONS

# Load training data from CSV file
def load_training_data(training_csv):
    return pd.read_csv(training_csv, delimiter=';')


# Load feature selection overview from CSV file
def load_overview(overview_file):
    return pd.read_csv(overview_file, delimiter=';')


# Train model for single operator-target combination
def train_single_model(df, operator, target, overview_df, output_dir, template):
    features = get_selected_features(overview_df, operator, target)

    if not features:
        return

    operator_df = filter_operator_data(df, operator)

    if len(operator_df) < 10:
        return

    X, y = prepare_training_data(operator_df, features, target)

    pipeline = create_and_train_pipeline(X, y)

    save_model(pipeline, operator, target, output_dir, template)


# Filter dataframe to specific operator type
def filter_operator_data(df, operator):
    operator_csv_name = operator.replace('_', ' ')
    return df[df['node_type'] == operator_csv_name].copy()


# Extract selected features from overview for operator-target combination
def get_selected_features(overview_df, operator, target):
    row = overview_df[(overview_df['operator'] == operator) & (overview_df['target'] == target)]

    if row.empty:
        return []

    features_str = row.iloc[0]['final_features']

    if pd.isna(features_str) or features_str.strip() == '':
        return []

    return [f.strip() for f in features_str.split(',')]


# Prepare features and target from training dataframe
def prepare_training_data(df_train, features, target):
    X = df_train[features]
    y = df_train[TARGET_NAME_MAP[target]]

    return X, y


# Create and train SVM pipeline with scaling
def create_and_train_pipeline(X, y):
    pipeline = Pipeline([
        ('scaler', MaxAbsScaler()),
        ('model', NuSVR(**SVM_PARAMS))
    ])

    pipeline.fit(X, y)

    return pipeline


# Save trained model pipeline to disk
def save_model(pipeline, operator, target, output_dir, template):
    model_dir = Path(output_dir) / 'Model' / template / target / operator
    model_dir.mkdir(parents=True, exist_ok=True)

    model_file = model_dir / 'model.pkl'
    joblib.dump(pipeline, model_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("training_csv", help="Path to template training CSV file")
    parser.add_argument("overview_file", help="Path to two_step_evaluation_overview.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for trained models")
    parser.add_argument("--template", required=True, help="Template name (e.g., Q1)")

    args = parser.parse_args()

    train_all_models_workflow(args.training_csv, args.overview_file, args.output_dir, args.template)
