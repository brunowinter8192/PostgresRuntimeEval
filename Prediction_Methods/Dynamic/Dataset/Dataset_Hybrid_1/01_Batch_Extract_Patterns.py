#!/usr/bin/env python3

# INFRASTRUCTURE
import subprocess
from pathlib import Path
from multiprocessing import Pool

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']

APPROACHES = {
    'approach_3': {'length': 0, 'required_operators': False, 'no_passthrough': False, 'threshold': 150},
    'approach_4': {'length': 0, 'required_operators': False, 'no_passthrough': True, 'threshold': 150},
}

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = SCRIPT_DIR.parent.parent.parent / 'Hybrid_1' / 'Datasets'
OPERATOR_DATASET_DIR = SCRIPT_DIR.parent / 'Dataset_Operator'
STATIC_PATTERNS_DIR = SCRIPT_DIR.parent.parent.parent / 'Hybrid_1' / 'Data_Generation' / 'csv'
OUTPUT_DIR = SCRIPT_DIR


# ORCHESTRATOR
def batch_extract_patterns() -> None:
    tasks = [(template, approach) for template in TEMPLATES for approach in APPROACHES.keys()]
    with Pool(14) as pool:
        pool.map(process_task, tasks)


# FUNCTIONS
# Process single template-approach combination
def process_task(task: tuple) -> None:
    template, approach = task
    print(f"{template}/{approach}...")

    approach_config = APPROACHES[approach]
    approach_dir = OUTPUT_DIR / template / approach

    run_extract(template, approach, approach_config, approach_dir)
    run_aggregate(template, approach_dir)
    run_clean(approach_dir)

    if approach_config['threshold'] > 0:
        run_filter(template, approach_dir, approach_config['threshold'])


# Extract patterns from training data
def run_extract(template: str, approach: str, config: dict, approach_dir: Path) -> None:
    cmd = [
        'python3', str(SCRIPTS_DIR / '03_Extract_Patterns.py'),
        str(OPERATOR_DATASET_DIR / template / 'training.csv'),
        '--output-dir', str(approach_dir)
    ]

    if config['length'] > 0:
        cmd.extend(['--length', str(config['length'])])
    if config['required_operators']:
        cmd.append('--required-operators')
    if config['no_passthrough']:
        cmd.append('--no-passthrough')

    subprocess.run(cmd, check=True)


# Aggregate parent+children into single rows
def run_aggregate(template: str, approach_dir: Path) -> None:
    subprocess.run([
        'python3', str(SCRIPTS_DIR / '04_Aggregate_Patterns.py'),
        str(approach_dir / 'patterns.csv'),
        str(approach_dir)
    ], check=True)


# Clean features unavailable at prediction time
def run_clean(approach_dir: Path) -> None:
    subprocess.run([
        'python3', str(SCRIPTS_DIR / '05_Clean_Patterns.py'),
        str(approach_dir)
    ], check=True)


# Filter patterns by occurrence threshold using Static pattern pool
def run_filter(template: str, approach_dir: Path, threshold: int) -> None:
    pattern_files = list(STATIC_PATTERNS_DIR.glob('01_patterns_*.csv'))
    if not pattern_files:
        return
    static_patterns = sorted(pattern_files)[-1]

    subprocess.run([
        'python3', str(SCRIPTS_DIR / '06_Filter_Patterns.py'),
        str(static_patterns),
        str(approach_dir / 'patterns.csv'),
        '--output-dir', str(approach_dir),
        '--threshold', str(threshold)
    ], check=True)


if __name__ == "__main__":
    batch_extract_patterns()
