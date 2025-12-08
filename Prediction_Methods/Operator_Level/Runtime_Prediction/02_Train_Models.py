#!/usr/bin/env python3

# INFRASTRUCTURE

import sys
import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
import joblib

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# From mapping_config.py: Get operator names target types and target mapping
from mapping_config import OPERATORS_FOLDER_NAMES, TARGET_TYPES, TARGET_NAME_MAP

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'SVM'))

# From ffs_config.py: Get SVM hyperparameters
from ffs_config import SVM_PARAMS


# ORCHESTRATOR

def train_all_models_workflow(dataset_dir, overview_file, output_dir):
    overview_df = load_overview(overview_file)
    for operator in OPERATORS_FOLDER_NAMES:
        for target in TARGET_TYPES:
            train_single_model(operator, target, dataset_dir, overview_df, output_dir)


# FUNCTIONS

# Load feature selection overview from CSV file
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


# Load training data for operator from CSV file
def load_training_data(dataset_dir, operator):
    operator_dir = Path(dataset_dir) / f'04a_{operator}'
    training_file = operator_dir / f'04a_{operator}.csv'
    return pd.read_csv(training_file, delimiter=';')


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
def save_model(pipeline, operator, target, output_dir):
    model_dir = Path(output_dir) / 'Model' / target / operator
    model_dir.mkdir(parents=True, exist_ok=True)

    model_file = model_dir / 'model.pkl'
    joblib.dump(pipeline, model_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_dir", help="Base directory containing operator training folders")
    parser.add_argument("overview_file", help="Path to two_step_evaluation_overview.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for trained models")
    args = parser.parse_args()

    train_all_models_workflow(args.dataset_dir, args.overview_file, args.output_dir)
