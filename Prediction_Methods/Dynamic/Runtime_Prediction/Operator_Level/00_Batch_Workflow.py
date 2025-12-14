# INFRASTRUCTURE
import subprocess
from pathlib import Path

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = SCRIPT_DIR.parent.parent.parent / 'Operator_Level' / 'Runtime_Prediction'
DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Operator'
OUTPUT_DIR = SCRIPT_DIR


# ORCHESTRATOR
def batch_workflow():
    for template in TEMPLATES:
        print(f"{template}...")
        run_ffs(template)
        run_train(template)
        run_predict(template)


# FUNCTIONS
# Run forward feature selection for template (uses local copy for LOTO compatibility)
def run_ffs(template: str) -> None:
    subprocess.run([
        'python3', str(SCRIPT_DIR / '01_Forward_Selection.py'),
        str(DATASET_DIR / template),
        '--output-dir', str(OUTPUT_DIR / template)
    ], check=True)


# Train SVM models for template
def run_train(template: str) -> None:
    subprocess.run([
        'python3', str(SCRIPTS_DIR / '02_Train_Models.py'),
        str(DATASET_DIR / template),
        str(OUTPUT_DIR / template / 'SVM' / 'two_step_evaluation_overview.csv'),
        '--output-dir', str(OUTPUT_DIR / template)
    ], check=True)


# Run bottom-up prediction for template
def run_predict(template: str) -> None:
    subprocess.run([
        'python3', str(SCRIPTS_DIR / '03_Query_Prediction.py'),
        str(DATASET_DIR / template / 'test.csv'),
        str(OUTPUT_DIR / template / 'SVM' / 'two_step_evaluation_overview.csv'),
        str(OUTPUT_DIR / template / 'Model'),
        '--output-file', str(OUTPUT_DIR / template / 'predictions.csv')
    ], check=True)


if __name__ == "__main__":
    batch_workflow()
