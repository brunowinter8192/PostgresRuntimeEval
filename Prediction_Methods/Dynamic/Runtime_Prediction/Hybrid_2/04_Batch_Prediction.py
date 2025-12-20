#!/usr/bin/env python3

# INFRASTRUCTURE

import subprocess
from pathlib import Path
from multiprocessing import Pool

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
STRATEGIES = ['Size', 'Frequency', 'Error']

SCRIPT_DIR = Path(__file__).resolve().parent
DYNAMIC_DIR = SCRIPT_DIR.parent.parent


# ORCHESTRATOR

# Run prediction for all template/strategy combinations
def batch_prediction() -> None:
    tasks = [(t, s) for t in TEMPLATES for s in STRATEGIES]
    with Pool(14) as pool:
        pool.starmap(run_prediction, tasks)


# FUNCTIONS

# Run prediction for single template/strategy combination
def run_prediction(template: str, strategy: str) -> None:
    test_file = DYNAMIC_DIR / 'Dataset' / 'Dataset_Operator' / template / 'test.csv'
    operator_model_dir = SCRIPT_DIR / 'Model' / 'Training' / template / 'Operator'
    # Empty path triggers mapping_config fallback in io.py
    operator_overview = ''
    pattern_model_dir = SCRIPT_DIR / 'Model' / 'Training' / template / 'Pattern'
    selected_patterns = SCRIPT_DIR / 'Selected_Patterns' / template / strategy / 'Epsilon' / 'selected_patterns.csv'

    # Error strategy uses size ordering as fallback
    meta_strategy = 'size' if strategy.lower() == 'error' else strategy.lower()
    pattern_metadata = SCRIPT_DIR / 'Selected_Patterns' / template / f'07_patterns_by_{meta_strategy}.csv'

    output_dir = SCRIPT_DIR / 'Evaluation' / template / strategy

    subprocess.run([
        'python3', str(SCRIPT_DIR / '12_Query_Prediction' / '12_Query_Prediction.py'),
        str(test_file),
        str(operator_model_dir),
        str(operator_overview),
        '--strategy', strategy.lower(),
        '--pattern-model-dir', str(pattern_model_dir),
        '--selected-patterns', str(selected_patterns),
        '--pattern-metadata', str(pattern_metadata),
        '--output-dir', str(output_dir)
    ], check=True, cwd=str(SCRIPT_DIR))


if __name__ == "__main__":
    batch_prediction()
