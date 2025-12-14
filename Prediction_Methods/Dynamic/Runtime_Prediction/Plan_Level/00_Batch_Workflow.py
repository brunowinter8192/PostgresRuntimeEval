#!/usr/bin/env python3

# INFRASTRUCTURE
import subprocess
from pathlib import Path

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']

SCRIPT_DIR = Path(__file__).resolve().parent
PLAN_LEVEL_1_SCRIPTS = SCRIPT_DIR.parent.parent.parent / 'Plan_Level_1' / 'Runtime_Prediction'
DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Plan'
OUTPUT_DIR = SCRIPT_DIR


# ORCHESTRATOR
def batch_workflow():
    for template in TEMPLATES:
        print(f"{template}...")
        run_ffs(template)
        run_train(template)


# FUNCTIONS
# Run forward feature selection for template
def run_ffs(template: str) -> None:
    subprocess.run([
        'python3', str(PLAN_LEVEL_1_SCRIPTS / '01_Forward_Selection.py'),
        str(DATASET_DIR / template / 'training.csv'),
        '--model', 'svm',
        '--output-dir', str(OUTPUT_DIR / template / 'SVM')
    ], check=True)


# Train SVM model and predict on test set
def run_train(template: str) -> None:
    subprocess.run([
        'python3', str(PLAN_LEVEL_1_SCRIPTS / '02_Train_Model.py'),
        str(DATASET_DIR / template / 'training.csv'),
        str(DATASET_DIR / template / 'test.csv'),
        '--model', 'svm',
        '--ffs-csv', str(OUTPUT_DIR / template / 'SVM' / '01_ffs_summary.csv'),
        '--output-dir', str(OUTPUT_DIR / template)
    ], check=True)


if __name__ == "__main__":
    batch_workflow()
