#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

import psycopg2

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Database connection settings
from mapping_config import DB_CONFIG


# ORCHESTRATOR

# Export EXPLAIN JSON output for one query per template, two for Q9
def export_explain_json(query_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "A_01a_explain_json_export.md"

    seed_files = get_first_seed_per_template(query_dir)
    conn = psycopg2.connect(**DB_CONFIG)
    sections = run_explain_all(seed_files, conn)
    q9_variant = find_q9_plan_variant(query_dir, conn, sections)
    if q9_variant:
        sections = insert_after_q9(sections, q9_variant)
    write_markdown(output_file, sections)
    conn.close()


# FUNCTIONS

# Get first seed file per template Q1-Q22 excluding Q15
def get_first_seed_per_template(query_dir: Path) -> list:
    first_seeds = []
    for template_num in range(1, 23):
        if template_num == 15:
            continue
        template_dir = query_dir / f"Q{template_num}"
        if template_dir.exists() and template_dir.is_dir():
            sql_files = sorted(template_dir.glob("*.sql"))
            if sql_files:
                first_seeds.append(sql_files[0])
    return first_seeds


# Run EXPLAIN for all seed files
def run_explain_all(seed_files: list, conn) -> list:
    sections = []
    for sql_file in seed_files:
        query = load_query(sql_file)
        explain_json = get_explain_json(conn, query)
        sections.append((sql_file, explain_json))
    return sections


# Find a Q9 seed with a different plan structure than the first Q9 entry
def find_q9_plan_variant(query_dir: Path, conn, sections: list):
    q9_section = next((s for s in sections if s[0].parent.name == 'Q9'), None)
    if not q9_section:
        return None
    reference = extract_plan_structure(q9_section[1])
    q9_dir = query_dir / "Q9"
    for sql_file in sorted(q9_dir.glob("*.sql")):
        if sql_file == q9_section[0]:
            continue
        query = load_query(sql_file)
        explain_json = get_explain_json(conn, query)
        if extract_plan_structure(explain_json) != reference:
            return (sql_file, explain_json)
    return None


# Extract ordered node types from plan JSON for structure comparison
def extract_plan_structure(plan_json) -> tuple:
    nodes = []
    def walk(node):
        nodes.append(node.get('Node Type', ''))
        for child in node.get('Plans', []):
            walk(child)
    walk(plan_json[0]['Plan'])
    return tuple(nodes)


# Insert Q9 variant section right after the first Q9 entry
def insert_after_q9(sections: list, variant: tuple) -> list:
    result = []
    for section in sections:
        result.append(section)
        if section[0].parent.name == 'Q9':
            result.append(variant)
    return result


# Load SQL query from file
def load_query(sql_file: Path) -> str:
    with open(sql_file, 'r') as f:
        return f.read().strip()


# Execute EXPLAIN query and return JSON plan
def get_explain_json(conn, query: str):
    conn.rollback()
    cursor = conn.cursor()
    explain_query = f"EXPLAIN (ANALYZE false, VERBOSE true, COSTS true, SUMMARY true, FORMAT JSON) {query}"
    cursor.execute(explain_query)
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    return result[0][0]


# Write complete markdown file from sections
def write_markdown(output_file: Path, sections: list) -> None:
    with open(output_file, 'w') as f:
        write_header(f, len(sections))
        for idx, (sql_file, explain_json) in enumerate(sections, 1):
            write_query_section(f, idx, sql_file, explain_json)


# Write markdown header with metadata
def write_header(f, total_queries: int) -> None:
    f.write("# EXPLAIN JSON Export - Plan Level Features\n\n")
    f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write(f"**Total Templates:** {total_queries}\n\n")
    f.write("**Purpose:** Raw EXPLAIN JSON output for feature exploration.\n\n")
    f.write("**EXPLAIN Options:** `ANALYZE false, VERBOSE true, COSTS true, SUMMARY true, FORMAT JSON`\n\n")
    f.write("---\n\n")


# Write query section with EXPLAIN JSON plan
def write_query_section(f, idx: int, sql_file: Path, explain_json) -> None:
    template = sql_file.parent.name
    f.write(f"## {idx}. {template} - {sql_file.name}\n\n")
    f.write(f"**Template:** {template}\n\n")
    f.write(f"**File:** `{sql_file.name}`\n\n")
    f.write("### EXPLAIN JSON\n\n")
    f.write("```json\n")
    f.write(json.dumps(explain_json, indent=2))
    f.write("\n```\n\n")
    f.write("---\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export EXPLAIN JSON for feature exploration")
    parser.add_argument("query_dir", help="Directory containing Q* template folders with SQL files")
    parser.add_argument("--output-dir", required=True, help="Output directory for markdown file")

    args = parser.parse_args()

    export_explain_json(
        query_dir=Path(args.query_dir),
        output_dir=Path(args.output_dir)
    )
