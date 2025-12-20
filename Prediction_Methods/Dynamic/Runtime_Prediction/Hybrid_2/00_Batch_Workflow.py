#!/usr/bin/env python3

# INFRASTRUCTURE
import subprocess
from pathlib import Path
from multiprocessing import Pool

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
EPSILON = 0.005

SCRIPT_DIR = Path(__file__).resolve().parent
DYNAMIC_DIR = SCRIPT_DIR.parent.parent

# Pre-trained models from Dynamic
OPERATOR_LEVEL_DIR = SCRIPT_DIR.parent / 'Operator_Level'
HYBRID_1_DIR = SCRIPT_DIR.parent / 'Hybrid_1'

# Dataset paths
DATASET_OPERATOR = DYNAMIC_DIR / 'Dataset' / 'Dataset_Operator'
DATASET_HYBRID_2 = DYNAMIC_DIR / 'Dataset' / 'Dataset_Hybrid_2'

# Global patterns from Hybrid_1
GLOBAL_PATTERNS = DYNAMIC_DIR.parent / 'Hybrid_1' / 'Data_Generation' / 'csv' / '01_patterns_20251217_152241.csv'

OUTPUT_DIR = SCRIPT_DIR


# ORCHESTRATOR
def batch_hybrid_2_workflow() -> None:
    with Pool(14) as pool:
        pool.map(process_template, TEMPLATES)


# FUNCTIONS
# Process single template
def process_template(template: str) -> None:
    print(f"\n{'='*60}")
    print(f"Processing {template}...")
    print(f"{'='*60}")

    template_output = OUTPUT_DIR / template
    template_output.mkdir(exist_ok=True, parents=True)

    pattern_selection_dir = template_output / 'Pattern_Selection'
    pattern_selection_dir.mkdir(exist_ok=True, parents=True)

    run_extract_test_patterns(template, pattern_selection_dir)
    run_order_patterns(template, pattern_selection_dir)
    run_pattern_selection(template, pattern_selection_dir)
    run_final_prediction(template)


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


# Order patterns by size (static strategy)
def run_order_patterns(template: str, output_dir: Path) -> None:
    print(f"  [2/4] Ordering patterns...")
    occurrences_file = output_dir / '06_test_pattern_occurrences.csv'

    # Need operator predictions for avg_mre calculation
    # Use Hybrid_1's pattern predictions as baseline (simpler approach)
    # Actually: 07_Order_Patterns needs operator_predictions
    # We generate a minimal prediction for ordering purposes
    operator_predictions = generate_operator_baseline_predictions(template)

    subprocess.run([
        'python3', str(SCRIPT_DIR / '07_Order_Patterns.py'),
        str(occurrences_file),
        '--operator-predictions', str(operator_predictions),
        '--output-dir', str(output_dir)
    ], check=True)


# Generate operator baseline predictions for Training_Test
def generate_operator_baseline_predictions(template: str) -> Path:
    # Use existing predictions from Hybrid_1 or generate new ones
    # For now, use the Hybrid_1 predictions as approximation
    hybrid_1_preds = HYBRID_1_DIR / template / 'approach_4' / 'predictions.csv'
    if hybrid_1_preds.exists():
        return hybrid_1_preds

    # Fallback: would need to run 04_Query_Prediction first
    # This shouldn't happen if Hybrid_1 is complete
    raise FileNotFoundError(f"Hybrid_1 predictions not found: {hybrid_1_preds}")


# Run greedy pattern selection (Size/Epsilon)
def run_pattern_selection(template: str, pattern_selection_dir: Path) -> None:
    print(f"  [3/4] Running pattern selection (Size/Epsilon)...")

    strategy_output = pattern_selection_dir / 'Size' / 'Epsilon'
    strategy_output.mkdir(exist_ok=True, parents=True)

    sorted_patterns = pattern_selection_dir / '07_patterns_by_size.csv'
    occurrences_file = pattern_selection_dir / '06_test_pattern_occurrences.csv'
    training_file = DATASET_HYBRID_2 / template / 'Training_Training.csv'
    test_file = DATASET_HYBRID_2 / template / 'Training_Test.csv'

    # Pre-trained models from Dynamic
    operator_model_dir = OPERATOR_LEVEL_DIR / template / 'Model'
    operator_ffs_dir = OPERATOR_LEVEL_DIR / template / 'SVM'
    pattern_ffs_file = HYBRID_1_DIR / template / 'approach_4' / 'SVM' / 'two_step_evaluation_overview.csv'
    pretrained_dir = HYBRID_1_DIR / template / 'approach_4' / 'Model'

    subprocess.run([
        'python3', str(SCRIPT_DIR / '10_Pattern_Selection' / '10_Pattern_Selection.py'),
        '--strategy', 'size',
        str(sorted_patterns),
        str(pattern_ffs_file),
        str(training_file),
        str(test_file),
        str(operator_model_dir),
        str(operator_ffs_dir),
        '--pattern-output-dir', str(strategy_output),
        '--pretrained-dir', str(pretrained_dir),
        '--pattern-occurrences-file', str(occurrences_file),
        '--epsilon', str(EPSILON),
        '--report'
    ], check=True)


# Run final prediction on LOTO holdout
def run_final_prediction(template: str) -> None:
    print(f"  [4/4] Running final prediction...")

    template_output = OUTPUT_DIR / template
    eval_output = template_output / 'Evaluation'
    eval_output.mkdir(exist_ok=True, parents=True)

    test_file = DATASET_OPERATOR / template / 'test.csv'
    operator_model_dir = OPERATOR_LEVEL_DIR / template / 'Model'
    operator_overview = OPERATOR_LEVEL_DIR / template / 'SVM' / 'two_step_evaluation_overview.csv'
    pattern_model_dir = HYBRID_1_DIR / template / 'approach_4' / 'Model'
    selected_patterns = template_output / 'Pattern_Selection' / 'Size' / 'Epsilon' / 'selected_patterns.csv'
    pattern_metadata = template_output / 'Pattern_Selection' / '07_patterns_by_size.csv'

    subprocess.run([
        'python3', str(SCRIPT_DIR / '12_Query_Prediction' / '12_Query_Prediction.py'),
        str(test_file),
        str(operator_model_dir),
        str(operator_overview),
        '--strategy', 'size',
        '--pattern-model-dir', str(pattern_model_dir),
        '--selected-patterns', str(selected_patterns),
        '--pattern-metadata', str(pattern_metadata),
        '--output-dir', str(eval_output)
    ], check=True)


if __name__ == "__main__":
    batch_hybrid_2_workflow()
