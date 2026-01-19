#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import json
import psycopg2
import subprocess
import csv
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

# From config.py: Build database configuration from parameters
from config import get_db_config

# From config.py: Get all query files from Q1-Q22 excluding Q15
from config import get_query_files_all_templates

# From config.py: Restart OrbStack and purge macOS cache
from config import restart_orbstack_and_purge

# From config.py: Wait for Docker daemon to be ready
from config import wait_for_docker_ready

# From config.py: Start Docker container by name
from config import start_container

# From config.py: Wait for PostgreSQL to accept connections
from config import wait_for_postgres

# From config.py: Default Docker container name
from config import DEFAULT_CONTAINER_NAME

# ORCHESTRATOR
def extract_all_targets(query_dir, output_dir, db_config, container_name):
    subprocess.run(['sudo', '-v'], capture_output=True)

    all_query_files = get_query_files_all_templates(query_dir)
    all_targets_data = []
    node_id_counter = [1]

    for query_file in all_query_files:
        query = load_query(query_file)

        if not prepare_cold_cache_environment(container_name, db_config):
            continue

        conn = psycopg2.connect(**db_config)
        explain_json = get_explain_analyse_json(conn, query)
        plan_root = explain_json[0]["Plan"]
        query_name = query_file.stem
        extract_targets(plan_root, query_name, node_id_counter, targets_data=all_targets_data)
        conn.close()

    export_targets_csv(all_targets_data, output_dir)

# FUNCTIONS

# Load SQL query from file
def load_query(query_file):
    with open(query_file, 'r') as f:
        return f.read().strip()

# Restart environment with cold cache and prepare database connection
def prepare_cold_cache_environment(container_name, db_config):
    if not restart_orbstack_and_purge():
        return False
    if not wait_for_docker_ready():
        return False
    start_container(container_name)
    return wait_for_postgres(db_config)

# Execute EXPLAIN ANALYSE query and return JSON plan with runtime metrics
def get_explain_analyse_json(conn, query):
    conn.rollback()
    cursor = conn.cursor()
    explain_query = f"EXPLAIN (ANALYZE true, VERBOSE true, COSTS true, FORMAT JSON) {query}"
    cursor.execute(explain_query)
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    return result[0][0]

# Recursively extract runtime targets from plan node and children
def extract_targets(plan_node, query_file, node_id_counter, depth=0, parent_relationship=None, targets_data=None):
    if targets_data is None:
        targets_data = []

    node_type = plan_node.get("Node Type", "Unknown")
    actual_startup_time = plan_node.get("Actual Startup Time", None)
    actual_total_time = plan_node.get("Actual Total Time", None)
    subplan_name = plan_node.get("Subplan Name", None)

    target_row = {
        'query_file': query_file,
        'node_id': node_id_counter[0],
        'node_type': node_type,
        'depth': depth,
        'parent_relationship': parent_relationship,
        'subplan_name': subplan_name,
        'actual_startup_time': actual_startup_time,
        'actual_total_time': actual_total_time
    }

    targets_data.append(target_row)
    node_id_counter[0] += 1

    children = plan_node.get("Plans", [])
    for child in children:
        child_parent_rel = child.get("Parent Relationship", None)
        extract_targets(child, query_file, node_id_counter, depth + 1,
                       parent_relationship=child_parent_rel, targets_data=targets_data)

    return targets_data

# Export targets data to CSV with semicolon delimiter
def export_targets_csv(all_targets_data, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    csv_path = output_path / '01b_targets.csv'

    fieldnames = [
        'query_file', 'node_id', 'node_type', 'depth',
        'parent_relationship', 'subplan_name',
        'actual_startup_time', 'actual_total_time'
    ]

    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(all_targets_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query_dir", help="Path to query directory")
    parser.add_argument("--output-dir", required=True, help="Output directory for CSV file")
    parser.add_argument("--container-name", default=DEFAULT_CONTAINER_NAME, help="Docker container name")
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

    extract_all_targets(
        query_dir=Path(args.query_dir),
        output_dir=args.output_dir,
        db_config=db_config,
        container_name=args.container_name
    )
