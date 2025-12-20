#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import subprocess
from pathlib import Path
from multiprocessing import Pool

ALL_TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
ALL_APPROACHES = ['approach_3', 'approach_4']

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = SCRIPT_DIR.parent.parent.parent / 'Hybrid_1' / 'Runtime_Prediction'
DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Hybrid_1'
OPERATOR_DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Operator'
OPERATOR_MODELS_DIR = SCRIPT_DIR.parent / 'Operator_Level'
OUTPUT_DIR = SCRIPT_DIR


# ORCHESTRATOR
def batch_predict(templates: list, approaches: list) -> None:
    tasks = [(template, approach) for template in templates for approach in approaches]
    with Pool(6) as pool:
        pool.map(process_task, tasks)


# FUNCTIONS

# Process single template-approach combination
def process_task(task: tuple) -> None:
    template, approach = task
    print(f"{template}/{approach}...")

    template_output = OUTPUT_DIR / template / approach
    pattern_dataset = DATASET_DIR / template / approach

    model_dir = template_output / 'Model'
    if not model_dir.exists():
        print(f"  Skipping: no Model/ directory (run 02_Pretrain_Models.py first)")
        return

    run_predict(template, approach, pattern_dataset, template_output)


# Run hybrid prediction
def run_predict(template: str, approach: str, pattern_dataset: Path, output_dir: Path) -> None:
    test_file = OPERATOR_DATASET_DIR / template / 'test.csv'

    # Use used_patterns.csv for pattern matching (same as training)
    patterns_csv = pattern_dataset / 'used_patterns.csv'
    if not patterns_csv.exists():
        patterns_csv = pattern_dataset / 'patterns_filtered.csv'
    if not patterns_csv.exists():
        patterns_csv = pattern_dataset / 'patterns.csv'

    pattern_overview = output_dir / 'SVM' / 'two_step_evaluation_overview.csv'
    operator_overview = OPERATOR_MODELS_DIR / template / 'SVM' / 'two_step_evaluation_overview.csv'
    model_dir = output_dir / 'Model'

    subprocess.run([
        'python3', str(SCRIPTS_DIR / '03_Predict_Queries' / '03_Predict_Queries.py'),
        str(test_file),
        str(patterns_csv),
        str(pattern_overview),
        str(operator_overview),
        str(model_dir),
        '--output-dir', str(output_dir)
    ], check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--templates", nargs="+", default=ALL_TEMPLATES, help="Templates to process")
    parser.add_argument("--approaches", nargs="+", default=ALL_APPROACHES, help="Approaches to process")
    args = parser.parse_args()
    batch_predict(args.templates, args.approaches)
