#!/usr/bin/env python3

# Infrastructure
import psycopg2
import json
from pathlib import Path
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'tpch',
    'user': 'postgres',
    'password': 'postgres'
}

QUERY_DIR = Path('/Users/brunowinter2000/Documents/Thesis/2025_2026/Plan-Level/Generated_Queries/Q9')
OUTPUT_DIR = Path('/Users/brunowinter2000/Documents/Thesis/2025_2026/Hybrid/Konzept/Q9Problem/md')

# Orchestrator
def export_q9_explains():
    sql_files = load_q9_queries()
    explain_data = execute_explains(sql_files)
    export_to_markdown(explain_data)

# Load all Q9 SQL query files
def load_q9_queries():
    return sorted(QUERY_DIR.glob('*.sql'))

# Execute EXPLAIN for all queries and collect results
def execute_explains(sql_files):
    conn = psycopg2.connect(**DB_CONFIG)
    results = []
    
    for sql_file in sql_files:
        with open(sql_file, 'r') as f:
            query = f.read().strip()
        
        try:
            cursor = conn.cursor()
            explain_query = f"EXPLAIN (VERBOSE true, COSTS true, FORMAT JSON) {query}"
            cursor.execute(explain_query)
            result = cursor.fetchall()
            explain_json = result[0][0]
            cursor.close()
            conn.commit()
            
            results.append({
                'filename': sql_file.name,
                'filepath': str(sql_file),
                'json': explain_json,
                'success': True,
                'error': None
            })
            
        except Exception as e:
            results.append({
                'filename': sql_file.name,
                'filepath': str(sql_file),
                'json': None,
                'success': False,
                'error': str(e)
            })
    
    conn.close()
    return results

# Export all EXPLAIN results to markdown file
def export_to_markdown(explain_data):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f'q9_explain_export_{timestamp}.md'
    
    with open(output_file, 'w') as f:
        f.write("# EXPLAIN JSON Export - Q9 All Seeds\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Total Queries:** {len(explain_data)}\n\n")
        f.write("---\n\n")
        
        for idx, data in enumerate(explain_data, 1):
            f.write(f"## {idx}. {data['filename']}\n\n")
            f.write(f"**File Path:** `{data['filepath']}`\n\n")
            
            if data['success']:
                f.write("### EXPLAIN JSON\n\n")
                f.write("```json\n")
                f.write(json.dumps(data['json'], indent=2))
                f.write("\n```\n\n")
            else:
                f.write(f"**ERROR:** {data['error']}\n\n")
            
            f.write("---\n\n")

if __name__ == "__main__":
    export_q9_explains()
