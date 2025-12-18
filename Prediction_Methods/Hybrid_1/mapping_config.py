#!/usr/bin/env python3

# INFRASTRUCTURE

TARGET_TYPES = ['execution_time', 'start_time']

NON_FEATURE_SUFFIXES = [
    '_node_id',
    '_node_type',
    '_depth',
    '_parent_relationship',
    '_subplan_name',
    '_template',
    'actual_startup_time',
    'actual_total_time'
]

LEAF_OPERATORS = ['SeqScan', 'IndexScan', 'IndexOnlyScan']

REQUIRED_OPERATORS = {'Hash', 'Hash Join', 'Seq Scan', 'Sort', 'Nested Loop'}

PASSTHROUGH_OPERATORS = {
    'Incremental Sort',
    'Gather Merge',
    'Gather',
    'Sort',
    'Limit',
    'Merge Join'
}

CHILD_ACTUAL_SUFFIXES = [
    '_Outer_actual_startup_time',
    '_Outer_actual_total_time',
    '_Inner_actual_startup_time',
    '_Inner_actual_total_time'
]

CHILD_TIMING_SUFFIXES = [
    '_Outer_st1', '_Outer_rt1', '_Outer_st2', '_Outer_rt2',
    '_Inner_st1', '_Inner_rt1', '_Inner_st2', '_Inner_rt2'
]

PARENT_CHILD_FEATURES = ['_st1', '_rt1', '_st2', '_rt2']

CHILD_FEATURES_TIMING = ['st1', 'rt1', 'st2', 'rt2']

FFS_SEED = 42
FFS_MIN_FEATURES = 1


# FUNCTIONS

# Convert pattern string to folder name format
def pattern_to_folder_name(pattern_str: str) -> str:
    import re
    clean = pattern_str.replace(' → ', '_')
    clean = clean.replace('[', '').replace(']', '')
    clean = clean.replace('(', '').replace(')', '')
    clean = clean.replace(', ', '_')
    clean = clean.replace(' ', '_')
    clean = re.sub(r'_+', '_', clean)
    return clean


# Check if operator type is a leaf node
def is_leaf_operator(operator_type: str) -> bool:
    return operator_type in LEAF_OPERATORS


# Check if operator type is passthrough
def is_passthrough_operator(operator_type: str) -> bool:
    return operator_type in PASSTHROUGH_OPERATORS
