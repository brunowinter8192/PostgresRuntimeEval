#!/usr/bin/env python3

# INFRASTRUCTURE

SEED = 42
MIN_FEATURES = 1

SPARSE_FEATURES_MAP = {
    'Seq_Scan': ['nt1', 'nt2', 'startup_cost', 'parallel_workers', 'st1', 'rt1', 'st2', 'rt2'],
    'Index_Scan': ['nt1', 'nt2', 'parallel_workers', 'st1', 'rt1', 'st2', 'rt2'],
    'Index_Only_Scan': ['nt1', 'nt2', 'parallel_workers', 'st1', 'rt1', 'st2', 'rt2']
}

SVM_PARAMS = {
    'kernel': 'rbf',
    'nu': 0.65,
    'C': 1.5,
    'gamma': 'scale',
    'cache_size': 500
}
