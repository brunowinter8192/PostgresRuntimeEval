#!/usr/bin/env python3

# INFRASTRUCTURE
import argparse
from pathlib import Path
import pandas as pd

TEMPLATES = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q12', 'Q13', 'Q14', 'Q18', 'Q19']


# ORCHESTRATOR
def compare_methods(hybrid_dir: Path, online_dir: Path, output_dir: Path, approach: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for template in TEMPLATES:
        hybrid_data = load_hybrid_predictions(hybrid_dir, template, approach)
        online_data = load_online_predictions(online_dir, template)

        if hybrid_data is not None and online_data is not None:
            comparison = compare_template(template, hybrid_data, online_data)
            results.append(comparison)

    write_report(results, output_dir / 'method_comparison.md')


# FUNCTIONS

# Load Hybrid_1 predictions for a template
def load_hybrid_predictions(hybrid_dir: Path, template: str, approach: str) -> pd.DataFrame:
    path = hybrid_dir / template / approach / 'predictions.csv'
    if not path.exists():
        return None
    return pd.read_csv(path, delimiter=';')


# Load Online_1 predictions for a template (aggregate all queries)
def load_online_predictions(online_dir: Path, template: str) -> pd.DataFrame:
    template_dir = online_dir / 'Evaluation' / 'Size' / template
    if not template_dir.exists():
        return None

    dfs = []
    for query_dir in template_dir.iterdir():
        if query_dir.is_dir():
            pred_file = query_dir / 'csv' / 'predictions.csv'
            if pred_file.exists():
                dfs.append(pd.read_csv(pred_file, delimiter=';'))

    if not dfs:
        return None
    return pd.concat(dfs, ignore_index=True)


# Compare a single template
def compare_template(template: str, hybrid_df: pd.DataFrame, online_df: pd.DataFrame) -> dict:
    hybrid_mre = calculate_query_mres(hybrid_df)
    online_mre = calculate_query_mres(online_df)

    hybrid_patterns = get_pattern_usage(hybrid_df, has_hash=True)
    online_patterns = get_pattern_usage(online_df, has_hash=False)

    return {
        'template': template,
        'hybrid_mean_mre': hybrid_mre['mean'],
        'online_mean_mre': online_mre['mean'],
        'diff': online_mre['mean'] - hybrid_mre['mean'],
        'better': 'Hybrid' if hybrid_mre['mean'] < online_mre['mean'] else ('Online' if online_mre['mean'] < hybrid_mre['mean'] else 'Equal'),
        'hybrid_patterns': hybrid_patterns,
        'online_patterns': online_patterns,
        'query_count': hybrid_mre['count']
    }


# Calculate MRE per query and return mean
def calculate_query_mres(df: pd.DataFrame) -> dict:
    query_mres = []
    for query_file in df['query_file'].unique():
        query_df = df[df['query_file'] == query_file]
        root = query_df[query_df['depth'] == 0].iloc[0]

        if root['actual_total_time'] > 0:
            mre = abs(root['predicted_total_time'] - root['actual_total_time']) / root['actual_total_time']
            query_mres.append(mre)

    return {
        'mean': sum(query_mres) / len(query_mres) if query_mres else 0,
        'count': len(query_mres)
    }


# Get pattern usage statistics
def get_pattern_usage(df: pd.DataFrame, has_hash: bool) -> dict:
    if has_hash:
        pattern_rows = df[df['prediction_type'] == 'pattern']
        if pattern_rows.empty:
            return {'pattern_count': 0, 'patterns': {}}

        pattern_counts = pattern_rows['pattern_hash'].value_counts().to_dict()
        return {
            'pattern_count': len(pattern_counts),
            'patterns': pattern_counts
        }
    else:
        pattern_rows = df[df['prediction_type'] == 'pattern']
        operator_rows = df[df['prediction_type'] == 'operator']
        return {
            'pattern_predictions': len(pattern_rows),
            'operator_predictions': len(operator_rows),
            'pattern_ratio': len(pattern_rows) / len(df) if len(df) > 0 else 0
        }


# Write markdown report
def write_report(results: list, output_path: Path) -> None:
    lines = []
    lines.append('# Method Comparison: Hybrid_1 vs Online_1')
    lines.append('')
    lines.append('## Summary')
    lines.append('')
    lines.append('| Template | Hybrid_1 MRE | Online_1 MRE | Diff | Better |')
    lines.append('|----------|--------------|--------------|------|--------|')

    for r in results:
        diff_str = f'+{r["diff"]*100:.2f}%' if r['diff'] > 0 else f'{r["diff"]*100:.2f}%'
        lines.append(f'| {r["template"]} | {r["hybrid_mean_mre"]*100:.2f}% | {r["online_mean_mre"]*100:.2f}% | {diff_str} | {r["better"]} |')

    hybrid_wins = sum(1 for r in results if r['better'] == 'Hybrid')
    online_wins = sum(1 for r in results if r['better'] == 'Online')
    lines.append('')
    lines.append(f'**Hybrid wins:** {hybrid_wins} | **Online wins:** {online_wins}')
    lines.append('')

    lines.append('## Pattern Usage per Template')
    lines.append('')

    for r in results:
        lines.append(f'### {r["template"]}')
        lines.append('')
        lines.append(f'**Hybrid_1:** {r["hybrid_patterns"]["pattern_count"]} unique patterns')

        if r['hybrid_patterns']['patterns']:
            lines.append('')
            for ph, count in sorted(r['hybrid_patterns']['patterns'].items(), key=lambda x: -x[1])[:5]:
                lines.append(f'- `{ph[:8]}`: {count} nodes')

        lines.append('')
        lines.append(f'**Online_1:** {r["online_patterns"]["pattern_predictions"]} pattern predictions, {r["online_patterns"]["operator_predictions"]} operator predictions ({r["online_patterns"]["pattern_ratio"]*100:.1f}% patterns)')
        lines.append('')

    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--approach', default='approach_3', help='Hybrid approach to compare')
    parser.add_argument('--output-dir', default='Evaluation', help='Output directory')
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    hybrid_dir = script_dir
    online_dir = script_dir.parent / 'Online_1'
    output_dir = script_dir / args.output_dir

    compare_methods(hybrid_dir, online_dir, output_dir, args.approach)
