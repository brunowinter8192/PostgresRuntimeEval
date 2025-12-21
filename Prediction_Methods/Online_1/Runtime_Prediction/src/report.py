#!/usr/bin/env python3

# INFRASTRUCTURE
from datetime import datetime
from pathlib import Path

# From tree.py: Query tree data structures
from .tree import build_tree_from_dataframe, extract_all_nodes, extract_pattern_node_ids


# FUNCTIONS

class ReportBuilder:
    def __init__(self, query_file: str, output_dir: str):
        self.query_file = query_file
        self.output_dir = output_dir
        self.lines = []
        self.timestamp = datetime.now()

        self.lines.append('# Online Prediction Report')
        self.lines.append('')
        self.lines.append(f'**Test Query:** {query_file}')
        self.lines.append(f'**Timestamp:** {self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}')
        self.lines.append('')

    def add_data_summary(self, df_tt, df_tv, df_train, df_test):
        self.lines.append('## Data Summary')
        self.lines.append('')
        self.lines.append('| Dataset | Rows | Purpose |')
        self.lines.append('|---------|------|---------|')
        self.lines.append(f'| Training_Training | {len(df_tt)} | Operator + Pattern Training |')
        self.lines.append(f'| Training_Test | {len(df_tv)} | Pattern Selection Eval |')
        self.lines.append(f'| Training | {len(df_train)} | Final Model Training |')
        self.lines.append(f'| Test | {len(df_test)} | Final Prediction |')
        self.lines.append('')

    def add_query_tree(self, query_ops, pattern_assignments: dict, consumed_nodes: set, patterns: dict):
        self.lines.append('## Query Tree')
        self.lines.append('')
        self.lines.append('```')

        root = build_tree_from_dataframe(query_ops)
        self._render_tree_node(root, 0, pattern_assignments, consumed_nodes, patterns)

        self.lines.append('```')
        self.lines.append('')

    def _render_tree_node(self, node, indent: int, pattern_assignments: dict, consumed_nodes: set, patterns: dict):
        prefix = '  ' * indent
        label = f'Node {node.node_id} ({node.node_type})'

        if node.node_id in pattern_assignments:
            pattern_hash = pattern_assignments[node.node_id]
            label += f' [PATTERN: {pattern_hash[:8]}]'
        elif node.node_id in consumed_nodes:
            label += ' [consumed]'

        if node.depth == 0:
            label += ' - ROOT'
        elif len(node.children) == 0:
            label += ' - LEAF'

        self.lines.append(f'{prefix}{label}')

        for child in node.children:
            self._render_tree_node(child, indent + 1, pattern_assignments, consumed_nodes, patterns)

    def add_pattern_assignments(self, pattern_assignments: dict, consumed_nodes: set, patterns: dict):
        self.lines.append('## Pattern Assignments')
        self.lines.append('')

        if not pattern_assignments:
            self.lines.append('No patterns selected.')
            self.lines.append('')
            return

        self.lines.append('| Pattern | Hash | Root Node | Consumed Nodes |')
        self.lines.append('|---------|------|-----------|----------------|')

        for root_node_id, pattern_hash in pattern_assignments.items():
            pattern_info = patterns.get(pattern_hash, {})
            pattern_str = pattern_info.get('pattern_string', 'Unknown')[:30]
            pattern_length = pattern_info.get('pattern_length', 1)

            consumed_by_pattern = [nid for nid in consumed_nodes if nid != root_node_id]
            consumed_str = ', '.join(str(nid) for nid in sorted(consumed_by_pattern)) or '-'

            self.lines.append(f'| {pattern_str} | {pattern_hash[:8]} | {root_node_id} | {consumed_str} |')

        self.lines.append('')

    def add_operator_training(self, op_type, samples):
        pass

    def add_operator_baseline(self, baseline_mre):
        self.lines.append('## Phase B: Operator Baseline')
        self.lines.append('')
        self.lines.append(f'- Baseline MRE: {baseline_mre*100:.2f}%')
        self.lines.append('')

    def add_patterns_in_query(self, patterns, ranking):
        self.lines.append('## Phase C: Patterns in Query')
        self.lines.append('')
        self.lines.append(f'- Total Patterns: {len(patterns)}')
        self.lines.append('')
        self.lines.append('| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |')
        self.lines.append('|------|----------------|--------|-----|---------|-------------|')

        ranking_lookup = {r['pattern_hash']: r for r in ranking}

        for pattern_hash, pattern_info in patterns.items():
            pattern_str = pattern_info['pattern_string'][:40] + '...' if len(pattern_info['pattern_string']) > 40 else pattern_info['pattern_string']

            if pattern_hash in ranking_lookup:
                r = ranking_lookup[pattern_hash]
                self.lines.append(f'| {pattern_hash[:8]} | {pattern_str} | {r["pattern_length"]} | {r["occurrence_count"]} | {r["avg_mre"]*100:.1f}% | {r["error_score"]:.4f} |')
            else:
                self.lines.append(f'| {pattern_hash[:8]} | {pattern_str} | {pattern_info["pattern_length"]} | 0 | - | - |')

        self.lines.append('')
        self.lines.append('**Legend:**')
        self.lines.append('- **Occ:** Pattern occurrences in Training_Test')
        self.lines.append('- **Avg MRE:** Average MRE of operator predictions at pattern root nodes')
        self.lines.append('- **Error Score:** Occ x Avg MRE (initial ranking metric)')
        self.lines.append('')
        self.lines.append('## Phase D: Pattern Selection')
        self.lines.append('')
        self.lines.append('| Iter | Pattern | Error Score | Delta | Status | Global MRE |')
        self.lines.append('|------|---------|-------------|-------|--------|-----------|')

    def add_selection_iteration(self, iteration, pattern_hash, candidate, delta, status, mre_after):
        delta_str = f'{delta*100:.4f}%' if delta else 'N/A'
        self.lines.append(f'| {iteration} | {pattern_hash[:8]} | {candidate["error_score"]:.4f} | {delta_str} | {status} | {mre_after*100:.2f}% |')

    def add_final_prediction(self, predictions, final_mre, baseline_mre):
        self.lines.append('')
        self.lines.append('**Legend:**')
        self.lines.append('- **Error Score:** Score at iteration time (recalculated after each ACCEPT)')
        self.lines.append('- **Delta:** MRE improvement if pattern is added')
        self.lines.append('- **Global MRE:** Overall MRE on Training_Test after this iteration')
        self.lines.append('')
        self.lines.append('## Phase E: Final Prediction')
        self.lines.append('')
        self.lines.append(f'- Final MRE: {final_mre*100:.2f}%')
        self.lines.append(f'- Improvement: {(baseline_mre - final_mre)*100:.2f}%')
        self.lines.append('')
        self.lines.append('| Node | Type | Actual | Predicted | MRE | Source |')
        self.lines.append('|------|------|--------|-----------|-----|--------|')

        for p in sorted(predictions, key=lambda x: x['depth']):
            mre = abs(p['predicted_total_time'] - p['actual_total_time']) / p['actual_total_time'] * 100 if p['actual_total_time'] > 0 else 0
            self.lines.append(f'| {p["node_id"]} | {p["node_type"]} | {p["actual_total_time"]:.2f} | {p["predicted_total_time"]:.2f} | {mre:.1f}% | {p["prediction_type"]} |')

    def add_prediction_chain(self, predictions: list, prediction_cache: dict, pattern_assignments: dict, consumed_nodes: set, patterns: dict):
        self.lines.append('')
        self.lines.append('## Prediction Chain (Bottom-Up)')
        self.lines.append('')

        sorted_predictions = sorted(predictions, key=lambda x: -x['depth'])

        for step, p in enumerate(sorted_predictions, 1):
            node_id = p['node_id']
            node_type = p['node_type']
            source = p['prediction_type']
            depth = p['depth']

            role = 'ROOT' if depth == 0 else ('LEAF' if p.get('is_leaf', False) else '')
            if node_id in pattern_assignments:
                role = 'PATTERN ROOT'

            self.lines.append(f'### Step {step}: Node {node_id} ({node_type}){" - " + role if role else ""}')
            self.lines.append('')
            self.lines.append(f'- **Source:** {source}')

            if node_id in pattern_assignments:
                pattern_hash = pattern_assignments[node_id]
                pattern_info = patterns.get(pattern_hash, {})
                pattern_str = pattern_info.get('pattern_string', 'Unknown')
                self.lines.append(f'- **Pattern:** {pattern_hash[:8]} ({pattern_str})')

                consumed_by_this = [nid for nid in consumed_nodes if nid != node_id]
                if consumed_by_this:
                    self.lines.append(f'- **Consumes:** Nodes {", ".join(str(nid) for nid in sorted(consumed_by_this))}')

            if node_id in prediction_cache:
                cache = prediction_cache[node_id]

                input_features = cache.get('input_features', {})
                if input_features:
                    self.lines.append('- **Input Features:**')
                    feature_strs = [f'  - {k}={v:.4f}' if isinstance(v, float) else f'  - {k}={v}' for k, v in sorted(input_features.items())]
                    self.lines.extend(feature_strs)

            self.lines.append(f'- **Output:** st={p["predicted_startup_time"]:.2f}, rt={p["predicted_total_time"]:.2f}')
            self.lines.append('')

    def save(self):
        md_dir = Path(self.output_dir) / 'md'
        md_dir.mkdir(parents=True, exist_ok=True)

        filename = 'report.md'

        with open(md_dir / filename, 'w') as f:
            f.write('\n'.join(self.lines))
