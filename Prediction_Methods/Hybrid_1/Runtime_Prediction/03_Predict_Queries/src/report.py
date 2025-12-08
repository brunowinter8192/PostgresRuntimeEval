# INFRASTRUCTURE

from datetime import datetime
from pathlib import Path

# From tree.py: Build query tree string
from src.tree import build_query_tree_string


# FUNCTIONS

# Format feature values for MD output
def format_feature_values(feature_dict: dict) -> str:
    parts = []
    for k, v in feature_dict.items():
        if isinstance(v, float):
            parts.append(f'{k}={v:.4f}')
        else:
            parts.append(f'{k}={v}')
    return ', '.join(parts)


# Export MD report for single query prediction
def export_md_report(
    query_file: str,
    test_file: str,
    pattern_overview_file: str,
    operator_overview_file: str,
    pattern_model_dir: str,
    operator_model_dir: str,
    df_query,
    predictions: list,
    steps: list,
    output_dir: str
) -> None:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    timestamp_display = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    md_dir = Path(output_dir) / 'md'
    md_dir.mkdir(parents=True, exist_ok=True)

    query_name = query_file.replace('.sql', '')
    md_file = md_dir / f'03_query_prediction_{query_name}_{timestamp}.md'

    lines = build_report_lines(
        query_file, timestamp_display, test_file, pattern_overview_file,
        operator_overview_file, pattern_model_dir, operator_model_dir,
        df_query, predictions, steps
    )

    with open(md_file, 'w') as f:
        f.write('\n'.join(lines))


# Build all report lines
def build_report_lines(
    query_file: str,
    timestamp: str,
    test_file: str,
    pattern_overview_file: str,
    operator_overview_file: str,
    pattern_model_dir: str,
    operator_model_dir: str,
    df_query,
    predictions: list,
    steps: list
) -> list:
    lines = []

    lines.extend(build_header_section(query_file, timestamp))
    lines.extend(build_algorithm_section())
    lines.extend(build_input_section(test_file, pattern_overview_file, operator_overview_file, pattern_model_dir, operator_model_dir))
    lines.extend(build_tree_section(df_query))
    lines.extend(build_chain_section(steps))
    lines.extend(build_results_section(predictions))

    return lines


# Build header section
def build_header_section(query_file: str, timestamp: str) -> list:
    return [
        '# Query Prediction Report (Hybrid_1)',
        '',
        f'**Query:** {query_file}',
        f'**Timestamp:** {timestamp}',
        ''
    ]


# Build algorithm section
def build_algorithm_section() -> list:
    return [
        '## Algorithm',
        '',
        'Child-to-Parent Bottom-Up Pattern Matching:',
        '1. Start bei tiefster depth, iteriere bis depth 0',
        '2. Fuer jeden Operator: Schaue zu Parent HOCH',
        '3. Versuche Pattern zu bilden: Parent + alle direkten Children',
        '4. Pattern matched -> Prediction fuer Parent, Parent + Children consumed',
        '5. Kein Pattern -> Operator-Fallback fuer einzelnen Node',
        '6. Predicted Values werden Child-Features (st1/rt1/st2/rt2) fuer hoehere Ebenen',
        ''
    ]


# Build input summary section
def build_input_section(test_file: str, pattern_overview: str, operator_overview: str, pattern_dir: str, operator_dir: str) -> list:
    return [
        '## Input Summary',
        '',
        f'- **Test File:** {Path(test_file).resolve()}',
        f'- **Pattern Overview:** {Path(pattern_overview).resolve()}',
        f'- **Operator Overview:** {Path(operator_overview).resolve()}',
        f'- **Pattern Models:** {Path(pattern_dir).resolve()}',
        f'- **Operator Models:** {Path(operator_dir).resolve()}',
        ''
    ]


# Build query tree section
def build_tree_section(df_query) -> list:
    return [
        '## Query Tree',
        '',
        '```',
        build_query_tree_string(df_query),
        '```',
        ''
    ]


# Build prediction chain section
def build_chain_section(steps: list) -> list:
    lines = ['## Prediction Chain (Bottom-Up)', '']

    for step in steps:
        if step['prediction_type'] == 'pattern':
            lines.extend(build_pattern_step(step))
        else:
            lines.extend(build_operator_step(step))

        lines.append(f"- **Model (execution_time):** {step['model_path_exec']}")
        lines.append(f"- **Model (start_time):** {step['model_path_start']}")
        lines.append('')
        lines.append(f"**Features (execution_time):** {', '.join(step['features_exec'])}")
        lines.append(f"**Input:** {format_feature_values(step['input_values_exec'])}")
        lines.append('')
        lines.append(f"**Features (start_time):** {', '.join(step['features_start'])}")
        lines.append(f"**Input:** {format_feature_values(step['input_values_start'])}")
        lines.append('')
        lines.append(f"**Output:** predicted_startup_time={step['predicted_startup_time']:.2f}, predicted_total_time={step['predicted_total_time']:.2f}")
        lines.append('')

    return lines


# Build pattern step lines
def build_pattern_step(step: dict) -> list:
    lines = [
        f"### Step {step['step']} (depth {step['depth']}): Pattern Match",
        '',
        f"- **Pattern:** {step['pattern_folder']} ({step['pattern_hash']})",
    ]

    consumed_str = ', '.join([f"Node {nid} ({ntype})" for nid, ntype in step['consumed_children']])
    lines.append(f"- **Consumed:** Node {step['parent_node_id']} ({step['parent_node_type']}), {consumed_str}")
    lines.append(f"- **Prediction for:** Node {step['parent_node_id']} ({step['parent_node_type']})")

    return lines


# Build operator step lines
def build_operator_step(step: dict) -> list:
    reason = step.get('reason', 'No pattern match available')
    return [
        f"### Step {step['step']} (depth {step['depth']}): Operator Fallback",
        '',
        f"- **Node:** {step['node_id']} ({step['node_type']})",
        f"- **Reason:** {reason}"
    ]


# Build prediction results section
def build_results_section(predictions: list) -> list:
    lines = [
        '## Prediction Results',
        '',
        '| Node | Type | Depth | Pred Type | Actual ST | Actual RT | Pred ST | Pred RT | MRE ST (%) | MRE RT (%) |',
        '|------|------|-------|-----------|-----------|-----------|---------|---------|------------|------------|'
    ]

    for pred in predictions:
        actual_st = pred['actual_startup_time']
        actual_rt = pred['actual_total_time']
        pred_st = pred['predicted_startup_time']
        pred_rt = pred['predicted_total_time']

        mre_st = abs(actual_st - pred_st) / actual_st * 100 if actual_st > 0 else 0
        mre_rt = abs(actual_rt - pred_rt) / actual_rt * 100 if actual_rt > 0 else 0

        lines.append(
            f"| {pred['node_id']} | {pred['node_type']} | {pred['depth']} | {pred['prediction_type']} "
            f"| {actual_st:.2f} | {actual_rt:.2f} | {pred_st:.2f} | {pred_rt:.2f} "
            f"| {mre_st:.1f} | {mre_rt:.1f} |"
        )

    lines.append('')

    return lines
