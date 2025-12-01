#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))
# From mapping_config.py: Pass-through operator detection
from mapping_config import PASSTHROUGH_OPERATORS

# ORCHESTRATOR
def compare_pattern_files(hybrid2_file: str, hybrid3_file: str, output_dir: str) -> None:
    h2_patterns = load_patterns(hybrid2_file)
    h3_patterns = load_patterns(hybrid3_file)
    removed_patterns = find_removed_patterns(h2_patterns, h3_patterns)
    new_patterns = find_new_patterns(h2_patterns, h3_patterns)
    report_content = generate_markdown_report(h2_patterns, h3_patterns, removed_patterns, new_patterns)
    export_markdown_report(report_content, output_dir)

# FUNCTIONS

# Load patterns from CSV file
def load_patterns(file_path: str) -> set:
    df = pd.read_csv(file_path, delimiter=';')
    return set(df['pattern'].tolist())

# Find patterns that exist in H2 but not in H3
def find_removed_patterns(h2_patterns: set, h3_patterns: set) -> set:
    return h2_patterns - h3_patterns

# Find patterns that exist in H3 but not in H2
def find_new_patterns(h2_patterns: set, h3_patterns: set) -> set:
    return h3_patterns - h2_patterns

# Generate markdown comparison report
def generate_markdown_report(h2_patterns: set, h3_patterns: set, removed_patterns: set, new_patterns: set) -> str:
    lines = []
    lines.append("# Pattern Comparison: Hybrid_2 vs Hybrid_3")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Hybrid_2 patterns:** {len(h2_patterns)}")
    lines.append(f"- **Hybrid_3 patterns:** {len(h3_patterns)}")
    lines.append(f"- **Removed patterns:** {len(removed_patterns)}")
    lines.append(f"- **New patterns:** {len(new_patterns)}")
    lines.append("")

    if removed_patterns:
        pt_removed = []
        non_pt_removed = []

        for pattern in sorted(removed_patterns):
            if ' → ' in pattern:
                parent = pattern.split(' → ')[0]
                if parent in PASSTHROUGH_OPERATORS:
                    pt_removed.append((pattern, parent))
                else:
                    non_pt_removed.append(pattern)

        lines.append("## Removed Patterns (Hybrid_2 → Hybrid_3)")
        lines.append("")

        if pt_removed:
            lines.append(f"### Pass-Through Parent Patterns ({len(pt_removed)})")
            lines.append("")
            for i, (pattern, parent) in enumerate(pt_removed, 1):
                lines.append(f"{i}. `{pattern}` [PT: {parent}]")
            lines.append("")

        if non_pt_removed:
            lines.append(f"### Non-PT Patterns ({len(non_pt_removed)})")
            lines.append("")
            for i, pattern in enumerate(non_pt_removed, 1):
                lines.append(f"{i}. `{pattern}`")
            lines.append("")

    if new_patterns:
        lines.append("## New Patterns (Hybrid_3 only)")
        lines.append("")
        for i, pattern in enumerate(sorted(new_patterns), 1):
            lines.append(f"{i}. `{pattern}`")
        lines.append("")

    lines.append("## Verification")
    lines.append("")

    all_pt_removed = all(
        p.split(' → ')[0] in PASSTHROUGH_OPERATORS
        for p in removed_patterns
        if ' → ' in p
    )

    if all_pt_removed:
        lines.append("- ✓ All removed patterns are Pass-Through parent patterns")
    else:
        lines.append("- ✗ Some removed patterns are NOT Pass-Through parents")

    lines.append(f"- ✓ Pass-Through operators: {', '.join(PASSTHROUGH_OPERATORS)}")
    lines.append("")

    return '\n'.join(lines)

# Export markdown report to file
def export_markdown_report(content: str, output_dir: str) -> None:
    md_dir = Path(output_dir) / 'md'
    md_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = md_dir / f'A_01a_pattern_comparison_{timestamp}.md'
    output_file.write_text(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("hybrid2_file", help="Path to Hybrid_2 pattern CSV")
    parser.add_argument("hybrid3_file", help="Path to Hybrid_3 pattern CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for comparison report")
    args = parser.parse_args()

    compare_pattern_files(args.hybrid2_file, args.hybrid3_file, args.output_dir)
