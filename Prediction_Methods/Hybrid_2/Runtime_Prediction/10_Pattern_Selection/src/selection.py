# INFRASTRUCTURE

import numpy as np
import pandas as pd

# From io.py: Export and logging functions
from src.io import (
    create_log_entry,
    calculate_mre,
    export_pattern_results,
    export_selection_summary
)

# From prediction.py: Prediction and training functions
from src.prediction import load_or_train_pattern_model, predict_all_queries

# From report.py: Report generation
from src.report import export_selection_report


# FUNCTIONS

# Calculate avg MRE for a pattern based on current predictions
def calculate_pattern_avg_mre(
    pattern_hash: str,
    predictions: list,
    pattern_occurrences: pd.DataFrame
) -> float:
    occurrences = pattern_occurrences[pattern_occurrences['pattern_hash'] == pattern_hash]

    pred_lookup = {}
    for p in predictions:
        key = (p['query_file'], p['node_id'])
        if p['actual_total_time'] > 0:
            mre = abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time']
            pred_lookup[key] = mre

    mre_values = []
    for _, occ in occurrences.iterrows():
        key = (occ['query_file'], occ['root_node_id'])
        if key in pred_lookup:
            mre_values.append(pred_lookup[key])

    return np.mean(mre_values) if mre_values else 1.0


# Run static selection for frequency/size strategies
def run_static_selection(
    sorted_patterns: pd.DataFrame,
    pattern_occurrences: pd.DataFrame,
    pattern_ffs: dict,
    df_training: pd.DataFrame,
    df_test: pd.DataFrame,
    operator_models: dict,
    operator_ffs: dict,
    output_dir: str,
    pretrained_dir: str,
    min_error_threshold: float = 0.1,
    epsilon: float = 0.0,
    strategy: str = 'frequency',
    report: bool = False,
    max_iteration: int = None
) -> None:
    initial_mre = 0.2297
    baseline_mre = initial_mre
    selected_pattern_models = {}
    selected_pattern_info = {}
    selected_patterns_order = []
    selection_log = []
    iteration_data = []
    collision_data = []

    current_predictions = predict_all_queries(
        df_test, operator_models, operator_ffs, {}, pattern_ffs, {}, []
    )

    operator_baseline_mre = calculate_operator_baseline_mre(current_predictions) if report else {}

    for idx, pattern_row in sorted_patterns.iterrows():
        if max_iteration is not None and idx > max_iteration:
            break

        pattern_hash = pattern_row['pattern_hash']
        pattern_string = pattern_row['pattern_string']
        pattern_length = int(pattern_row['pattern_length'])
        operator_count = int(pattern_row['operator_count'])
        occurrence_count = int(pattern_row.get('occurrence_count', 0))
        root_operator = pattern_string.split(' -> ')[0] if ' -> ' in pattern_string else pattern_string

        avg_mre = calculate_pattern_avg_mre(
            pattern_hash, current_predictions, pattern_occurrences
        )

        if avg_mre < min_error_threshold:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_LOW_ERROR', idx
            ))
            if report:
                iteration_data.append(create_iteration_entry(
                    idx, pattern_hash, pattern_string, operator_count, occurrence_count,
                    root_operator, avg_mre, min_error_threshold, baseline_mre, None, None, 'SKIPPED_LOW_ERROR'
                ))
            continue

        if pattern_hash not in pattern_ffs:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_NO_FFS', idx
            ))
            if report:
                iteration_data.append(create_iteration_entry(
                    idx, pattern_hash, pattern_string, operator_count, occurrence_count,
                    root_operator, avg_mre, min_error_threshold, baseline_mre, None, None, 'SKIPPED_NO_FFS'
                ))
            continue

        pattern_model = load_or_train_pattern_model(
            pretrained_dir, df_training, pattern_hash, pattern_length, operator_count, pattern_ffs[pattern_hash]
        )

        if pattern_model is None:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_TRAIN_FAILED', idx
            ))
            if report:
                iteration_data.append(create_iteration_entry(
                    idx, pattern_hash, pattern_string, operator_count, occurrence_count,
                    root_operator, avg_mre, min_error_threshold, baseline_mre, None, None, 'SKIPPED_TRAIN_FAILED'
                ))
            continue

        test_models = {**selected_pattern_models, pattern_hash: pattern_model}
        test_info = {**selected_pattern_info, pattern_hash: {'length': pattern_length, 'operator_count': operator_count}}
        test_order = [h for h, _ in selected_patterns_order] + [pattern_hash]

        predictions = predict_all_queries(
            df_test, operator_models, operator_ffs, test_models, pattern_ffs, test_info, test_order
        )

        new_mre = calculate_mre(predictions)

        if new_mre < baseline_mre - epsilon:
            status = 'SELECTED'
            selected_pattern_models[pattern_hash] = pattern_model
            selected_pattern_info[pattern_hash] = {'length': pattern_length, 'operator_count': operator_count, 'string': pattern_string}
            selected_patterns_order.append((pattern_hash, idx))
            log_baseline = baseline_mre
            baseline_mre = new_mre
            delta = log_baseline - new_mre
            current_predictions = predictions
        else:
            status = 'REJECTED'
            log_baseline = baseline_mre
            delta = new_mre - baseline_mre

            if report:
                collision = detect_collision(
                    pattern_hash, pattern_string, operator_count, idx,
                    pattern_occurrences, selected_pattern_info, selected_patterns_order
                )
                if collision:
                    collision_data.append(collision)

        export_pattern_results(output_dir, pattern_hash, pattern_string, predictions, new_mre, status)

        selection_log.append(create_log_entry(
            pattern_hash, pattern_string, log_baseline, new_mre, delta, status, idx
        ))

        if report:
            iteration_data.append(create_iteration_entry(
                idx, pattern_hash, pattern_string, operator_count, occurrence_count,
                root_operator, avg_mre, min_error_threshold, log_baseline, new_mre, delta, status
            ))

    export_selection_summary(output_dir, selection_log)

    if report:
        summary = build_summary(selection_log, initial_mre, baseline_mre)
        export_selection_report(
            output_dir, strategy, iteration_data, collision_data,
            operator_baseline_mre, summary, max_iteration
        )


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
    pretrained_dir: str,
    epsilon: float = 0.0,
    strategy: str = 'error',
    report: bool = False,
    max_iteration: int = None
) -> None:
    initial_mre = 0.2297
    baseline_mre = initial_mre
    selected_pattern_models = {}
    selected_pattern_info = {}
    selected_patterns_order = []
    consumed_hashes = set()
    selection_log = []
    iteration_data = []
    collision_data = []

    occurrence_counts = error_baseline.set_index('pattern_hash')['occurrence_count'].to_dict() if 'occurrence_count' in error_baseline.columns else {}

    current_predictions = predict_all_queries(
        df_test, operator_models, operator_ffs, {}, pattern_ffs, {}, []
    )

    operator_baseline_mre = calculate_operator_baseline_mre(current_predictions) if report else {}

    iteration = 0

    while True:
        if max_iteration is not None and iteration > max_iteration:
            break

        error_ranking = calculate_error_ranking(
            current_predictions, pattern_occurrences, consumed_hashes, error_baseline
        )

        if error_ranking.empty:
            break

        candidate = select_next_candidate(error_ranking, pattern_ffs, consumed_hashes)

        if candidate is None:
            break

        pattern_hash = candidate['pattern_hash']
        pattern_info_row = error_baseline[error_baseline['pattern_hash'] == pattern_hash].iloc[0]
        pattern_string = pattern_info_row['pattern_string']
        pattern_length = int(pattern_info_row['pattern_length'])
        operator_count = int(pattern_info_row['operator_count'])
        occurrence_count = occurrence_counts.get(pattern_hash, 0)
        root_operator = pattern_string.split(' -> ')[0] if ' -> ' in pattern_string else pattern_string

        consumed_hashes.add(pattern_hash)

        if pattern_hash not in pattern_ffs:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_NO_FFS', iteration
            ))
            if report:
                iteration_data.append(create_iteration_entry(
                    iteration, pattern_hash, pattern_string, operator_count, occurrence_count,
                    root_operator, candidate.get('avg_mre', 0), 0, baseline_mre, None, None, 'SKIPPED_NO_FFS'
                ))
            continue

        pattern_model = load_or_train_pattern_model(
            pretrained_dir, df_training, pattern_hash, pattern_length, operator_count, pattern_ffs[pattern_hash]
        )

        if pattern_model is None:
            selection_log.append(create_log_entry(
                pattern_hash, pattern_string, baseline_mre, None, None, 'SKIPPED_TRAIN_FAILED', iteration
            ))
            if report:
                iteration_data.append(create_iteration_entry(
                    iteration, pattern_hash, pattern_string, operator_count, occurrence_count,
                    root_operator, candidate.get('avg_mre', 0), 0, baseline_mre, None, None, 'SKIPPED_TRAIN_FAILED'
                ))
            continue

        test_models = {**selected_pattern_models, pattern_hash: pattern_model}
        test_info = {**selected_pattern_info, pattern_hash: {'length': pattern_length, 'operator_count': operator_count}}
        test_order = [h for h, _ in selected_patterns_order] + [pattern_hash]

        new_predictions = predict_all_queries(
            df_test, operator_models, operator_ffs, test_models, pattern_ffs, test_info, test_order
        )

        new_mre = calculate_mre(new_predictions)

        if new_mre < baseline_mre - epsilon:
            status = 'SELECTED'
            selected_pattern_models[pattern_hash] = pattern_model
            selected_pattern_info[pattern_hash] = {'length': pattern_length, 'operator_count': operator_count, 'string': pattern_string}
            selected_patterns_order.append((pattern_hash, iteration))
            log_baseline = baseline_mre
            baseline_mre = new_mre
            delta = log_baseline - new_mre
            current_predictions = new_predictions
        else:
            status = 'REJECTED'
            log_baseline = baseline_mre
            delta = new_mre - baseline_mre

            if report:
                collision = detect_collision(
                    pattern_hash, pattern_string, operator_count, iteration,
                    pattern_occurrences, selected_pattern_info, selected_patterns_order
                )
                if collision:
                    collision_data.append(collision)

        export_pattern_results(output_dir, pattern_hash, pattern_string, new_predictions, new_mre, status)

        selection_log.append(create_log_entry(
            pattern_hash, pattern_string, log_baseline, new_mre, delta, status, iteration
        ))

        if report:
            iteration_data.append(create_iteration_entry(
                iteration, pattern_hash, pattern_string, operator_count, occurrence_count,
                root_operator, candidate.get('avg_mre', 0), 0, log_baseline, new_mre, delta, status
            ))

        iteration += 1

    export_selection_summary(output_dir, selection_log)

    if report:
        summary = build_summary(selection_log, initial_mre, baseline_mre)
        export_selection_report(
            output_dir, strategy, iteration_data, collision_data,
            operator_baseline_mre, summary, max_iteration
        )


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


# Calculate operator baseline MRE from initial predictions
def calculate_operator_baseline_mre(predictions: list) -> dict:
    operator_mre = {}

    for pred in predictions:
        op_type = pred['node_type']
        actual = pred['actual_total_time']
        predicted = pred['predicted_total_time']

        if actual > 0:
            mre = abs(predicted - actual) / actual

            if op_type not in operator_mre:
                operator_mre[op_type] = {'mre_sum': 0, 'count': 0}

            operator_mre[op_type]['mre_sum'] += mre
            operator_mre[op_type]['count'] += 1

    result = {}
    for op_type, data in operator_mre.items():
        result[op_type] = {
            'mre': data['mre_sum'] / data['count'] if data['count'] > 0 else 0,
            'count': data['count']
        }

    return result


# Create iteration entry for report
def create_iteration_entry(
    iteration: int,
    pattern_hash: str,
    pattern_string: str,
    operator_count: int,
    occurrence_count: int,
    root_operator: str,
    operator_mre: float,
    threshold: float,
    baseline_mre: float,
    new_mre: float,
    delta: float,
    status: str
) -> dict:
    return {
        'iteration': iteration,
        'pattern_hash': pattern_hash,
        'pattern_string': pattern_string,
        'operator_count': operator_count,
        'occurrence_count': occurrence_count,
        'root_operator': root_operator,
        'operator_mre': operator_mre,
        'threshold': threshold,
        'baseline_mre': baseline_mre,
        'new_mre': new_mre,
        'delta': delta,
        'status': status
    }


# Detect collision with already selected patterns
def detect_collision(
    rejected_hash: str,
    rejected_string: str,
    rejected_size: int,
    iteration: int,
    pattern_occurrences: pd.DataFrame,
    selected_pattern_info: dict,
    selected_patterns_order: list
) -> dict:
    rejected_occs = pattern_occurrences[pattern_occurrences['pattern_hash'] == rejected_hash]

    if rejected_occs.empty:
        return None

    rejected_roots = set(zip(rejected_occs['query_file'], rejected_occs['root_node_id']))

    for selected_hash, selected_iter in selected_patterns_order:
        selected_info = selected_pattern_info.get(selected_hash, {})
        selected_size = selected_info.get('operator_count', 0)
        selected_string = selected_info.get('string', 'N/A')

        selected_occs = pattern_occurrences[pattern_occurrences['pattern_hash'] == selected_hash]

        if selected_occs.empty:
            continue

        selected_roots = set(zip(selected_occs['query_file'], selected_occs['root_node_id']))

        overlap = rejected_roots & selected_roots

        if overlap and selected_size > rejected_size:
            return {
                'iteration': iteration,
                'rejected_hash': rejected_hash,
                'rejected_pattern_string': rejected_string,
                'rejected_size': rejected_size,
                'winning_hash': selected_hash,
                'winning_pattern_string': selected_string,
                'winning_size': selected_size,
                'winning_iteration': selected_iter,
                'conflicting_nodes': list(overlap)[:5]
            }

    return None


# Build summary from selection log
def build_summary(selection_log: list, initial_mre: float, final_mre: float) -> dict:
    total = len(selection_log)
    selected = sum(1 for entry in selection_log if entry.get('status') == 'SELECTED')
    rejected = sum(1 for entry in selection_log if entry.get('status') == 'REJECTED')
    skipped_low_error = sum(1 for entry in selection_log if entry.get('status') == 'SKIPPED_LOW_ERROR')
    skipped_no_ffs = sum(1 for entry in selection_log if entry.get('status') == 'SKIPPED_NO_FFS')

    return {
        'total': total,
        'selected': selected,
        'rejected': rejected,
        'skipped_low_error': skipped_low_error,
        'skipped_no_ffs': skipped_no_ffs,
        'initial_mre': initial_mre,
        'final_mre': final_mre
    }
