#!/usr/bin/env python3

# INFRASTRUCTURE

PATTERNS = [
    'Hash_Join_Seq_Scan_Outer_Hash_Inner',
    'Hash_Join_Nested_Loop_Outer_Hash_Inner',
    'Nested_Loop_Hash_Join_Outer_Index_Scan_Inner',
    'Nested_Loop_Seq_Scan_Outer_Index_Scan_Inner',
    'Gather_Aggregate_Outer',
    'Hash_Join_Hash_Join_Outer_Hash_Inner',
    'Gather_Hash_Join_Outer',
    'Nested_Loop_Merge_Join_Outer_Index_Scan_Inner',
    'Gather_Nested_Loop_Outer'
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

FFS_SEED = 42
FFS_MIN_FEATURES = 1

PASSTHROUGH_OPERATORS = [
    'Incremental Sort',
    'Merge Join',
    'Limit',
    'Sort',
    'Hash',
    'Gather Merge',
    'Aggregate'
]


# FUNCTIONS

# Check if operator is pass-through
def is_passthrough_operator(operator_type: str) -> bool:
    return operator_type in PASSTHROUGH_OPERATORS

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
