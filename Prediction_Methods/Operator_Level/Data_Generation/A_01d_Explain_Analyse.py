#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import json
import psycopg2
import subprocess
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

# From config.py: Build database configuration from parameters
from config import get_db_config

# From config.py: Get first seed file per template Q1-Q22 excluding Q15
from config import get_first_seed_per_template

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
def export_explain_analyse_cold_cache(query_dir, output_dir, db_config, container_name):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    output_file = output_path / 'A_01d_explain_analyse_cold_cache.md'

    subprocess.run(['sudo', '-v'], capture_output=True)

    sql_files = get_first_seed_per_template(query_dir)

    with open(output_file, 'w') as f:
        write_header(f, len(sql_files))

        for idx, sql_file in enumerate(sql_files, 1):
            query = load_query(sql_file)
            process_query_with_cold_cache(f, idx, sql_file, query, db_config, container_name)

# FUNCTIONS

# Load SQL query from file
def load_query(sql_file):
    with open(sql_file, 'r') as f:
        return f.read().strip()

# Process query with cold cache restart and write results
def process_query_with_cold_cache(f, idx, sql_file, query, db_config, container_name):
    if not restart_orbstack_and_purge():
        write_error_section(f, idx, sql_file, "Restart failed")
        return

    if not wait_for_docker_ready():
        write_error_section(f, idx, sql_file, "Docker failed")
        return

    start_container(container_name)

    if not wait_for_postgres(db_config):
        write_error_section(f, idx, sql_file, "Postgres failed")
        return

    conn = psycopg2.connect(**db_config)
    explain_json = get_explain_analyse_json(conn, query)
    write_query_section(f, idx, sql_file, explain_json)
    conn.close()

# Execute EXPLAIN ANALYSE query and return JSON plan with runtime metrics
def get_explain_analyse_json(conn, query):
    conn.rollback()
    cursor = conn.cursor()
    explain_query = f"EXPLAIN (ANALYZE true, VERBOSE true, COSTS true, SUMMARY true, BUFFERS true, FORMAT JSON) {query}"
    cursor.execute(explain_query)
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    return result[0][0]

# Write markdown header with metadata
def write_header(f, total_queries):
    f.write("# EXPLAIN ANALYSE JSON - COLD CACHE - First Seeds\n\n")
    f.write(f"**Total Queries:** {total_queries}\n\n")
    f.write("---\n\n")

# Write query section with EXPLAIN ANALYSE JSON plan
def write_query_section(f, idx, sql_file, explain_json):
    template = sql_file.name.split('_')[0]
    f.write(f"## {idx}. {sql_file.name}\n\n")
    f.write(f"**Template:** {template}\n\n")
    f.write("### EXPLAIN ANALYSE JSON\n\n")
    f.write("```json\n")
    f.write(json.dumps(explain_json, indent=2))
    f.write("\n```\n\n")
    f.write("---\n\n")

# Write error section when cold cache preparation fails
def write_error_section(f, idx, sql_file, error_message):
    f.write(f"## {idx}. {sql_file.name}\n\n")
    f.write(f"**ERROR:** {error_message}\n\n")
    f.write("---\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query_dir", help="Path to query directory")
    parser.add_argument("--output-dir", required=True, help="Output directory for markdown file")
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

    export_explain_analyse_cold_cache(
        query_dir=Path(args.query_dir),
        output_dir=args.output_dir,
        db_config=db_config,
        container_name=args.container_name
    )
