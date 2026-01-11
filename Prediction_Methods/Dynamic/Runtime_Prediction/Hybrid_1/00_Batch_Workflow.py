# INFRASTRUCTURE
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


# ORCHESTRATOR
def batch_workflow():
    run_pretrain()
    run_predict()


# FUNCTIONS

# Train pattern models for all templates (operators come from Operator_Level)
def run_pretrain() -> None:
    print("02_Pretrain_Models...")
    subprocess.run([
        'python3', str(SCRIPT_DIR / '02_Pretrain_Models.py')
    ], check=True)


# Run hybrid prediction for all templates
def run_predict() -> None:
    print("03_Predict...")
    subprocess.run([
        'python3', str(SCRIPT_DIR / '03_Predict.py')
    ], check=True)


if __name__ == "__main__":
    batch_workflow()
