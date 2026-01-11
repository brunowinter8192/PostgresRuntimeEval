#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import hashlib
import pandas as pd
from pathlib import Path
from multiprocessing import Pool

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']
APPROACHES = ['approach_3']

SCRIPT_DIR = Path(__file__).resolve().parent
OPERATOR_DATASET_DIR = SCRIPT_DIR.parent / 'Dataset_Operator'


# ORCHESTRATOR
def batch_dry_prediction() -> None:
    tasks = [(template, approach) for template in TEMPLATES for approach in APPROACHES]
    with Pool(6) as pool:
        pool.map(process_template, tasks)


# FUNCTIONS

# Process single template-approach combination
def process_template(task: tuple) -> None:
    template, approach = task
    approach_dir = SCRIPT_DIR / template / approach
    test_file = OPERATOR_DATASET_DIR / template / 'test.csv'

    if not test_file.exists():
        return

    patterns_file = approach_dir / 'patterns_filtered.csv'
    if not patterns_file.exists():
        patterns_file = approach_dir / 'patterns.csv'
    if not patterns_file.exists():
        return

    df_test = pd.read_csv(test_file, delimiter=';')
    pattern_info, pattern_order = load_pattern_info(patterns_file)

    used_patterns, plan_stats = collect_used_patterns(df_test, pattern_info, pattern_order)

    export_used_patterns(used_patterns, pattern_info, approach_dir)
    export_md_report(template, used_patterns, pattern_info, plan_stats, len(df_test['query_file'].unique()), approach_dir)


# Load pattern info from CSV sorted by length descending
def load_pattern_info(patterns_file: Path) -> tuple:
    df = pd.read_csv(patterns_file, delimiter=';')
    df_sorted = df.sort_values(['pattern_length', 'occurrence_count'], ascending=[False, False])
    pattern_order = df_sorted['pattern_hash'].tolist()

    pattern_info = {}
    for _, row in df_sorted.iterrows():
        pattern_hash = row['pattern_hash']
        pattern_info[pattern_hash] = {
            'pattern_string': row['pattern_string'],
            'length': int(row['pattern_length']),
            'operator_count': row.get('operator_count', row['pattern_length']),
            'occurrence_count': int(row.get('occurrence_count', 0))
        }

    return pattern_info, pattern_order


# Collect used patterns from all test queries
def collect_used_patterns(df_test: pd.DataFrame, pattern_info: dict, pattern_order: list) -> tuple:
    used_patterns = set()
    plan_hashes_seen = set()
    tree_data = []

    for query_file in df_test['query_file'].unique():
        query_ops = df_test[df_test['query_file'] == query_file].sort_values('node_id').reset_index(drop=True)
        plan_hash = compute_plan_hash(query_ops)

        if plan_hash in plan_hashes_seen:
            continue

        plan_hashes_seen.add(plan_hash)

        root = build_tree_from_dataframe(query_ops)
        all_nodes = extract_all_nodes(root)
        consumed_nodes, pattern_assignments = build_pattern_assignments(all_nodes, pattern_info, pattern_order)

        used_patterns.update(pattern_assignments.values())
        tree_data.append({
            'query_ops': query_ops,
            'consumed_nodes': consumed_nodes,
            'pattern_assignments': pattern_assignments,
            'query_file': query_file
        })

    return used_patterns, {'unique_plans': len(tree_data), 'trees': tree_data}


# Export used patterns to CSV
def export_used_patterns(used_patterns: set, pattern_info: dict, output_dir: Path) -> None:
    rows = []
    for pattern_hash in sorted(used_patterns):
        info = pattern_info.get(pattern_hash, {})
        rows.append({
            'pattern_hash': pattern_hash,
            'pattern_string': info.get('pattern_string', ''),
            'pattern_length': info.get('length', 0),
            'occurrence_count': info.get('occurrence_count', 0)
        })

    df = pd.DataFrame(rows)
    df.to_csv(output_dir / 'used_patterns.csv', index=False, sep=';')


# Export MD report
def export_md_report(template: str, used_patterns: set, pattern_info: dict, plan_stats: dict, total_queries: int, output_dir: Path) -> None:
    md_dir = output_dir / 'md'
    md_dir.mkdir(exist_ok=True)

    total_patterns = len(pattern_info)
    used_count = len(used_patterns)
    reduction = ((total_patterns - used_count) / total_patterns * 100) if total_patterns > 0 else 0

    lines = [
        f'# Dry Prediction Report: {template}',
        '',
        '## Summary',
        '',
        f'- **Total Test Queries:** {total_queries}',
        f'- **Unique Plan Structures:** {plan_stats["unique_plans"]}',
        f'- **Total Patterns Available:** {total_patterns}',
        f'- **Patterns Used:** {used_count}',
        f'- **Reduction:** {reduction:.1f}%',
        '',
        '## Used Patterns',
        ''
    ]

    for pattern_hash in sorted(used_patterns):
        info = pattern_info.get(pattern_hash, {})
        pattern_string = info.get('pattern_string', 'Unknown')
        lines.append(f'- `{pattern_hash[:12]}...` {pattern_string}')

    lines.extend(['', '## Query Trees', ''])

    for i, tree_info in enumerate(plan_stats.get('trees', []), 1):
        lines.append(f'### Plan {i} (Example: {tree_info["query_file"]})')
        lines.append('')
        lines.append('```')
        tree_lines = render_tree_markdown(
            tree_info['query_ops'],
            tree_info['consumed_nodes'],
            tree_info['pattern_assignments']
        )
        lines.extend(tree_lines)
        lines.append('```')
        lines.append('')

    report_file = md_dir / '00_dry_prediction_report.md'
    report_file.write_text('\n'.join(lines))


# Render query tree as markdown with pattern annotations
def render_tree_markdown(df_query: pd.DataFrame, consumed_nodes: set, pattern_assignments: dict) -> list:
    lines = []
    min_depth = df_query['depth'].min()

    for _, row in df_query.iterrows():
        depth = row['depth']
        indent = '  ' * (depth - min_depth)
        node_type = row['node_type']
        node_id = row['node_id']

        marker = ''
        if node_id in pattern_assignments:
            marker = ' [PATTERN ROOT]'
        elif node_id in consumed_nodes:
            marker = ' [consumed]'

        suffix = ' - ROOT' if depth == min_depth else ''
        lines.append(f'{indent}Node {node_id} ({node_type}){marker}{suffix}')

    return lines


# Tree building and pattern matching functions

class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# Build tree structure from flat DataFrame
def build_tree_from_dataframe(query_ops: pd.DataFrame) -> QueryNode:
    nodes = {}
    root = None
    min_depth = query_ops['depth'].min()

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'] if pd.notna(row['parent_relationship']) else '',
            depth=row['depth'],
            node_id=row['node_id']
        )
        nodes[row['node_id']] = node

        if row['depth'] == min_depth:
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
def extract_all_nodes(node: QueryNode) -> list:
    nodes = [node]
    for child in node.children:
        nodes.extend(extract_all_nodes(child))
    return nodes


# Compute MD5 hash for pattern subtree structure
def compute_pattern_hash(node: QueryNode, remaining_length: int) -> str:
    if remaining_length == 1 or len(node.children) == 0:
        return hashlib.md5(node.node_type.encode()).hexdigest()

    child_hashes = []
    for child in node.children:
        child_hash = compute_pattern_hash(child, remaining_length - 1)
        combined = f"{child_hash}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)
    return hashlib.md5(combined_string.encode()).hexdigest()


# Check if node has subtree of required depth
def has_children_at_length(node: QueryNode, pattern_length: int) -> bool:
    if pattern_length == 1:
        return True
    if pattern_length == 2:
        return len(node.children) > 0
    if len(node.children) == 0:
        return False
    return any(has_children_at_length(child, pattern_length - 1) for child in node.children)


# Extract all node IDs in pattern subtree
def extract_pattern_node_ids(node: QueryNode, remaining_length: int) -> list:
    if remaining_length == 1 or len(node.children) == 0:
        return [node.node_id]

    node_ids = [node.node_id]
    for child in node.children:
        child_ids = extract_pattern_node_ids(child, remaining_length - 1)
        node_ids.extend(child_ids)
    return node_ids


# Build pattern assignments matching patterns to query nodes
def build_pattern_assignments(all_nodes: list, pattern_info: dict, pattern_order: list) -> tuple:
    consumed_nodes = set()
    pattern_assignments = {}

    for pattern_hash in pattern_order:
        if pattern_hash not in pattern_info:
            continue

        info = pattern_info[pattern_hash]
        pattern_length = info['length']

        for node in all_nodes:
            if node.node_id in consumed_nodes:
                continue
            if not has_children_at_length(node, pattern_length):
                continue

            pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
            if any(nid in consumed_nodes for nid in pattern_node_ids):
                continue

            computed_hash = compute_pattern_hash(node, pattern_length)
            if computed_hash == pattern_hash:
                # Single-Pattern-Constraint: Skip if this pattern would consume ALL nodes
                would_consume_all = (len(consumed_nodes) == 0 and len(pattern_node_ids) == len(all_nodes))
                if would_consume_all:
                    continue

                consumed_nodes.update(pattern_node_ids)
                pattern_assignments[node.node_id] = pattern_hash

    return consumed_nodes, pattern_assignments


# Compute hash for unique plan structure
def compute_plan_hash(query_ops: pd.DataFrame) -> str:
    sorted_ops = query_ops.sort_values('node_id')
    structure = [(row['node_type'], row['depth'], row['parent_relationship'])
                 for _, row in sorted_ops.iterrows()]
    return hashlib.md5(str(structure).encode()).hexdigest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--templates", nargs='+', default=TEMPLATES, help="Templates to process")
    args = parser.parse_args()

    TEMPLATES = args.templates
    batch_dry_prediction()
