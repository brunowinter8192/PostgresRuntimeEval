#!/usr/bin/env python3

# INFRASTRUCTURE
import pandas as pd
import numpy as np
import hashlib
import shutil
from pathlib import Path
from datetime import datetime
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
import joblib

HYBRID7_BASE = Path('/Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Hybrid_7')
OUTPUT_BASE = Path('/Users/brunowinter2000/Documents/Thesis/Thesis_Final/Misc/Konzepte/Hybrid/Hybrid_7')

SVM_PARAMS = {
    'kernel': 'rbf',
    'nu': 0.65,
    'C': 1.5,
    'gamma': 'scale',
    'cache_size': 500
}


# ORCHESTRATOR
def run_debug_workflow():
    clear_old_pattern_models()

    operator_models = load_operator_models()
    operator_ffs = load_operator_ffs()
    pattern_ffs = load_pattern_ffs()
    sorted_patterns = load_sorted_patterns()
    df_training = load_training_data()
    df_test = load_test_data()

    pattern_row = sorted_patterns.iloc[0]
    pattern_hash = pattern_row['pattern_hash']
    pattern_string = pattern_row['pattern_string']
    pattern_length = pattern_row['pattern_length']

    training_debug = []
    pattern_model = train_pattern_model_with_debug(
        df_training, pattern_hash, pattern_length, pattern_ffs[pattern_hash], training_debug
    )

    export_training_debug(training_debug, pattern_hash, pattern_string)

    queries_per_template = select_one_query_per_template(df_test)

    for query_file in queries_per_template:
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)

        prediction_debug = predict_query_with_debug(
            query_ops, operator_models, operator_ffs,
            pattern_model, pattern_ffs[pattern_hash],
            pattern_hash, pattern_length
        )

        export_query_debug(query_file, query_ops, prediction_debug, pattern_hash, pattern_string)


# FUNCTIONS

# Clear existing pattern models
def clear_old_pattern_models():
    pattern_model_dir = HYBRID7_BASE / 'Runtime_Prediction' / 'Model' / 'Patterns_Frequency'
    if pattern_model_dir.exists():
        shutil.rmtree(pattern_model_dir)
    pattern_model_dir.mkdir(parents=True, exist_ok=True)


# Load operator models from Hybrid_7
def load_operator_models() -> dict:
    models = {'execution_time': {}, 'start_time': {}}
    model_path = HYBRID7_BASE / 'Runtime_Prediction' / 'Model' / 'Operator'

    for target in ['execution_time', 'start_time']:
        target_dir = model_path / target
        if not target_dir.exists():
            continue

        for op_dir in target_dir.iterdir():
            if op_dir.is_dir():
                model_file = op_dir / 'model.pkl'
                if model_file.exists():
                    models[target][op_dir.name] = joblib.load(model_file)

    return models


# Load operator FFS features
def load_operator_ffs() -> dict:
    features = {'execution_time': {}, 'start_time': {}}
    ffs_path = HYBRID7_BASE / 'Runtime_Prediction' / 'SVM' / 'Operator'

    for target in ['execution_time', 'start_time']:
        target_dir = ffs_path / target
        if not target_dir.exists():
            continue

        for op_folder in target_dir.iterdir():
            if op_folder.is_dir() and op_folder.name.endswith('_csv'):
                op_name = op_folder.name.replace('_csv', '')
                ffs_file = op_folder / 'final_features.csv'
                if ffs_file.exists():
                    df = pd.read_csv(ffs_file, delimiter=';')
                    df = df.sort_values('order')
                    features[target][op_name] = df['feature'].tolist()

    return features


# Load pattern FFS features from overview CSV
def load_pattern_ffs() -> dict:
    ffs_file = HYBRID7_BASE / 'Runtime_Prediction' / 'SVM' / 'Pattern' / 'pattern_ffs_overview.csv'
    df = pd.read_csv(ffs_file, delimiter=';')
    features = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern']
        target = row['target']

        if pattern_hash not in features:
            features[pattern_hash] = {}

        if pd.isna(row['final_features']) or row['final_features'] == '':
            features[pattern_hash][target] = []
        else:
            features[pattern_hash][target] = [f.strip() for f in row['final_features'].split(',')]

    return features


# Load sorted patterns
def load_sorted_patterns() -> pd.DataFrame:
    file_path = HYBRID7_BASE / 'Runtime_Prediction' / 'Selected_Patterns' / '06_patterns_by_frequency.csv'
    return pd.read_csv(file_path, delimiter=';')


# Load training data (main plan only)
def load_training_data() -> pd.DataFrame:
    file_path = HYBRID7_BASE / 'Dataset' / 'Training_Training.csv'
    df = pd.read_csv(file_path, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Load test data (main plan only)
def load_test_data() -> pd.DataFrame:
    file_path = HYBRID7_BASE / 'Dataset' / 'Training_Test.csv'
    df = pd.read_csv(file_path, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Select one query per template
def select_one_query_per_template(df_test: pd.DataFrame) -> list:
    df_test['template'] = df_test['query_file'].apply(lambda x: x.split('_')[0])
    templates = df_test['template'].unique()

    selected = []
    for template in sorted(templates):
        template_queries = df_test[df_test['template'] == template]['query_file'].unique()
        if len(template_queries) > 0:
            selected.append(template_queries[0])

    return selected


# Train pattern model with debug output
def train_pattern_model_with_debug(
    df_training: pd.DataFrame,
    pattern_hash: str,
    pattern_length: int,
    ffs_features: dict,
    training_debug: list
) -> dict:
    aggregated_rows = []

    for query_file in df_training['query_file'].unique():
        query_ops = df_training[df_training['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            if not has_children_at_length(node, pattern_length):
                continue

            computed_hash = compute_pattern_hash(node, pattern_length)
            if computed_hash != pattern_hash:
                continue

            pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
            pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]
            aggregated = aggregate_pattern_for_training(pattern_rows, pattern_length)

            if aggregated:
                aggregated['_query_file'] = query_file
                aggregated['_root_node_id'] = node.node_id
                aggregated_rows.append(aggregated)

    if len(aggregated_rows) < 5:
        return None

    df_agg = pd.DataFrame(aggregated_rows)

    exec_features = ffs_features.get('execution_time', [])
    start_features = ffs_features.get('start_time', [])

    exec_features_valid = [f for f in exec_features if f in df_agg.columns]
    start_features_valid = [f for f in start_features if f in df_agg.columns]

    for _, row in df_agg.iterrows():
        debug_entry = {
            'query_file': row['_query_file'],
            'root_node_id': row['_root_node_id'],
            'actual_startup_time': row.get('actual_startup_time', 0),
            'actual_total_time': row.get('actual_total_time', 0),
            'exec_features': {f: row.get(f, 0) for f in exec_features_valid},
            'start_features': {f: row.get(f, 0) for f in start_features_valid}
        }
        training_debug.append(debug_entry)

    X_exec = df_agg[exec_features_valid].fillna(0)
    X_start = df_agg[start_features_valid].fillna(0)
    y_exec = df_agg['actual_total_time']
    y_start = df_agg['actual_startup_time']

    model_exec = Pipeline([('scaler', MaxAbsScaler()), ('model', NuSVR(**SVM_PARAMS))])
    model_start = Pipeline([('scaler', MaxAbsScaler()), ('model', NuSVR(**SVM_PARAMS))])

    model_exec.fit(X_exec, y_exec)
    model_start.fit(X_start, y_start)

    return {
        'execution_time': model_exec,
        'start_time': model_start,
        'features_exec': exec_features_valid,
        'features_start': start_features_valid
    }


# Predict query with full debug trace
def predict_query_with_debug(
    query_ops: pd.DataFrame,
    operator_models: dict,
    operator_ffs: dict,
    pattern_model: dict,
    pattern_ffs_features: dict,
    pattern_hash: str,
    pattern_length: int
) -> list:
    root = build_tree_from_dataframe(query_ops)
    all_nodes = extract_all_nodes(root)
    nodes_by_depth = sorted(all_nodes, key=lambda n: n.depth, reverse=True)

    prediction_cache = {}
    consumed_nodes = set()
    debug_steps = []
    step_counter = [0]

    for node in nodes_by_depth:
        if node.node_id in consumed_nodes:
            continue

        matched_pattern = match_pattern(node, pattern_hash, pattern_length)

        if matched_pattern:
            step_counter[0] += 1
            pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
            consumed_nodes.update(pattern_node_ids)

            debug_step = predict_pattern_with_debug(
                node, query_ops, pattern_model, prediction_cache, pattern_length,
                pattern_node_ids, pattern_hash, step_counter[0]
            )

            for nid in pattern_node_ids:
                prediction_cache[nid] = {
                    'start': debug_step['predicted_startup_time'],
                    'exec': debug_step['predicted_total_time']
                }

            debug_steps.append(debug_step)
        else:
            step_counter[0] += 1
            debug_step = predict_operator_with_debug(
                node, query_ops, operator_models, operator_ffs, prediction_cache, step_counter[0]
            )

            prediction_cache[node.node_id] = {
                'start': debug_step['predicted_startup_time'],
                'exec': debug_step['predicted_total_time']
            }

            debug_steps.append(debug_step)

    return debug_steps


# Predict pattern with debug info
def predict_pattern_with_debug(
    node, query_ops: pd.DataFrame, model: dict, prediction_cache: dict,
    pattern_length: int, pattern_node_ids: list, pattern_hash: str, step_num: int
) -> dict:
    pattern_rows = query_ops[query_ops['node_id'].isin(pattern_node_ids)]
    root_row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]

    aggregated, feature_sources = aggregate_pattern_with_cache_debug(
        pattern_rows, pattern_length, query_ops, prediction_cache
    )

    X_exec = pd.DataFrame([[aggregated.get(f, 0) for f in model['features_exec']]], columns=model['features_exec'])
    X_start = pd.DataFrame([[aggregated.get(f, 0) for f in model['features_start']]], columns=model['features_start'])

    pred_exec = model['execution_time'].predict(X_exec)[0]
    pred_start = model['start_time'].predict(X_start)[0]

    return {
        'step': step_num,
        'type': 'pattern',
        'pattern_hash': pattern_hash,
        'pattern_nodes': pattern_node_ids,
        'root_node_id': node.node_id,
        'root_node_type': node.node_type,
        'root_depth': node.depth,
        'all_aggregated_features': aggregated,
        'feature_sources': feature_sources,
        'model_input_exec': {f: aggregated.get(f, 0) for f in model['features_exec']},
        'model_input_start': {f: aggregated.get(f, 0) for f in model['features_start']},
        'predicted_startup_time': pred_start,
        'predicted_total_time': pred_exec,
        'actual_startup_time': root_row['actual_startup_time'],
        'actual_total_time': root_row['actual_total_time'],
        'cache_update': pattern_node_ids
    }


# Predict operator with debug info
def predict_operator_with_debug(
    node, query_ops: pd.DataFrame, operator_models: dict, operator_ffs: dict,
    prediction_cache: dict, step_num: int
) -> dict:
    op_name = node.node_type.replace(' ', '_')
    row = query_ops[query_ops['node_id'] == node.node_id].iloc[0]

    features, feature_sources = build_operator_features_debug(row, node, query_ops, prediction_cache)

    if op_name not in operator_models['execution_time'] or op_name not in operator_models['start_time']:
        return {
            'step': step_num,
            'type': 'operator',
            'operator': node.node_type,
            'node_id': node.node_id,
            'depth': node.depth,
            'all_features': features,
            'feature_sources': feature_sources,
            'model_input_exec': {},
            'model_input_start': {},
            'predicted_startup_time': 0.0,
            'predicted_total_time': 0.0,
            'actual_startup_time': row['actual_startup_time'],
            'actual_total_time': row['actual_total_time'],
            'cache_update': [node.node_id],
            'error': f'No model for operator {op_name}'
        }

    model_exec = operator_models['execution_time'][op_name]
    model_start = operator_models['start_time'][op_name]

    exec_feature_names = list(model_exec.feature_names_in_)
    start_feature_names = list(model_start.feature_names_in_)

    X_exec = pd.DataFrame([[features.get(f, 0) for f in exec_feature_names]], columns=exec_feature_names)
    X_start = pd.DataFrame([[features.get(f, 0) for f in start_feature_names]], columns=start_feature_names)

    pred_exec = model_exec.predict(X_exec)[0]
    pred_start = model_start.predict(X_start)[0]

    return {
        'step': step_num,
        'type': 'operator',
        'operator': node.node_type,
        'node_id': node.node_id,
        'depth': node.depth,
        'all_features': features,
        'feature_sources': feature_sources,
        'model_input_exec': {f: features.get(f, 0) for f in exec_feature_names},
        'model_input_start': {f: features.get(f, 0) for f in start_feature_names},
        'predicted_startup_time': pred_start,
        'predicted_total_time': pred_exec,
        'actual_startup_time': row['actual_startup_time'],
        'actual_total_time': row['actual_total_time'],
        'cache_update': [node.node_id]
    }


# Build operator features with debug source tracking
def build_operator_features_debug(row, node, query_ops: pd.DataFrame, prediction_cache: dict) -> tuple:
    features = {}
    sources = {}

    for col in row.index:
        if col not in ['query_file', 'subplan_name', 'actual_startup_time', 'actual_total_time']:
            features[col] = row[col]
            sources[col] = f'row[{col}]'

    features['st1'] = 0.0
    features['rt1'] = 0.0
    features['st2'] = 0.0
    features['rt2'] = 0.0
    sources['st1'] = 'default(0)'
    sources['rt1'] = 'default(0)'
    sources['st2'] = 'default(0)'
    sources['rt2'] = 'default(0)'

    for child in node.children:
        if child.node_id in prediction_cache:
            pred = prediction_cache[child.node_id]
            if child.parent_relationship == 'Outer':
                features['st1'] = pred['start']
                features['rt1'] = pred['exec']
                sources['st1'] = f'cache[{child.node_id}].start'
                sources['rt1'] = f'cache[{child.node_id}].exec'
            elif child.parent_relationship == 'Inner':
                features['st2'] = pred['start']
                features['rt2'] = pred['exec']
                sources['st2'] = f'cache[{child.node_id}].start'
                sources['rt2'] = f'cache[{child.node_id}].exec'

    return features, sources


# Aggregate pattern with cache and debug source tracking
def aggregate_pattern_with_cache_debug(
    pattern_rows: pd.DataFrame,
    pattern_length: int,
    full_query_ops: pd.DataFrame,
    prediction_cache: dict
) -> tuple:
    if pattern_rows.empty:
        return {}, {}

    pattern_rows = pattern_rows.sort_values('depth').reset_index(drop=True)
    root = build_tree_from_dataframe(pattern_rows)
    pattern_node_ids = set(pattern_rows['node_id'].tolist())

    aggregated = {}
    sources = {}

    aggregate_subtree_with_cache_debug(
        root, pattern_rows, full_query_ops, prediction_cache, pattern_node_ids,
        pattern_length - 1, aggregated, sources, is_root=True
    )

    return aggregated, sources


# Aggregate subtree with cache and debug tracking
def aggregate_subtree_with_cache_debug(
    node, pattern_rows: pd.DataFrame, full_query_ops: pd.DataFrame,
    prediction_cache: dict, pattern_node_ids: set, remaining_depth: int,
    aggregated: dict, sources: dict, is_root: bool = False
):
    row = pattern_rows[pattern_rows['node_id'] == node.node_id].iloc[0]
    node_type_clean = node.node_type.replace(' ', '')

    if is_root:
        prefix = node_type_clean + '_'
        aggregated['actual_startup_time'] = row['actual_startup_time']
        aggregated['actual_total_time'] = row['actual_total_time']
        sources['actual_startup_time'] = f'node[{node.node_id}]'
        sources['actual_total_time'] = f'node[{node.node_id}]'
    else:
        prefix = node_type_clean + '_' + node.parent_relationship + '_'

    for col in row.index:
        if col not in ['query_file', 'subplan_name', 'actual_startup_time', 'actual_total_time']:
            key = prefix + col
            aggregated[key] = row[col]
            sources[key] = f'node[{node.node_id}].{col}'

    aggregated[prefix + 'st1'] = 0.0
    aggregated[prefix + 'rt1'] = 0.0
    aggregated[prefix + 'st2'] = 0.0
    aggregated[prefix + 'rt2'] = 0.0
    sources[prefix + 'st1'] = 'default(0)'
    sources[prefix + 'rt1'] = 'default(0)'
    sources[prefix + 'st2'] = 'default(0)'
    sources[prefix + 'rt2'] = 'default(0)'

    full_children = get_children_from_full_query(full_query_ops, node.node_id)
    for child_row in full_children:
        child_id = child_row['node_id']
        if child_id not in pattern_node_ids and child_id in prediction_cache:
            pred = prediction_cache[child_id]
            rel = child_row['parent_relationship']
            if rel == 'Outer':
                aggregated[prefix + 'st1'] = pred['start']
                aggregated[prefix + 'rt1'] = pred['exec']
                sources[prefix + 'st1'] = f'cache[{child_id}].start'
                sources[prefix + 'rt1'] = f'cache[{child_id}].exec'
            elif rel == 'Inner':
                aggregated[prefix + 'st2'] = pred['start']
                aggregated[prefix + 'rt2'] = pred['exec']
                sources[prefix + 'st2'] = f'cache[{child_id}].start'
                sources[prefix + 'rt2'] = f'cache[{child_id}].exec'

    if remaining_depth > 0:
        children_sorted = sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1, c.node_type))
        for child in children_sorted:
            aggregate_subtree_with_cache_debug(
                child, pattern_rows, full_query_ops, prediction_cache, pattern_node_ids,
                remaining_depth - 1, aggregated, sources, is_root=False
            )


# Get children from full query ops
def get_children_from_full_query(full_query_ops: pd.DataFrame, parent_node_id: int) -> list:
    parent_row = full_query_ops[full_query_ops['node_id'] == parent_node_id]
    if parent_row.empty:
        return []

    parent_depth = parent_row.iloc[0]['depth']
    parent_idx = parent_row.index[0]
    children = []

    for idx in range(parent_idx + 1, len(full_query_ops)):
        row = full_query_ops.iloc[idx]
        if row['depth'] == parent_depth + 1:
            children.append(row)
        elif row['depth'] <= parent_depth:
            break

    return children


# Aggregate pattern for training (no cache)
def aggregate_pattern_for_training(pattern_rows: pd.DataFrame, pattern_length: int) -> dict:
    if pattern_rows.empty:
        return None

    pattern_rows = pattern_rows.sort_values('depth').reset_index(drop=True)
    root = build_tree_from_dataframe(pattern_rows)

    aggregated = {}
    aggregate_subtree_for_training(root, pattern_rows, pattern_length - 1, aggregated, is_root=True)

    return aggregated


# Aggregate subtree for training
def aggregate_subtree_for_training(node, pattern_rows: pd.DataFrame, remaining_depth: int, aggregated: dict, is_root: bool = False):
    row = pattern_rows[pattern_rows['node_id'] == node.node_id].iloc[0]
    node_type_clean = node.node_type.replace(' ', '')

    if is_root:
        prefix = node_type_clean + '_'
        aggregated['actual_startup_time'] = row['actual_startup_time']
        aggregated['actual_total_time'] = row['actual_total_time']
    else:
        prefix = node_type_clean + '_' + node.parent_relationship + '_'

    for col in row.index:
        if col not in ['query_file', 'subplan_name', 'actual_startup_time', 'actual_total_time']:
            aggregated[prefix + col] = row[col]

    aggregated[prefix + 'st1'] = row.get('st1', 0)
    aggregated[prefix + 'rt1'] = row.get('rt1', 0)
    aggregated[prefix + 'st2'] = row.get('st2', 0)
    aggregated[prefix + 'rt2'] = row.get('rt2', 0)

    if remaining_depth > 0:
        children_sorted = sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1, c.node_type))
        for child in children_sorted:
            aggregate_subtree_for_training(child, pattern_rows, remaining_depth - 1, aggregated, is_root=False)


# Build tree from flat DataFrame
def build_tree_from_dataframe(query_ops: pd.DataFrame):
    nodes = {}
    root = None
    min_depth = query_ops['depth'].min()

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'] if pd.notna(row['parent_relationship']) else '',
            depth=row['depth'],
            node_id=row['node_id']
        )
        nodes[row['node_id']] = node
        if row['depth'] == min_depth:
            root = node

    for idx, row in query_ops.iterrows():
        current_node = nodes[row['node_id']]
        current_depth = row['depth']

        for j in range(idx + 1, len(query_ops)):
            next_row = query_ops.iloc[j]
            if next_row['depth'] == current_depth + 1:
                child_node = nodes[next_row['node_id']]
                current_node.add_child(child_node)
            elif next_row['depth'] <= current_depth:
                break

    return root


# Extract all nodes from tree
def extract_all_nodes(node) -> list:
    nodes = [node]
    for child in node.children:
        nodes.extend(extract_all_nodes(child))
    return nodes


# Check if node has children at target length
def has_children_at_length(node, pattern_length: int) -> bool:
    if pattern_length == 1:
        return True
    if pattern_length == 2:
        return len(node.children) > 0
    if len(node.children) == 0:
        return False
    return any(has_children_at_length(child, pattern_length - 1) for child in node.children)


# Compute pattern hash
def compute_pattern_hash(node, remaining_length: int) -> str:
    if remaining_length == 1 or len(node.children) == 0:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_pattern_hash(child, remaining_length - 1)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)
    return hashlib.md5(combined_string.encode()).hexdigest()


# Extract pattern node IDs
def extract_pattern_node_ids(node, remaining_length: int) -> list:
    if remaining_length == 1 or len(node.children) == 0:
        return [node.node_id]

    node_ids = [node.node_id]
    for child in node.children:
        child_ids = extract_pattern_node_ids(child, remaining_length - 1)
        node_ids.extend(child_ids)

    return node_ids


# Match node against target pattern
def match_pattern(node, pattern_hash: str, pattern_length: int) -> bool:
    if not has_children_at_length(node, pattern_length):
        return False

    computed_hash = compute_pattern_hash(node, pattern_length)
    return computed_hash == pattern_hash


# Export training debug to markdown
def export_training_debug(training_debug: list, pattern_hash: str, pattern_string: str):
    output_dir = OUTPUT_BASE / 'md'
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'00_training_debug_{timestamp}.md'

    lines = [
        '# Pattern Training Debug',
        '',
        f'**Pattern Hash:** {pattern_hash}',
        f'**Pattern String:** {pattern_string}',
        f'**Training Samples:** {len(training_debug)}',
        '',
        '## Training Samples',
        ''
    ]

    for i, sample in enumerate(training_debug[:20], 1):
        lines.append(f'### Sample {i}: {sample["query_file"]} (node_id {sample["root_node_id"]})')
        lines.append('')
        lines.append(f'**Targets:** startup={sample["actual_startup_time"]:.3f}, total={sample["actual_total_time"]:.3f}')
        lines.append('')
        lines.append('**Execution Time Features:**')
        lines.append('')
        lines.append('| Feature | Value |')
        lines.append('|---------|-------|')
        for f, v in sample['exec_features'].items():
            lines.append(f'| {f} | {v:.4f} |')
        lines.append('')
        lines.append('**Start Time Features:**')
        lines.append('')
        lines.append('| Feature | Value |')
        lines.append('|---------|-------|')
        for f, v in sample['start_features'].items():
            lines.append(f'| {f} | {v:.4f} |')
        lines.append('')
        lines.append('---')
        lines.append('')

    if len(training_debug) > 20:
        lines.append(f'... and {len(training_debug) - 20} more samples')

    with open(output_dir / filename, 'w') as f:
        f.write('\n'.join(lines))


# Export query debug to markdown
def export_query_debug(query_file: str, query_ops: pd.DataFrame, debug_steps: list, pattern_hash: str, pattern_string: str):
    output_dir = OUTPUT_BASE / 'md'
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    template = query_file.split('_')[0]
    filename = f'{template}_{query_file}_debug_{timestamp}.md'

    pattern_steps = [s for s in debug_steps if s['type'] == 'pattern']
    operator_steps = [s for s in debug_steps if s['type'] == 'operator']

    lines = [
        f'# Debug Prediction: {query_file}',
        '',
        '## Overview',
        f'- Total operators: {len(query_ops)}',
        f'- Pattern predictions: {len(pattern_steps)}',
        f'- Operator predictions: {len(operator_steps)}',
        f'- Target pattern: {pattern_string}',
        '',
        '## Bottom-Up Execution (Deepest First)',
        ''
    ]

    for step in debug_steps:
        if step['type'] == 'pattern':
            lines.extend(format_pattern_debug_step(step))
        else:
            lines.extend(format_operator_debug_step(step))
        lines.append('')

    with open(output_dir / filename, 'w') as f:
        f.write('\n'.join(lines))


# Format pattern debug step
def format_pattern_debug_step(step: dict) -> list:
    lines = [
        f'### Step {step["step"]}: Pattern Prediction ({step["root_node_type"]}, depth {step["root_depth"]}, node_id {step["root_node_id"]})',
        '',
        f'**Pattern Hash:** {step["pattern_hash"]}',
        f'**Pattern Nodes:** {step["pattern_nodes"]}',
        ''
    ]

    lines.append('**Model Input (Execution Time):**')
    lines.append('')
    lines.append('| Feature | Value | Source |')
    lines.append('|---------|-------|--------|')
    for f, v in step['model_input_exec'].items():
        source = step['feature_sources'].get(f, 'unknown')
        lines.append(f'| {f} | {v:.4f} | {source} |')
    lines.append('')

    lines.append('**Model Input (Start Time):**')
    lines.append('')
    lines.append('| Feature | Value | Source |')
    lines.append('|---------|-------|--------|')
    for f, v in step['model_input_start'].items():
        source = step['feature_sources'].get(f, 'unknown')
        lines.append(f'| {f} | {v:.4f} | {source} |')
    lines.append('')

    lines.append('**Prediction:**')
    lines.append('')
    lines.append('| Target | Predicted | Actual | Error % |')
    lines.append('|--------|-----------|--------|---------|')

    actual_start = step['actual_startup_time']
    actual_exec = step['actual_total_time']
    pred_start = step['predicted_startup_time']
    pred_exec = step['predicted_total_time']

    err_start = abs(pred_start - actual_start) / actual_start * 100 if actual_start > 0 else 0
    err_exec = abs(pred_exec - actual_exec) / actual_exec * 100 if actual_exec > 0 else 0

    lines.append(f'| start_time | {pred_start:.3f} | {actual_start:.3f} | {err_start:.1f}% |')
    lines.append(f'| exec_time | {pred_exec:.3f} | {actual_exec:.3f} | {err_exec:.1f}% |')
    lines.append('')

    lines.append(f'**Cache Update:** nodes {step["cache_update"]} -> st={pred_start:.3f}, rt={pred_exec:.3f}')
    lines.append('')
    lines.append('---')

    return lines


# Format operator debug step
def format_operator_debug_step(step: dict) -> list:
    lines = [
        f'### Step {step["step"]}: Operator Prediction ({step["operator"]}, depth {step["depth"]}, node_id {step["node_id"]})',
        ''
    ]

    if 'error' in step:
        lines.append(f'**ERROR:** {step["error"]}')
        lines.append('')

    lines.append('**Model Input (Execution Time):**')
    lines.append('')
    lines.append('| Feature | Value | Source |')
    lines.append('|---------|-------|--------|')
    for f, v in step['model_input_exec'].items():
        source = step['feature_sources'].get(f, 'unknown')
        lines.append(f'| {f} | {v:.4f} | {source} |')
    lines.append('')

    lines.append('**Model Input (Start Time):**')
    lines.append('')
    lines.append('| Feature | Value | Source |')
    lines.append('|---------|-------|--------|')
    for f, v in step['model_input_start'].items():
        source = step['feature_sources'].get(f, 'unknown')
        lines.append(f'| {f} | {v:.4f} | {source} |')
    lines.append('')

    lines.append('**Prediction:**')
    lines.append('')
    lines.append('| Target | Predicted | Actual | Error % |')
    lines.append('|--------|-----------|--------|---------|')

    actual_start = step['actual_startup_time']
    actual_exec = step['actual_total_time']
    pred_start = step['predicted_startup_time']
    pred_exec = step['predicted_total_time']

    err_start = abs(pred_start - actual_start) / actual_start * 100 if actual_start > 0 else 0
    err_exec = abs(pred_exec - actual_exec) / actual_exec * 100 if actual_exec > 0 else 0

    lines.append(f'| start_time | {pred_start:.3f} | {actual_start:.3f} | {err_start:.1f}% |')
    lines.append(f'| exec_time | {pred_exec:.3f} | {actual_exec:.3f} | {err_exec:.1f}% |')
    lines.append('')

    lines.append(f'**Cache Update:** node {step["cache_update"]} -> st={pred_start:.3f}, rt={pred_exec:.3f}')
    lines.append('')
    lines.append('---')

    return lines


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


if __name__ == '__main__':
    run_debug_workflow()
