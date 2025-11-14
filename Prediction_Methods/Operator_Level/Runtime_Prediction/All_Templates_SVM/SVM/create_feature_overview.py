#!/usr/bin/env python3

import sys
import pandas as pd
from pathlib import Path


CHILD_FEATURES = {'st1', 'rt1', 'st2', 'rt2', 'nt1', 'nt2'}

NEEDS_CHILD_FEATURES = [
    'Aggregate', 'Hash_Join', 'Hash', 'Sort', 'Gather',
    'Gather_Merge', 'Limit', 'Nested_Loop', 'Merge_Join',
    'Incremental_Sort'
]

NO_CHILD_FEATURES_NEEDED = ['Seq_Scan', 'Index_Scan', 'Index_Only_Scan']

OPERATORS = [
    'Aggregate', 'Gather', 'Gather_Merge', 'Hash', 'Hash_Join',
    'Incremental_Sort', 'Index_Only_Scan', 'Index_Scan', 'Limit',
    'Merge_Join', 'Nested_Loop', 'Seq_Scan', 'Sort'
]

TARGETS = ['execution_time', 'start_time']


def generate_overview_workflow(svm_dir, output_dir):
    overview_data = collect_operator_target_data(svm_dir)
    overview_df = create_overview_dataframe(overview_data)
    export_overview(overview_df, output_dir)


# Collect feature selection results for all operator-target combinations
def collect_operator_target_data(svm_dir):
    overview_data = []
    
    for operator in OPERATORS:
        for target in TARGETS:
            target_dir = Path(svm_dir) / target
            result = analyze_operator_target(operator, target, target_dir)
            
            if result:
                overview_data.append(result)
    
    return overview_data


# Analyze feature selection results for single operator-target combination
def analyze_operator_target(operator, target, target_dir):
    operator_csv_dir = target_dir / f'{operator}_csv'
    
    selected_file = operator_csv_dir / 'selected_features_seed42.csv'
    results_file = operator_csv_dir / 'ffs_results_seed42.csv'
    
    if not selected_file.exists() or not results_file.exists():
        return None
    
    selected_df = pd.read_csv(selected_file, delimiter=';')
    results_df = pd.read_csv(results_file, delimiter=';')
    
    original_features = set(selected_df['feature'].tolist())
    original_count = len(original_features)
    
    selected_rows = results_df[results_df['was_selected'] == True]
    if len(selected_rows) > 0:
        mre_original = selected_rows.iloc[-1]['mre']
    else:
        mre_original = None
    
    if operator in NO_CHILD_FEATURES_NEEDED:
        has_all_child_features = True
        child_complete_iteration = None
        final_features = original_features
        final_count = original_count
        mre_final = mre_original
    
    elif operator in NEEDS_CHILD_FEATURES:
        has_all_child_features = CHILD_FEATURES.issubset(original_features)
        
        if has_all_child_features:
            child_complete_iteration = None
            final_features = original_features
            final_count = original_count
            mre_final = mre_original
        else:
            child_features_found = set()
            child_complete_iteration = None
            features_up_to_iteration = []
            
            for _, row in results_df.iterrows():
                feature = row['feature_tested']
                iteration = row['iteration']
                
                features_up_to_iteration.append(feature)
                
                if feature in CHILD_FEATURES:
                    child_features_found.add(feature)
                
                if len(child_features_found) == 6:
                    child_complete_iteration = iteration
                    mre_final = row['mre']
                    break
            
            if child_complete_iteration is not None:
                final_features = set(features_up_to_iteration)
                final_count = len(final_features)
            else:
                final_features = original_features
                final_count = original_count
                mre_final = mre_original
                child_complete_iteration = 'INCOMPLETE'
    
    return {
        'operator': operator,
        'target': target,
        'original_count': original_count,
        'has_all_child_features': has_all_child_features,
        'child_complete_iteration': child_complete_iteration if child_complete_iteration else '',
        'final_count': final_count,
        'selected_features_ffs': ', '.join(sorted(original_features)),
        'final_features': ', '.join(sorted(final_features)),
        'mre_original': f'{mre_original:.4f}' if mre_original is not None else '',
        'mre_final': f'{mre_final:.4f}' if mre_final is not None else ''
    }


# Create DataFrame from collected operator-target data
def create_overview_dataframe(overview_data):
    return pd.DataFrame(overview_data)


# Save feature overview to CSV file
def export_overview(overview_df, output_dir):
    output_path = Path(output_dir) / 'feature_selection_overview.csv'
    overview_df.to_csv(output_path, index=False, sep=';')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    
    svm_directory = sys.argv[1]
    output_directory = sys.argv[2]
    
    generate_overview_workflow(svm_directory, output_directory)
