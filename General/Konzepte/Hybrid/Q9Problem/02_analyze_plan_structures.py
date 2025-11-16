#!/usr/bin/env python3

# Infrastructure
import json
import re
import pandas as pd
from pathlib import Path
from datetime import datetime
from collections import Counter

MD_DIR = Path('/Users/brunowinter2000/Documents/Thesis/2025_2026/Hybrid/Konzept/Q9Problem/md')
OUTPUT_DIR = Path('/Users/brunowinter2000/Documents/Thesis/2025_2026/Hybrid/Konzept/Q9Problem/csv')

# Orchestrator
def analyze_plan_structures():
    md_file = get_latest_md_file()
    plan_data = extract_plans_from_md(md_file)
    plan_structures = extract_all_plan_structures(plan_data)
    analysis_results = analyze_unique_plans(plan_structures)
    export_results(analysis_results)

# Get the most recent markdown file
def get_latest_md_file():
    md_files = sorted(MD_DIR.glob('q9_explain_export_*.md'), reverse=True)
    return md_files[0]

# Extract all JSON plans from markdown file
def extract_plans_from_md(md_file):
    with open(md_file, 'r') as f:
        content = f.read()
    
    pattern = r'## \d+\. (Q9_\d+_seed_\d+\.sql).*?```json\n(.*?)\n```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    plans = []
    for filename, json_str in matches:
        try:
            json_data = json.loads(json_str)
            plans.append({
                'filename': filename,
                'json': json_data
            })
        except json.JSONDecodeError:
            pass
    
    return plans

# Extract plan structures for all queries
def extract_all_plan_structures(plan_data):
    structures = []
    
    for item in plan_data:
        plan_tree = item['json'][0]['Plan']
        structure_str = serialize_plan_structure(plan_tree)
        structures.append({
            'filename': item['filename'],
            'structure': structure_str
        })
    
    return structures

# Serialize plan tree structure to comparable string
def serialize_plan_structure(node, depth=0):
    node_type = node.get('Node Type', 'Unknown')
    rel = node.get('Parent Relationship', '')
    
    structure_parts = [f"{'  ' * depth}{node_type}"]
    
    if rel:
        structure_parts[0] += f" ({rel})"
    
    plans = node.get('Plans', [])
    for child in plans:
        structure_parts.append(serialize_plan_structure(child, depth + 1))
    
    return '\n'.join(structure_parts)

# Analyze unique plan structures and count occurrences
def analyze_unique_plans(plan_structures):
    structures_list = [item['structure'] for item in plan_structures]
    structure_counts = Counter(structures_list)
    
    unique_plans = []
    for structure, count in structure_counts.items():
        files = [item['filename'] for item in plan_structures if item['structure'] == structure]
        unique_plans.append({
            'plan_id': len(unique_plans) + 1,
            'occurrence_count': count,
            'percentage': (count / len(plan_structures)) * 100,
            'example_files': ', '.join(files[:3]),
            'structure': structure
        })
    
    return {
        'total_queries': len(plan_structures),
        'unique_plans': len(structure_counts),
        'plans': unique_plans
    }

# Export analysis results to CSV
def export_results(results):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    summary_data = {
        'total_queries': [results['total_queries']],
        'unique_plans': [results['unique_plans']]
    }
    summary_df = pd.DataFrame(summary_data)
    summary_file = OUTPUT_DIR / f'q9_plan_summary_{timestamp}.csv'
    summary_df.to_csv(summary_file, sep=';', index=False)
    
    details_df = pd.DataFrame(results['plans'])
    details_df = details_df.sort_values('occurrence_count', ascending=False)
    details_file = OUTPUT_DIR / f'q9_plan_details_{timestamp}.csv'
    details_df.to_csv(details_file, sep=';', index=False)

if __name__ == "__main__":
    analyze_plan_structures()
