#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import csv
import subprocess
import time
from pathlib import Path

import psycopg2

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Database connection and container settings
from mapping_config import DB_CONFIG, CONTAINER_NAME


# ORCHESTRATOR

# Execute TPC-H queries with cold cache restart and collect runtime measurements
def runtime_collection_workflow(query_dir: Path, output_dir: Path) -> None:
    subprocess.run(['sudo', '-v'], capture_output=True)
    query_files = get_all_query_files(query_dir)
    results = execute_all_queries(query_files)
    export_results(results, output_dir)


# FUNCTIONS

# Collect all SQL query files from template directories
def get_all_query_files(query_dir: Path) -> list:
    all_files = []
    for template_dir in sorted(query_dir.glob('Q*')):
        if template_dir.is_dir():
            all_files.extend(sorted(template_dir.glob('*.sql')))
    return all_files


# Execute all queries with cold cache restart between each
def execute_all_queries(query_files: list) -> list:
    results = []
    for query_file in query_files:
        result = execute_single_query_with_restart(query_file)
        if result:
            results.append(result)
    return results


# Execute single query after full cache purge and container restart
def execute_single_query_with_restart(query_file: Path) -> dict:
    with open(query_file, 'r') as f:
        query = f.read().strip()

    if not restart_orbstack_and_purge():
        return None

    if not wait_for_docker_ready():
        return None

    start_container()

    if not wait_for_postgres():
        return None

    conn = psycopg2.connect(**DB_CONFIG)
    runtime_ms = execute_query(conn, query)
    conn.close()

    return {
        'query_file': query_file.name,
        'template': query_file.parent.name,
        'runtime': runtime_ms
    }


# Restart OrbStack and purge system memory cache
def restart_orbstack_and_purge() -> bool:
    subprocess.run(['osascript', '-e', 'quit app "OrbStack"'], capture_output=True)
    if not wait_for_orbstack_stopped():
        return False
    subprocess.run(['sudo', 'purge'], capture_output=True)
    subprocess.run(['open', '-a', 'OrbStack', '-g'], capture_output=True)
    if not wait_for_orbstack_running():
        return False
    return True


# Wait for OrbStack process to fully stop
def wait_for_orbstack_stopped(max_attempts: int = 30) -> bool:
    for attempt in range(max_attempts):
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if 'OrbStack.app' not in result.stdout:
            return True
        time.sleep(0.5)
    return False


# Wait for OrbStack to report running status
def wait_for_orbstack_running(max_attempts: int = 60) -> bool:
    for attempt in range(max_attempts):
        try:
            result = subprocess.run(['orbctl', 'status'], capture_output=True, text=True, timeout=2)
            if 'Running' in result.stdout:
                return True
        except subprocess.TimeoutExpired:
            pass
        time.sleep(1)
    return False


# Wait for Docker daemon to be ready
def wait_for_docker_ready(max_attempts: int = 60) -> bool:
    for attempt in range(max_attempts):
        try:
            result = subprocess.run(['docker', 'ps'], capture_output=True, timeout=3)
            if result.returncode == 0:
                return True
        except subprocess.TimeoutExpired:
            pass
        time.sleep(1)
    return False


# Start the PostgreSQL container
def start_container() -> None:
    subprocess.run(['docker', 'start', CONTAINER_NAME], capture_output=True)


# Wait for PostgreSQL database to accept connections
def wait_for_postgres(max_attempts: int = 30) -> bool:
    for attempt in range(max_attempts):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            conn.close()
            return True
        except psycopg2.OperationalError:
            time.sleep(1)
    return False


# Execute SQL query and return runtime in milliseconds
def execute_query(conn, query: str) -> float:
    conn.rollback()
    cursor = conn.cursor()
    start_time = time.perf_counter()
    cursor.execute(query)
    cursor.fetchall()
    end_time = time.perf_counter()
    cursor.close()
    conn.commit()
    return (end_time - start_time) * 1000


# Export runtime results to CSV file with semicolon delimiter
def export_results(results: list, output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    csv_path = output_dir / '01_runtimes.csv'

    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['query_file', 'template', 'runtime'], delimiter=';')
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect query runtimes with cold cache restart")
    parser.add_argument("query_dir", help="Directory containing Q* template folders with SQL files")
    parser.add_argument("--output-dir", default=None, help="Output directory for CSV (default: script_dir/csv)")

    args = parser.parse_args()

    query_path = Path(args.query_dir)
    if args.output_dir:
        output_path = Path(args.output_dir)
    else:
        output_path = Path(__file__).parent / 'csv'

    runtime_collection_workflow(query_path, output_path)
