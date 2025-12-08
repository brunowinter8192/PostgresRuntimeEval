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

    for _, row in query_ops.iterrows():
        node = QueryNode(
            node_type=row['node_type'],
            parent_relationship=row['parent_relationship'] if pd.notna(row['parent_relationship']) else '',
            depth=row['depth'],
            node_id=row['node_id']
        )
        nodes[row['node_id']] = node

        if row['depth'] == min_depth:
            root = node

    for idx in range(len(query_ops)):
        current_row = query_ops.iloc[idx]
        current_node = nodes[current_row['node_id']]
        current_depth = current_row['depth']

        for j in range(idx + 1, len(query_ops)):
            next_row = query_ops.iloc[j]

            if next_row['depth'] == current_depth + 1:
                child_node = nodes[next_row['node_id']]
                current_node.add_child(child_node)
            elif next_row['depth'] <= current_depth:
                break

    return root


# Extract all nodes from tree as flat list
def extract_all_nodes(node: QueryNode) -> list:
    nodes = [node]

    for child in node.children:
        nodes.extend(extract_all_nodes(child))

    return nodes


# Compute MD5 hash for depth-1 pattern (parent + direct children)
def compute_pattern_hash(node: QueryNode) -> str:
    if len(node.children) == 0:
        return None

    child_hashes = []
    for child in node.children:
        combined = f"{child.node_type}:{child.parent_relationship}"
        child_hashes.append(combined)

    child_hashes.sort()
    combined_string = node.node_type + '|' + '|'.join(child_hashes)

    return hashlib.md5(combined_string.encode()).hexdigest()


# Build query tree string for visualization
def build_query_tree_string(df_query: pd.DataFrame) -> str:
    lines = []
    min_depth = df_query['depth'].min()

    for _, row in df_query.iterrows():
        depth = row['depth']
        indent = '  ' * (depth - min_depth)
        node_type = row['node_type']
        node_id = row['node_id']
        suffix = ' - ROOT' if depth == min_depth else ''
        lines.append(f'{indent}Node {node_id} ({node_type}){suffix}')

    return '\n'.join(lines)
