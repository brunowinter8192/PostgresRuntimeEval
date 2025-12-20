# INFRASTRUCTURE

from datetime import datetime
from pathlib import Path


# FUNCTIONS

# Export selection report as markdown
def export_selection_report(
    output_dir: str,
    strategy: str,
    iteration_data: list,
    collision_data: list,
    operator_baseline_mre: dict,
    summary: dict,
    max_iteration: int = None
) -> None:
    md_dir = Path(output_dir)
    md_dir.mkdir(parents=True, exist_ok=True)
    md_file = md_dir / 'selection_report.md'

    lines = build_report_lines(
        strategy, iteration_data, collision_data,
        operator_baseline_mre, summary, max_iteration
    )

    with open(md_file, 'w') as f:
        f.write('\n'.join(lines))


# Build all report lines
def build_report_lines(
    strategy: str,
    iteration_data: list,
    collision_data: list,
    operator_baseline_mre: dict,
    summary: dict,
    max_iteration: int = None
) -> list:
    lines = []

    lines.extend(build_header_section(strategy))
    lines.extend(build_summary_section(summary))
    lines.extend(build_operator_baseline_section(operator_baseline_mre))
    lines.extend(build_iteration_section(iteration_data, max_iteration))
    lines.extend(build_collision_section(collision_data, max_iteration))

    return lines


# Build header section
def build_header_section(strategy: str) -> list:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return [
        '# Pattern Selection Report',
        '',
        f'**Strategy:** {strategy}',
        f'**Generated:** {timestamp}',
        ''
    ]


# Build summary section
def build_summary_section(summary: dict) -> list:
    lines = [
        '## Summary',
        '',
        f"**Total Patterns:** {summary.get('total', 0)}",
        f"**Selected:** {summary.get('selected', 0)}",
        f"**Rejected:** {summary.get('rejected', 0)}",
        f"**Skipped (Low Error):** {summary.get('skipped_low_error', 0)}",
        f"**Skipped (No FFS):** {summary.get('skipped_no_ffs', 0)}",
        f"**Skipped (Low Template Count):** {summary.get('skipped_low_template', 0)}",
        '',
        f"**Initial MRE:** {summary.get('initial_mre', 0) * 100:.2f}%",
        f"**Final MRE:** {summary.get('final_mre', 0) * 100:.2f}%",
        f"**Improvement:** {(summary.get('initial_mre', 0) - summary.get('final_mre', 0)) * 100:.2f}%",
        ''
    ]
    return lines


# Build operator baseline MRE section
def build_operator_baseline_section(operator_baseline_mre: dict) -> list:
    lines = [
        '## Operator Baseline MRE',
        '',
        '| Operator | Mean MRE (%) | Count |',
        '|----------|--------------|-------|'
    ]

    sorted_ops = sorted(operator_baseline_mre.items(), key=lambda x: x[1]['mre'], reverse=True)

    for op_name, data in sorted_ops:
        mre_pct = data['mre'] * 100
        count = data['count']
        lines.append(f'| {op_name} | {mre_pct:.1f} | {count} |')

    lines.append('')
    return lines


# Build iteration log section
def build_iteration_section(iteration_data: list, max_iteration: int = None) -> list:
    lines = ['## Iteration Log', '']

    filtered = iteration_data
    if max_iteration is not None:
        filtered = [d for d in iteration_data if d['iteration'] <= max_iteration]

    for data in filtered:
        lines.extend(build_single_iteration(data))

    return lines


# Build single iteration entry
def build_single_iteration(data: dict) -> list:
    status = data.get('status', 'UNKNOWN')
    pattern_string = data.get('pattern_string', 'N/A')
    iteration = data.get('iteration', 0)

    lines = [f'### Iteration {iteration}: {pattern_string}', '']

    lines.append(f"**Pattern Hash:** `{data.get('pattern_hash', 'N/A')}`")
    lines.append(f"**Operator Count:** {data.get('operator_count', 0)}")
    lines.append(f"**Occurrences:** {data.get('occurrence_count', 0)}")
    lines.append('')

    root_op = data.get('root_operator', 'N/A')
    op_mre = data.get('operator_mre', 0) * 100
    threshold = data.get('threshold', 0.1) * 100

    lines.append(f"**Root Operator:** {root_op}")
    lines.append(f"**Operator MRE:** {op_mre:.1f}%")

    if status.startswith('SKIPPED'):
        lines.append(f"**Check:** {op_mre:.1f}% < {threshold:.0f}% threshold")
        lines.append(f"**Status:** {status}")
    else:
        lines.append(f"**Check:** {op_mre:.1f}% > {threshold:.0f}% threshold -> EVALUATE")
        lines.append('')

        baseline_mre = data.get('baseline_mre', 0) * 100
        new_mre = data.get('new_mre', 0) * 100
        delta = data.get('delta', 0) * 100

        lines.append(f"**MRE Before:** {baseline_mre:.2f}%")
        lines.append(f"**MRE After:** {new_mre:.2f}%")

        if status == 'SELECTED':
            lines.append(f"**Delta:** -{abs(delta):.2f}%")
        else:
            lines.append(f"**Delta:** +{abs(delta):.2f}%")

        lines.append(f"**Status:** {status}")

    lines.append('')
    return lines


# Build collision log section
def build_collision_section(collision_data: list, max_iteration: int = None) -> list:
    if not collision_data:
        return ['## Collision Log', '', 'No collisions detected.', '']

    lines = ['## Collision Log', '']

    filtered = collision_data
    if max_iteration is not None:
        filtered = [c for c in collision_data if c['iteration'] <= max_iteration]

    if not filtered:
        lines.append('No collisions in selected iterations.')
        lines.append('')
        return lines

    for collision in filtered:
        lines.extend(build_single_collision(collision))

    return lines


# Build single collision entry
def build_single_collision(collision: dict) -> list:
    rejected_string = collision.get('rejected_pattern_string', 'N/A')
    iteration = collision.get('iteration', 0)

    lines = [f'### Collision at Iteration {iteration}: {rejected_string}', '']

    lines.append(f"**Rejected Pattern:** {rejected_string}")
    lines.append(f"**Rejected Hash:** `{collision.get('rejected_hash', 'N/A')}`")
    lines.append(f"**Rejected Size:** {collision.get('rejected_size', 0)} operators")
    lines.append('')

    lines.append(f"**Winning Pattern:** {collision.get('winning_pattern_string', 'N/A')}")
    lines.append(f"**Winning Hash:** `{collision.get('winning_hash', 'N/A')}`")
    lines.append(f"**Winning Size:** {collision.get('winning_size', 0)} operators")
    lines.append(f"**Selected in Iteration:** {collision.get('winning_iteration', 'N/A')}")
    lines.append('')

    lines.append(f"**Conflicting Nodes:** {collision.get('conflicting_nodes', [])}")
    lines.append(f"**Rule:** Larger pattern ({collision.get('winning_size', 0)} ops) takes priority over smaller ({collision.get('rejected_size', 0)} ops)")
    lines.append('')

    return lines
