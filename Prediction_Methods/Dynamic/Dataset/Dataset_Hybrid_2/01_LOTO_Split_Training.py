#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
RANDOM_SEED = 42
TRAIN_TRAIN_RATIO = 0.8


# ORCHESTRATOR
def loto_split_workflow(input_dir: Path, output_dir: Path) -> None:
    for template in TEMPLATES:
        training_file = input_dir / template / 'training.csv'
        if not training_file.exists():
            continue
        create_train_splits(training_file, template, output_dir)


# FUNCTIONS
# Load training dataset with semicolon delimiter
def load_data(input_path: Path) -> pd.DataFrame:
    return pd.read_csv(input_path, delimiter=';')


# Split training into Training_Training (80%) and Training_Test (20%)
def create_train_splits(training_file: Path, template: str, output_dir: Path) -> None:
    df = load_data(training_file)
    df = add_template_column(df)
    train_train_queries, train_test_queries = split_queries_by_template(df)

    template_dir = output_dir / template
    template_dir.mkdir(parents=True, exist_ok=True)

    export_split(df, train_train_queries, template_dir / 'Training_Training.csv')
    export_split(df, train_test_queries, template_dir / 'Training_Test.csv')


# Extract template from query_file and add as column
def add_template_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['template'] = df['query_file'].str.extract(r'(Q\d+)_')[0]
    return df


# Split queries stratified by template (80/20)
def split_queries_by_template(df: pd.DataFrame) -> tuple[list, list]:
    train_queries = []
    test_queries = []

    for tmpl in sorted(df['template'].unique()):
        template_queries = df[df['template'] == tmpl]['query_file'].unique().tolist()
        train_q, test_q = train_test_split(
            template_queries,
            train_size=TRAIN_TRAIN_RATIO,
            random_state=RANDOM_SEED,
            shuffle=True
        )
        train_queries.extend(train_q)
        test_queries.extend(test_q)

    return train_queries, test_queries


# Export rows belonging to specified queries
def export_split(df: pd.DataFrame, queries: list, output_path: Path) -> None:
    df[df['query_file'].isin(queries)].drop(columns=['template']).to_csv(
        output_path, sep=';', index=False
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True, help="Path to Dataset_Operator with Qx/ folders")
    parser.add_argument("--output-dir", required=True, help="Output directory for Hybrid_2 splits")

    args = parser.parse_args()

    loto_split_workflow(Path(args.input_dir), Path(args.output_dir))
