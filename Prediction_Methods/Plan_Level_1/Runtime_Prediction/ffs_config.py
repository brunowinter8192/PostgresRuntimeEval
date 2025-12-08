"""
Forward Feature Selection configuration for Plan_Level_1 workflow.

Contains shared FFS parameters and model registry for all baseline models.
Each model loads selected features dynamically from FFS CSV output (01_multi_seed_summary.csv).

No hardcoded feature lists - all features are determined through FFS and stored in CSV.
"""

# Forward feature selection parameters
FFS_CONFIG = {
    'min_features': 1,            # Minimum features to select before stopping
    'seeds': [42],                # Random seed for cross-validation
    'n_splits': 5                 # Number of CV folds
}

# Model registry with configurations for all baseline models
MODEL_REGISTRY = {
    'svm': {
        'name': 'SVM',
        'class_name': 'NuSVR',
        'module': 'sklearn.svm',
        'use_scaler': True,
        'scaler_class': 'MaxAbsScaler',
        'scaler_module': 'sklearn.preprocessing',
        'output_folder': 'SVM',
        'params': {
            'kernel': 'rbf',
            'nu': 0.5,
            'C': 5.0,
            'gamma': 'scale',
            'cache_size': 500
        }
    },
    'random_forest': {
        'name': 'RandomForest',
        'class_name': 'RandomForestRegressor',
        'module': 'sklearn.ensemble',
        'use_scaler': False,
        'output_folder': 'Random_Forest',
        'params': {
            'n_estimators': 1000,
            'max_depth': None,
            'min_samples_split': 2,
            'min_samples_leaf': 1,
            'max_features': 'sqrt',
            'bootstrap': True,
            'oob_score': True,
            'n_jobs': -1,
            'random_state': 42,
            'verbose': 0,
            'warm_start': False,
            'max_samples': None
        }
    },
    'xgboost': {
        'name': 'XGBoost',
        'class_name': 'XGBRegressor',
        'module': 'xgboost',
        'use_scaler': False,
        'output_folder': 'XGBoost',
        'params': {
            'objective': 'reg:squarederror',
            'max_depth': 7,
            'min_child_weight': 5,
            'learning_rate': 0.05,
            'n_estimators': 1000,
            'reg_alpha': 1.0,
            'reg_lambda': 5.0,
            'gamma': 0.5,
            'subsample': 0.8,
            'colsample_bytree': 0.6,
            'colsample_bylevel': 0.7,
            'tree_method': 'hist',
            'max_bin': 256,
            'n_jobs': -1,
            'random_state': 42
        }
    }
}
