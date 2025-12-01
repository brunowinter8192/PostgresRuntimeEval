# INFRASTRUCTURE

import argparse
from pathlib import Path
from collections import defaultdict
import pandas as pd

CHILD_FEATURES = ['st1', 'rt1', 'st2', 'rt2', 'nt1', 'nt2']

# ORCHESTRATOR

def analysis_workflow(svm_base_dir: Path, output_dir: Path) -> None:
    missing_data = collect_missing_features(svm_base_dir)
    report = generate_report(missing_data)
    export_report(report, output_dir)

# FUNCTIONS

# Collect missing child features from all two_step_evaluation_overview.csv files
def collect_missing_features(svm_base_dir: Path) -> dict:
    missing_by_operator = defaultdict(lambda: defaultdict(list))

    for template_dir in sorted(svm_base_dir.iterdir()):
        if not template_dir.is_dir() or not template_dir.name.startswith('Q'):
            continue

        overview_file = template_dir / 'two_step_evaluation_overview.csv'
        if not overview_file.exists():
            continue

        template = template_dir.name
        df = pd.read_csv(overview_file, delimiter=';')

        for _, row in df.iterrows():
            operator = row['operator']
            target = row['target']
            final_features = set(f.strip() for f in row['final_features'].split(','))

            missing = [f for f in CHILD_FEATURES if f not in final_features]
            if missing:
                missing_by_operator[operator][(target, template)] = missing

    return missing_by_operator

# Generate markdown report
def generate_report(missing_data: dict) -> str:
    lines = ['# Missing Child Features Analysis', '']
    lines.append(f'Child features checked: {", ".join(CHILD_FEATURES)}')
    lines.append('')

    if not missing_data:
        lines.append('All operators have all child features in final_features.')
        return '\n'.join(lines)

    for operator in sorted(missing_data.keys()):
        lines.append(f'## {operator}')
        lines.append('')
        lines.append('| Target | Template | Missing Features |')
        lines.append('|--------|----------|------------------|')

        for (target, template), missing in sorted(missing_data[operator].items()):
            lines.append(f'| {target} | {template} | {", ".join(missing)} |')

        lines.append('')

    summary = generate_summary(missing_data)
    lines.extend(summary)

    return '\n'.join(lines)

# Generate summary section
def generate_summary(missing_data: dict) -> list:
    lines = ['## Summary', '']

    feature_missing_count = defaultdict(int)
    operator_missing_count = defaultdict(int)

    for operator, entries in missing_data.items():
        for (target, template), missing in entries.items():
            operator_missing_count[operator] += 1
            for feature in missing:
                feature_missing_count[feature] += 1

    lines.append('### Missing count per feature')
    lines.append('')
    for feature in CHILD_FEATURES:
        count = feature_missing_count.get(feature, 0)
        lines.append(f'- {feature}: {count} times missing')

    lines.append('')
    lines.append('### Operators with missing child features')
    lines.append('')
    for operator, count in sorted(operator_missing_count.items(), key=lambda x: -x[1]):
        lines.append(f'- {operator}: {count} entries with missing features')

    return lines

# Export report to markdown file
def export_report(report: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / 'missing_child_features.md'
    output_file.write_text(report)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("svm_base_dir", help="Base directory containing Q1/, Q3/, ... folders")
    parser.add_argument("--output-dir", required=True, help="Output directory for MD report")

    args = parser.parse_args()

    analysis_workflow(Path(args.svm_base_dir), Path(args.output_dir))
