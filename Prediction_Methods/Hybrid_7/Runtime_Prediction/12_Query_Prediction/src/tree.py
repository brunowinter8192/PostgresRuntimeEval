# INFRASTRUCTURE

import hashlib
import pandas as pd


class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.children = []

    # Append child node to children list
    def add_child(self, child_node):
        self.children.append(child_node)


# FUNCTIONS

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


# Get direct children from full query ops by node ID
def get_children_from_full_query(full_query_ops: pd.DataFrame, parent_node_id: int) -> list:
    parent_row = full_query_ops[full_query_ops['node_id'] == parent_node_id]

    if parent_row.empty:
        return []

    parent_depth = parent_row.iloc[0]['depth']
    parent_idx = parent_row.index[0]
    children = []

    for idx in range(parent_idx + 1, len(full_query_ops)):
        row = full_query_ops.iloc[idx]

        if row['depth'] == parent_depth + 1:
            children.append(row)
        elif row['depth'] <= parent_depth:
            break

    return children


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


# Build pattern assignments matching patterns to query nodes (Phase 1)
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

            computed_hash = compute_pattern_hash(node, pattern_length)
            if computed_hash == pattern_hash:
                pattern_node_ids = extract_pattern_node_ids(node, pattern_length)
                consumed_nodes.update(pattern_node_ids)
                pattern_assignments[node.node_id] = pattern_hash

    return consumed_nodes, pattern_assignments
