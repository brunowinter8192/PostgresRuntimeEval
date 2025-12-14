#!/usr/bin/env python3

# INFRASTRUCTURE
import subprocess
from pathlib import Path
from multiprocessing import Pool

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
APPROACHES = ['approach_3']

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = SCRIPT_DIR.parent.parent.parent / 'Hybrid_1' / 'Runtime_Prediction'
DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Hybrid_1'
OPERATOR_DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Operator'
OPERATOR_MODELS_DIR = SCRIPT_DIR.parent / 'Operator_Level'
OUTPUT_DIR = SCRIPT_DIR


# ORCHESTRATOR
def batch_hybrid_prediction() -> None:
    tasks = [(template, approach) for template in TEMPLATES for approach in APPROACHES]
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

    run_ffs(pattern_dataset, template_output, pattern_filter)
    run_train(pattern_dataset, template_output, pattern_filter)
    link_operator_models(template, template_output)
    run_predict(template, approach, pattern_dataset, template_output)


# Run forward feature selection for patterns
def run_ffs(pattern_dataset: Path, output_dir: Path, pattern_filter: Path) -> None:
    cmd = [
        'python3', str(SCRIPTS_DIR / '01_Feature_Selection.py'),
        str(pattern_dataset),
        '--output-dir', str(output_dir)
    ]
    if pattern_filter.exists():
        cmd.extend(['--pattern-filter', str(pattern_filter)])
    subprocess.run(cmd, check=True)


# Train pattern SVM models
def run_train(pattern_dataset: Path, output_dir: Path, pattern_filter: Path) -> None:
    cmd = [
        'python3', str(SCRIPTS_DIR / '02_Train_Models.py'),
        str(pattern_dataset),
        str(output_dir / 'SVM' / 'two_step_evaluation_overview.csv'),
        '--output-dir', str(output_dir)
    ]
    if pattern_filter.exists():
        cmd.extend(['--pattern-filter', str(pattern_filter)])
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


# Run hybrid prediction
def run_predict(template: str, approach: str, pattern_dataset: Path, output_dir: Path) -> None:
    test_file = OPERATOR_DATASET_DIR / template / 'test.csv'
    patterns_csv = pattern_dataset / 'patterns.csv'

    patterns_filtered = pattern_dataset / 'patterns_filtered.csv'
    if patterns_filtered.exists():
        patterns_csv = patterns_filtered

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
    batch_hybrid_prediction()
