#!/usr/bin/env python3

# INFRASTRUCTURE

import sys
import argparse
import pandas as pd
from pathlib import Path
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
import joblib

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# From mapping_config.py: Get operator names and target configuration
from mapping_config import OPERATOR_CSV_TO_FOLDER, TARGET_TYPES, TARGET_NAME_MAP

# From ffs_config.py: Get SVM hyperparameters
from Runtime_Prediction.ffs_config import SVM_PARAMS


# ORCHESTRATOR

def train_final_operators(training_file: str, overview_file: str, output_dir: str) -> None:
    df_training = load_training_data(training_file)
    df_overview = load_overview(overview_file)
    training_results = []

    for operator_csv, operator_folder in OPERATOR_CSV_TO_FOLDER.items():
        df_operator = extract_operator_data(df_training, operator_csv)

        if df_operator.empty:
            continue

        for target in TARGET_TYPES:
            result = train_single_model(
                df_operator, operator_folder, target, df_overview, output_dir
            )
            if result:
                training_results.append(result)

    export_training_summary(training_results, output_dir)


# FUNCTIONS

# Load full training dataset
def load_training_data(training_file: str) -> pd.DataFrame:
    df = pd.read_csv(training_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load feature overview from CSV file
def load_overview(overview_file: str) -> pd.DataFrame:
    return pd.read_csv(overview_file, delimiter=';')


# Extract data for single operator type
def extract_operator_data(df: pd.DataFrame, operator_csv: str) -> pd.DataFrame:
    return df[df['node_type'] == operator_csv].copy()


# Train model for single operator-target combination
def train_single_model(
    df_operator: pd.DataFrame,
    operator_folder: str,
    target: str,
    df_overview: pd.DataFrame,
    output_dir: str
) -> dict:
    features = get_selected_features(df_overview, operator_folder, target)

    if not features:
        return None

    X, y = prepare_training_data(df_operator, features, target)

    if X.empty:
        return None

    pipeline = create_and_train_pipeline(X, y)
    save_model(pipeline, operator_folder, target, output_dir)

    return {
        'operator': operator_folder,
        'target': target,
        'samples': len(df_operator),
        'features': len(features),
        'status': 'SUCCESS'
    }


# Extract selected features from overview for operator-target combination
def get_selected_features(df_overview: pd.DataFrame, operator: str, target: str) -> list:
    row = df_overview[
        (df_overview['operator'] == operator) & (df_overview['target'] == target)
    ]

    if row.empty:
        return []

    features_str = row.iloc[0]['final_features']

    if pd.isna(features_str) or features_str.strip() == '':
        return []

    return [f.strip() for f in features_str.split(',')]


# Prepare features and target from training dataframe
def prepare_training_data(df: pd.DataFrame, features: list, target: str) -> tuple:
    available_features = [f for f in features if f in df.columns]

    if not available_features:
        return pd.DataFrame(), pd.Series()

    X = df[available_features]
    y = df[TARGET_NAME_MAP[target]]

    return X, y


# Create and train SVM pipeline with scaling
def create_and_train_pipeline(X: pd.DataFrame, y: pd.Series) -> Pipeline:
    pipeline = Pipeline([
        ('scaler', MaxAbsScaler()),
        ('model', NuSVR(**SVM_PARAMS))
    ])

    pipeline.fit(X, y)

    return pipeline


# Save trained model pipeline to disk
def save_model(pipeline: Pipeline, operator: str, target: str, output_dir: str) -> None:
    model_dir = Path(output_dir) / target / operator
    model_dir.mkdir(parents=True, exist_ok=True)

    model_file = model_dir / 'model.pkl'
    joblib.dump(pipeline, model_file)


# Export training summary to CSV
def export_training_summary(results: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(results)
    df.to_csv(output_path / 'training_summary.csv', sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("training_file", help="Path to Training.csv (full training data)")
    parser.add_argument("overview_file", help="Path to two_step_evaluation_overview.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for trained models")
    args = parser.parse_args()

    train_final_operators(args.training_file, args.overview_file, args.output_dir)
