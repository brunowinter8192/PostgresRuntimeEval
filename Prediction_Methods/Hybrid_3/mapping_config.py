#!/usr/bin/env python3

# INFRASTRUCTURE

PATTERNS = [
    'Aggregate_Aggregate_Outer',
    'Aggregate_Gather_Merge_Outer',
    'Aggregate_Gather_Outer',
    'Aggregate_Hash_Join_Outer',
    'Aggregate_Index_Scan_Outer',
    'Aggregate_Nested_Loop_Outer',
    'Aggregate_Seq_Scan_Outer',
    'Aggregate_Sort_Outer',
    'Gather_Aggregate_Outer',
    'Gather_Hash_Join_Outer',
    'Gather_Merge_Aggregate_Outer',
    'Gather_Merge_Incremental_Sort_Outer',
    'Gather_Merge_Sort_Outer',
    'Gather_Nested_Loop_Outer',
    'Hash_Join_Hash_Join_Outer_Hash_Inner',
    'Hash_Join_Nested_Loop_Outer_Hash_Inner',
    'Hash_Join_Seq_Scan_Outer_Hash_Inner',
    'Nested_Loop_Hash_Join_Outer_Index_Scan_Inner',
    'Nested_Loop_Merge_Join_Outer_Index_Scan_Inner',
    'Nested_Loop_Seq_Scan_Outer_Index_Scan_Inner'
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

PASSTHROUGH_OPERATORS = [
    'Incremental Sort',
    'Merge Join',
    'Limit',
    'Sort',
    'Hash'
]


# FUNCTIONS

# Check if operator is pass-through
def is_passthrough_operator(operator_type: str) -> bool:
    return operator_type in PASSTHROUGH_OPERATORS
