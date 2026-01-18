#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import pandas as pd
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATASET_DIR = SCRIPT_DIR.parent.parent / 'Dataset' / 'Dataset_Hybrid_1'

ALL_TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR

def generate_pattern_statistics(approach: str, output_dir: str) -> None:
    rows = collect_statistics(approach)
    rows_with_total = add_total_row(rows)
    export_csv(rows_with_total, output_dir)


# FUNCTIONS

# Collect pattern statistics per template
def collect_statistics(approach: str) -> list:
    rows = []

    for template in ALL_TEMPLATES:
        template_dir = DATASET_DIR / template / approach
        available = count_csv_rows(template_dir / 'patterns_filtered.csv')
        used = count_csv_rows(template_dir / 'used_patterns.csv')

        reduction_pct = (1 - used / available) * 100 if available > 0 else 0

        rows.append({
            'template': template,
            'available_patterns': available,
            'used_patterns': used,
            'reduction_pct': round(reduction_pct, 1)
        })

    return rows


# Count data rows in CSV (excluding header)
def count_csv_rows(csv_path: Path) -> int:
    if not csv_path.exists():
        return 0
    df = pd.read_csv(csv_path, delimiter=';')
    return len(df)


# Add total and mean rows
def add_total_row(rows: list) -> list:
    n = len(rows)
    total_available = sum(r['available_patterns'] for r in rows)
    total_used = sum(r['used_patterns'] for r in rows)
    total_reduction = (1 - total_used / total_available) * 100 if total_available > 0 else 0

    mean_available = total_available / n
    mean_used = total_used / n
    mean_reduction = sum(r['reduction_pct'] for r in rows) / n

    rows.append({
        'template': 'Total',
        'available_patterns': total_available,
        'used_patterns': total_used,
        'reduction_pct': round(total_reduction, 1)
    })

    rows.append({
        'template': 'Mean',
        'available_patterns': round(mean_available, 1),
        'used_patterns': round(mean_used, 1),
        'reduction_pct': round(mean_reduction, 1)
    })

    return rows


# Export statistics to CSV
def export_csv(rows: list, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    lines = ['template;available_patterns;used_patterns;reduction_pct']
    for r in rows:
        avail = int(r['available_patterns']) if r['available_patterns'] == int(r['available_patterns']) else r['available_patterns']
        used = int(r['used_patterns']) if r['used_patterns'] == int(r['used_patterns']) else r['used_patterns']
        lines.append(f"{r['template']};{avail};{used};{r['reduction_pct']}")

    with open(output_path / 'A_01d_pattern_statistics.csv', 'w') as f:
        f.write('\n'.join(lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--approach", default="approach_3", help="Approach to analyze")
    parser.add_argument("--output-dir", required=True, help="Output directory for CSV")
    args = parser.parse_args()

    generate_pattern_statistics(args.approach, args.output_dir)
