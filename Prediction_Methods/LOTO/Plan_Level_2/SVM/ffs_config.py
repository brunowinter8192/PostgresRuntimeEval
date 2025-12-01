#!/usr/bin/env python3

# INFRASTRUCTURE

# Metadata columns to exclude from features
METADATA_COLUMNS = ['query_file', 'template', 'runtime']

# Target column
TARGET = 'runtime'

# Forward feature selection parameters
FFS_CONFIG = {
    'min_features': 10,
    'seeds': [42],
    'n_splits': 5
}

# SVM model configuration
SVM_CONFIG = {
    'class_name': 'NuSVR',
    'module': 'sklearn.svm',
    'use_scaler': True,
    'scaler_class': 'MaxAbsScaler',
    'scaler_module': 'sklearn.preprocessing',
    'params': {
        'kernel': 'rbf',
        'nu': 0.5,
        'C': 5.0,
        'gamma': 'scale',
        'cache_size': 500
    }
}
