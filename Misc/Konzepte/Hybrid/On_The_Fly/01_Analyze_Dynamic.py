#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import hashlib
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import pandas as pd

THRESHOLD = 150

# ORCHESTRATOR

def analyze_workflow(baseline_dir: str, output_dir: str) -> None:
    baseline_path = Path(baseline_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    template_folders = sorted([d for d in baseline_path.iterdir() if d.is_dir()])

    for template_folder in template_folders:
        analyze_template(template_folder, output_path)


def analyze_template(template_folder: Path, output_path: Path) -> None:
    template_name = template_folder.name
    training_file = template_folder / 'training_cleaned.csv'
    test_file = template_folder / '02_test_cleaned.csv'

    if not training_file.exists() or not test_file.exists():
        return

    df_training = load_data(training_file)
    df_test = load_data(test_file)

    hash_index, hash_queries = build_hash_index(df_training)
    operator_counts = count_operators(df_training)

    query_files = df_test['query_file'].unique()

    if template_name == 'Q9':
        variants = detect_plan_variants(df_test)
        for variant_idx, variant_queries in enumerate(variants):
            first_query = variant_queries[0]
            query_ops = df_test[df_test['query_file'] == first_query].sort_values('node_id').reset_index(drop=True)
            generate_analysis_md(template_name, query_ops, hash_index, hash_queries, operator_counts, output_path, variant_idx + 1)
    else:
        first_query = query_files[0]
        query_ops = df_test[df_test['query_file'] == first_query].sort_values('node_id').reset_index(drop=True)
        generate_analysis_md(template_name, query_ops, hash_index, hash_queries, operator_counts, output_path)


# FUNCTIONS

# Load data from CSV with semicolon delimiter
def load_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')


# Count operators in training data
def count_operators(df_training: pd.DataFrame) -> dict:
    return df_training['node_type'].value_counts().to_dict()


# Detect plan variants based on root operator structure
def detect_plan_variants(df_test: pd.DataFrame) -> list:
    variants = defaultdict(list)

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree(query_ops)
        structure_hash = compute_hash_at_depth(root, get_max_depth(root))
        variants[structure_hash].append(query_file)

    return list(variants.values())


# Build hash index from training data with query tracking
def build_hash_index(df_training: pd.DataFrame) -> tuple:
    hash_counts = defaultdict(int)
    hash_queries = defaultdict(set)

    for query_file in df_training['query_file'].unique():
        query_ops = df_training[df_training['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree(query_ops)
        collect_subtree_hashes(root, hash_counts, hash_queries, query_file)

    return dict(hash_counts), {k: list(v) for k, v in hash_queries.items()}


# Collect all subtree hashes from a node recursively
def collect_subtree_hashes(node, hash_counts: dict, hash_queries: dict, query_file: str) -> None:
    max_depth = get_max_depth(node)

    for depth in range(max_depth + 1):
        subtree_hash = compute_hash_at_depth(node, depth)
        hash_counts[subtree_hash] += 1
        hash_queries[subtree_hash].add(query_file)

    for child in node.children:
        collect_subtree_hashes(child, hash_counts, hash_queries, query_file)


# Get maximum depth of subtree from node
def get_max_depth(node) -> int:
    if not node.children:
        return 0
    return 1 + max(get_max_depth(child) for child in node.children)


# Compute structural hash at specific depth
def compute_hash_at_depth(node, remaining_depth: int) -> str:
    if remaining_depth == 0 or not node.children:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_hash_at_depth(child, remaining_depth - 1)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)

    return hashlib.md5(combined_string.encode()).hexdigest()


# Build tree structure from DataFrame
def build_tree(query_ops: pd.DataFrame):
    nodes = {}
    root = None

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'],
            depth=row['depth'],
            node_id=row['node_id'],
            df_index=idx
        )
        nodes[row['node_id']] = node

        if row['depth'] == 0:
            root = node

    for idx, row in query_ops.iterrows():
        current_node = nodes[row['node_id']]
        current_depth = row['depth']

        for j in range(idx + 1, len(query_ops)):
            next_row = query_ops.iloc[j]

            if next_row['depth'] == current_depth + 1:
                child_node = nodes[next_row['node_id']]
                current_node.add_child(child_node)
            elif next_row['depth'] <= current_depth:
                break

    return root


# Get leaf nodes of a pattern at specific depth
def get_pattern_leaf_nodes(node, remaining_depth: int) -> list:
    if remaining_depth == 0 or not node.children:
        return [node]

    leaf_nodes = []
    for child in node.children:
        leaf_nodes.extend(get_pattern_leaf_nodes(child, remaining_depth - 1))
    return leaf_nodes


# Find patterns recursively with threshold-based shrinking
def find_patterns_recursive(node, hash_index: dict, consumed: set) -> list:
    if node.df_index in consumed:
        return []

    execution_plan = []
    max_depth = get_max_depth(node)

    for depth in range(max_depth, -1, -1):
        subtree_hash = compute_hash_at_depth(node, depth)
        count = hash_index.get(subtree_hash, 0)

        if count >= THRESHOLD:
            node_ids = extract_node_ids_at_depth(node, depth)
            consumed.update(node_ids)

            execution_plan.append({
                'type': 'pattern',
                'pattern_hash': subtree_hash,
                'root_node': node,
                'depth': depth,
                'node_ids': node_ids,
                'training_count': count
            })

            leaf_nodes = get_pattern_leaf_nodes(node, depth)
            for leaf in leaf_nodes:
                for child in leaf.children:
                    child_plan = find_patterns_recursive(child, hash_index, consumed)
                    execution_plan.extend(child_plan)

            return execution_plan

    consumed.add(node.df_index)
    execution_plan.append({
        'type': 'operator',
        'node': node,
        'df_index': node.df_index
    })

    for child in node.children:
        child_plan = find_patterns_recursive(child, hash_index, consumed)
        execution_plan.extend(child_plan)

    return execution_plan


# Extract node IDs at specific depth from node
def extract_node_ids_at_depth(node, remaining_depth: int) -> set:
    if remaining_depth == 0 or not node.children:
        return {node.df_index}

    node_ids = {node.df_index}
    for child in node.children:
        node_ids.update(extract_node_ids_at_depth(child, remaining_depth - 1))

    return node_ids


# Generate pattern string representation
def generate_pattern_string(node, remaining_depth: int) -> str:
    if remaining_depth == 0 or not node.children:
        return node.node_type

    children_sorted = sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1 if c.parent_relationship == 'Inner' else 2, c.node_type))

    child_strings = []
    for child in children_sorted:
        child_str = generate_pattern_string(child, remaining_depth - 1)
        child_strings.append(f"{child_str} ({child.parent_relationship})")

    return f"{node.node_type} -> [{', '.join(child_strings)}]"


# Extract nodes in subtree at depth
def extract_subtree_nodes(node, remaining_depth: int) -> list:
    nodes = [(node.depth, node.node_type, node.parent_relationship, node.node_id)]

    if remaining_depth > 0 and node.children:
        children_sorted = sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1 if c.parent_relationship == 'Inner' else 2, c.node_type))
        for child in children_sorted:
            nodes.extend(extract_subtree_nodes(child, remaining_depth - 1))

    return nodes


# Generate markdown analysis file
def generate_analysis_md(template_name: str, query_ops: pd.DataFrame, hash_index: dict, hash_queries: dict, operator_counts: dict, output_path: Path, variant: int = None) -> None:
    root = build_tree(query_ops)
    execution_plan = find_patterns_recursive(root, hash_index, set())

    total_operators = len(query_ops)
    pattern_steps = [s for s in execution_plan if s['type'] == 'pattern']
    operator_steps = [s for s in execution_plan if s['type'] == 'operator']

    pattern_nodes = sum(len(s['node_ids']) for s in pattern_steps)
    operator_nodes = len(operator_steps)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    variant_suffix = f'_variant{variant}' if variant else ''
    filename = f'{template_name}{variant_suffix}_{timestamp}.md'

    lines = []
    lines.append(f'# Dynamic Prediction Analysis: {template_name}{f" (Variant {variant})" if variant else ""}')
    lines.append('')
    lines.append('## Strategy: Dynamic Pattern Matching (Top-Down Shrinking)')
    lines.append('')
    lines.append('## Overview')
    lines.append(f'- Total operators in query: {total_operators}')
    lines.append(f'- Pattern-based predictions: {len(pattern_steps)} (covering {pattern_nodes} nodes)')
    lines.append(f'- Operator-based predictions: {len(operator_steps)}')
    lines.append(f'- Threshold: {THRESHOLD}')
    lines.append('')
    lines.append('## Execution Steps (Top-Down Order, Bottom-Up Execution)')
    lines.append('')

    for step_idx, step in enumerate(execution_plan, 1):
        lines.append(f'### Step {step_idx}')
        lines.append('')

        if step['type'] == 'pattern':
            root_node = step['root_node']
            depth = step['depth']
            pattern_hash = step['pattern_hash']
            training_count = step['training_count']
            pattern_string = generate_pattern_string(root_node, depth)
            subtree_nodes = extract_subtree_nodes(root_node, depth)

            training_queries = hash_queries.get(pattern_hash, [])

            lines.append('**Type:** Pattern Model')
            lines.append(f'**Pattern Hash:** {pattern_hash}')
            source_templates = sorted(set(q.split('_')[0] for q in training_queries))
            lines.append(f'**Training Source:** {", ".join(source_templates)}')
            lines.append(f'**Training Count:** {training_count}')
            lines.append(f'**Training Queries:** {len(training_queries)} unique queries')
            lines.append(f'**Pattern String:** {pattern_string}')
            lines.append(f'**Pattern Depth:** {depth + 1}')
            lines.append(f'**Root Operator:** {root_node.node_type} (depth {root_node.depth}, node_id {root_node.node_id})')
            lines.append(f'**Consumed Nodes:** {len(step["node_ids"])}')
            lines.append('')
            lines.append('**Training Query Examples:**')
            for q in training_queries[:5]:
                lines.append(f'- {q}')
            if len(training_queries) > 5:
                lines.append(f'- ... and {len(training_queries) - 5} more')
            lines.append('')
            lines.append('**Pattern Structure:**')

            for node_depth, node_type, parent_rel, node_id in subtree_nodes:
                rel_str = parent_rel if pd.notna(parent_rel) else 'root'
                lines.append(f'- Depth {node_depth}: {node_type} ({rel_str}) (node_id {node_id})')

        else:
            node = step['node']
            op_count = operator_counts.get(node.node_type, 0)

            lines.append('**Type:** Operator Model')
            lines.append(f'**Operator:** {node.node_type}')
            lines.append(f'**Training Count:** {op_count}')
            lines.append(f'**Depth:** {node.depth}')
            lines.append(f'**Node ID:** {node.node_id}')
            lines.append(f'**Parent Relationship:** {node.parent_relationship if pd.notna(node.parent_relationship) else "root"}')

        lines.append('')
        lines.append('')

    output_file = output_path / filename
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int, df_index: int = None):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.df_index = df_index
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('baseline_dir', help='Path to Dynamic/Datasets/Baseline_SVM/')
    parser.add_argument('--output-dir', required=True, help='Output directory for markdown files')
    args = parser.parse_args()

    analyze_workflow(args.baseline_dir, args.output_dir)
