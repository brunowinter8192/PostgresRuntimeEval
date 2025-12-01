#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import json
import pandas as pd
import joblib

# From mapping_config.py: Configuration constants
from mapping_config import TARGET_TYPES


# FUNCTIONS

# Save models
def save_models(output_dir: str, query_file: str, operator_models: dict, pattern_models: dict) -> None:
    models_dir = Path(output_dir) / 'models' / query_file

    for target_type in TARGET_TYPES:
        for op_name, model_info in operator_models[target_type].items():
            op_dir = models_dir / 'operators' / op_name
            op_dir.mkdir(parents=True, exist_ok=True)
            joblib.dump(model_info['model'], op_dir / f'model_{target_type}.pkl')

    for pattern_hash, model_info in pattern_models.items():
        pattern_dir = models_dir / 'patterns' / pattern_hash
        pattern_dir.mkdir(parents=True, exist_ok=True)
        joblib.dump(model_info['execution_time'], pattern_dir / 'model_execution_time.pkl')
        joblib.dump(model_info['start_time'], pattern_dir / 'model_start_time.pkl')
        with open(pattern_dir / 'features.json', 'w') as f:
            json.dump({'features': model_info['features']}, f)


# Save CSV outputs
def save_csv_outputs(output_dir: str, query_file: str, selection_log: list, predictions: list) -> None:
    csv_dir = Path(output_dir) / 'csv'
    csv_dir.mkdir(parents=True, exist_ok=True)

    pd.DataFrame(selection_log).to_csv(csv_dir / f'selection_log_{query_file}.csv', sep=';', index=False)
    pd.DataFrame(predictions).to_csv(csv_dir / f'predictions_{query_file}.csv', sep=';', index=False)
