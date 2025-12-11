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

CHILD_FEATURES = ['st1', 'rt1', 'st2', 'rt2', 'nt1', 'nt2']

TARGET_NAME_MAP = {
    'execution_time': 'actual_total_time',
    'start_time': 'actual_startup_time'
}

TARGET_TYPES = ['execution_time', 'start_time']

NON_FEATURE_SUFFIXES = [
    '_node_id',
    '_node_type',
    '_depth',
    '_parent_relationship',
    '_subplan_name',
    'actual_startup_time',
    'actual_total_time'
]

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

OPERATORS_FOLDER_NAMES = list(OPERATOR_CSV_TO_FOLDER.values())

LEAF_OPERATORS = ['SeqScan', 'IndexScan', 'IndexOnlyScan']

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


# FUNCTIONS

# Convert operator CSV name to folder name format
def csv_name_to_folder_name(csv_name):
    return OPERATOR_CSV_TO_FOLDER.get(csv_name, csv_name.replace(' ', '_'))
