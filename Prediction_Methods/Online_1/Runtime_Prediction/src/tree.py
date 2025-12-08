#!/usr/bin/env python3

# INFRASTRUCTURE
import pandas as pd


# FUNCTIONS

class QueryNode:
    def __init__(self, node_type: str, parent_relationship: str, depth: int, node_id: int, row_data=None):
        self.node_type = node_type
        self.parent_relationship = parent_relationship
        self.depth = depth
        self.node_id = node_id
        self.row_data = row_data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# Build tree from flat DataFrame
def build_tree_from_dataframe(query_ops: pd.DataFrame, include_row_data: bool = False):
    nodes = {}
    root = None
    min_depth = query_ops['depth'].min()

    for idx, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'] if pd.notna(row['parent_relationship']) else '',
            depth=row['depth'],
            node_id=row['node_id'],
            row_data=row if include_row_data else None
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


# Extract all nodes from tree
def extract_all_nodes(node) -> list:
    nodes = [node]
    for child in node.children:
        nodes.extend(extract_all_nodes(child))
    return nodes


# Check if node has children at target length
def has_children_at_length(node, pattern_length: int) -> bool:
    if pattern_length == 1:
        return True
    if pattern_length == 2:
        return len(node.children) > 0
    if len(node.children) == 0:
        return False
    return any(has_children_at_length(child, pattern_length - 1) for child in node.children)


# Count operators in pattern
def count_operators(node, remaining_length: int) -> int:
    if remaining_length == 1 or len(node.children) == 0:
        return 1
    child_counts = sum(count_operators(child, remaining_length - 1) for child in node.children)
    return 1 + child_counts


# Extract pattern node IDs
def extract_pattern_node_ids(node, remaining_length: int) -> list:
    if remaining_length == 1 or len(node.children) == 0:
        return [node.node_id]

    node_ids = [node.node_id]
    for child in node.children:
        child_ids = extract_pattern_node_ids(child, remaining_length - 1)
        node_ids.extend(child_ids)

    return node_ids


# Get children from full query
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
