#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
import hashlib
import re
from collections import defaultdict


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
def analyze_subtree_containment(input_file: str, output_dir: str) -> None:
    df = load_and_filter_data(input_file)
    template_trees = build_all_trees(df)
    full_hashes = compute_full_tree_hashes(template_trees)
    containment = find_subtree_containment(template_trees, full_hashes)
    export_results(containment, output_dir)


# FUNCTIONS

# Load training data and filter to main plan
def load_and_filter_data(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file, delimiter=';')
    return df[df['subplan_name'].isna() | (df['subplan_name'] == '')]

# Extract template name from query_file
def extract_template(query_file: str) -> str:
    match = re.match(r'(Q\d+)_', query_file)
    return match.group(1) if match else 'Unknown'

# Build all trees grouped by template
def build_all_trees(df: pd.DataFrame) -> dict:
    template_trees = defaultdict(list)

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)

        if root is None:
            continue

        template = extract_template(query_file)
        template_trees[template].append({
            'query_file': query_file,
            'root': root,
            'tree_size': count_all_nodes(root)
        })

    return template_trees

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

# Count all nodes in tree
def count_all_nodes(node) -> int:
    return 1 + sum(count_all_nodes(child) for child in node.children)

# Compute hash for complete tree
def compute_tree_hash(node) -> str:
    if len(node.children) == 0:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_tree_hash(child)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)

    return hashlib.md5(combined_string.encode()).hexdigest()

# Generate pattern string
def generate_pattern_string(node) -> str:
    if len(node.children) == 0:
        return node.node_type

    if len(node.children) == 1:
        child = node.children[0]
        child_str = generate_pattern_string(child)
        rel = f" ({child.parent_relationship})" if child.parent_relationship else ""
        return f"{node.node_type} -> {child_str}{rel}"

    children_strs = []
    for child in sorted(node.children, key=lambda c: (0 if c.parent_relationship == 'Outer' else 1)):
        child_str = generate_pattern_string(child)
        rel = f" ({child.parent_relationship})" if child.parent_relationship else ""
        children_strs.append(f"{child_str}{rel}")

    return f"{node.node_type} -> [{', '.join(children_strs)}]"

# Compute full tree hashes for each template (take first query as representative)
def compute_full_tree_hashes(template_trees: dict) -> dict:
    full_hashes = {}

    for template, trees in template_trees.items():
        if trees:
            root = trees[0]['root']
            full_hashes[template] = {
                'hash': compute_tree_hash(root),
                'pattern_string': generate_pattern_string(root),
                'tree_size': trees[0]['tree_size']
            }

    return full_hashes

# Extract all subtree hashes from a tree (excluding root)
def extract_all_subtree_hashes(node) -> list:
    subtrees = []

    for child in node.children:
        child_hash = compute_tree_hash(child)
        child_size = count_all_nodes(child)
        subtrees.append({
            'hash': child_hash,
            'size': child_size,
            'pattern_string': generate_pattern_string(child)
        })
        subtrees.extend(extract_all_subtree_hashes(child))

    return subtrees

# Find which templates' full trees appear as subtrees in other templates
def find_subtree_containment(template_trees: dict, full_hashes: dict) -> list:
    results = []

    for container_template, trees in template_trees.items():
        if not trees:
            continue

        root = trees[0]['root']
        subtree_hashes = extract_all_subtree_hashes(root)
        subtree_hash_set = {s['hash'] for s in subtree_hashes}

        for contained_template, info in full_hashes.items():
            if contained_template == container_template:
                continue

            if info['hash'] in subtree_hash_set:
                results.append({
                    'container_template': container_template,
                    'container_size': full_hashes[container_template]['tree_size'],
                    'contained_template': contained_template,
                    'contained_size': info['tree_size'],
                    'contained_pattern': info['pattern_string']
                })

    return results

# Export results
def export_results(containment: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if containment:
        df = pd.DataFrame(containment)
        df = df.sort_values(['container_template', 'contained_template'])
        output_file = output_path / 'A_02_subtree_containment.csv'
        df.to_csv(output_file, sep=';', index=False)
    else:
        output_file = output_path / 'A_02_subtree_containment.csv'
        with open(output_file, 'w') as f:
            f.write("No subtree containment found - no template's full tree appears as subtree in another template\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to operator dataset CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    analyze_subtree_containment(args.input_file, args.output_dir)
