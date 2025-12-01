#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import pandas as pd
import hashlib
from pathlib import Path
from datetime import datetime

sys.path.insert(0, '/Users/brunowinter2000/Documents/Thesis/Thesis_Final/Prediction_Methods/Hybrid_5')

# From mapping_config.py: Pattern list
from mapping_config import PATTERNS


# ORCHESTRATOR
def run_optimized_plan_workflow(operator_dataset_file, query_name, pattern_csv, pattern_plan_leafs_csv, output_dir):
    df_operators = load_operator_dataset(operator_dataset_file, query_name)
    pattern_info = load_pattern_info(pattern_csv)
    plan_leaf_mapping = load_pattern_plan_leaf_mapping(pattern_plan_leafs_csv)
    root = build_full_tree(df_operators)
    execution_plan = build_optimized_plan_greedy(root, pattern_info, df_operators)
    annotate_passthrough_logic(execution_plan, df_operators, plan_leaf_mapping)
    export_execution_plan(execution_plan, output_dir, query_name, df_operators)


# FUNCTIONS

# Load operator dataset and filter for specific query
def load_operator_dataset(dataset_file, query_name):
    df = pd.read_csv(dataset_file, delimiter=';')
    df_query = df[df['query_file'] == query_name].copy()
    df_query = df_query[df_query['subplan_name'].isna() | (df_query['subplan_name'] == '')]
    return df_query.sort_values('node_id').reset_index(drop=True)

# Load pattern information from pattern mining CSV
def load_pattern_info(pattern_csv):
    df = pd.read_csv(pattern_csv, delimiter=';')
    pattern_map = {}
    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']
        if pattern_hash in PATTERNS:
            pattern_map[pattern_hash] = {
                'string': row['pattern_string'],
                'length': row['pattern_length']
            }
    return pattern_map

# Load pattern plan leaf mapping from 04_Identify_Pattern_Plan_Leafs.py output
def load_pattern_plan_leaf_mapping(pattern_plan_leafs_csv):
    df = pd.read_csv(pattern_plan_leafs_csv, delimiter=';')
    mapping = {}

    for _, row in df.iterrows():
        pattern_hash = row['pattern_hash']
        prefix = row['pattern_leaf_prefix']
        is_plan_leaf = row['is_plan_leaf'] == 'ja'

        if pattern_hash not in mapping:
            mapping[pattern_hash] = {}

        mapping[pattern_hash][prefix] = is_plan_leaf

    return mapping

# Build full tree from dataframe
def build_full_tree(df_operators):
    return build_subtree_from_index(df_operators, 0)

# Build subtree from dataframe index
def build_subtree_from_index(df_operators, node_idx):
    if node_idx >= len(df_operators):
        return None

    node_row = df_operators.iloc[node_idx]
    tree_node = QueryNode(
        node_type=node_row['node_type'],
        parent_relationship=node_row['parent_relationship'],
        depth=node_row['depth'],
        node_id=node_row['node_id'],
        df_index=node_idx
    )

    children_indices = get_children_indices(df_operators, node_idx)
    for child_idx in children_indices:
        child_node = build_subtree_from_index(df_operators, child_idx)
        if child_node:
            tree_node.add_child(child_node)

    return tree_node

# Get children indices for node
def get_children_indices(df_operators, parent_idx):
    parent_row = df_operators.iloc[parent_idx]
    parent_depth = parent_row['depth']
    children = []

    for idx in range(parent_idx + 1, len(df_operators)):
        row = df_operators.iloc[idx]
        if row['depth'] == parent_depth + 1:
            children.append(idx)
        elif row['depth'] <= parent_depth:
            break

    return children

# Build optimized execution plan using greedy pattern matching (largest first)
def build_optimized_plan_greedy(root, pattern_info, df_operators):
    plan_steps = []
    consumed_indices = set()

    patterns_by_length = sorted(pattern_info.items(), key=lambda x: x[1]['length'], reverse=True)

    all_nodes = extract_all_nodes_with_depth(root)
    all_nodes_sorted = sorted(all_nodes, key=lambda n: n.depth)

    for node in all_nodes_sorted:
        if node.df_index in consumed_indices:
            continue

        matched_pattern = try_match_largest_pattern(node, patterns_by_length)

        if matched_pattern:
            pattern_hash, pattern_info_item = matched_pattern
            pattern_length = pattern_info_item['length']
            pattern_string = pattern_info_item['string']
            handle_pattern_match(node, pattern_hash, pattern_length, pattern_string, plan_steps, consumed_indices, df_operators)
        else:
            handle_operator_node(node, plan_steps, consumed_indices)

    return plan_steps

# Extract all nodes from tree with depth ordering
def extract_all_nodes_with_depth(node):
    nodes = [node]
    for child in node.children:
        nodes.extend(extract_all_nodes_with_depth(child))
    return nodes

# Try to match largest available pattern
def try_match_largest_pattern(node, patterns_by_length):
    for pattern_hash, pattern_info in patterns_by_length:
        pattern_length = pattern_info['length']

        if not has_sufficient_depth(node, pattern_length):
            continue

        computed_hash = compute_hash_at_length(node, pattern_length)

        if computed_hash == pattern_hash:
            return (pattern_hash, pattern_info)

    return None

# Check if node has sufficient depth for pattern
def has_sufficient_depth(node, target_length):
    if target_length == 1:
        return True
    if len(node.children) == 0:
        return False
    return any(has_sufficient_depth(child, target_length - 1) for child in node.children)

# Compute structural hash for pattern at specific length
def compute_hash_at_length(node, remaining_length):
    if remaining_length == 1 or len(node.children) == 0:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_hash_at_length(child, remaining_length - 1)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)

    return hashlib.md5(combined_string.encode()).hexdigest()

# Handle pattern match
def handle_pattern_match(node, pattern_hash, pattern_length, pattern_string, plan_steps, consumed_indices, df_operators):
    consumed_nodes = collect_subtree_indices(node, pattern_length)
    consumed_indices.update(consumed_nodes)

    consumed_details = get_consumed_node_details(consumed_nodes, df_operators)

    step = {
        'type': 'pattern',
        'pattern_hash': pattern_hash,
        'pattern_length': pattern_length,
        'pattern_string': pattern_string,
        'root_operator': node.node_type,
        'root_depth': node.depth,
        'root_node_id': node.node_id,
        'consumed_nodes': len(consumed_nodes),
        'consumed_details': consumed_details
    }
    plan_steps.append(step)

# Handle operator node (no pattern match)
def handle_operator_node(node, plan_steps, consumed_indices):
    consumed_indices.add(node.df_index)

    step = {
        'type': 'operator',
        'operator': node.node_type,
        'depth': node.depth,
        'node_id': node.node_id
    }
    plan_steps.append(step)

# Collect all indices in subtree up to target length
def collect_subtree_indices(node, remaining_length):
    indices = {node.df_index}

    if remaining_length > 1:
        for child in node.children:
            indices.update(collect_subtree_indices(child, remaining_length - 1))

    return indices

# Get details of consumed nodes
def get_consumed_node_details(consumed_indices, df_operators):
    details = []
    for idx in sorted(consumed_indices):
        row = df_operators.iloc[idx]
        details.append({
            'node_id': row['node_id'],
            'node_type': row['node_type'],
            'depth': row['depth'],
            'parent_relationship': row['parent_relationship']
        })
    return details

# Annotate execution plan with pass-through logic
def annotate_passthrough_logic(execution_plan, df_operators, plan_leaf_mapping):
    for step in execution_plan:
        if step['type'] == 'pattern':
            annotate_pattern_passthrough(step, df_operators, plan_leaf_mapping)
        else:
            annotate_operator_passthrough(step, df_operators)

# Annotate pattern step with pass-through information
def annotate_pattern_passthrough(step, df_operators, plan_leaf_mapping):
    pattern_hash = step['pattern_hash']
    consumed_details = step['consumed_details']

    pattern_leafs = [d for d in consumed_details if is_pattern_leaf(d, consumed_details)]
    required_child_features = []

    if pattern_hash in plan_leaf_mapping:
        for leaf in pattern_leafs:
            prefix = clean_node_type(leaf['node_type']) + '_' + leaf['parent_relationship']
            is_plan_leaf = plan_leaf_mapping[pattern_hash].get(prefix, False)

            if not is_plan_leaf:
                required_child_features.append(f"{prefix}: rt1, rt2, st1, st2")

    step['required_child_features'] = required_child_features
    step['emitted_targets'] = ['actual_startup_time (st)', 'actual_total_time (rt)']
    step['passthrough_mapping'] = generate_passthrough_mapping(step['root_operator'], step.get('consumed_details', [{}])[0].get('parent_relationship'))

# Annotate operator step with pass-through information
def annotate_operator_passthrough(step, df_operators):
    node_id = step['node_id']
    operator_row = df_operators[df_operators['node_id'] == node_id].iloc[0]

    children = get_operator_children(operator_row, df_operators)
    required_child_features = []

    for child in children:
        prefix = clean_node_type(child['node_type']) + '_' + child['parent_relationship']
        required_child_features.append(f"{prefix}: rt1, rt2, st1, st2")

    step['required_child_features'] = required_child_features
    step['emitted_targets'] = ['actual_startup_time (st)', 'actual_total_time (rt)']
    step['passthrough_mapping'] = generate_passthrough_mapping(step['operator'], operator_row['parent_relationship'])

# Check if node is a pattern leaf (has no children within pattern)
def is_pattern_leaf(node_detail, all_consumed_details):
    node_depth = node_detail['depth']
    max_depth = max(d['depth'] for d in all_consumed_details)
    return node_depth == max_depth

# Get operator children from dataframe
def get_operator_children(operator_row, df_operators):
    operator_depth = operator_row['depth']
    operator_idx = operator_row.name
    children = []

    for idx in range(operator_idx + 1, len(df_operators)):
        row = df_operators.iloc[idx]
        if row['depth'] == operator_depth + 1:
            children.append({
                'node_type': row['node_type'],
                'parent_relationship': row['parent_relationship']
            })
        elif row['depth'] <= operator_depth:
            break

    return children

# Generate pass-through mapping description
def generate_passthrough_mapping(node_type, parent_relationship):
    if not parent_relationship or pd.isna(parent_relationship):
        return "Root node - no pass-through to parent"

    return f"Emitted targets become child features for parent: st -> st1/st2, rt -> rt1/rt2 (based on {parent_relationship} relationship)"

# Clean node type for column naming
def clean_node_type(node_type):
    return node_type.replace(' ', '')


# Export execution plan to markdown file
def export_execution_plan(execution_plan, output_dir, query_name, df_operators):
    output_path = Path(output_dir) / 'md'
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{query_name}_optimized_plan_{timestamp}.md"

    md_content = generate_markdown(execution_plan, query_name, df_operators)

    with open(output_path / filename, 'w') as f:
        f.write(md_content)

# Generate markdown content for execution plan
def generate_markdown(execution_plan, query_name, df_operators):
    pattern_count = sum(1 for s in execution_plan if s['type'] == 'pattern')
    operator_count = sum(1 for s in execution_plan if s['type'] == 'operator')

    lines = [
        f"# Optimized Execution Plan: {query_name}",
        "",
        "## Strategy: Greedy Pattern Matching (Largest First)",
        "",
        "## Overview",
        f"- Total operators in query: {len(df_operators)}",
        f"- Total predictions needed: {len(execution_plan)}",
        f"- Pattern-based predictions: {pattern_count}",
        f"- Operator-based predictions: {operator_count}",
        f"- Reduction: {len(df_operators) - len(execution_plan)} operators covered by patterns",
        "",
        "## Execution Steps (Top-Down Order)",
        ""
    ]

    for idx, step in enumerate(execution_plan, 1):
        lines.append(f"### Step {idx}")
        lines.append("")

        if step['type'] == 'pattern':
            lines.extend(format_pattern_step(step))
        else:
            lines.extend(format_operator_step(step))

        lines.append("")

    return '\n'.join(lines)

# Format pattern step for markdown
def format_pattern_step(step):
    lines = [
        f"**Type:** Pattern Model",
        f"**Pattern Hash:** {step['pattern_hash']}",
        f"**Pattern String:** {step['pattern_string']}",
        f"**Pattern Length:** {step['pattern_length']}",
        f"**Root Operator:** {step['root_operator']} (depth {step['root_depth']}, node_id {step['root_node_id']})",
        f"**Consumed Nodes:** {step['consumed_nodes']}",
        ""
    ]

    if step.get('consumed_details'):
        lines.append("**Pattern Structure:**")
        for detail in step['consumed_details']:
            rel = f" ({detail['parent_relationship']})" if detail['parent_relationship'] else ""
            lines.append(f"- Depth {detail['depth']}: {detail['node_type']}{rel} (node_id {detail['node_id']})")
        lines.append("")

    lines.append("**Pass-Through Logic:**")
    lines.append("")

    if step.get('required_child_features'):
        lines.append("*Required Child Features:*")
        for feature in step['required_child_features']:
            lines.append(f"- {feature}")
    else:
        lines.append("*Required Child Features:* None (all pattern leafs are plan leafs)")
    lines.append("")

    lines.append("*Emitted Targets:*")
    for target in step.get('emitted_targets', []):
        lines.append(f"- {target}")
    lines.append("")

    lines.append(f"*Pass-Through Mapping:* {step.get('passthrough_mapping', 'N/A')}")
    lines.append("")

    return lines

# Format operator step for markdown
def format_operator_step(step):
    lines = [
        f"**Type:** Operator Model",
        f"**Operator:** {step['operator']} (depth {step['depth']}, node_id {step['node_id']})",
        ""
    ]

    lines.append("**Pass-Through Logic:**")
    lines.append("")

    if step.get('required_child_features'):
        lines.append("*Required Child Features:*")
        for feature in step['required_child_features']:
            lines.append(f"- {feature}")
    else:
        lines.append("*Required Child Features:* None (leaf operator)")
    lines.append("")

    lines.append("*Emitted Targets:*")
    for target in step.get('emitted_targets', []):
        lines.append(f"- {target}")
    lines.append("")

    lines.append(f"*Pass-Through Mapping:* {step.get('passthrough_mapping', 'N/A')}")
    lines.append("")

    return lines


class QueryNode:
    def __init__(self, node_type, parent_relationship, depth, node_id, df_index):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.df_index = df_index
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python 02_create_optimized_plan.py <operator_dataset_csv> <query_name> <pattern_csv> <pattern_plan_leafs_csv> <output_dir>")
        sys.exit(1)

    operator_dataset_csv = sys.argv[1]
    query_file_name = sys.argv[2]
    pattern_csv = sys.argv[3]
    pattern_plan_leafs_csv = sys.argv[4]
    output_directory = sys.argv[5]

    run_optimized_plan_workflow(operator_dataset_csv, query_file_name, pattern_csv, pattern_plan_leafs_csv, output_directory)
