#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))


# ORCHESTRATOR
def show_example_instances(dataset_base_dir: str, pattern_hash: str, output_dir: str) -> None:
    pattern_dir = Path(dataset_base_dir) / pattern_hash
    training_file = pattern_dir / 'training.csv'

    if not training_file.exists():
        return

    df = load_training_data(training_file)
    examples = extract_example_instances(df)
    export_examples_report(examples, pattern_hash, output_dir)


# FUNCTIONS

# Load training pattern dataset
def load_training_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')

# Extract example instances with different operator counts
def extract_example_instances(df: pd.DataFrame) -> dict:
    operator_counts = df.groupby('query_file').size()

    examples_by_count = {}

    for count in sorted(operator_counts.unique()):
        queries_with_count = operator_counts[operator_counts == count].index.tolist()

        num_examples = min(2, len(queries_with_count))
        selected_queries = queries_with_count[:num_examples]

        examples_by_count[count] = []
        for query in selected_queries:
            query_data = df[df['query_file'] == query]
            examples_by_count[count].append({
                'query_file': query,
                'data': query_data
            })

    return examples_by_count

# Export examples report to markdown
def export_examples_report(examples: dict, pattern_hash: str, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    report_file = output_path / f'A_01g_example_instances_{pattern_hash}.md'

    with open(report_file, 'w') as f:
        f.write(f'# Example Pattern Instances - `{pattern_hash}`\n\n')
        f.write('Showing example instances with different operator counts.\n\n')

        for count in sorted(examples.keys()):
            f.write(f'## Instances with {count} Operators\n\n')

            for idx, example in enumerate(examples[count], 1):
                query_file = example['query_file']
                data = example['data']

                f.write(f'### Example {idx}: `{query_file}`\n\n')
                f.write(f'**Total rows:** {len(data)}\n\n')

                f.write('| Row | node_id | node_type | depth | parent_relationship |\n')
                f.write('|-----|---------|-----------|-------|---------------------|\n')

                for _, row in data.iterrows():
                    parent_rel = row['parent_relationship'] if pd.notna(row['parent_relationship']) else 'None'
                    f.write(f'| {_+1} | {row["node_id"]} | {row["node_type"]} | {row["depth"]} | {parent_rel} |\n')

                f.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_base_dir", help="Base directory containing pattern subdirectories")
    parser.add_argument("pattern_hash", help="Pattern hash to analyze")
    parser.add_argument("--output-dir", required=True, help="Output directory for markdown report")
    args = parser.parse_args()

    show_example_instances(args.dataset_base_dir, args.pattern_hash, args.output_dir)
