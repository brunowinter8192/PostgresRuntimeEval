#!/usr/bin/env python3

# INFRASTRUCTURE

SEED = 42
MIN_FEATURES = 1

SVM_PARAMS = {
    'kernel': 'rbf',
    'nu': 0.65,
    'C': 1.5,
    'gamma': 'scale',
    'cache_size': 500
}

TARGET_TYPES = ['execution_time', 'start_time']

TARGET_NAME_MAP = {
    'execution_time': 'actual_total_time',
    'start_time': 'actual_startup_time'
}

OPERATOR_METADATA = ['query_file', 'node_id', 'depth', 'parent_relationship', 'subplan_name']

OPERATOR_TARGETS = ['actual_startup_time', 'actual_total_time']

CHILD_FEATURES = ['st1', 'rt1', 'st2', 'rt2', 'nt1', 'nt2']

CHILD_FEATURES_TIMING = ['st1', 'rt1', 'st2', 'rt2']

LEAF_OPERATORS = ['Seq Scan', 'Index Scan', 'Index Only Scan']
