#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import numpy as np
import hashlib
import json
from pathlib import Path
from sklearn.svm import NuSVR
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
import joblib
from joblib import Parallel, delayed
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from Runtime_Prediction.ffs_config import SVM_PARAMS


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.children = []

    # Append child node to children list
    def add_child(self, child_node):
        self.children.append(child_node)


# ORCHESTRATOR
def pretrain_all_patterns(
    pattern_ffs_file: str,
    patterns_metadata_file: str,
    training_file: str,
    output_dir: str,
    n_jobs: int
) -> None:
    pattern_ffs = load_pattern_ffs(pattern_ffs_file)
    patterns_metadata = load_patterns_metadata(patterns_metadata_file)
    df_training = load_training_data(training_file)

    trainable_patterns = filter_trainable_patterns(patterns_metadata, pattern_ffs)

    Parallel(n_jobs=n_jobs, verbose=10)(
        delayed(train_single_pattern)(
            row['pattern_hash'],
            int(row['pattern_length']),
            int(row['operator_count']),
            pattern_ffs[row['pattern_hash']],
            df_training,
            output_dir
        )
        for _, row in trainable_patterns.iterrows()
    )


# FUNCTIONS

# Load pattern FFS features from overview CSV
def load_pattern_ffs(pattern_ffs_file: str) -> dict:
    df = pd.read_csv(pattern_ffs_file, delimiter=';')
    features = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']
        target = row['target']

        if pattern_hash not in features:
            features[pattern_hash] = {}

        if pd.isna(row['final_features']) or row['final_features'] == '':
            features[pattern_hash][target] = []
        else:
            features[pattern_hash][target] = [f.strip() for f in row['final_features'].split(',')]

    return features


# Load patterns metadata
def load_patterns_metadata(patterns_metadata_file: str) -> pd.DataFrame:
    return pd.read_csv(patterns_metadata_file, delimiter=';')


# Load training data
def load_training_data(training_file: str) -> pd.DataFrame:
    df = pd.read_csv(training_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]


# Filter patterns that have FFS features for both targets
def filter_trainable_patterns(patterns_metadata: pd.DataFrame, pattern_ffs: dict) -> pd.DataFrame:
    trainable = []
    for _, row in patterns_metadata.iterrows():
        pattern_hash = row['pattern_hash']
        if pattern_hash not in pattern_ffs:
            continue
        ffs = pattern_ffs[pattern_hash]
        if ffs.get('execution_time') and ffs.get('start_time'):
            trainable.append(row)
    return pd.DataFrame(trainable)


# Train single pattern (called in parallel)
def train_single_pattern(
    pattern_hash: str,
    pattern_length: int,
    operator_count: int,
    ffs_features: dict,
    df_training: pd.DataFrame,
    output_dir: str
) -> dict:
    result = {
        'pattern_hash': pattern_hash,
        'pattern_length': pattern_length,
        'status': 'FAILED',
        'reason': ''
    }

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
            aggregated = aggregate_pattern(pattern_rows, pattern_length)
            if aggregated:
                aggregated_rows.append(aggregated)

    if len(aggregated_rows) < 5:
        result['reason'] = f'insufficient_samples ({len(aggregated_rows)})'
        return result

    df_agg = pd.DataFrame(aggregated_rows)

    exec_features = ffs_features.get('execution_time', [])
    start_features = ffs_features.get('start_time', [])

    exec_features_valid = [f for f in exec_features if f in df_agg.columns]
    start_features_valid = [f for f in start_features if f in df_agg.columns]

    if not exec_features_valid or not start_features_valid:
        result['reason'] = 'no_valid_features'
        return result

    X_exec = df_agg[exec_features_valid].fillna(0)
    X_start = df_agg[start_features_valid].fillna(0)
    y_exec = df_agg['actual_total_time']
    y_start = df_agg['actual_startup_time']

    model_exec = Pipeline([('scaler', MaxAbsScaler()), ('model', NuSVR(**SVM_PARAMS))])
    model_start = Pipeline([('scaler', MaxAbsScaler()), ('model', NuSVR(**SVM_PARAMS))])

    model_exec.fit(X_exec, y_exec)
    model_start.fit(X_start, y_start)

    save_pattern_model(output_dir, pattern_hash, model_exec, model_start, exec_features_valid, start_features_valid)

    result['status'] = 'SUCCESS'
    result['samples'] = len(aggregated_rows)
    result['exec_features'] = len(exec_features_valid)
    result['start_features'] = len(start_features_valid)
    return result


# Save pattern model to disk
def save_pattern_model(
    output_dir: str,
    pattern_hash: str,
    model_exec,
    model_start,
    features_exec: list,
    features_start: list
) -> None:
    pattern_dir = Path(output_dir) / pattern_hash
    pattern_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(model_exec, pattern_dir / 'model_execution_time.pkl')
    joblib.dump(model_start, pattern_dir / 'model_start_time.pkl')

    with open(pattern_dir / 'features.json', 'w') as f:
        json.dump({
            'features_exec': features_exec,
            'features_start': features_start
        }, f)


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


# Aggregate pattern rows for training
def aggregate_pattern(pattern_rows: pd.DataFrame, pattern_length: int) -> dict:
    if pattern_rows.empty:
        return None

    pattern_rows = pattern_rows.sort_values('depth').reset_index(drop=True)
    root = build_tree_from_dataframe(pattern_rows)

    return aggregate_subtree(root, pattern_rows, pattern_length - 1, is_root=True)


# Aggregate subtree recursively
def aggregate_subtree(node, pattern_rows: pd.DataFrame, remaining_depth: int, is_root: bool = False) -> dict:
    aggregated = {}
    row = pattern_rows[pattern_rows['node_id'] == node.node_id].iloc[0]
    node_type_clean = node.node_type.replace(' ', '')

    if is_root:
        prefix = node_type_clean + '_'
        aggregated['query_file'] = row['query_file']
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
            child_agg = aggregate_subtree(child, pattern_rows, remaining_depth - 1, is_root=False)
            aggregated.update(child_agg)

    return aggregated


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern_ffs_file', help='Path to SVM/Pattern/pattern_ffs_overview.csv')
    parser.add_argument('patterns_metadata_file', help='Path to 06_patterns_by_frequency.csv')
    parser.add_argument('training_file', help='Path to Training_Training.csv')
    parser.add_argument('--output-dir', required=True, help='Output directory (Model/Patterns_Pretrained)')
    parser.add_argument('--n-jobs', type=int, default=-1, help='Number of parallel jobs (-1 = all cores)')
    args = parser.parse_args()

    pretrain_all_patterns(
        args.pattern_ffs_file,
        args.patterns_metadata_file,
        args.training_file,
        args.output_dir,
        args.n_jobs
    )
