#!/usr/bin/env python3
import sys
import psycopg2
import subprocess
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

CONTAINER_NAME = 'tpch-postgres'
RUNS = 5

def wait_for_orbstack_stopped(max_attempts=30):
    for attempt in range(max_attempts):
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if 'OrbStack.app' not in result.stdout:
            return True
        time.sleep(0.5)
    return False

def wait_for_orbstack_running(max_attempts=60):
    for attempt in range(max_attempts):
        try:
            result = subprocess.run(['orbctl', 'status'], capture_output=True, text=True, timeout=2)
            if 'Running' in result.stdout:
                return True
        except:
            pass
        time.sleep(1)
    return False

def wait_for_docker_ready(max_attempts=60):
    for attempt in range(max_attempts):
        try:
            result = subprocess.run(['docker', 'ps'], capture_output=True, timeout=3)
            if result.returncode == 0:
                return True
        except:
            pass
        time.sleep(1)
    return False

def wait_for_postgres(max_attempts=30):
    for attempt in range(max_attempts):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            conn.close()
            return True
        except psycopg2.OperationalError:
            time.sleep(1)
    return False

def restart_orbstack_and_purge():
    subprocess.run(['osascript', '-e', 'quit app "OrbStack"'], capture_output=True)
    
    if not wait_for_orbstack_stopped():
        return False
    
    subprocess.run(['sudo', 'purge'], capture_output=True)
    subprocess.run(['open', '-a', 'OrbStack', '-g'], capture_output=True)
    
    if not wait_for_orbstack_running():
        return False
    
    return True

def start_container():
    subprocess.run(['docker', 'start', CONTAINER_NAME], capture_output=True)

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

def get_query_file(query_dir, template_num):
    template_dir = query_dir / f'Q{template_num}'
    query_file = template_dir / f'Q{template_num}_1_seed_0101000000.sql'
    return query_file if query_file.exists() else None

def get_unique_csv_path(base_path):
    if not base_path.exists():
        return base_path
    
    base_name = base_path.stem
    extension = base_path.suffix
    parent = base_path.parent
    
    counter = 1
    while True:
        new_path = parent / f"{base_name}_{counter}{extension}"
        if not new_path.exists():
            return new_path
        counter += 1

def main():
    query_dir = Path(sys.argv[1])
    
    subprocess.run(['sudo', '-v'], capture_output=True)
    
    results = []
    
    for template_num in range(1, 23):
        if template_num == 15:
            continue
        
        query_file = get_query_file(query_dir, template_num)
        
        if not query_file:
            continue
        
        with open(query_file, 'r') as f:
            query = f.read().strip()
        
        times = []
        for run in range(1, RUNS + 1):
            if not restart_orbstack_and_purge():
                print(f"Q{template_num} Run {run}: RESTART_FAILED")
                continue
            
            if not wait_for_docker_ready():
                print(f"Q{template_num} Run {run}: DOCKER_FAILED")
                continue
            
            start_container()
            
            if not wait_for_postgres():
                print(f"Q{template_num} Run {run}: POSTGRES_FAILED")
                continue
            
            conn = psycopg2.connect(**DB_CONFIG)
            exec_time = execute_query(conn, query)
            conn.close()
            
            times.append(exec_time)
        
        if len(times) >= 2:
            mean = sum(times) / len(times)
            variance = sum((t - mean) ** 2 for t in times) / (len(times) - 1)
            std_dev = variance ** 0.5
            cv = (std_dev / mean) * 100
            
            row = {
                'query_file': query_file.name,
                'template': query_file.parent.name,
                'mean_ms': mean,
                'std_dev_ms': std_dev,
                'cv_percent': cv
            }
            for i, t in enumerate(times, 1):
                row[f'run_{i}_ms'] = t
            results.append(row)
            print(f"Q{template_num} Complete: {len(times)} runs, mean={mean:.2f}ms, cv={cv:.2f}%")
        else:
            print(f"Q{template_num} FAILED: Not enough successful runs ({len(times)}/5)")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    script_dir = Path(__file__).parent
    csv_dir = script_dir / 'csv'
    csv_dir.mkdir(exist_ok=True)
    
    base_csv_file = csv_dir / f'runtime_{timestamp}.csv'
    csv_file = get_unique_csv_path(base_csv_file)
    
    fieldnames = ['query_file', 'template', 'mean_ms', 'std_dev_ms', 'cv_percent'] + [f'run_{i}_ms' for i in range(1, RUNS + 1)]
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    print(f"Results saved to: {csv_file}")

if __name__ == "__main__":
    main()
