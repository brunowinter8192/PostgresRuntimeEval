# INFRASTRUCTURE

import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

# From mapping_config.py: Passthrough operators
from mapping_config import PASSTHROUGH_OPERATORS


# FUNCTIONS

# Export MD report for single query prediction
def export_md_report(
    query_file: str,
    df_query,
    predictions: list,
    steps: list,
    consumed_nodes: set,
    pattern_assignments: dict,
    pattern_info: dict,
    output_dir: str,
    plan_hash: str = '',
    passthrough: bool = False
) -> None:
    md_dir = Path(output_dir) / 'md'
    md_dir.mkdir(parents=True, exist_ok=True)

    template = query_file.split('_')[0]
    hash_suffix = f'_{plan_hash[:8]}' if plan_hash else ''
    md_file = md_dir / f'03_{template}{hash_suffix}.md'

    lines = build_report_lines(query_file, df_query, predictions, steps, consumed_nodes, pattern_assignments, pattern_info, passthrough)

    with open(md_file, 'w') as f:
        f.write('\n'.join(lines))


# Build all report lines
def build_report_lines(query_file: str, df_query, predictions: list, steps: list, consumed_nodes: set, pattern_assignments: dict, pattern_info: dict, passthrough: bool = False) -> list:
    lines = []

    lines.extend(build_header_section(query_file))
    lines.extend(build_pattern_summary_section(pattern_assignments, pattern_info))
    lines.extend(build_tree_section(df_query, consumed_nodes, pattern_assignments, passthrough))
    lines.extend(build_chain_section(steps))
    lines.extend(build_results_section(predictions))

    return lines


# Build header section
def build_header_section(query_file: str) -> list:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return [
        '# Query Prediction Report (Hybrid_1)',
        '',
        f'**Query:** {query_file}',
        f'**Timestamp:** {timestamp}',
        ''
    ]


# Build pattern summary section
def build_pattern_summary_section(pattern_assignments: dict, pattern_info: dict) -> list:
    lines = ['## Pattern Assignments', '']

    if not pattern_assignments:
        lines.append('No patterns matched.')
        lines.append('')
        return lines

    lines.append(f'**Total Patterns Matched:** {len(pattern_assignments)}')
    lines.append('')
    lines.append('| Root Node | Pattern Hash | Pattern String |')
    lines.append('|-----------|--------------|----------------|')

    for node_id, pattern_hash in sorted(pattern_assignments.items()):
        info = pattern_info.get(pattern_hash, {})
        pattern_string = info.get('pattern_string', 'N/A')
        lines.append(f'| {node_id} | {pattern_hash[:12]}... | {pattern_string} |')

    lines.append('')
    return lines


# Build query tree section with pattern markers
def build_tree_section(df_query, consumed_nodes: set, pattern_assignments: dict, passthrough: bool = False) -> list:
    lines = ['## Query Tree', '', '```']

    min_depth = df_query['depth'].min()

    for _, row in df_query.iterrows():
        depth = row['depth']
        indent = '  ' * (depth - min_depth)
        node_type = row['node_type']
        node_id = row['node_id']

        marker = ''
        if node_id in pattern_assignments:
            marker = ' [PATTERN ROOT]'
        elif node_id in consumed_nodes:
            marker = ' [consumed]'
        elif passthrough and node_type in PASSTHROUGH_OPERATORS:
            marker = ' [PASSTHROUGH]'

        suffix = ' - ROOT' if depth == min_depth else ''
        lines.append(f'{indent}Node {node_id} ({node_type}){marker}{suffix}')

    lines.append('```')
    lines.append('')
    return lines


# Build prediction chain section
def build_chain_section(steps: list) -> list:
    lines = ['## Prediction Chain (Bottom-Up)', '']

    for step in steps:
        if step['prediction_type'] == 'pattern':
            lines.append(f"### Step {step['step']} (depth {step['depth']}): Pattern Match")
            lines.append('')
            lines.append(f"- **Pattern:** {step['pattern_string']}")
            lines.append(f"- **Hash:** {step['pattern_hash']}")
            lines.append(f"- **Root:** Node {step['parent_node_id']} ({step['parent_node_type']})")
            consumed_str = ', '.join([f"Node {nid} ({ntype})" for nid, ntype in step['consumed_children']])
            if consumed_str:
                lines.append(f"- **Consumed Children:** {consumed_str}")
        elif step['prediction_type'] == 'passthrough':
            lines.append(f"### Step {step['step']} (depth {step['depth']}): Passthrough")
            lines.append('')
            lines.append(f"- **Node:** {step['node_id']} ({step['node_type']})")
            lines.append(f"- **Reason:** {step['reason']}")
        else:
            lines.append(f"### Step {step['step']} (depth {step['depth']}): Operator Fallback")
            lines.append('')
            lines.append(f"- **Node:** {step['node_id']} ({step['node_type']})")
            lines.append(f"- **Reason:** {step['reason']}")

        lines.append(f"- **Output:** st={step['predicted_startup_time']:.2f}, rt={step['predicted_total_time']:.2f}")
        lines.append('')

    return lines


# Build prediction results section
def build_results_section(predictions: list) -> list:
    lines = [
        '## Prediction Results',
        '',
        '| Node | Type | Depth | Pred Type | Actual RT | Pred RT | MRE (%) |',
        '|------|------|-------|-----------|-----------|---------|---------|'
    ]

    for pred in sorted(predictions, key=lambda x: x['depth']):
        actual_rt = pred['actual_total_time']
        pred_rt = pred['predicted_total_time']
        mre_rt = abs(actual_rt - pred_rt) / actual_rt * 100 if actual_rt > 0 else 0

        lines.append(
            f"| {pred['node_id']} | {pred['node_type']} | {pred['depth']} | {pred['prediction_type']} "
            f"| {actual_rt:.2f} | {pred_rt:.2f} | {mre_rt:.1f} |"
        )

    lines.append('')
    return lines
