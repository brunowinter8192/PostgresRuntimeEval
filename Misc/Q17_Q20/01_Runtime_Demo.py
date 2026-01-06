# INFRASTRUCTURE
import argparse
import time
from pathlib import Path

import psycopg2

DEFAULT_DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'tpch',
    'user': 'postgres',
    'password': 'postgres'
}


# ORCHESTRATOR
def main(queries_dir: Path, output_dir: Path, runs: int) -> None:
    conn = connect_db()

    q17_files = sorted((queries_dir / 'Q17').glob('*.sql'))[:runs]
    q20_files = sorted((queries_dir / 'Q20').glob('*.sql'))[:runs]

    q17_runtimes = execute_queries(conn, q17_files, 'Q17')
    q20_runtimes = execute_queries(conn, q20_files, 'Q20')

    conn.close()

    export_results(q17_runtimes, q20_runtimes, output_dir)


# FUNCTIONS
# Establish database connection
def connect_db() -> psycopg2.extensions.connection:
    return psycopg2.connect(**DEFAULT_DB_CONFIG)


# Execute queries and measure runtimes
def execute_queries(conn, sql_files: list, query_type: str) -> list:
    runtimes = []
    for sql_file in sql_files:
        query = sql_file.read_text()
        runtime_ms = execute_single_query(conn, query)
        runtimes.append({
            'file': sql_file.name,
            'runtime_ms': runtime_ms,
            'runtime_s': runtime_ms / 1000
        })
    return runtimes


# Execute single query with timing
def execute_single_query(conn, query: str) -> float:
    conn.rollback()
    cursor = conn.cursor()

    start_time = time.perf_counter()
    cursor.execute(query)
    cursor.fetchall()
    end_time = time.perf_counter()

    cursor.close()
    conn.commit()

    return (end_time - start_time) * 1000


# Export results to markdown
def export_results(q17_runtimes: list, q20_runtimes: list, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    lines = ['# Q17 & Q20 Runtime Demonstration', '']
    lines.append('Demonstrates that Q17 and Q20 have exceptionally long runtimes.')
    lines.append('')

    lines.append('## Q17 Runtimes')
    lines.append('')
    for r in q17_runtimes:
        lines.append(f"- **{r['file']}:** {r['runtime_s']:.2f}s ({r['runtime_ms']:.0f}ms)")
    lines.append('')
    avg_q17 = sum(r['runtime_s'] for r in q17_runtimes) / len(q17_runtimes)
    lines.append(f"**Average Q17:** {avg_q17:.2f}s")
    lines.append('')

    lines.append('## Q20 Runtimes')
    lines.append('')
    for r in q20_runtimes:
        lines.append(f"- **{r['file']}:** {r['runtime_s']:.2f}s ({r['runtime_ms']:.0f}ms)")
    lines.append('')
    avg_q20 = sum(r['runtime_s'] for r in q20_runtimes) / len(q20_runtimes)
    lines.append(f"**Average Q20:** {avg_q20:.2f}s")
    lines.append('')

    output_file = output_dir / '01_runtime_demo.md'
    output_file.write_text('\n'.join(lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("queries_dir", help="Directory containing Q17/ and Q20/ folders")
    parser.add_argument("--output-dir", required=True, help="Output directory for MD export")
    parser.add_argument("--runs", type=int, default=5, help="Number of query executions per type (default: 5)")

    args = parser.parse_args()

    main(Path(args.queries_dir), Path(args.output_dir), args.runs)
