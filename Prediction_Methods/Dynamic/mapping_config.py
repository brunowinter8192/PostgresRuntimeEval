#!/usr/bin/env python3

# INFRASTRUCTURE

# SVM Parameters (from Online_1)
SVM_PARAMS = {
    'kernel': 'rbf',
    'nu': 0.65,
    'C': 1.5,
    'gamma': 'scale',
    'cache_size': 500
}

# Online Selection Parameters
EPSILON = 0.005  # 0.5% minimum improvement
MIN_ERROR_THRESHOLD = 0.1  # 10% - skip patterns with avg_mre below
STRATEGIES = ['error', 'size', 'frequency']
DEFAULT_STRATEGY = 'error'

# Operator Feature-Set (10 base features)
OPERATOR_FEATURES = [
    'np', 'nt', 'nt1', 'nt2', 'sel',
    'startup_cost', 'total_cost', 'plan_width',
    'reltuples', 'parallel_workers'
]

# Child Features (timing + structural)
CHILD_FEATURES_TIMING = ['st1', 'rt1', 'st2', 'rt2']
CHILD_FEATURES_STRUCTURAL = ['nt1', 'nt2']
CHILD_FEATURES = CHILD_FEATURES_TIMING + CHILD_FEATURES_STRUCTURAL

# Pattern Feature-Set (14 features, prefixed per operator in pattern)
PATTERN_FEATURES = [
    'nt', 'nt1', 'nt2',
    'np', 'plan_width',
    'rt1', 'rt2', 'st1', 'st2',
    'sel', 'reltuples',
    'parallel_workers',
    'startup_cost', 'total_cost'
]

# Target columns
OPERATOR_TARGETS = ['actual_startup_time', 'actual_total_time']

# Non-feature suffixes (for pattern datasets - columns to exclude from features)
NON_FEATURE_SUFFIXES = [
    '_node_id', '_node_type', '_depth', '_parent_relationship',
    '_subplan_name', '_template', 'actual_startup_time', 'actual_total_time'
]

# Target columns
TARGET_NAME_MAP = {
    'execution_time': 'actual_total_time',
    'start_time': 'actual_startup_time'
}

TARGET_TYPES = ['execution_time', 'start_time']

# Metadata columns (not features)
METADATA_COLUMNS = [
    'query_file', 'node_id', 'node_type',
    'depth', 'parent_relationship', 'subplan_name', 'template'
]
OPERATOR_METADATA = METADATA_COLUMNS  # Alias for Online_1 compatibility

# Leaf operators (no child timing features)
LEAF_OPERATORS = ['Seq Scan', 'Index Scan', 'Index Only Scan']

# Operator name mapping (CSV name -> folder name)
OPERATOR_CSV_TO_FOLDER = {
    'Aggregate': 'Aggregate',
    'Gather': 'Gather',
    'Gather Merge': 'Gather_Merge',
    'Hash': 'Hash',
    'Hash Join': 'Hash_Join',
    'Incremental Sort': 'Incremental_Sort',
    'Index Only Scan': 'Index_Only_Scan',
    'Index Scan': 'Index_Scan',
    'Limit': 'Limit',
    'Merge Join': 'Merge_Join',
    'Nested Loop': 'Nested_Loop',
    'Seq Scan': 'Seq_Scan',
    'Sort': 'Sort'
}


# FUNCTIONS

# Get feature set for operator (removes timing for leafs)
def get_operator_features(node_type: str) -> list:
    base = OPERATOR_FEATURES.copy()
    if node_type in LEAF_OPERATORS:
        return base + CHILD_FEATURES_STRUCTURAL
    return base + CHILD_FEATURES


# Convert operator CSV name to folder name format
def csv_name_to_folder_name(csv_name: str) -> str:
    return OPERATOR_CSV_TO_FOLDER.get(csv_name, csv_name.replace(' ', '_'))


# Get pattern features with prefix
def get_pattern_features_with_prefix(prefix: str, is_leaf: bool) -> list:
    features = []
    for f in PATTERN_FEATURES:
        if is_leaf and f in CHILD_FEATURES_TIMING:
            continue
        features.append(f'{prefix}{f}')
    return features
