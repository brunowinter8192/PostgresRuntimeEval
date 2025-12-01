#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import psycopg2
import subprocess
import time
import csv
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

# From config.py: Build database configuration from parameters
from config import get_db_config

# From config.py: Default Docker container name
from config import DEFAULT_CONTAINER_NAME

# From config.py: Restart OrbStack and purge macOS cache
from config import restart_orbstack_and_purge

# From config.py: Wait for Docker daemon to be ready
from config import wait_for_docker_ready

# From config.py: Start Docker container by name
from config import start_container

# From config.py: Wait for PostgreSQL to accept connections
from config import wait_for_postgres

# ORCHESTRATOR
def validate_cold_cache(query_dir, output_dir, runs, db_config, container_name):
    subprocess.run(['sudo', '-v'], capture_output=True)

    sql_files = get_first_seed_q1(query_dir)
    all_runs = []
    stats = []

    for sql_file in sql_files:
        query = load_query(sql_file)
        times = execute_cold_cache_runs(query, sql_file, runs, db_config, container_name)

        for exec_time in times:
            all_runs.append({'query_file': sql_file.name, 'runtime': exec_time})

        if len(times) >= 2:
            stats.append(calculate_statistics(sql_file.name, times))

    export_results(output_dir, all_runs, stats)

# FUNCTIONS

# Get first seed query file from Q1 template
def get_first_seed_q1(query_dir):
    template_dir = query_dir / 'Q1'
    if template_dir.exists() and template_dir.is_dir():
        sql_files = sorted(template_dir.glob('*.sql'))
        if sql_files:
            return [sql_files[0]]
    return []

# Load SQL query from file
def load_query(sql_file):
    with open(sql_file, 'r') as f:
        return f.read().strip()

# Execute query multiple times with cold cache restarts between runs
def execute_cold_cache_runs(query, sql_file, runs, db_config, container_name):
    times = []
    for run in range(1, runs + 1):
        if not restart_orbstack_and_purge():
            continue
        if not wait_for_docker_ready():
            continue
        start_container(container_name)
        if not wait_for_postgres(db_config):
            continue

        conn = psycopg2.connect(**db_config)
        exec_time = execute_query(conn, query)
        conn.close()
        times.append(exec_time)

    return times

# Execute query and measure execution time in milliseconds
def execute_query(conn, query):
    conn.rollback()
    cursor = conn.cursor()
    start_time = time.perf_counter()
    cursor.execute(query)
    cursor.fetchall()
    end_time = time.perf_counter()
    cursor.close()
    conn.commit()
    return (end_time - start_time) * 1000

# Calculate mean and span statistics from execution times
def calculate_statistics(query_name, times):
    mean = sum(times) / len(times)
    span_ms = max(times) - min(times)
    span_percent = (span_ms / mean) * 100
    return {
        'query_file': query_name,
        'mean': mean,
        'spannweite_percent': span_percent,
        'spannweite_ms': span_ms
    }

# Export cold cache runs and statistics to CSV files
def export_results(output_dir, all_runs, stats):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    runs_csv = output_path / 'cold_cache_runs.csv'
    with open(runs_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['query_file', 'runtime'], delimiter=';')
        writer.writeheader()
        writer.writerows(all_runs)

    stats_csv = output_path / 'cold_cache_stats.csv'
    with open(stats_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['query_file', 'mean', 'spannweite_percent', 'spannweite_ms'], delimiter=';')
        writer.writeheader()
        writer.writerows(stats)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query_dir", help="Path to query directory")
    parser.add_argument("--output-dir", default="./", help="Output directory for CSV files")
    parser.add_argument("--runs", type=int, default=5, help="Number of cold cache runs")
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

    validate_cold_cache(
        query_dir=Path(args.query_dir),
        output_dir=args.output_dir,
        runs=args.runs,
        db_config=db_config,
        container_name=args.container_name
    )
