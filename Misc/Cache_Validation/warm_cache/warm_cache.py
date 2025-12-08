#!/usr/bin/env python3
import sys
import psycopg2
import time
import csv
from pathlib import Path
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'tpch',
    'user': 'postgres',
    'password': 'postgres'
}

RUNS = 5

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

def get_query_file(queries_dir, template_num):
    template_dir = queries_dir / f'Q{template_num}'
    query_file = template_dir / f'Q{template_num}_1_seed_0101000000.sql'
    return query_file if query_file.exists() else None

def main():
    queries_dir = Path(sys.argv[1])
    
    conn = psycopg2.connect(**DB_CONFIG)
    
    templates = range(1, 23)
    results = []
    
    for template_num in templates:
        query_file = get_query_file(queries_dir, template_num)
        
        if not query_file:
            continue
        
        with open(query_file, 'r') as f:
            query = f.read().strip()
        
        times = []
        for run in range(1, RUNS + 1):
            exec_time = execute_query(conn, query)
            times.append(exec_time)
            print(f"Q{template_num} Run {run}/5: {exec_time:.2f}ms")
        
        if len(times) >= 2:
            mean = sum(times) / len(times)
            variance = sum((t - mean) ** 2 for t in times) / (len(times) - 1)
            std_dev = variance ** 0.5
            cv = (std_dev / mean) * 100
            
            row = {
                'query': f'Q{template_num}',
                'mean_ms': mean,
                'std_dev_ms': std_dev,
                'cv_percent': cv
            }
            for i, t in enumerate(times, 1):
                row[f'run_{i}_ms'] = t
            results.append(row)
            print(f"Q{template_num} Complete: mean={mean:.2f}ms, cv={cv:.2f}%\n")
    
    conn.close()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    script_dir = Path(__file__).parent
    csv_dir = script_dir / 'csv'
    csv_dir.mkdir(exist_ok=True)
    csv_file = csv_dir / f'warm_cache_{timestamp}.csv'
    
    if results:
        fieldnames = ['query', 'mean_ms', 'std_dev_ms', 'cv_percent'] + [f'run_{i}_ms' for i in range(1, RUNS + 1)]
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"\nResults saved to: {csv_file}")
    else:
        print("\nNo results to save")

if __name__ == "__main__":
    main()
