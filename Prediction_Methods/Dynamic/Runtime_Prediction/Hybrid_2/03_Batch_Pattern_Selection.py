#!/usr/bin/env python3

# INFRASTRUCTURE
import subprocess
import argparse
from pathlib import Path
from multiprocessing import Pool

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
STRATEGIES = ['size', 'frequency', 'error']

SCRIPT_DIR = Path(__file__).resolve().parent
DYNAMIC_DIR = SCRIPT_DIR.parent.parent

DATASET_HYBRID_2 = DYNAMIC_DIR / 'Dataset' / 'Dataset_Hybrid_2' / 'Training_Training'
OPERATOR_LEVEL_DIR = SCRIPT_DIR.parent / 'Operator_Level'
GLOBAL_PATTERNS = DYNAMIC_DIR.parent / 'Hybrid_1' / 'Data_Generation' / 'csv' / '01_patterns_20251217_152241.csv'


# ORCHESTRATOR
def batch_pattern_selection(templates: list, epsilon: float, max_iteration: int) -> None:
    tasks = [(t, epsilon, max_iteration) for t in templates]
    with Pool(14) as pool:
        pool.map(process_template, tasks)


# FUNCTIONS

# Process single template
def process_template(task: tuple) -> None:
    template, epsilon, max_iteration = task
    print(f"\n{'='*60}")
    print(f"Processing {template}...")
    print(f"{'='*60}")

    output_dir = SCRIPT_DIR / 'Selected_Patterns' / template
    output_dir.mkdir(exist_ok=True, parents=True)

    run_extract_test_patterns(template, output_dir)
    run_order_patterns(template, output_dir)

    for strategy in STRATEGIES:
        run_pattern_selection(template, strategy, output_dir, epsilon, max_iteration)


# Extract pattern occurrences in Training_Test
def run_extract_test_patterns(template: str, output_dir: Path) -> None:
    print(f"  [1/4] Extracting test patterns...")
    test_file = DATASET_HYBRID_2 / template / 'Training_Test.csv'

    subprocess.run([
        'python3', str(SCRIPT_DIR / '06_Extract_Test_Patterns.py'),
        str(test_file),
        str(GLOBAL_PATTERNS),
        '--output-dir', str(output_dir)
    ], check=True)


# Order patterns by size/frequency
def run_order_patterns(template: str, output_dir: Path) -> None:
    print(f"  [2/4] Ordering patterns...")
    occurrences_file = output_dir / '06_test_pattern_occurrences.csv'

    operator_predictions = OPERATOR_LEVEL_DIR / template / 'predictions.csv'

    subprocess.run([
        'python3', str(SCRIPT_DIR / '07_Order_Patterns.py'),
        str(occurrences_file),
        '--operator-predictions', str(operator_predictions),
        '--output-dir', str(output_dir)
    ], check=True)


# Run greedy pattern selection
def run_pattern_selection(template: str, strategy: str, output_dir: Path, epsilon: float, max_iteration: int) -> None:
    print(f"  [{STRATEGIES.index(strategy)+3}/4] Running pattern selection ({strategy}/Epsilon)...")

    strategy_output = output_dir / strategy.capitalize() / 'Epsilon'
    strategy_output.mkdir(exist_ok=True, parents=True)

    if strategy == 'error':
        sorted_patterns = output_dir / '07_patterns_by_frequency.csv'
    else:
        sorted_patterns = output_dir / f'07_patterns_by_{strategy}.csv'

    training_file = DATASET_HYBRID_2 / template / 'Training_Training.csv'
    test_file = DATASET_HYBRID_2 / template / 'Training_Test.csv'
    operator_model_dir = SCRIPT_DIR / 'Model' / 'Training_Training' / template / 'Operator'
    operator_ffs_dir = OPERATOR_LEVEL_DIR / template / 'SVM'
    pretrained_dir = SCRIPT_DIR / 'Model' / 'Training_Training' / template / 'Pattern'
    occurrences_file = output_dir / '06_test_pattern_occurrences.csv'

    cmd = [
        'python3', str(SCRIPT_DIR / '10_Pattern_Selection' / '10_Pattern_Selection.py'),
        '--strategy', strategy,
        str(sorted_patterns),
        str(training_file),
        str(test_file),
        str(operator_model_dir),
        str(operator_ffs_dir),
        '--pattern-output-dir', str(strategy_output),
        '--pretrained-dir', str(pretrained_dir),
        '--pattern-occurrences-file', str(occurrences_file),
        '--epsilon', str(epsilon)
    ]

    if max_iteration:
        cmd.extend(['--max-iteration', str(max_iteration)])

    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--templates", nargs="+", default=TEMPLATES, help="Templates to process")
    parser.add_argument("--epsilon", type=float, default=0.005, help="Min MRE improvement (default: 0.005)")
    parser.add_argument("--max-iteration", type=int, default=150, help="Max iterations (default: 150)")
    args = parser.parse_args()

    batch_pattern_selection(args.templates, args.epsilon, args.max_iteration)
