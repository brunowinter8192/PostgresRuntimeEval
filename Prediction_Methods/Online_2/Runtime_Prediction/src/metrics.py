#!/usr/bin/env python3

# INFRASTRUCTURE
import numpy as np


# FUNCTIONS

# Calculate MRE on root operators
def calculate_mre(predictions: list) -> float:
    root_preds = [p for p in predictions if p['depth'] == 0]
    if not root_preds:
        return float('inf')

    mre_values = []
    for p in root_preds:
        if p['actual_total_time'] > 0:
            mre = abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time']
            mre_values.append(mre)

    return np.mean(mre_values) if mre_values else float('inf')


# Calculate MRE for single query
def calculate_query_mre(predictions: list) -> float:
    root_preds = [p for p in predictions if p['depth'] == 0]
    if not root_preds:
        return float('inf')

    p = root_preds[0]
    if p['actual_total_time'] > 0:
        return abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time']
    return float('inf')


# Create prediction result dict
def create_prediction_result(row, pred_start: float, pred_exec: float, prediction_type: str) -> dict:
    return {
        'query_file': row['query_file'],
        'node_id': row['node_id'],
        'node_type': row['node_type'],
        'depth': row['depth'],
        'parent_relationship': row['parent_relationship'],
        'actual_startup_time': row['actual_startup_time'],
        'actual_total_time': row['actual_total_time'],
        'predicted_startup_time': pred_start,
        'predicted_total_time': pred_exec,
        'prediction_type': prediction_type
    }
