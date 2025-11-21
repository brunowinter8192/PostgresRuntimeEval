#!/usr/bin/env python3

# Infrastructure
import sys
import pandas as pd
from pathlib import Path
from datetime import datetime

PATTERNS = [
    'Hash_Join_Seq_Scan_Outer_Hash_Inner',
    'Hash_Seq_Scan_Outer',
    'Hash_Hash_Join_Outer',
    'Hash_Join_Nested_Loop_Outer_Hash_Inner',
    'Nested_Loop_Hash_Join_Outer_Index_Scan_Inner',
    'Sort_Hash_Join_Outer',
    'Nested_Loop_Seq_Scan_Outer_Index_Scan_Inner',
    'Gather_Aggregate_Outer',
    'Aggregate_Hash_Join_Outer',
    'Aggregate_Gather_Outer',
    'Aggregate_Seq_Scan_Outer',
    'Hash_Join_Hash_Join_Outer_Hash_Inner',
    'Aggregate_Nested_Loop_Outer',
    'Sort_Nested_Loop_Outer',
    'Incremental_Sort_Nested_Loop_Outer',
    'Nested_Loop_Merge_Join_Outer_Index_Scan_Inner',
    'Hash_Aggregate_Outer',
    'Sort_Seq_Scan_Outer',
    'Gather_Nested_Loop_Outer',
    'Gather_Hash_Join_Outer',
    'Hash_Index_Only_Scan_Outer'
]

PASSTHROUGH_OPERATORS = {'Incremental Sort', 'Merge Join', 'Limit', 'Sort', 'Hash'}

# Orchestrator
def run_execution_plan_workflow(operator_dataset_file, query_name, pattern_overview_file, operator_overview_file, output_dir):
    df_operators = load_operator_dataset(operator_dataset_file, query_name)
    df_patterns = load_pattern_overview(pattern_overview_file)
    df_operator_features = load_operator_overview(operator_overview_file)
    pattern_features = extract_pattern_features(df_patterns)
    operator_features = extract_operator_features(df_operator_features)
    execution_plan = build_execution_plan_bottom_up(df_operators, pattern_features)
    export_execution_plan(execution_plan, output_dir, query_name, df_operators, pattern_features, operator_features)


# Load operator dataset and filter for specific query
def load_operator_dataset(dataset_file, query_name):
    df = pd.read_csv(dataset_file, delimiter=';')
    df_query = df[df['query_file'] == query_name].copy()
    df_query = df_query[df_query['subplan_name'].isna() | (df_query['subplan_name'] == '')]
    return df_query.sort_values('node_id').reset_index(drop=True)

# Load pattern overview from CSV file
def load_pattern_overview(pattern_file):
    return pd.read_csv(pattern_file, delimiter=';')

# Load operator feature overview from CSV file
def load_operator_overview(operator_file):
    return pd.read_csv(operator_file, delimiter=';')

# Extract pattern features and child requirements
def extract_pattern_features(df_patterns):
    pattern_dict = {}
    for _, row in df_patterns.iterrows():
        pattern_name = row['pattern']
        if pattern_name not in pattern_dict:
            pattern_dict[pattern_name] = {}
        
        target = row['target']
        final_features = [f.strip() for f in row['final_features'].split(',')]
        missing_child = [] if pd.isna(row['missing_child_features']) else [f.strip() for f in row['missing_child_features'].split(',')]
        
        pattern_dict[pattern_name][target] = {
            'final_features': final_features,
            'missing_child_features': missing_child
        }
    
    return pattern_dict

# Extract operator features from overview
def extract_operator_features(df_operators):
    operator_dict = {}

    if 'operator' not in df_operators.columns:
        return operator_dict

    for _, row in df_operators.iterrows():
        operator = row['operator']
        if operator not in operator_dict:
            operator_dict[operator] = {}

        target = row['target']
        final_features = [f.strip() for f in row['final_features'].split(',')]

        operator_dict[operator][target] = {
            'final_features': final_features
        }

    return operator_dict

# Build execution plan bottom-up from deepest depth to root
def build_execution_plan_bottom_up(df_operators, pattern_features):
    plan_steps = []
    consumed_by_pattern = set()
    consumed_by_operator = set()
    predictions = {}
    max_depth = df_operators['depth'].max()
    
    for depth in range(max_depth, -1, -1):
        operators_at_depth = df_operators[df_operators['depth'] == depth]
        
        for idx in operators_at_depth.index:
            if idx in consumed_by_pattern or idx in consumed_by_operator:
                continue
            
            op_row = df_operators.loc[idx]
            parent_idx = find_parent_operator(df_operators, idx)
            
            if parent_idx is None:
                children_info = get_children_info(df_operators, idx)
                aggregated_row = build_operator_aggregated_row(df_operators, idx, predictions)
                step = create_operator_step(op_row, children_info, predictions, aggregated_row)
                plan_steps.append(step)
                consumed_by_operator.add(idx)
                pred_key = (op_row['node_type'], op_row['depth'])
                predictions[pred_key] = {'predicted_startup_time': 0.0, 'predicted_total_time': 0.0}
                continue
            
            if parent_idx in consumed_by_operator or parent_idx in consumed_by_pattern:
                continue
            
            parent_row = df_operators.loc[parent_idx]

            if parent_row['depth'] < 1:
                continue

            siblings_indices = find_all_siblings(df_operators, idx, parent_idx)
            
            if any(sib_idx in consumed_by_pattern or sib_idx in consumed_by_operator for sib_idx in siblings_indices):
                continue
            
            children_info = build_children_info_list(df_operators, siblings_indices)
            pattern_match = try_match_pattern_with_parent(parent_row, children_info, pattern_features, predictions, df_operators)
            
            if pattern_match:
                aggregated_row = aggregate_pattern_rows(df_operators, parent_idx, siblings_indices, predictions)
                step = create_pattern_step(parent_row, children_info, pattern_match, pattern_features, aggregated_row)
                plan_steps.append(step)
                
                consumed_by_pattern.add(parent_idx)
                for sib_idx in siblings_indices:
                    consumed_by_pattern.add(sib_idx)
                
                pred_key = (parent_row['node_type'], parent_row['depth'])
                predictions[pred_key] = {'predicted_startup_time': 0.0, 'predicted_total_time': 0.0}
        
        for idx in operators_at_depth.index:
            if idx in consumed_by_pattern or idx in consumed_by_operator:
                continue

            op_row = df_operators.loc[idx]
            children_info = get_children_info(df_operators, idx)
            aggregated_row = build_operator_aggregated_row(df_operators, idx, predictions)
            step = create_operator_step(op_row, children_info, predictions, aggregated_row)
            plan_steps.append(step)
            consumed_by_operator.add(idx)
            pred_key = (op_row['node_type'], op_row['depth'])

            if step['type'] == 'passthrough':
                predictions[pred_key] = {
                    'predicted_startup_time': step['predicted_startup_time'],
                    'predicted_total_time': step['predicted_total_time']
                }
            else:
                predictions[pred_key] = {'predicted_startup_time': 0.0, 'predicted_total_time': 0.0}
    
    return plan_steps


# Aggregate pattern rows from parent and children
def aggregate_pattern_rows(df_operators, parent_idx, children_indices, predictions):
    parent_row = df_operators.loc[parent_idx]
    aggregated = {}
    
    aggregated['query_file'] = parent_row['query_file']
    
    parent_normalized = parent_row['node_type'].replace(' ', '')
    parent_prefix = parent_normalized + '_'
    
    for col in parent_row.index:
        if col not in ['query_file']:
            aggregated[parent_prefix + col] = parent_row[col]
    
    children_sorted = []
    for child_idx in children_indices:
        child_row = df_operators.loc[child_idx]
        children_sorted.append({
            'row': child_row,
            'index': child_idx,
            'relationship': child_row['parent_relationship'],
            'node_type': child_row['node_type']
        })
    
    children_sorted = sorted(children_sorted, key=lambda x: (0 if x['relationship'] == 'Outer' else 1))
    
    for child in children_sorted:
        child_row = child['row']
        child_idx = child['index']
        child_normalized = child['node_type'].replace(' ', '')
        child_prefix = child_normalized + '_' + child['relationship'] + '_'
        
        for col in child_row.index:
            if col not in ['query_file', 'st1', 'rt1', 'st2', 'rt2']:
                aggregated[child_prefix + col] = child_row[col]
        
        grandchildren = get_children_info(df_operators, child_idx)
        
        aggregated[child_prefix + 'st1'] = 0.0
        aggregated[child_prefix + 'rt1'] = 0.0
        aggregated[child_prefix + 'st2'] = 0.0
        aggregated[child_prefix + 'rt2'] = 0.0
        
        for grandchild in grandchildren:
            pred_key = (grandchild['node_type'], grandchild['depth'])
            if pred_key in predictions:
                if grandchild['parent_relationship'] == 'Outer':
                    aggregated[child_prefix + 'st1'] = predictions[pred_key]['predicted_startup_time']
                    aggregated[child_prefix + 'rt1'] = predictions[pred_key]['predicted_total_time']
                elif grandchild['parent_relationship'] == 'Inner':
                    aggregated[child_prefix + 'st2'] = predictions[pred_key]['predicted_startup_time']
                    aggregated[child_prefix + 'rt2'] = predictions[pred_key]['predicted_total_time']
    
    return aggregated

# Build operator aggregated row with child predictions
def build_operator_aggregated_row(df_operators, operator_idx, predictions):
    op_row = df_operators.loc[operator_idx]
    aggregated = dict(op_row)
    
    children = get_children_info(df_operators, operator_idx)
    
    aggregated['st1'] = 0.0
    aggregated['rt1'] = 0.0
    aggregated['st2'] = 0.0
    aggregated['rt2'] = 0.0
    
    for child in children:
        pred_key = (child['node_type'], child['depth'])
        if pred_key in predictions:
            if child['parent_relationship'] == 'Outer':
                aggregated['st1'] = predictions[pred_key]['predicted_startup_time']
                aggregated['rt1'] = predictions[pred_key]['predicted_total_time']
            elif child['parent_relationship'] == 'Inner':
                aggregated['st2'] = predictions[pred_key]['predicted_startup_time']
                aggregated['rt2'] = predictions[pred_key]['predicted_total_time']
    
    return aggregated


# Get children information for operator
def get_children_info(df_query, parent_idx):
    parent_row = df_query.loc[parent_idx]
    parent_depth = parent_row['depth']
    children = []
    
    for idx in range(parent_idx + 1, len(df_query)):
        row = df_query.iloc[idx]
        if row['depth'] == parent_depth + 1:
            children.append({
                'index': df_query.index[idx],
                'node_type': row['node_type'],
                'depth': row['depth'],
                'parent_relationship': row['parent_relationship']
            })
        elif row['depth'] <= parent_depth:
            break
    
    return children

# Find parent operator for given operator
def find_parent_operator(df_operators, operator_idx):
    op_row = df_operators.loc[operator_idx]
    op_depth = op_row['depth']
    
    if op_depth == 0:
        return None
    
    for idx in range(operator_idx - 1, -1, -1):
        row = df_operators.iloc[idx]
        if row['depth'] == op_depth - 1:
            return df_operators.index[idx]
    
    return None

# Find all siblings of operator including itself
def find_all_siblings(df_operators, operator_idx, parent_idx):
    parent_row = df_operators.loc[parent_idx]
    parent_depth = parent_row['depth']
    siblings = []
    
    for idx in range(parent_idx + 1, len(df_operators)):
        row = df_operators.iloc[idx]
        if row['depth'] == parent_depth + 1:
            siblings.append(df_operators.index[idx])
        elif row['depth'] <= parent_depth:
            break
    
    return siblings

# Build children info list from sibling indices
def build_children_info_list(df_operators, sibling_indices):
    children_info = []
    for idx in sibling_indices:
        row = df_operators.loc[idx]
        children_info.append({
            'index': idx,
            'node_type': row['node_type'],
            'depth': row['depth'],
            'parent_relationship': row['parent_relationship']
        })
    return children_info

# Try to match pattern with parent operator
def try_match_pattern_with_parent(parent_row, children_info, pattern_features, predictions, df_operators):
    if len(children_info) == 0:
        return None

    if parent_row['node_type'] in PASSTHROUGH_OPERATORS:
        return None

    pattern_key = build_pattern_key(parent_row['node_type'], children_info)

    if pattern_key not in PATTERNS:
        return None

    if pattern_key not in pattern_features:
        return None

    pattern_data = pattern_features[pattern_key]
    needs_child_features = len(pattern_data['execution_time']['missing_child_features']) > 0

    if needs_child_features:
        if not check_child_features_available(pattern_key, pattern_features, children_info, predictions, df_operators):
            return None

    return pattern_key

# Create pattern step entry for execution plan
def create_pattern_step(parent_row, children_info, pattern_key, pattern_features, aggregated_row):
    pattern_data = pattern_features[pattern_key]
    is_leaf = len(pattern_data['execution_time']['missing_child_features']) == 0
    
    operators = [(parent_row['node_type'], parent_row['depth'])]
    for child in children_info:
        operators.append((child['node_type'], child['depth']))
    
    return {
        'type': 'pattern',
        'pattern_name': pattern_key,
        'is_leaf': 'Leaf' if is_leaf else 'Non-Leaf',
        'operators': operators,
        'required_features_exec': pattern_data['execution_time']['final_features'],
        'required_features_start': pattern_data['start_time']['final_features'],
        'child_features_needed': pattern_data['execution_time']['missing_child_features'],
        'aggregated_row': aggregated_row
    }

# Create operator step entry for execution plan
def create_operator_step(op_row, children_info, predictions, aggregated_row):
    if op_row['node_type'] in PASSTHROUGH_OPERATORS:
        if len(children_info) == 1:
            child_key = (children_info[0]['node_type'], children_info[0]['depth'])
            if child_key in predictions:
                return {
                    'type': 'passthrough',
                    'operator': op_row['node_type'],
                    'depth': op_row['depth'],
                    'child': children_info[0],
                    'predicted_startup_time': predictions[child_key]['predicted_startup_time'],
                    'predicted_total_time': predictions[child_key]['predicted_total_time'],
                    'aggregated_row': aggregated_row
                }

    required_predictions = []
    for child in children_info:
        pred_key = (child['node_type'], child['depth'])
        if pred_key in predictions:
            required_predictions.append(pred_key)

    return {
        'type': 'operator',
        'operator': op_row['node_type'],
        'depth': op_row['depth'],
        'children': [(c['node_type'], c['depth']) for c in children_info],
        'required_child_predictions': required_predictions,
        'aggregated_row': aggregated_row
    }


# Build pattern key from operator and children
def build_pattern_key(parent_type, children_info):
    parent_normalized = parent_type.replace(' ', '_')
    
    if len(children_info) == 1:
        child_normalized = children_info[0]['node_type'].replace(' ', '_')
        relationship = children_info[0]['parent_relationship']
        return f"{parent_normalized}_{child_normalized}_{relationship}"
    
    if len(children_info) == 2:
        children_sorted = sorted(children_info, key=lambda x: (0 if x['parent_relationship'] == 'Outer' else 1))
        outer_normalized = children_sorted[0]['node_type'].replace(' ', '_')
        inner_normalized = children_sorted[1]['node_type'].replace(' ', '_')
        return f"{parent_normalized}_{outer_normalized}_Outer_{inner_normalized}_Inner"
    
    return None

# Check if child features are available for non-leaf pattern
def check_child_features_available(pattern_key, pattern_features, children_info, predictions, df_operators):
    pattern_data = pattern_features[pattern_key]
    missing_child_features = pattern_data['execution_time']['missing_child_features']
    
    if len(missing_child_features) == 0:
        return True
    
    for child in children_info:
        grandchildren = get_children_info(df_operators, child['index'])
        for grandchild in grandchildren:
            pred_key = (grandchild['node_type'], grandchild['depth'])
            if pred_key not in predictions:
                return False
    
    return True

# Format parent operator features for pattern
def format_pattern_parent_features(parent_op, parent_depth, parent_row, pattern_data, step):
    lines = [f"#### {parent_op} (Parent)", ""]
    
    parent_normalized = parent_op.replace(' ', '')
    prefix = parent_normalized + '_'
    
    exec_features = pattern_data['execution_time']['final_features']
    start_features = pattern_data['start_time']['final_features']
    
    parent_exec_features = [f for f in exec_features if f.startswith(prefix)]
    child_exec_features = [f for f in exec_features if not f.startswith(prefix)]
    
    lines.append("**Expected Features (execution_time model):**")
    for feat in exec_features:
        lines.append(f"- {feat}")
    lines.append("")
    
    lines.append("**Test Data Mapping (execution_time):**")
    for feat in parent_exec_features:
        base_feat = feat.replace(prefix, '')
        lines.append(f"- {base_feat} (row depth {parent_depth}) → {feat}")
    for child_feat in child_exec_features:
        lines.append(f"- {child_feat} (from child operator)")
    lines.append("")
    
    parent_start_features = [f for f in start_features if f.startswith(prefix)]
    child_start_features = [f for f in start_features if not f.startswith(prefix)]
    
    lines.append("**Expected Features (start_time model):**")
    for feat in start_features:
        lines.append(f"- {feat}")
    lines.append("")
    
    lines.append("**Test Data Mapping (start_time):**")
    for feat in parent_start_features:
        base_feat = feat.replace(prefix, '')
        lines.append(f"- {base_feat} (row depth {parent_depth}) → {feat}")
    for child_feat in child_start_features:
        lines.append(f"- {child_feat} (from child operator)")
    lines.append("")
    
    child_features = step.get('child_features_needed', [])
    if child_features:
        lines.append("**Child Features Needed:**")
        for feat in child_features:
            lines.append(f"- {feat}")
        lines.append("")
    
    return lines

# Format child operator features for pattern
def format_pattern_child_features(child_op, child_depth, child_row, relationship, pattern_data, step):
    lines = [f"#### {child_op} (Child {relationship})", ""]
    
    child_normalized = child_op.replace(' ', '')
    prefix = child_normalized + '_' + relationship + '_'
    
    exec_features = pattern_data['execution_time']['final_features']
    child_exec_features = [f for f in exec_features if f.startswith(prefix)]
    
    lines.append("**Expected Features (execution_time model):**")
    for feat in child_exec_features:
        lines.append(f"- {feat}")
    lines.append("")
    
    lines.append("**Test Data Mapping (execution_time):**")
    for feat in child_exec_features:
        base_feat = feat.replace(prefix, '')
        lines.append(f"- {base_feat} (row depth {child_depth}) → {feat}")
    lines.append("")
    
    start_features = pattern_data['start_time']['final_features']
    child_start_features = [f for f in start_features if f.startswith(prefix)]
    
    lines.append("**Expected Features (start_time model):**")
    for feat in child_start_features:
        lines.append(f"- {feat}")
    lines.append("")
    
    lines.append("**Test Data Mapping (start_time):**")
    for feat in child_start_features:
        base_feat = feat.replace(prefix, '')
        lines.append(f"- {base_feat} (row depth {child_depth}) → {feat}")
    lines.append("")
    
    return lines

# Format emitted targets for pattern
def format_pattern_emitted_targets(parent_op, parent_depth, parent_row):
    lines = [
        "**Emitted Targets:**",
        "- execution_time model → predicted_total_time",
        "- start_time model → predicted_startup_time",
        ""
    ]
    
    relationship = parent_row['parent_relationship']
    if pd.notna(relationship) and relationship != '':
        lines.append("**Targets to Features (for parent operator at depth {}):**".format(parent_depth - 1))
        if relationship == 'Outer':
            lines.append("- predicted_startup_time → st1")
            lines.append("- predicted_total_time → rt1")
        elif relationship == 'Inner':
            lines.append("- predicted_startup_time → st2")
            lines.append("- predicted_total_time → rt2")
        lines.append("")
    
    return lines

# Format operator features
def format_operator_features(operator, depth, op_row, op_data, step):
    lines = []
    
    exec_features = op_data['execution_time']['final_features']
    start_features = op_data['start_time']['final_features']
    
    static_features = ['np', 'nt', 'nt1', 'nt2', 'sel', 'startup_cost', 'total_cost', 'plan_width', 'reltuples', 'parallel_workers']
    child_features = ['st1', 'rt1', 'st2', 'rt2']
    
    lines.append("**Expected Features (execution_time model):**")
    for feat in exec_features:
        lines.append(f"- {feat}")
    lines.append("")
    
    exec_static = [f for f in exec_features if f in static_features]
    exec_child = [f for f in exec_features if f in child_features]
    
    lines.append("**Test Data Mapping (execution_time):**")
    for feat in exec_static:
        lines.append(f"- {feat} (row depth {depth}) → {feat}")
    lines.append("")
    
    if exec_child:
        lines.append("**Child Features from Predictions (execution_time):**")
        children_with_rel = []
        for child_type, child_depth in step['children']:
            rel = 'Outer' if 'rt1' in exec_child or 'st1' in exec_child else 'Inner'
            children_with_rel.append((child_type, child_depth, rel))
        
        if len(children_with_rel) == 2:
            children_with_rel[0] = (children_with_rel[0][0], children_with_rel[0][1], 'Outer')
            children_with_rel[1] = (children_with_rel[1][0], children_with_rel[1][1], 'Inner')
        
        for child_type, child_depth, rel in children_with_rel:
            if rel == 'Outer' and ('rt1' in exec_child or 'st1' in exec_child):
                if 'rt1' in exec_child:
                    lines.append(f"- {child_type} (depth {child_depth}, Outer) predicted_total_time → rt1")
                if 'st1' in exec_child:
                    lines.append(f"- {child_type} (depth {child_depth}, Outer) predicted_startup_time → st1")
            elif rel == 'Inner' and ('rt2' in exec_child or 'st2' in exec_child):
                if 'rt2' in exec_child:
                    lines.append(f"- {child_type} (depth {child_depth}, Inner) predicted_total_time → rt2")
                if 'st2' in exec_child:
                    lines.append(f"- {child_type} (depth {child_depth}, Inner) predicted_startup_time → st2")
        lines.append("")
    
    start_static = [f for f in start_features if f in static_features]
    start_child = [f for f in start_features if f in child_features]
    
    lines.append("**Expected Features (start_time model):**")
    for feat in start_features:
        lines.append(f"- {feat}")
    lines.append("")
    
    lines.append("**Test Data Mapping (start_time):**")
    for feat in start_static:
        lines.append(f"- {feat} (row depth {depth}) → {feat}")
    lines.append("")
    
    if start_child:
        lines.append("**Child Features from Predictions (start_time):**")
        children_with_rel = []
        for child_type, child_depth in step['children']:
            rel = 'Outer'
            children_with_rel.append((child_type, child_depth, rel))
        
        if len(children_with_rel) == 2:
            children_with_rel[0] = (children_with_rel[0][0], children_with_rel[0][1], 'Outer')
            children_with_rel[1] = (children_with_rel[1][0], children_with_rel[1][1], 'Inner')
        
        for child_type, child_depth, rel in children_with_rel:
            if rel == 'Outer':
                if 'rt1' in start_child:
                    lines.append(f"- {child_type} (depth {child_depth}, Outer) predicted_total_time → rt1")
                if 'st1' in start_child:
                    lines.append(f"- {child_type} (depth {child_depth}, Outer) predicted_startup_time → st1")
            elif rel == 'Inner':
                if 'rt2' in start_child:
                    lines.append(f"- {child_type} (depth {child_depth}, Inner) predicted_total_time → rt2")
                if 'st2' in start_child:
                    lines.append(f"- {child_type} (depth {child_depth}, Inner) predicted_startup_time → st2")
        lines.append("")
    
    return lines

# Format emitted targets for operator
def format_operator_emitted_targets(operator, depth, op_row):
    lines = [
        "**Emitted Targets:**",
        "- execution_time model → predicted_total_time",
        "- start_time model → predicted_startup_time",
        ""
    ]
    
    relationship = op_row['parent_relationship']
    if pd.notna(relationship) and relationship != '':
        lines.append(f"**Targets to Features (for parent operator at depth {depth - 1}):**")
        if relationship == 'Outer':
            lines.append("- predicted_startup_time → st1")
            lines.append("- predicted_total_time → rt1")
        elif relationship == 'Inner':
            lines.append("- predicted_startup_time → st2")
            lines.append("- predicted_total_time → rt2")
        lines.append("")
    
    return lines


# Export execution plan to markdown file
def export_execution_plan(execution_plan, output_dir, query_name, df_operators, pattern_features, operator_features):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{query_name}_execution_plan_{timestamp}.md"
    
    md_content = generate_markdown(execution_plan, query_name, df_operators, pattern_features, operator_features)
    
    with open(output_path / filename, 'w') as f:
        f.write(md_content)

# Generate markdown content for execution plan
def generate_markdown(execution_plan, query_name, df_operators, pattern_features, operator_features):
    lines = [
        f"# Execution Plan: {query_name}",
        "",
        "## Overview",
        f"- Total steps: {len(execution_plan)}",
        f"- Pattern-based steps: {sum(1 for s in execution_plan if s['type'] == 'pattern')}",
        f"- Operator-based steps: {sum(1 for s in execution_plan if s['type'] == 'operator')}",
        f"- Pass-through steps: {sum(1 for s in execution_plan if s['type'] == 'passthrough')}",
        "",
        "## Execution Steps (Bottom-Up)",
        ""
    ]

    for idx, step in enumerate(execution_plan, 1):
        lines.append(f"### Step {idx}")
        lines.append("")

        if step['type'] == 'pattern':
            lines.extend(format_pattern_step(step, df_operators, pattern_features))
        elif step['type'] == 'passthrough':
            lines.extend(format_passthrough_step(step))
        else:
            lines.extend(format_operator_step(step, df_operators, operator_features))

        lines.append("")

    return '\n'.join(lines)

# Format pass-through step for markdown
def format_passthrough_step(step):
    lines = [
        f"**Type:** Pass-Through Operator",
        f"**Operator:** {step['operator']}",
        f"**Depth:** {step['depth']}",
        "",
        "**Pass-Through Logic:**",
        f"- Child: {step['child']['node_type']} (depth {step['child']['depth']})",
        f"- predicted_startup_time = {step['predicted_startup_time']:.4f} (from child)",
        f"- predicted_total_time = {step['predicted_total_time']:.4f} (from child)",
        "",
        "**Note:** This operator passes through child predictions without modification.",
        ""
    ]
    return lines

# Format pattern step for markdown
def format_pattern_step(step, df_operators, pattern_features):
    lines = [
        f"**Type:** Pattern Model",
        f"**Pattern:** {step['pattern_name']}",
        f"**Leaf Pattern:** {step['is_leaf']}",
        "",
        "**Operators:**"
    ]
    
    for op_type, depth in step['operators']:
        lines.append(f"- {op_type} (depth {depth})")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    pattern_name = step['pattern_name']
    pattern_data = pattern_features[pattern_name]
    aggregated_row = step['aggregated_row']
    
    exec_features = pattern_data['execution_time']['final_features']
    start_features = pattern_data['start_time']['final_features']
    
    lines.append("**Expected Features (execution_time model):**")
    for feat in exec_features:
        value = aggregated_row.get(feat, 'N/A')
        lines.append(f"- {feat} = {value}")
    lines.append("")
    
    lines.append("**Feature Aggregation (execution_time):**")
    for feat in exec_features:
        source_info = extract_pattern_feature_source(feat, step['operators'], aggregated_row, df_operators)
        if source_info:
            lines.append(f"- {source_info['base_feat']} (row depth {source_info['depth']}, {source_info['operator']}) = {source_info['value']} → {feat}")
    lines.append("")
    
    lines.append("**Expected Features (start_time model):**")
    for feat in start_features:
        value = aggregated_row.get(feat, 'N/A')
        lines.append(f"- {feat} = {value}")
    lines.append("")
    
    lines.append("**Feature Aggregation (start_time):**")
    for feat in start_features:
        source_info = extract_pattern_feature_source(feat, step['operators'], aggregated_row, df_operators)
        if source_info:
            lines.append(f"- {source_info['base_feat']} (row depth {source_info['depth']}, {source_info['operator']}) = {source_info['value']} → {feat}")
    lines.append("")
    
    child_features = step.get('child_features_needed', [])
    if child_features:
        lines.append("**Child Features Needed (from predictions):**")
        for feat in child_features:
            value = aggregated_row.get(feat, 'N/A')
            lines.append(f"- {feat} = {value}")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    
    parent_op, parent_depth = step['operators'][0]
    parent_row = df_operators[(df_operators['node_type'] == parent_op) & (df_operators['depth'] == parent_depth)].iloc[0]
    lines.extend(format_pattern_emitted_targets(parent_op, parent_depth, parent_row))
    
    return lines

# Extract source information for pattern feature
def extract_pattern_feature_source(feature, operators, aggregated_row, df_operators):
    parent_op, parent_depth = operators[0]
    parent_normalized = parent_op.replace(' ', '')
    
    if feature.startswith(parent_normalized + '_'):
        base_feat = feature.replace(parent_normalized + '_', '')
        parent_row = df_operators[(df_operators['node_type'] == parent_op) & (df_operators['depth'] == parent_depth)].iloc[0]
        return {
            'base_feat': base_feat,
            'depth': parent_depth,
            'operator': parent_op,
            'value': aggregated_row.get(feature, 'N/A')
        }
    
    for child_op, child_depth in operators[1:]:
        child_normalized = child_op.replace(' ', '')
        for rel in ['Outer', 'Inner']:
            prefix = child_normalized + '_' + rel + '_'
            if feature.startswith(prefix):
                base_feat = feature.replace(prefix, '')
                child_row = df_operators[(df_operators['node_type'] == child_op) & (df_operators['depth'] == child_depth)].iloc[0]
                return {
                    'base_feat': base_feat,
                    'depth': child_depth,
                    'operator': f"{child_op} {rel}",
                    'value': aggregated_row.get(feature, 'N/A')
                }
    
    return None

# Format operator step for markdown
def format_operator_step(step, df_operators, operator_features):
    lines = [
        f"**Type:** Operator Model",
        f"**Operator:** {step['operator']}",
        f"**Depth:** {step['depth']}",
        ""
    ]
    
    if step['children']:
        lines.append("**Children:**")
        for child_type, child_depth in step['children']:
            lines.append(f"- {child_type} (depth {child_depth})")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    
    operator = step['operator']
    depth = step['depth']
    op_row = df_operators[(df_operators['node_type'] == operator) & (df_operators['depth'] == depth)].iloc[0]
    
    operator_normalized = operator.replace(' ', '_')
    if operator_normalized in operator_features:
        op_data = operator_features[operator_normalized]
        lines.extend(format_operator_features(operator, depth, op_row, op_data, step))
    
    lines.append("---")
    lines.append("")
    lines.extend(format_operator_emitted_targets(operator, depth, op_row))
    
    return lines


if __name__ == "__main__":
    if len(sys.argv) != 6:
        sys.exit(1)
    
    operator_dataset_csv = sys.argv[1]
    query_file_name = sys.argv[2]
    pattern_overview_csv = sys.argv[3]
    operator_overview_csv = sys.argv[4]
    output_directory = sys.argv[5]
    
    run_execution_plan_workflow(operator_dataset_csv, query_file_name, pattern_overview_csv, operator_overview_csv, output_directory)
