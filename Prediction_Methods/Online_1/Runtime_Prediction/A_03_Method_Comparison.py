#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
import pandas as pd
from pathlib import Path
from collections import defaultdict

# ORCHESTRATOR
def compare_methods(h1_dir: str, h2_dir: str, o1_dir: str, output_dir: str) -> None:
    h1 = load_approach_data(Path(h1_dir), "hybrid1")
    h2 = load_approach_data(Path(h2_dir), "hybrid2")
    o1 = load_approach_data(Path(o1_dir), "online1")
    comparison = merge_comparison(h1, h2, o1)
    overall = {"h1": h1["overall"], "h2": h2["overall"], "o1": o1["overall"]}
    paths = {"h1": h1_dir, "h2": h2_dir, "o1": o1_dir}
    export_csv(comparison, overall, output_dir)
    export_report(comparison, overall, paths, output_dir)


# FUNCTIONS

# Load template MRE, overall MRE, and pattern data for an approach
def load_approach_data(dir_path: Path, approach_type: str) -> dict:
    template_mre = load_template_mre(dir_path)
    overall_mre = load_overall_mre(dir_path)
    pattern_mapping = load_pattern_template_mapping(dir_path, approach_type)
    return {"mre": template_mre, "overall": overall_mre, "patterns": pattern_mapping}


# Load template_mre.csv
def load_template_mre(dir_path: Path) -> pd.DataFrame:
    mre_file = dir_path / "template_mre.csv"
    df = pd.read_csv(mre_file, delimiter=';')
    return df[['template', 'mean_mre_pct']].set_index('template')


# Load overall_mre.csv
def load_overall_mre(dir_path: Path) -> float:
    mre_file = dir_path / "overall_mre.csv"
    df = pd.read_csv(mre_file, delimiter=';')
    return df[df['metric'] == 'mean_mre']['percentage'].values[0]


# Load pattern→template mapping based on approach type
def load_pattern_template_mapping(dir_path: Path, approach_type: str) -> dict:
    if approach_type == "online1":
        return load_online1_patterns(dir_path)
    else:
        return load_hybrid_patterns(dir_path)


# Online_1: patterns_comparison.csv has templates column
def load_online1_patterns(dir_path: Path) -> dict:
    patterns_file = dir_path / "patterns_comparison.csv"
    if not patterns_file.exists():
        patterns_file = dir_path / "patterns_selected.csv"

    df = pd.read_csv(patterns_file, delimiter=';')
    mapping = defaultdict(set)

    for _, row in df.iterrows():
        templates = row['templates'].split(',') if pd.notna(row['templates']) else []
        for template in templates:
            mapping[template.strip()].add(row['pattern_hash'][:8])

    return dict(mapping)


# Hybrid_1/2: derive from predictions.csv (query_file column)
def load_hybrid_patterns(dir_path: Path) -> dict:
    predictions_file = dir_path / "predictions.csv"
    if not predictions_file.exists():
        sibling_predictions = dir_path.parent.parent / "Predictions" / dir_path.name / "predictions.csv"
        if sibling_predictions.exists():
            predictions_file = sibling_predictions
    df = pd.read_csv(predictions_file, delimiter=';')

    pattern_df = df[df['prediction_type'] == 'pattern'].copy()
    pattern_df['template'] = pattern_df['query_file'].apply(lambda x: x.split('_')[0])

    mapping = defaultdict(set)
    for _, row in pattern_df.iterrows():
        if pd.notna(row['pattern_hash']) and row['pattern_hash']:
            mapping[row['template']].add(row['pattern_hash'][:8])

    return dict(mapping)


# Merge data from all approaches into comparison DataFrame
def merge_comparison(h1: dict, h2: dict, o1: dict) -> pd.DataFrame:
    all_templates = sorted(
        set(h1['mre'].index) | set(h2['mre'].index) | set(o1['mre'].index),
        key=lambda x: int(x[1:])
    )

    rows = []
    for template in all_templates:
        h1_mre = h1['mre'].loc[template, 'mean_mre_pct'] if template in h1['mre'].index else None
        h2_mre = h2['mre'].loc[template, 'mean_mre_pct'] if template in h2['mre'].index else None
        o1_mre = o1['mre'].loc[template, 'mean_mre_pct'] if template in o1['mre'].index else None

        h1_patterns = ','.join(sorted(h1['patterns'].get(template, set())))
        h2_patterns = ','.join(sorted(h2['patterns'].get(template, set())))
        o1_patterns = ','.join(sorted(o1['patterns'].get(template, set())))

        h1_h2_delta = round(h2_mre - h1_mre, 2) if h1_mre and h2_mre else None
        h2_o1_delta = round(o1_mre - h2_mre, 2) if h2_mre and o1_mre else None

        rows.append({
            'template': template,
            'h1_mre': round(h1_mre, 2) if h1_mre else None,
            'h2_mre': round(h2_mre, 2) if h2_mre else None,
            'o1_mre': round(o1_mre, 2) if o1_mre else None,
            'h1_h2_delta': h1_h2_delta,
            'h2_o1_delta': h2_o1_delta,
            'h1_patterns': h1_patterns or '-',
            'h2_patterns': h2_patterns or '-',
            'o1_patterns': o1_patterns or '-'
        })

    return pd.DataFrame(rows)


# Export comparison to CSV
def export_csv(comparison: pd.DataFrame, overall: dict, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    comparison.to_csv(output_path / 'method_comparison.csv', sep=';', index=False)

    overall_df = pd.DataFrame([{
        'metric': 'overall_mre',
        'h1': round(overall['h1'], 2),
        'h2': round(overall['h2'], 2),
        'o1': round(overall['o1'], 2),
        'h1_h2_delta': round(overall['h2'] - overall['h1'], 2),
        'h2_o1_delta': round(overall['o1'] - overall['h2'], 2)
    }])
    overall_df.to_csv(output_path / 'overall_comparison.csv', sep=';', index=False)


# Export markdown report
def export_report(comparison: pd.DataFrame, overall: dict, paths: dict, output_dir: str) -> None:
    output_path = Path(output_dir)

    h1_h2_better = sum(1 for d in comparison['h1_h2_delta'] if d and d < 0)
    h1_h2_worse = sum(1 for d in comparison['h1_h2_delta'] if d and d > 0)
    h2_o1_better = sum(1 for d in comparison['h2_o1_delta'] if d and d < 0)
    h2_o1_worse = sum(1 for d in comparison['h2_o1_delta'] if d and d > 0)

    h1_h2_overall_symbol = get_delta_symbol(overall['h2'] - overall['h1'])
    h2_o1_overall_symbol = get_delta_symbol(overall['o1'] - overall['h2'])

    lines = [
        "# Method Comparison Report",
        "",
        "**Ordering (Dumb -> Intelligent):** Hybrid_1 -> Hybrid_2 -> Online_1",
        "",
        "## Input Paths",
        "",
        f"- **Hybrid_1:** `{paths['h1']}`",
        f"- **Hybrid_2:** `{paths['h2']}`",
        f"- **Online_1:** `{paths['o1']}`",
        "",
        "## Summary",
        "",
        f"**Overall MRE:** H1={overall['h1']:.2f}% {h1_h2_overall_symbol} H2={overall['h2']:.2f}% {h2_o1_overall_symbol} O1={overall['o1']:.2f}%",
        "",
        f"- **H1 -> H2:** {h1_h2_better} templates improved, {h1_h2_worse} templates worsened (overall: {overall['h2'] - overall['h1']:+.2f}%)",
        f"- **H2 -> O1:** {h2_o1_better} templates improved, {h2_o1_worse} templates worsened (overall: {overall['o1'] - overall['h2']:+.2f}%)",
        "",
        "## Template MRE Comparison",
        "",
    ]

    for _, row in comparison.iterrows():
        h1_h2_symbol = get_delta_symbol(row['h1_h2_delta'])
        h2_o1_symbol = get_delta_symbol(row['h2_o1_delta'])

        lines.append(f"### {row['template']}")
        lines.append("")
        lines.append(f"- **MRE:** H1={row['h1_mre']}% {h1_h2_symbol} H2={row['h2_mre']}% {h2_o1_symbol} O1={row['o1_mre']}%")
        lines.append(f"- **H1 Patterns:** {row['h1_patterns']}")
        lines.append(f"- **H2 Patterns:** {row['h2_patterns']}")
        lines.append(f"- **O1 Patterns:** {row['o1_patterns']}")
        lines.append("")

    with open(output_path / 'method_comparison.md', 'w') as f:
        f.write('\n'.join(lines))


# Get symbol for delta direction
def get_delta_symbol(delta) -> str:
    if delta is None:
        return "->"
    if delta < -0.5:
        return "✓->"
    if delta > 0.5:
        return "✗->"
    return "≈->"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("h1_dir", help="Hybrid_1 evaluation directory")
    parser.add_argument("h2_dir", help="Hybrid_2 evaluation directory")
    parser.add_argument("o1_dir", help="Online_1 analysis directory")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()
    compare_methods(args.h1_dir, args.h2_dir, args.o1_dir, args.output_dir)
