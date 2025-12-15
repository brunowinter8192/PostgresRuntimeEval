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
