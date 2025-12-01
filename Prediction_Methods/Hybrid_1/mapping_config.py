#!/usr/bin/env python3

# INFRASTRUCTURE

PATTERNS = [
    'Hash_Join_Seq_Scan_Outer_Hash_Inner',
    'Hash_Seq_Scan_Outer',
    'Hash_Hash_Join_Outer',
    'Hash_Join_Nested_Loop_Outer_Hash_Inner',
    'Nested_Loop_Hash_Join_Outer_Index_Scan_Inner',
    'Sort_Hash_Join_Outer',
    'Nested_Loop_Seq_Scan_Outer_Index_Scan_Inner',
    'Gather_Aggregate_Outer',
    'Aggregate_Hash_Join_Outer',
    'Aggregate_Gather_Outer',
    'Aggregate_Seq_Scan_Outer',
    'Hash_Join_Hash_Join_Outer_Hash_Inner',
    'Aggregate_Nested_Loop_Outer',
    'Sort_Nested_Loop_Outer',
    'Incremental_Sort_Nested_Loop_Outer',
    'Nested_Loop_Merge_Join_Outer_Index_Scan_Inner',
    'Hash_Aggregate_Outer',
    'Sort_Seq_Scan_Outer',
    'Gather_Nested_Loop_Outer',
    'Gather_Hash_Join_Outer',
    'Hash_Index_Only_Scan_Outer'
]

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

LEAF_OPERATORS = ['SeqScan', 'IndexScan', 'IndexOnlyScan']

REQUIRED_OPERATORS = {'Gather', 'Hash', 'Hash Join', 'Nested Loop', 'Seq Scan'}

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
