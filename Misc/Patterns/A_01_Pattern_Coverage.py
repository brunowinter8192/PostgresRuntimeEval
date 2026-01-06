#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import hashlib
import re


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# ORCHESTRATOR
def analyze_pattern_coverage(input_file: str, output_dir: str) -> None:
    df = load_and_filter_data(input_file)
    coverage_data = compute_full_coverage_patterns(df)
    cross_template = analyze_cross_template(coverage_data)
    export_results(cross_template, output_dir)


# FUNCTIONS

# Load training data and filter to main plan
def load_and_filter_data(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]

# Extract template name from query_file
def extract_template(query_file: str) -> str:
    match = re.match(r'(Q\d+)_', query_file)
    return match.group(1) if match else 'Unknown'

# Compute full-coverage pattern for each query
def compute_full_coverage_patterns(df: pd.DataFrame) -> list:
    results = []

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)

        if root is None:
            continue

        tree_depth = get_tree_depth(root)
        tree_size = count_all_nodes(root)

        full_pattern_hash = compute_pattern_hash_full(root)
        pattern_string = generate_pattern_string_full(root)

        template = extract_template(query_file)

        results.append({
            'template': template,
            'query_file': query_file,
            'full_pattern_hash': full_pattern_hash,
            'pattern_string': pattern_string,
            'tree_depth': tree_depth,
            'tree_size': tree_size
        })

    return results

# Build tree structure from flat DataFrame
def build_tree_from_dataframe(query_ops: pd.DataFrame):
    nodes = {}
    root = None

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'] if pd.notna(row['parent_relationship']) else '',
            depth=row['depth'],
            node_id=row['node_id']
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

# Get maximum depth of tree
def get_tree_depth(node, current_depth=0) -> int:
    if len(node.children) == 0:
        return current_depth

    return max(get_tree_depth(child, current_depth + 1) for child in node.children)

# Count all nodes in tree
def count_all_nodes(node) -> int:
    return 1 + sum(count_all_nodes(child) for child in node.children)

# Compute hash for complete tree (no length limit)
def compute_pattern_hash_full(node) -> str:
    if len(node.children) == 0:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_pattern_hash_full(child)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)

    return hashlib.md5(combined_string.encode()).hexdigest()

# Generate readable pattern string for complete tree
def generate_pattern_string_full(node) -> str:
    if len(node.children) == 0:
        return node.node_type

    if len(node.children) == 1:
        child = node.children[0]
        child_str = generate_pattern_string_full(child)
        rel = f" ({child.parent_relationship})" if child.parent_relationship else ""
        return f"{node.node_type} -> {child_str}{rel}"

    children_strs = []
    for child in sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1 if c.parent_relationship == 'Inner' else 2, c.node_type)):
        child_str = generate_pattern_string_full(child)
        rel = f" ({child.parent_relationship})" if child.parent_relationship else ""
        children_strs.append(f"{child_str}{rel}")

    children_combined = ', '.join(children_strs)
    return f"{node.node_type} -> [{children_combined}]"

# Analyze cross-template pattern occurrences
def analyze_cross_template(coverage_data: list) -> pd.DataFrame:
    df = pd.DataFrame(coverage_data)

    hash_to_templates = df.groupby('full_pattern_hash')['template'].apply(lambda x: sorted(set(x))).to_dict()

    df['templates_with_pattern'] = df['full_pattern_hash'].map(hash_to_templates)
    df['also_in_templates'] = df.apply(
        lambda row: [t for t in row['templates_with_pattern'] if t != row['template']],
        axis=1
    )
    df['cross_template_count'] = df['also_in_templates'].apply(len)

    df = df.drop(columns=['templates_with_pattern'])

    return df.sort_values(['template', 'query_file'])

# Export results
def export_results(df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    output_file = output_path / 'A_01_pattern_coverage.csv'
    df.to_csv(output_file, sep=';', index=False)

    summary_file = output_path / 'A_01_pattern_coverage_summary.csv'
    summary = df.groupby('template').agg({
        'full_pattern_hash': 'nunique',
        'tree_size': ['min', 'max', 'mean'],
        'cross_template_count': lambda x: (x > 0).sum()
    }).round(1)
    summary.columns = ['unique_patterns', 'min_tree_size', 'max_tree_size', 'avg_tree_size', 'queries_with_cross_template']
    summary = summary.reset_index()
    summary.to_csv(summary_file, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    analyze_pattern_coverage(args.input_file, args.output_dir)
