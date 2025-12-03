#!/usr/bin/env python3

# INFRASTRUCTURE

# Pattern threshold for dynamic pattern search
THRESHOLD = 151

# Child timing features to remove from test sets
CHILD_FEATURES_TIMING = ['st1', 'rt1', 'st2', 'rt2']

# Fixed feature set for operator-level prediction
CHILD_FEATURES = ['nt1', 'nt2', 'st1', 'rt1', 'st2', 'rt2']
BASE_FEATURES = ['total_cost', 'plan_width', 'sel', 'startup_cost']
FEATURE_SET = CHILD_FEATURES + BASE_FEATURES


