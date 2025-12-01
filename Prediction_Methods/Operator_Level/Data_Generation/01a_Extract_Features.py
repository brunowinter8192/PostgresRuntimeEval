#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import json
import psycopg2
import csv
import argparse
from pathlib import Path
from datetime import datetime

sys.path.append(str(Path(__file__).parent))

# From config.py: Build database configuration from parameters
from config import get_db_config

# From config.py: Get all query files from Q1-Q22 excluding Q15
from config import get_query_files_all_templates

# ORCHESTRATOR
def extract_all_features(query_dir, output_dir, db_config):
    all_query_files = get_query_files_all_templates(query_dir)
    conn = psycopg2.connect(**db_config)

    all_features_data = []
    node_id_counter = [1]

    for query_file in all_query_files:
        query = load_query(query_file)
        explain_json = get_explain_json(conn, query)
        plan_root = explain_json[0]["Plan"]
        query_name = query_file.stem
        extract_features(plan_root, query_name, conn, node_id_counter, features_data=all_features_data)

    conn.close()

    export_features_csv(all_features_data, output_dir)

# FUNCTIONS

# Load SQL query from file
def load_query(query_file):
    with open(query_file, 'r') as f:
        return f.read().strip()

# Execute EXPLAIN query and return JSON plan
def get_explain_json(conn, query):
    conn.rollback()
    cursor = conn.cursor()
    explain_query = f"EXPLAIN (ANALYZE false, VERBOSE true, COSTS true, FORMAT JSON) {query}"
    cursor.execute(explain_query)
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    return result[0][0]

# Recursively extract features from plan node and children
def extract_features(plan_node, query_file, conn, node_id_counter, depth=0, parent_relationship=None, features_data=None):
    if features_data is None:
        features_data = []

    node_type = plan_node.get("Node Type", "Unknown")
    nt = plan_node.get("Plan Rows", 0)
    startup_cost = plan_node.get("Startup Cost", 0.0)
    total_cost = plan_node.get("Total Cost", 0.0)
    plan_width = plan_node.get("Plan Width", 0)
    subplan_name = plan_node.get("Subplan Name", None)
    parallel_workers = plan_node.get("Workers Planned", 0)

    np, reltuples = get_table_statistics(plan_node, conn, node_type)
    nt1, nt2 = get_child_row_counts(plan_node)
    sel = calculate_selectivity(node_type, nt, nt1, nt2, reltuples)

    feature_row = {
        'query_file': query_file,
        'node_id': node_id_counter[0],
        'node_type': node_type,
        'depth': depth,
        'parent_relationship': parent_relationship,
        'subplan_name': subplan_name,
        'np': np,
        'nt': nt,
        'nt1': nt1,
        'nt2': nt2,
        'sel': sel,
        'startup_cost': startup_cost,
        'total_cost': total_cost,
        'plan_width': plan_width,
        'reltuples': reltuples,
        'parallel_workers': parallel_workers
    }

    features_data.append(feature_row)
    node_id_counter[0] += 1

    children = plan_node.get("Plans", [])
    for child in children:
        child_parent_rel = child.get("Parent Relationship", None)
        extract_features(child, query_file, conn, node_id_counter, depth + 1,
                        parent_relationship=child_parent_rel, features_data=features_data)

    return features_data

# Get table statistics from pg_class for scan operators
def get_table_statistics(plan_node, conn, node_type):
    relation_name = plan_node.get("Relation Name")
    if relation_name and node_type in ["Seq Scan", "Index Scan", "Index Only Scan", "Bitmap Heap Scan"]:
        pg_stats = get_pg_class_stats(conn, relation_name)
        return pg_stats['relpages'], pg_stats['reltuples']
    return 0, 0

# Query pg_class for relpages and reltuples statistics
def get_pg_class_stats(conn, table_name):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT relpages, reltuples
        FROM pg_class
        WHERE relname = %s AND relkind = 'r'
    """, (table_name,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return {'relpages': result[0], 'reltuples': result[1]}
    return {'relpages': 0, 'reltuples': 0}

# Extract row counts from outer and inner child nodes
def get_child_row_counts(plan_node):
    nt1 = 0
    nt2 = 0
    children = plan_node.get("Plans", [])
    for child in children:
        child_rel = child.get("Parent Relationship")
        if child_rel == "Outer":
            nt1 = child.get("Plan Rows", 0)
        elif child_rel == "Inner":
            nt2 = child.get("Plan Rows", 0)
    return nt1, nt2

# Calculate selectivity based on node type and row counts
def calculate_selectivity(node_type, nt, nt1, nt2, reltuples):
    if node_type in ["Seq Scan", "Index Scan", "Index Only Scan", "Bitmap Heap Scan"]:
        if reltuples > 0:
            return nt / reltuples
        return 0
    elif node_type in ["Hash Join", "Merge Join", "Nested Loop"]:
        if (nt1 * nt2) > 0:
            return nt / (nt1 * nt2)
        return 0
    elif nt1 > 0:
        return nt / nt1
    return 0

# Export features data to CSV with semicolon delimiter
def export_features_csv(all_features_data, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = output_path / f'features_{timestamp}.csv'

    fieldnames = [
        'query_file', 'node_id', 'node_type', 'depth',
        'parent_relationship', 'subplan_name',
        'np', 'nt', 'nt1', 'nt2', 'sel',
        'startup_cost', 'total_cost', 'plan_width',
        'reltuples', 'parallel_workers'
    ]

    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(all_features_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query_dir", help="Path to query directory")
    parser.add_argument("--output-dir", required=True, help="Output directory for CSV file")
    parser.add_argument("--db-host", default="localhost", help="Database host")
    parser.add_argument("--db-port", type=int, default=5432, help="Database port")
    parser.add_argument("--db-name", default="tpch", help="Database name")
    parser.add_argument("--db-user", default="postgres", help="Database user")
    parser.add_argument("--db-password", default="postgres", help="Database password")

    args = parser.parse_args()

    db_config = get_db_config(
        host=args.db_host,
        port=args.db_port,
        database=args.db_name,
        user=args.db_user,
        password=args.db_password
    )

    extract_all_features(
        query_dir=Path(args.query_dir),
        output_dir=args.output_dir,
        db_config=db_config
    )
