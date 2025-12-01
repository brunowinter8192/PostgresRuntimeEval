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
def export_pg_class_statistics(query_dir, output_dir, db_config):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_path / f'pg_class_per_operator_{timestamp}.md'

    sql_files = get_first_seed_per_template(query_dir)
    conn = psycopg2.connect(**db_config)

    with open(output_file, 'w') as f:
        write_header(f, len(sql_files))

        for idx, sql_file in enumerate(sql_files, 1):
            query = load_query(sql_file)
            explain_json = get_explain_json(conn, query)

            operators_data = []
            traverse_plan(explain_json[0]["Plan"], operators_data)

            write_query_section(f, idx, sql_file, operators_data, conn)

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

# Traverse plan tree and extract operator information with tables
def traverse_plan(plan_node, operators_data, operator_id=0):
    operator_id += 1
    node_type = plan_node.get("Node Type", "Unknown")
    tables = extract_tables_from_operator(plan_node)

    operators_data.append({
        'operator_id': operator_id,
        'node_type': node_type,
        'tables': tables,
        'plan_rows': plan_node.get("Plan Rows", 0),
        'plan_width': plan_node.get("Plan Width", 0),
        'startup_cost': plan_node.get("Startup Cost", 0.0),
        'total_cost': plan_node.get("Total Cost", 0.0)
    })

    if "Plans" in plan_node:
        for child in plan_node["Plans"]:
            operator_id = traverse_plan(child, operators_data, operator_id)

    return operator_id

# Extract all table names referenced by operator
def extract_tables_from_operator(plan_node):
    tables = set()

    if "Relation Name" in plan_node:
        tables.add(plan_node["Relation Name"])

    if "Group Key" in plan_node:
        for key in plan_node["Group Key"]:
            if isinstance(key, str) and "." in key:
                table = key.split(".")[0]
                tables.add(table)

    if "Output" in plan_node:
        for col in plan_node["Output"]:
            if isinstance(col, str) and "." in col:
                parts = col.split(".")
                if len(parts) >= 2:
                    table = parts[0]
                    if not table.startswith("("):
                        tables.add(table)

    if "Sort Key" in plan_node:
        for key in plan_node["Sort Key"]:
            if isinstance(key, str) and "." in key:
                table = key.split(".")[0]
                tables.add(table)

    if "Hash Cond" in plan_node:
        cond = plan_node["Hash Cond"]
        if isinstance(cond, str):
            for part in cond.split():
                if "." in part:
                    table = part.split(".")[0].strip("()")
                    if table and not table.startswith("("):
                        tables.add(table)

    return tables

# Write markdown header with metadata
def write_header(f, total_queries):
    f.write("# PG_CLASS Statistics - Per Operator\n\n")
    f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write(f"**Total Queries:** {total_queries}\n\n")
    f.write("---\n\n")

# Write query section with all operators
def write_query_section(f, idx, sql_file, operators_data, conn):
    f.write(f"## {idx}. {sql_file.name}\n\n")
    f.write(f"**Template:** Q{sql_file.name.split('_')[0][1:]}\n\n")
    f.write(f"**Total Operators:** {len(operators_data)}\n\n")

    for op_idx, op_data in enumerate(operators_data, 1):
        write_operator_section(f, op_idx, op_data, conn)

# Write operator section with table statistics
def write_operator_section(f, op_idx, op_data, conn):
    f.write(f"### Operator {op_idx}: {op_data['node_type']}\n\n")
    f.write(f"**Operator ID:** {op_data['operator_id']}\n\n")
    f.write(f"**Plan Rows:** {op_data['plan_rows']:,}\n\n")
    f.write(f"**Plan Width:** {op_data['plan_width']}\n\n")
    f.write(f"**Startup Cost:** {op_data['startup_cost']:.2f}\n\n")
    f.write(f"**Total Cost:** {op_data['total_cost']:.2f}\n\n")

    if op_data['tables']:
        write_table_statistics(f, op_data['tables'], conn)
    else:
        f.write("**No table references found**\n\n")

    f.write("---\n\n")

# Query and write pg_class statistics for referenced tables
def write_table_statistics(f, tables, conn):
    f.write(f"**Referenced Tables:** {', '.join(sorted(tables))}\n\n")

    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            relname,
            reltuples::bigint,
            relpages::bigint,
            relkind
        FROM pg_class
        WHERE relname = ANY(%s)
        ORDER BY relname
    """, (list(tables),))

    pg_results = cursor.fetchall()
    cursor.close()

    if pg_results:
        f.write("#### PG_CLASS Statistics\n\n")
        f.write("| Table Name | reltuples | relpages | Kind |\n")
        f.write("|------------|-----------|----------|------|\n")
        for row in pg_results:
            relname, reltuples, relpages, relkind = row
            kind_name = {'r': 'table', 'i': 'index'}.get(relkind, relkind)
            f.write(f"| {relname} | {reltuples:,} | {relpages:,} | {kind_name} |\n")
        f.write("\n")

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

    export_pg_class_statistics(
        query_dir=Path(args.query_dir),
        output_dir=args.output_dir,
        db_config=db_config
    )
