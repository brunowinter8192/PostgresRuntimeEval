#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import hashlib
from pathlib import Path
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
def analyze_interference(pattern_hashes: list, dataset_file: str, patterns_file: str, output_dir: str) -> None:
    patterns_meta = load_patterns_metadata(patterns_file, pattern_hashes)
    all_matches = scan_pattern_matches(dataset_file, patterns_meta)
    sorted_patterns = sort_by_priority(patterns_meta, pattern_hashes)
    results = compute_node_level_interference(all_matches, sorted_patterns, pattern_hashes)
    export_results(results, pattern_hashes, output_dir)


# FUNCTIONS

# Load pattern metadata for specified hashes
def load_patterns_metadata(patterns_file: str, pattern_hashes: list) -> dict:
    df = pd.read_csv(patterns_file, delimiter=';')
    meta = {}
    for _, row in df.iterrows():
        if row['pattern_hash'] in pattern_hashes:
            meta[row['pattern_hash']] = {
                'pattern_string': row['pattern_string'],
                'pattern_length': row['pattern_length'],
                'operator_count': row['operator_count']
            }
    return meta


# Scan dataset for all pattern matches (node-level)
def scan_pattern_matches(dataset_file: str, patterns_meta: dict) -> list:
    df = pd.read_csv(dataset_file, delimiter=';')
    df = df[df['subplan_name'].isna() | (df['subplan_name'] == '')]

    all_matches = []
    max_length = max(p['pattern_length'] for p in patterns_meta.values()) if patterns_meta else 2

    for query_file in df['query_file'].unique():
        query_ops = df[df['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)

        for node in all_nodes:
            for pattern_length in range(2, max_length + 1):
                if not has_children_at_length(node, pattern_length):
                    break
                computed_hash = compute_pattern_hash_at_length(node, pattern_length)
                if computed_hash in patterns_meta:
                    pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
                    all_matches.append({
                        'query_file': query_file,
                        'node': node,
                        'pattern_hash': computed_hash,
                        'pattern_length': pattern_length,
                        'pattern_node_ids': set(pattern_node_ids),
                        'depth': node.depth
                    })

    return all_matches


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


# Extract all nodes from tree recursively
def extract_all_nodes(node) -> list:
    nodes = [node]
    for child in node.children:
        nodes.extend(extract_all_nodes(child))
    return nodes


# Check if node has children at target pattern length
def has_children_at_length(node, pattern_length: int) -> bool:
    if pattern_length == 1:
        return True
    if pattern_length == 2:
        return len(node.children) > 0
    if len(node.children) == 0:
        return False
    return any(has_children_at_length(child, pattern_length - 1) for child in node.children)


# Compute structural hash for pattern at specific length
def compute_pattern_hash_at_length(node, remaining_length: int) -> str:
    if remaining_length == 1 or len(node.children) == 0:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_pattern_hash_at_length(child, remaining_length - 1)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)
    return hashlib.md5(combined_string.encode()).hexdigest()


# Extract all node IDs covered by pattern
def extract_pattern_node_ids(node, remaining_length: int) -> list:
    if remaining_length == 1 or len(node.children) == 0:
        return [node.node_id]

    node_ids = [node.node_id]
    for child in node.children:
        child_ids = extract_pattern_node_ids(child, remaining_length - 1)
        node_ids.extend(child_ids)

    return node_ids


# Sort patterns by priority (length DESC, then input order)
def sort_by_priority(patterns_meta: dict, input_order: list) -> list:
    indexed = []
    for i, ph in enumerate(input_order):
        if ph in patterns_meta:
            indexed.append({
                'pattern_hash': ph,
                'pattern_string': patterns_meta[ph]['pattern_string'],
                'pattern_length': patterns_meta[ph]['pattern_length'],
                'input_order': i
            })

    indexed.sort(key=lambda x: (-x['pattern_length'], x['input_order']))

    for i, item in enumerate(indexed):
        item['priority'] = i + 1

    return indexed


# Get selection order index for a pattern hash
def get_selection_order_index(pattern_hash: str, input_order: list) -> int:
    try:
        return input_order.index(pattern_hash)
    except ValueError:
        return len(input_order)


# Compute node-level interference between patterns
def compute_node_level_interference(all_matches: list, sorted_patterns: list, input_order: list) -> list:
    queries = defaultdict(list)
    for match in all_matches:
        queries[match['query_file']].append(match)

    pattern_stats = {p['pattern_hash']: {
        'occurrences': 0,
        'wins': 0,
        'blocked': 0,
        'blocked_by': defaultdict(int),
        'templates': set(),
        'templates_wins': set()
    } for p in sorted_patterns}

    for query_file, matches in queries.items():
        template = query_file.split('_')[0]

        matches.sort(key=lambda m: (
            -m['pattern_length'],
            get_selection_order_index(m['pattern_hash'], input_order)
        ))

        consumed_nodes = set()

        for match in matches:
            ph = match['pattern_hash']
            pattern_node_ids = match['pattern_node_ids']

            pattern_stats[ph]['occurrences'] += 1
            pattern_stats[ph]['templates'].add(template)

            overlap = pattern_node_ids & consumed_nodes
            if overlap:
                pattern_stats[ph]['blocked'] += 1
                blocker = find_blocker_for_nodes(overlap, matches, match, consumed_nodes, input_order)
                if blocker:
                    pattern_stats[ph]['blocked_by'][blocker] += 1
            else:
                pattern_stats[ph]['wins'] += 1
                pattern_stats[ph]['templates_wins'].add(template)
                consumed_nodes.update(pattern_node_ids)

    results = []
    for p in sorted_patterns:
        ph = p['pattern_hash']
        stats = pattern_stats[ph]

        blocked_by_str = '; '.join(
            f"{bh[:8]}:{count}"
            for bh, count in sorted(stats['blocked_by'].items(), key=lambda x: -x[1])
        )

        templates_str = ','.join(sorted(stats['templates'], key=lambda x: int(x[1:])))
        templates_wins_str = ','.join(sorted(stats['templates_wins'], key=lambda x: int(x[1:])))

        results.append({
            'pattern_hash': ph,
            'pattern_string': p['pattern_string'],
            'pattern_length': p['pattern_length'],
            'priority': p['priority'],
            'occurrences': stats['occurrences'],
            'wins': stats['wins'],
            'blocked': stats['blocked'],
            'templates': templates_str,
            'templates_wins': templates_wins_str,
            'blocked_by': blocked_by_str
        })

    return results


# Find which pattern blocked the given nodes
def find_blocker_for_nodes(overlap_nodes: set, matches: list, current_match: dict, consumed_before: set, input_order: list) -> str:
    current_priority = (
        -current_match['pattern_length'],
        get_selection_order_index(current_match['pattern_hash'], input_order)
    )

    for match in matches:
        if match is current_match:
            continue

        match_priority = (
            -match['pattern_length'],
            get_selection_order_index(match['pattern_hash'], input_order)
        )

        if match_priority >= current_priority:
            continue

        if match['pattern_node_ids'] & overlap_nodes:
            return match['pattern_hash']

    return None


# Export results to CSV
def export_results(results: list, pattern_hashes: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    short_hashes = '_'.join(h[:8] for h in pattern_hashes[:3])
    if len(pattern_hashes) > 3:
        short_hashes += f'_plus{len(pattern_hashes) - 3}'

    filename = f'A_02f_interference_{short_hashes}.csv'
    df = pd.DataFrame(results)
    df.to_csv(output_path / filename, sep=';', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern_hashes', nargs='+', help='Pattern hashes to analyze (order = selection priority)')
    parser.add_argument('--dataset', required=True, help='Dataset CSV for pattern scanning')
    parser.add_argument('--patterns', required=True, help='Patterns CSV with metadata')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    args = parser.parse_args()

    analyze_interference(args.pattern_hashes, args.dataset, args.patterns, args.output_dir)
