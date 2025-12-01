#!/usr/bin/env python3

# INFRASTRUCTURE

# Pattern hash IDs extracted from Data_Generation/csv/01_patterns_20251124_133434.csv
# Pass-through operators excluded as pattern roots (startup_total_ratio > 0.95)
# All patterns with > 120 occurrences, lengths 2-9
# Total: 32 patterns
PATTERNS = [
    '895c6e8c1a30a094329d71cef3111fbd',
    '2e0f44eff91c745724a56159cf7e0d6f',
    '3cfa90d7df3cd40936e985146fc5ec76',
    'c53c43965386239f53c764b9a60720dd',
    '634cdbe24fda21720ccd3dc746d5c979',
    '7d4e78be851232c5a0cc7a0cf9df4593',
    'f4cb205adfd108034c883c87871a6da8',
    'bb9308256700fc12e4125487e887832e',
    'e0e3c3e1b229568ff01695a42f46d8ea',
    '2422d11162cb474bacd9ebfa0bc68bb2',
    '2e8f3f675d9e1253d227c0b1edebeefb',
    '30d6e09bdb501c499cb36578168e324f',
    '2873b8c3a1759afe345ffbdfc9bdcba7',
    '37515ad868a103fed23cf07c65b8a248',
    'bd9dfa7bb8f3b0473cdfb5cd4277dc3a',
    'af27a52b75459a4f4068970057686d71',
    '7a51ce50a8f4529f944f9df797fa04b8',
    '4db0722060ee43c47566ae44a34d98aa',
    '9d0e407c0aa5052a4246612a4a2e0ad2',
    '545b5e576c5930d559d8e42d610637d8',
    'ec92bdaa27b47a2a45a6787f34350878',
    '422b9b8c0f34b5a74aeec7b834afb9ea',
    '440e6274a192d28a59f1aa9e2963c5a5',
    'f4603221ed908983d5775a3734bacac0',
    '5bfce15946616546d0be06b28c79e909',
    'e1d7e5b4b64fa2791f32be783ffb6013',
    '3d4c3db9a0977643bddc82d44c93492c',
    'ef93d4fc6e5b9506d1cf51950a1c2be7',
    'c302739ba5fe522ac572bfdbdd8c26e9',
    '9ce781b0006e0486de27d9cf912f5f3b',
    '5ae97df8a6895acd1a7e15f6e5b6f95f',
    'a95bee4e9ae59bc7fb7a48a1a7973a31'
]

# Operator count per pattern (number of nodes in pattern structure)
# Calculated from Datasets/Baseline/<hash>/training.csv using formula: actual_rows / occurrence_count
PATTERN_OPERATOR_COUNT = {
    '895c6e8c1a30a094329d71cef3111fbd': 3,
    '2e0f44eff91c745724a56159cf7e0d6f': 3,
    '3cfa90d7df3cd40936e985146fc5ec76': 3,
    'c53c43965386239f53c764b9a60720dd': 3,
    '634cdbe24fda21720ccd3dc746d5c979': 2,
    '7d4e78be851232c5a0cc7a0cf9df4593': 3,
    'f4cb205adfd108034c883c87871a6da8': 4,
    'bb9308256700fc12e4125487e887832e': 4,
    'e0e3c3e1b229568ff01695a42f46d8ea': 5,
    '2422d11162cb474bacd9ebfa0bc68bb2': 6,
    '2e8f3f675d9e1253d227c0b1edebeefb': 3,
    '30d6e09bdb501c499cb36578168e324f': 6,
    '2873b8c3a1759afe345ffbdfc9bdcba7': 6,
    '37515ad868a103fed23cf07c65b8a248': 6,
    'bd9dfa7bb8f3b0473cdfb5cd4277dc3a': 6,
    'af27a52b75459a4f4068970057686d71': 5,
    '7a51ce50a8f4529f944f9df797fa04b8': 9,
    '4db0722060ee43c47566ae44a34d98aa': 8,
    '9d0e407c0aa5052a4246612a4a2e0ad2': 8,
    '545b5e576c5930d559d8e42d610637d8': 7,
    'ec92bdaa27b47a2a45a6787f34350878': 7,
    '422b9b8c0f34b5a74aeec7b834afb9ea': 6,
    '440e6274a192d28a59f1aa9e2963c5a5': 9,
    'f4603221ed908983d5775a3734bacac0': 11,
    '5bfce15946616546d0be06b28c79e909': 9,
    'e1d7e5b4b64fa2791f32be783ffb6013': 9,
    '3d4c3db9a0977643bddc82d44c93492c': 12,
    'ef93d4fc6e5b9506d1cf51950a1c2be7': 11,
    'c302739ba5fe522ac572bfdbdd8c26e9': 10,
    '9ce781b0006e0486de27d9cf912f5f3b': 14,
    '5ae97df8a6895acd1a7e15f6e5b6f95f': 12,
    'a95bee4e9ae59bc7fb7a48a1a7973a31': 15,
}

# Pattern leaf timing features to retain during cleaning
# Generated from Data_Generation/csv/02_pattern_leafs_20251124_133954.csv
# Format: {hash: [list of timing feature column names]}
PATTERN_LEAF_TIMING_FEATURES = {
    '895c6e8c1a30a094329d71cef3111fbd': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '2e0f44eff91c745724a56159cf7e0d6f': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'NestedLoop_Outer_st1', 'NestedLoop_Outer_rt1', 'NestedLoop_Outer_st2', 'NestedLoop_Outer_rt2'],
    '3cfa90d7df3cd40936e985146fc5ec76': ['HashJoin_Outer_st1', 'HashJoin_Outer_rt1', 'HashJoin_Outer_st2', 'HashJoin_Outer_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2'],
    'c53c43965386239f53c764b9a60720dd': ['IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '634cdbe24fda21720ccd3dc746d5c979': ['Aggregate_Outer_st1', 'Aggregate_Outer_rt1', 'Aggregate_Outer_st2', 'Aggregate_Outer_rt2'],
    '7d4e78be851232c5a0cc7a0cf9df4593': ['HashJoin_Outer_st1', 'HashJoin_Outer_rt1', 'HashJoin_Outer_st2', 'HashJoin_Outer_rt2', 'Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2'],
    'f4cb205adfd108034c883c87871a6da8': ['SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    'bb9308256700fc12e4125487e887832e': ['HashJoin_Outer_st1', 'HashJoin_Outer_rt1', 'HashJoin_Outer_st2', 'HashJoin_Outer_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    'e0e3c3e1b229568ff01695a42f46d8ea': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '2422d11162cb474bacd9ebfa0bc68bb2': ['HashJoin_Outer_st1', 'HashJoin_Outer_rt1', 'HashJoin_Outer_st2', 'HashJoin_Outer_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '2e8f3f675d9e1253d227c0b1edebeefb': ['HashJoin_Outer_st1', 'HashJoin_Outer_rt1', 'HashJoin_Outer_st2', 'HashJoin_Outer_rt2'],
    '30d6e09bdb501c499cb36578168e324f': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'NestedLoop_Outer_st1', 'NestedLoop_Outer_rt1', 'NestedLoop_Outer_st2', 'NestedLoop_Outer_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '2873b8c3a1759afe345ffbdfc9bdcba7': ['IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '37515ad868a103fed23cf07c65b8a248': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    'bd9dfa7bb8f3b0473cdfb5cd4277dc3a': ['HashJoin_Outer_st1', 'HashJoin_Outer_rt1', 'HashJoin_Outer_st2', 'HashJoin_Outer_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    'af27a52b75459a4f4068970057686d71': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '7a51ce50a8f4529f944f9df797fa04b8': ['IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '4db0722060ee43c47566ae44a34d98aa': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '9d0e407c0aa5052a4246612a4a2e0ad2': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '545b5e576c5930d559d8e42d610637d8': ['SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    'ec92bdaa27b47a2a45a6787f34350878': ['HashJoin_Outer_st1', 'HashJoin_Outer_rt1', 'HashJoin_Outer_st2', 'HashJoin_Outer_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '422b9b8c0f34b5a74aeec7b834afb9ea': ['SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '440e6274a192d28a59f1aa9e2963c5a5': ['HashJoin_Outer_st1', 'HashJoin_Outer_rt1', 'HashJoin_Outer_st2', 'HashJoin_Outer_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    'f4603221ed908983d5775a3734bacac0': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '5bfce15946616546d0be06b28c79e909': ['HashJoin_Outer_st1', 'HashJoin_Outer_rt1', 'HashJoin_Outer_st2', 'HashJoin_Outer_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    'e1d7e5b4b64fa2791f32be783ffb6013': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '3d4c3db9a0977643bddc82d44c93492c': ['HashJoin_Outer_st1', 'HashJoin_Outer_rt1', 'HashJoin_Outer_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    'ef93d4fc6e5b9506d1cf51950a1c2be7': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    'c302739ba5fe522ac572bfdbdd8c26e9': ['SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '9ce781b0006e0486de27d9cf912f5f3b': ['Hash_Inner_st1', 'Hash_Inner_rt1', 'Hash_Inner_st2', 'Hash_Inner_rt2', 'IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    '5ae97df8a6895acd1a7e15f6e5b6f95f': ['IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
    'a95bee4e9ae59bc7fb7a48a1a7973a31': ['IndexScan_Inner_st1', 'IndexScan_Inner_rt1', 'IndexScan_Inner_st2', 'IndexScan_Inner_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_rt1', 'SeqScan_Outer_st2', 'SeqScan_Outer_rt2'],
}

# Target types for two-step feature selection
TARGET_TYPES = ['execution_time', 'start_time']

# Target type to column name mapping
TARGET_NAME_MAP = {
    'execution_time': 'actual_total_time',
    'start_time': 'actual_startup_time'
}

# Column suffixes to exclude from feature selection (structural metadata)
# These columns provide structural information but are not predictive features
NON_FEATURE_SUFFIXES = [
    '_node_id',
    '_node_type',
    '_depth',
    '_parent_relationship',
    '_subplan_name',
    'actual_startup_time',
    'actual_total_time'
]

# Forward Feature Selection configuration
# Synchronized with Runtime_Prediction/ffs_config.py values
FFS_SEED = 42
FFS_MIN_FEATURES = 1

# Pass-through operators with startup_total_ratio > 0.95
# Operators where actual_startup_time / actual_total_time > 0.95
# Source: operator_runtime_analysis_20251124_132539.csv
PASSTHROUGH_OPERATORS = [
    'Incremental Sort',
    'Merge Join',
    'Sort',
    'Hash',
    'Limit',
    'Gather Merge',
    'Aggregate'
]


# FUNCTIONS

# Check if operator is pass-through
def is_passthrough_operator(operator_type: str) -> bool:
    return operator_type in PASSTHROUGH_OPERATORS
