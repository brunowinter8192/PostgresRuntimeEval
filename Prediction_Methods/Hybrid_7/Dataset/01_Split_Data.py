# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

RANDOM_SEED = 42
TRAIN_TEST_RATIO = 0.8
TRAIN_TRAIN_RATIO = 0.8

# ORCHESTRATOR

def split_workflow(input_path: Path, output_dir: Path) -> None:
    df = load_data(input_path)
    queries = get_unique_queries(df)
    train_queries, test_queries = split_queries(queries, TRAIN_TEST_RATIO)
    train_train_queries, train_test_queries = split_queries(train_queries, TRAIN_TRAIN_RATIO)
    export_split(df, train_queries, output_dir / "Training.csv")
    export_split(df, test_queries, output_dir / "Test.csv")
    export_split(df, train_train_queries, output_dir / "Training_Training.csv")
    export_split(df, train_test_queries, output_dir / "Training_Test.csv")

# FUNCTIONS

# Load operator dataset with semicolon delimiter
def load_data(input_path: Path) -> pd.DataFrame:
    return pd.read_csv(input_path, delimiter=';')

# Extract unique query identifiers
def get_unique_queries(df: pd.DataFrame) -> list:
    return df['query_file'].unique().tolist()

# Split queries into two sets based on ratio
def split_queries(queries: list, ratio: float) -> tuple:
    return train_test_split(queries, train_size=ratio, random_state=RANDOM_SEED)

# Export rows belonging to specified queries
def export_split(df: pd.DataFrame, queries: list, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df[df['query_file'].isin(queries)].to_csv(output_path, sep=';', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to 02_operator_dataset_with_children.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory for split files")
    args = parser.parse_args()

    split_workflow(Path(args.input), Path(args.output_dir))
