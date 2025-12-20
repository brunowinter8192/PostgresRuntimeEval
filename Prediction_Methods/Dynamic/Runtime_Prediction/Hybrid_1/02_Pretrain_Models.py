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
OPERATOR_MODELS_DIR = SCRIPT_DIR.parent / 'Operator_Level'
OUTPUT_DIR = SCRIPT_DIR


# ORCHESTRATOR
def batch_pretrain(templates: list, approaches: list) -> None:
    tasks = [(template, approach) for template in templates for approach in approaches]
    with Pool(6) as pool:
        pool.map(process_task, tasks)


# FUNCTIONS

# Process single template-approach combination
def process_task(task: tuple) -> None:
    template, approach = task
    print(f"{template}/{approach}...")

    template_output = OUTPUT_DIR / template / approach
    template_output.mkdir(exist_ok=True, parents=True)

    pattern_dataset = DATASET_DIR / template / approach
    pattern_filter = pattern_dataset / 'used_patterns.csv'

    if not pattern_filter.exists():
        print(f"  Skipping: no used_patterns.csv")
        return

    run_ffs(pattern_dataset, template_output, pattern_filter)
    run_train(pattern_dataset, template_output, pattern_filter)
    link_operator_models(template, template_output)


# Run forward feature selection for patterns
def run_ffs(pattern_dataset: Path, output_dir: Path, pattern_filter: Path) -> None:
    cmd = [
        'python3', str(SCRIPTS_DIR / '01_Feature_Selection.py'),
        str(pattern_dataset),
        '--output-dir', str(output_dir),
        '--pattern-filter', str(pattern_filter)
    ]
    subprocess.run(cmd, check=True)


# Train pattern SVM models
def run_train(pattern_dataset: Path, output_dir: Path, pattern_filter: Path) -> None:
    cmd = [
        'python3', str(SCRIPTS_DIR / '02_Train_Models.py'),
        str(pattern_dataset),
        str(output_dir / 'SVM' / 'two_step_evaluation_overview.csv'),
        '--output-dir', str(output_dir),
        '--pattern-filter', str(pattern_filter)
    ]
    subprocess.run(cmd, check=True)


# Create symlinks to operator models from Operator_Level
def link_operator_models(template: str, output_dir: Path) -> None:
    operator_src = OPERATOR_MODELS_DIR / template / 'Model'
    operators_dst = output_dir / 'Model' / 'Operators'

    if operators_dst.exists():
        return

    operators_dst.mkdir(parents=True, exist_ok=True)

    for target in ['execution_time', 'start_time']:
        target_dst = operators_dst / target / 'operators'
        target_dst.mkdir(parents=True, exist_ok=True)

        target_src = operator_src / target
        if not target_src.exists():
            continue

        for op_dir in target_src.iterdir():
            if op_dir.is_dir():
                link = target_dst / op_dir.name
                if not link.exists():
                    link.symlink_to(op_dir.resolve())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--templates", nargs="+", default=ALL_TEMPLATES, help="Templates to process")
    parser.add_argument("--approaches", nargs="+", default=ALL_APPROACHES, help="Approaches to process")
    args = parser.parse_args()
    batch_pretrain(args.templates, args.approaches)
