#!/usr/bin/env python3

# INFRASTRUCTURE

OPERATOR_FEATURES = [
    'np', 'nt', 'nt1', 'nt2', 'sel',
    'startup_cost', 'total_cost', 'plan_width',
    'reltuples', 'parallel_workers'
]

OPERATOR_TARGETS = [
    'actual_startup_time',
    'actual_total_time'
]

OPERATOR_METADATA = [
    'query_file', 'node_id', 'node_type',
    'depth', 'parent_relationship', 'subplan_name'
]

CHILD_FEATURES_TIMING = ['st1', 'rt1', 'st2', 'rt2']
CHILD_FEATURES_STRUCTURAL = ['nt1', 'nt2']
CHILD_FEATURES = CHILD_FEATURES_TIMING + CHILD_FEATURES_STRUCTURAL

TARGET_NAME_MAP = {
    'execution_time': 'actual_total_time',
    'start_time': 'actual_startup_time'
}

TARGET_TYPES = ['execution_time', 'start_time']

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

OPERATORS_CSV_NAMES = list(OPERATOR_CSV_TO_FOLDER.keys())
OPERATORS_FOLDER_NAMES = list(OPERATOR_CSV_TO_FOLDER.values())

LEAF_OPERATORS = ['Seq Scan', 'Index Scan', 'Index Only Scan']


# FUNCTIONS

# Convert operator CSV name to folder name format
def csv_name_to_folder_name(csv_name):
    return OPERATOR_CSV_TO_FOLDER.get(csv_name, csv_name.replace(' ', '_'))


# Convert operator folder name to CSV name format
def folder_name_to_csv_name(folder_name):
    reverse_map = {v: k for k, v in OPERATOR_CSV_TO_FOLDER.items()}
    return reverse_map.get(folder_name, folder_name.replace('_', ' '))


# Check if operator is a leaf node type
def is_leaf_operator(operator_csv_name):
    return operator_csv_name in LEAF_OPERATORS


# Get all dataset columns including features targets and metadata
def get_all_columns():
    return OPERATOR_FEATURES + OPERATOR_TARGETS + OPERATOR_METADATA


# Get feature column names for model training
def get_feature_columns():
    return OPERATOR_FEATURES.copy()
