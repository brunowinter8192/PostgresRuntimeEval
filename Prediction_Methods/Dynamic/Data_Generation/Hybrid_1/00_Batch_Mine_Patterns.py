#!/usr/bin/env python3

# INFRASTRUCTURE
import subprocess
from pathlib import Path
from multiprocessing import Pool

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = SCRIPT_DIR.parent.parent.parent / 'Hybrid_1' / 'Data_Generation'
DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Operator'
OUTPUT_DIR = SCRIPT_DIR


# ORCHESTRATOR
def batch_mine_patterns() -> None:
    with Pool(14) as pool:
        pool.map(mine_template, TEMPLATES)


# FUNCTIONS
# Mine patterns for single template
def mine_template(template: str) -> None:
    print(f"{template}...")
    template_output = OUTPUT_DIR / template
    template_output.mkdir(exist_ok=True, parents=True)

    subprocess.run([
        'python3', str(SCRIPTS_DIR / '01_Find_Patterns.py'),
        str(DATASET_DIR / template / 'training.csv'),
        '--output-dir', str(template_output)
    ], check=True)


if __name__ == "__main__":
    batch_mine_patterns()
