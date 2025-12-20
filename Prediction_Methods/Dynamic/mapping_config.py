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
