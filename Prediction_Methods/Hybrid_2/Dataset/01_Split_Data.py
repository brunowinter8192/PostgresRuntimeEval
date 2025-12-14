# INFRASTRUCTURE
import argparse
import shutil
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

RANDOM_SEED = 42
TRAIN_TRAIN_SIZE = 96
TRAIN_TEST_SIZE = 24


# ORCHESTRATOR
def split_workflow(training_path: Path, test_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    copy_file(test_path, output_dir / "Test.csv")
    copy_file(training_path, output_dir / "Training.csv")
    df = load_data(training_path)
    train_train_queries, train_test_queries = split_queries_by_template(df, TRAIN_TRAIN_SIZE, TRAIN_TEST_SIZE)
    export_split(df, train_train_queries, output_dir / "Training_Training.csv")
    export_split(df, train_test_queries, output_dir / "Training_Test.csv")


# FUNCTIONS

# Copy source file to destination
def copy_file(src: Path, dst: Path) -> None:
    shutil.copy(src, dst)


# Load dataset with semicolon delimiter
def load_data(input_path: Path) -> pd.DataFrame:
    return pd.read_csv(input_path, delimiter=';')


# Split queries stratified by template
def split_queries_by_template(df: pd.DataFrame, train_size: int, test_size: int) -> tuple[list, list]:
    train_queries = []
    test_queries = []

    for template in sorted(df['template'].unique()):
        template_queries = df[df['template'] == template]['query_file'].unique().tolist()
        train_q, test_q = train_test_split(
            template_queries,
            train_size=train_size,
            test_size=test_size,
            random_state=RANDOM_SEED,
            shuffle=True
        )
        train_queries.extend(train_q)
        test_queries.extend(test_q)

    return train_queries, test_queries


# Export rows belonging to specified queries
def export_split(df: pd.DataFrame, queries: list, output_path: Path) -> None:
    df[df['query_file'].isin(queries)].to_csv(output_path, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("training_csv", help="Path to Hybrid_1 training.csv")
    parser.add_argument("test_csv", help="Path to Hybrid_1 test.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for split files")
    args = parser.parse_args()

    split_workflow(Path(args.training_csv), Path(args.test_csv), Path(args.output_dir))
