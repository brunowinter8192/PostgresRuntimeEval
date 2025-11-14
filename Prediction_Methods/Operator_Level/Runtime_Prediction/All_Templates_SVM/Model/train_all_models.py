#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
import joblib


OPERATORS = [
    'Aggregate', 'Gather', 'Gather_Merge', 'Hash', 'Hash_Join',
    'Incremental_Sort', 'Index_Only_Scan', 'Index_Scan', 'Limit',
    'Merge_Join', 'Nested_Loop', 'Seq_Scan', 'Sort'
]

TARGETS = ['execution_time', 'start_time']


def train_all_models_workflow(dataset_dir, overview_file, output_dir):
    overview_df = load_overview(overview_file)
    for operator in OPERATORS:
        for target in TARGETS:
            train_single_model(operator, target, dataset_dir, overview_df, output_dir)


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
    operator_dir = Path(dataset_dir) / operator
    training_file = operator_dir / f'{operator}.csv'
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
    target_columns = {
        'execution_time': 'actual_total_time',
        'start_time': 'actual_startup_time'
    }
    
    X = df_train[features]
    y = df_train[target_columns[target]]
    
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
    model_dir = Path(output_dir) / target / operator
    model_dir.mkdir(parents=True, exist_ok=True)
    
    model_file = model_dir / 'model.pkl'
    joblib.dump(pipeline, model_file)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    
    dataset_directory = sys.argv[1]
    overview_csv = sys.argv[2]
    output_directory = sys.argv[3]
    
    train_all_models_workflow(dataset_directory, overview_csv, output_directory)
