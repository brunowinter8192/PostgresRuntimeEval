#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import pandas as pd

# From training.py: Model training
from .training import train_single_pattern

# From prediction.py: Query prediction
from .prediction import predict_all_queries_with_patterns

# From mining.py: Ranking calculation
from .mining import calculate_ranking

# From metrics.py: MRE calculation
from .metrics import calculate_mre

# From mapping_config.py: Configuration constants
from mapping_config import EPSILON, MIN_ERROR_THRESHOLD, DEFAULT_STRATEGY


# FUNCTIONS

# Run pattern selection loop
def run_pattern_selection(
    df_tt: pd.DataFrame,
    df_tv: pd.DataFrame,
    patterns: dict,
    pattern_occurrences: dict,
    initial_ranking: list,
    operator_models: dict,
    current_predictions: list,
    baseline_mre: float,
    report,
    min_error_threshold: float = MIN_ERROR_THRESHOLD,
    strategy: str = DEFAULT_STRATEGY
) -> tuple:
    selected_patterns = set()
    pattern_models = {}
    selection_log = []
    consumed_hashes = set()
    error_scores = {r['pattern_hash']: r['error_score'] for r in initial_ranking}

    current_ranking = initial_ranking.copy()
    iteration = 0

    while current_ranking:
        candidate = current_ranking[0]
        pattern_hash = candidate['pattern_hash']

        consumed_hashes.add(pattern_hash)
        current_ranking = [r for r in current_ranking if r['pattern_hash'] != pattern_hash]

        if candidate['avg_mre'] < min_error_threshold:
            selection_log.append(_create_selection_log_entry(
                iteration, pattern_hash, candidate, None, None, 'SKIPPED_LOW_ERROR', baseline_mre
            ))
            report.add_selection_iteration(iteration, pattern_hash, candidate, None, 'SKIPPED_LOW_ERROR', baseline_mre)
            iteration += 1
            continue

        pattern_info = patterns[pattern_hash]

        pattern_model = train_single_pattern(df_tt, pattern_hash, pattern_info)

        if pattern_model is None:
            selection_log.append(_create_selection_log_entry(
                iteration, pattern_hash, candidate, None, None, 'SKIPPED_TRAIN_FAILED', baseline_mre
            ))
            report.add_selection_iteration(iteration, pattern_hash, candidate, None, 'SKIPPED_TRAIN_FAILED', baseline_mre)
            iteration += 1
            continue

        test_models = {**pattern_models, pattern_hash: pattern_model}
        test_selected = selected_patterns | {pattern_hash}

        new_predictions = predict_all_queries_with_patterns(
            df_tv, operator_models, test_models, patterns, test_selected, error_scores
        )

        new_mre = calculate_mre(new_predictions)
        delta = baseline_mre - new_mre

        if delta > EPSILON:
            status = 'ACCEPTED'
            selected_patterns.add(pattern_hash)
            pattern_models[pattern_hash] = pattern_model
            baseline_mre = new_mre
            current_predictions = new_predictions

            current_ranking = calculate_ranking(
                current_predictions, pattern_occurrences, patterns, consumed_hashes, strategy
            )
        else:
            status = 'REJECTED'

        selection_log.append(_create_selection_log_entry(
            iteration, pattern_hash, candidate, new_mre, delta, status, baseline_mre
        ))

        report.add_selection_iteration(iteration, pattern_hash, candidate, delta, status, baseline_mre)

        iteration += 1

    return selected_patterns, pattern_models, selection_log


# Create selection log entry
def _create_selection_log_entry(iteration, pattern_hash, candidate, new_mre, delta, status, current_mre) -> dict:
    return {
        'iteration': iteration,
        'pattern_hash': pattern_hash,
        'pattern_string': candidate['pattern_string'],
        'error_score': candidate['error_score'],
        'new_mre': new_mre,
        'delta': delta,
        'status': status,
        'mre_after': current_mre
    }
