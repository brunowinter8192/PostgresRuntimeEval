#!/usr/bin/env python3

# INFRASTRUCTURE
import sys
import psycopg2
import json
import argparse
from pathlib import Path
from datetime import datetime

sys.path.append(str(Path(__file__).parent))

# From config.py: Build database configuration from parameters
from config import get_db_config

# From config.py: Get first seed file per template Q1-Q22 excluding Q15
from config import get_first_seed_per_template

# ORCHESTRATOR
def export_explain_json(query_dir, output_dir, db_config):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_path / f'explain_json_export_{timestamp}.md'

    sql_files = get_first_seed_per_template(query_dir)
    conn = psycopg2.connect(**db_config)

    with open(output_file, 'w') as f:
        write_header(f, len(sql_files))

        for idx, sql_file in enumerate(sql_files, 1):
            query = load_query(sql_file)
            explain_json = get_explain_json(conn, query)
            write_query_section(f, idx, sql_file, explain_json)

    conn.close()

# FUNCTIONS

# Load SQL query from file
def load_query(sql_file):
    with open(sql_file, 'r') as f:
        return f.read().strip()

# Execute EXPLAIN query and return JSON plan
def get_explain_json(conn, query):
    cursor = conn.cursor()
    explain_query = f"EXPLAIN (VERBOSE true, COSTS true, FORMAT JSON) {query}"
    cursor.execute(explain_query)
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    return result[0][0]

# Write markdown header with metadata
def write_header(f, total_queries):
    f.write("# EXPLAIN JSON Export - All Queries\n\n")
    f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write(f"**Total Queries:** {total_queries}\n\n")
    f.write("---\n\n")

# Write query section with EXPLAIN JSON plan
def write_query_section(f, idx, sql_file, explain_json):
    f.write(f"## {idx}. {sql_file.name}\n\n")
    f.write(f"**Template:** Q{sql_file.name.split('_')[0][1:]}\n\n")
    f.write(f"**File Path:** `{sql_file}`\n\n")
    f.write("### EXPLAIN JSON\n\n")
    f.write("```json\n")
    f.write(json.dumps(explain_json, indent=2))
    f.write("\n```\n\n")
    f.write("---\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query_dir", help="Path to query directory")
    parser.add_argument("--output-dir", required=True, help="Output directory for markdown file")
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

    export_explain_json(
        query_dir=Path(args.query_dir),
        output_dir=args.output_dir,
        db_config=db_config
    )
