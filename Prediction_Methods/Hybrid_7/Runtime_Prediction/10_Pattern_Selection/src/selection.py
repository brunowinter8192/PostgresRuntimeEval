# INFRASTRUCTURE

import numpy as np
import pandas as pd

# From io.py: Export and logging functions
from src.io import (
    create_log_entry,
    calculate_mre,
    save_pattern_model,
    export_pattern_results,
    export_selection_summary
)

# From prediction.py: Prediction and training functions
from src.prediction import load_or_train_pattern_model, predict_all_queries


# FUNCTIONS

# Run static selection for frequency/size strategies
def run_static_selection(
    sorted_patterns: pd.DataFrame,
    pattern_ffs: dict,
    df_training: pd.DataFrame,
    df_test: pd.DataFrame,
    operator_models: dict,
    operator_ffs: dict,
    output_dir: str,
    model_dir: str,
    pretrained_dir: str
) -> None:
    baseline_mre = 0.2297
    selected_pattern_models = {}
    selected_pattern_info = {}
    selection_log = []

    for idx, pattern_row in sorted_patterns.iterrows():
        pattern_hash = pattern_row['pattern_hash']
        pattern_string = pattern_row['pattern_string']
        pattern_length = int(pattern_row['pattern_length'])
        operator_count = int(pattern_row['operator_count'])

        if pattern_hash not in pattern_ffs:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_NO_FFS', idx
            ))
            continue

        pattern_model = load_or_train_pattern_model(
            pretrained_dir, df_training, pattern_hash, pattern_length, operator_count, pattern_ffs[pattern_hash]
        )

        if pattern_model is None:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_TRAIN_FAILED', idx
            ))
            continue

        test_models = {**selected_pattern_models, pattern_hash: pattern_model}
        test_info = {**selected_pattern_info, pattern_hash: {'length': pattern_length, 'operator_count': operator_count}}

        predictions = predict_all_queries(
            df_test, operator_models, operator_ffs, test_models, pattern_ffs, test_info
        )

        new_mre = calculate_mre(predictions)

        if new_mre < baseline_mre:
            status = 'SELECTED'
            selected_pattern_models[pattern_hash] = pattern_model
            selected_pattern_info[pattern_hash] = {'length': pattern_length, 'operator_count': operator_count}
            save_pattern_model(model_dir, pattern_hash, pattern_model)
            old_baseline = baseline_mre
            baseline_mre = new_mre
            delta = old_baseline - new_mre
        else:
            status = 'REJECTED'
            delta = new_mre - baseline_mre

        export_pattern_results(output_dir, pattern_hash, pattern_string, predictions, new_mre, status)

        selection_log.append(create_log_entry(
            pattern_hash, pattern_string, baseline_mre, new_mre, delta, status, idx
        ))

    export_selection_summary(output_dir, selection_log)


# Run dynamic error-based selection with re-ranking
def run_error_selection(
    error_baseline: pd.DataFrame,
    pattern_occurrences: pd.DataFrame,
    pattern_ffs: dict,
    df_training: pd.DataFrame,
    df_test: pd.DataFrame,
    operator_models: dict,
    operator_ffs: dict,
    output_dir: str,
    model_dir: str,
    pretrained_dir: str
) -> None:
    baseline_mre = 0.2297
    selected_pattern_models = {}
    selected_pattern_info = {}
    consumed_hashes = set()
    selection_log = []

    current_predictions = predict_all_queries(
        df_test, operator_models, operator_ffs, {}, pattern_ffs, {}
    )

    iteration = 0

    while True:
        error_ranking = calculate_error_ranking(
            current_predictions, pattern_occurrences, consumed_hashes, error_baseline
        )

        if error_ranking.empty:
            break

        candidate = select_next_candidate(error_ranking, pattern_ffs, consumed_hashes)

        if candidate is None:
            break

        pattern_hash = candidate['pattern_hash']
        pattern_info = error_baseline[error_baseline['pattern_hash'] == pattern_hash].iloc[0]
        pattern_string = pattern_info['pattern_string']
        pattern_length = int(pattern_info['pattern_length'])
        operator_count = int(pattern_info['operator_count'])

        consumed_hashes.add(pattern_hash)

        if pattern_hash not in pattern_ffs:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_NO_FFS', iteration
            ))
            continue

        pattern_model = load_or_train_pattern_model(
            pretrained_dir, df_training, pattern_hash, pattern_length, operator_count, pattern_ffs[pattern_hash]
        )

        if pattern_model is None:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_TRAIN_FAILED', iteration
            ))
            continue

        test_models = {**selected_pattern_models, pattern_hash: pattern_model}
        test_info = {**selected_pattern_info, pattern_hash: {'length': pattern_length, 'operator_count': operator_count}}

        new_predictions = predict_all_queries(
            df_test, operator_models, operator_ffs, test_models, pattern_ffs, test_info
        )

        new_mre = calculate_mre(new_predictions)

        if new_mre < baseline_mre:
            status = 'SELECTED'
            selected_pattern_models[pattern_hash] = pattern_model
            selected_pattern_info[pattern_hash] = {'length': pattern_length, 'operator_count': operator_count}
            save_pattern_model(model_dir, pattern_hash, pattern_model)
            old_baseline = baseline_mre
            baseline_mre = new_mre
            delta = old_baseline - new_mre
            current_predictions = new_predictions
        else:
            status = 'REJECTED'
            delta = new_mre - baseline_mre

        export_pattern_results(output_dir, pattern_hash, pattern_string, new_predictions, new_mre, status)

        selection_log.append(create_log_entry(
            pattern_hash, pattern_string, baseline_mre, new_mre, delta, status, iteration
        ))

        iteration += 1

    export_selection_summary(output_dir, selection_log)


# Calculate error ranking based on current predictions (for error strategy)
def calculate_error_ranking(
    predictions: list,
    pattern_occurrences: pd.DataFrame,
    consumed_hashes: set,
    error_baseline: pd.DataFrame
) -> pd.DataFrame:
    available = pattern_occurrences[~pattern_occurrences['pattern_hash'].isin(consumed_hashes)]

    if available.empty:
        return pd.DataFrame()

    pred_lookup = {}

    for p in predictions:
        key = (p['query_file'], p['node_id'])

        if p['actual_total_time'] > 0:
            mre = abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time']
            pred_lookup[key] = mre

    metadata_dict = {}

    for _, row in error_baseline.iterrows():
        metadata_dict[row['pattern_hash']] = {
            'pattern_string': row['pattern_string'],
            'pattern_length': row['pattern_length'],
            'operator_count': row['operator_count']
        }

    results = []

    for pattern_hash in available['pattern_hash'].unique():
        occurrences = available[available['pattern_hash'] == pattern_hash]
        mre_values = []

        for _, occ in occurrences.iterrows():
            key = (occ['query_file'], occ['root_node_id'])

            if key in pred_lookup:
                mre_values.append(pred_lookup[key])

        if mre_values:
            avg_mre = np.mean(mre_values)
            error_score = len(occurrences) * avg_mre

            meta = metadata_dict.get(pattern_hash, {})
            results.append({
                'pattern_hash': pattern_hash,
                'pattern_string': meta.get('pattern_string', ''),
                'pattern_length': meta.get('pattern_length', 0),
                'operator_count': meta.get('operator_count', 0),
                'occurrence_count': len(occurrences),
                'avg_mre': avg_mre,
                'avg_mre_pct': avg_mre * 100,
                'error_score': error_score
            })

    if not results:
        return pd.DataFrame()

    return pd.DataFrame(results).sort_values(
        by=['error_score', 'pattern_hash'],
        ascending=[False, True]
    ).reset_index(drop=True)


# Select next candidate pattern with highest error_score that has FFS
def select_next_candidate(
    error_ranking: pd.DataFrame,
    pattern_ffs: dict,
    consumed_hashes: set
) -> dict:
    for _, row in error_ranking.iterrows():
        pattern_hash = row['pattern_hash']

        if pattern_hash in consumed_hashes:
            continue

        if pattern_hash in pattern_ffs:
            return row.to_dict()

    return None
