#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import numpy as np
import pandas as pd

# From training.py: Model training
from .training import train_single_pattern

# From prediction.py: Query prediction
from .prediction import predict_all_queries_with_single_pattern


# FUNCTIONS

# Select patterns using online comparison (Paper Section 4)
def select_patterns_online(
    df_tt: pd.DataFrame,
    df_tv: pd.DataFrame,
    patterns: dict,
    pattern_occurrences: dict,
    initial_ranking: list,
    operator_models: dict,
    operator_predictions: list,
    report
) -> tuple:
    """
    For each pattern: Compare Operator-MRE vs Pattern-MRE.
    If Pattern better → select.
    """
    selected_patterns = set()
    pattern_models = {}
    selection_log = []

    report.add_pattern_selection_header()

    for candidate in initial_ranking:
        pattern_hash = candidate['pattern_hash']
        pattern_info = patterns[pattern_hash]
        occ_list = pattern_occurrences.get(pattern_hash, [])

        operator_mre = _calculate_mre_for_pattern(occ_list, operator_predictions)

        pattern_model = train_single_pattern(df_tt, pattern_hash, pattern_info)
        if pattern_model is None:
            raise ValueError(f"Training failed for pattern {pattern_hash}")

        pattern_predictions = predict_all_queries_with_single_pattern(
            df_tv, operator_models, pattern_model, patterns, pattern_hash
        )

        pattern_mre = _calculate_mre_for_pattern(occ_list, pattern_predictions)

        decision = 'SELECTED' if pattern_mre < operator_mre else 'NOT_SELECTED'

        if decision == 'SELECTED':
            selected_patterns.add(pattern_hash)
            pattern_models[pattern_hash] = pattern_model

        selection_log.append({
            'pattern_hash': pattern_hash,
            'pattern_string': pattern_info['pattern_string'],
            'error_score': candidate.get('error_score', 0),
            'operator_mre': operator_mre,
            'pattern_mre': pattern_mre,
            'decision': decision
        })

        report.add_pattern_comparison(pattern_hash, pattern_info, operator_mre, pattern_mre, decision)

    return selected_patterns, pattern_models, selection_log


# Calculate MRE for pattern occurrences only
def _calculate_mre_for_pattern(occ_list: list, predictions: list) -> float:
    pred_lookup = {(p['query_file'], p['node_id']): p for p in predictions}

    mre_values = []
    for occ in occ_list:
        key = (occ['query_file'], occ['root_node_id'])
        if key in pred_lookup:
            p = pred_lookup[key]
            if p['actual_total_time'] > 0:
                mre = abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time']
                mre_values.append(mre)

    return np.mean(mre_values) if mre_values else float('inf')
