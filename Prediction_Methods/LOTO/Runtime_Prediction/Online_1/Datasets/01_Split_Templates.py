# INFRASTRUCTURE
import pandas as pd
from pathlib import Path
import argparse

# ORCHESTRATOR

# Process 13-out-of-14 template split for all templates
def main_workflow(input_file: str, output_base_dir: str) -> None:
    df = load_data(input_file)
    df['template'] = df['query_file'].apply(extract_template)
    process_all_templates(df, output_base_dir)

# FUNCTIONS

# Extract template name from query_file
def extract_template(query_file: str) -> str:
    return query_file.split('_')[0]

# Load data from CSV with semicolon delimiter
def load_data(input_file: str) -> pd.DataFrame:
    return pd.read_csv(input_file, delimiter=';')

# Create train and test split for given template
def create_split_for_template(df: pd.DataFrame, test_template: str) -> tuple:
    test_df = df[df['template'] == test_template].copy()
    train_df = df[df['template'] != test_template].copy()
    return train_df, test_df

# Export split to subdirectory
def export_split(train_df: pd.DataFrame, test_df: pd.DataFrame, output_dir: Path, template_name: str) -> None:
    template_dir = output_dir / template_name
    template_dir.mkdir(parents=True, exist_ok=True)

    train_df.drop(columns=['template']).to_csv(
        template_dir / 'training_cleaned.csv',
        sep=';',
        index=False
    )
    test_df.drop(columns=['template']).to_csv(
        template_dir / 'test_cleaned.csv',
        sep=';',
        index=False
    )

# Process all templates and create splits
def process_all_templates(df: pd.DataFrame, output_base_dir: str) -> None:
    output_dir = Path(output_base_dir)
    templates = sorted(df['template'].unique())

    for template in templates:
        train_df, test_df = create_split_for_template(df, template)
        export_split(train_df, test_df, output_dir, template)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input CSV file (02_operator_dataset_cleaned.csv)")
    parser.add_argument("--output-dir", required=True, help="Output base directory (Baseline/)")

    args = parser.parse_args()
    main_workflow(args.input, args.output_dir)
