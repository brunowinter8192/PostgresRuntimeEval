"""
Central mapping configuration for Plan_Level_1 workflow.

Defines dataset structure with explicit feature and metadata mappings
based on complete_dataset.csv. Used across Data_Generation and
Runtime_Prediction modules.

For forward feature selection configuration, see ffs_config.py.
"""

# INFRASTRUCTURE

# Database connection settings for TPC-H benchmark
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'tpch',
    'user': 'postgres',
    'password': 'postgres'
}

# Docker container name for PostgreSQL
CONTAINER_NAME = 'tpch-postgres'

# Metadata columns
PLAN_METADATA = ['query_file', 'template']

# Target column
PLAN_TARGET = 'runtime'

# Operator types tracked in feature extraction
OPERATOR_TYPES = [
    'Aggregate',
    'Gather',
    'Gather Merge',
    'Hash',
    'Hash Join',
    'Incremental Sort',
    'Index Only Scan',
    'Index Scan',
    'Limit',
    'Merge Join',
    'Nested Loop',
    'Seq Scan',
    'Sort'
]

# Backwards compatibility: columns to exclude from feature analysis
METADATA_COLUMNS = PLAN_METADATA + [PLAN_TARGET]

# Features to remove when transforming Baseline to State_1
FEATURES_TO_REMOVE_FOR_STATE_1 = [
    'workers_planned',
    'parallel_aware_count',
    'max_tree_depth',
    'planning_time_ms',
    'jit_functions',
    'subplan_count',
    'initplan_count',
    'strategy_hashed',
    'strategy_plain',
    'strategy_sorted',
    'partial_mode_simple',
    'partial_mode_partial',
    'partial_mode_finalize',
    'group_key_count',
    'group_key_columns',
    'sort_key_count',
    'sort_key_columns'
]


# FUNCTIONS

# Get all State_1 dataset columns in correct order
def get_state_1_columns():
    structural = ['p_st_cost', 'p_tot_cost', 'p_rows', 'p_width', 'op_count']
    result = ['row_count', 'byte_count']
    operator_cols = [
        f"{op.replace(' ', '_')}_{metric}"
        for op in OPERATOR_TYPES
        for metric in ['cnt', 'rows']
    ]
    return PLAN_METADATA + structural + result + operator_cols + [PLAN_TARGET]
