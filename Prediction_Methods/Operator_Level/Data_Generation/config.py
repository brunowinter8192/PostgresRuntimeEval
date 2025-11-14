#!/usr/bin/env python3

# INFRASTRUCTURE
import psycopg2
import subprocess
import time
from pathlib import Path

DEFAULT_DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'tpch',
    'user': 'postgres',
    'password': 'postgres'
}

DEFAULT_CONTAINER_NAME = 'tpch-postgres'

# FUNCTIONS

def get_db_config(host=None, port=None, database=None, user=None, password=None):
    config = DEFAULT_DB_CONFIG.copy()
    if host: config['host'] = host
    if port: config['port'] = port
    if database: config['database'] = database
    if user: config['user'] = user
    if password: config['password'] = password
    return config

def wait_for_orbstack_stopped(max_attempts=30):
    for attempt in range(max_attempts):
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if 'OrbStack.app' not in result.stdout:
            return True
        time.sleep(0.5)
    return False

def wait_for_orbstack_running(max_attempts=60):
    for attempt in range(max_attempts):
        result = subprocess.run(['orbctl', 'status'], capture_output=True, text=True, timeout=2)
        if 'Running' in result.stdout:
            return True
        time.sleep(1)
    return False

def wait_for_docker_ready(max_attempts=60):
    for attempt in range(max_attempts):
        result = subprocess.run(['docker', 'ps'], capture_output=True, timeout=3)
        if result.returncode == 0:
            return True
        time.sleep(1)
    return False

def wait_for_postgres(db_config, max_attempts=30):
    for attempt in range(max_attempts):
        conn = psycopg2.connect(**db_config)
        conn.close()
        return True
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

def start_container(container_name):
    subprocess.run(['docker', 'start', container_name], capture_output=True)

def get_query_files_all_templates(query_dir):
    all_files = []
    for template_num in range(1, 23):
        if template_num == 15:
            continue
        template_dir = query_dir / f'Q{template_num}'
        if template_dir.exists():
            sql_files = sorted(template_dir.glob('Q*.sql'))
            all_files.extend(sql_files)
    return all_files

def get_first_seed_per_template(query_dir):
    first_seeds = []
    for template_num in range(1, 23):
        if template_num == 15:
            continue
        template_dir = query_dir / f'Q{template_num}'
        if template_dir.exists() and template_dir.is_dir():
            sql_files = sorted(template_dir.glob('*.sql'))
            if sql_files:
                first_seeds.append(sql_files[0])
    return first_seeds
