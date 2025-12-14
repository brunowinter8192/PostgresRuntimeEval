# INFRASTRUCTURE
import argparse
from pathlib import Path

import pandas as pd


# ORCHESTRATOR
def verify_workflow(baseline_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    training_df = load_data(baseline_dir / "Training.csv")
    test_df = load_data(baseline_dir / "Test.csv")
    train_train_df = load_data(baseline_dir / "Training_Training.csv")
    train_test_df = load_data(baseline_dir / "Training_Test.csv")
    main_split = build_comparison(training_df, test_df, "Training", "Test")
    sub_split = build_comparison(train_train_df, train_test_df, "Training_Training", "Training_Test")
    export_results(main_split, output_dir / "01c_main_split_verification.csv")
    export_results(sub_split, output_dir / "01c_sub_split_verification.csv")


# FUNCTIONS

# Load dataset with semicolon delimiter
def load_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, delimiter=';')


# Count unique queries per template
def count_queries_per_template(df: pd.DataFrame) -> pd.Series:
    return df.groupby('template')['query_file'].nunique()


# Build comparison dataframe for two splits
def build_comparison(df1: pd.DataFrame, df2: pd.DataFrame, name1: str, name2: str) -> pd.DataFrame:
    counts1 = count_queries_per_template(df1)
    counts2 = count_queries_per_template(df2)
    result = pd.DataFrame({
        'template': counts1.index,
        name1: counts1.values,
        name2: counts2.values
    })
    result['total'] = result[name1] + result[name2]
    return result


# Export results to CSV
def export_results(df: pd.DataFrame, path: Path) -> None:
    df.to_csv(path, sep=';', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline_dir", help="Path to Baseline directory with split files")
    parser.add_argument("--output-dir", required=True, help="Output directory for verification CSVs")
    args = parser.parse_args()

    verify_workflow(Path(args.baseline_dir), Path(args.output_dir))
