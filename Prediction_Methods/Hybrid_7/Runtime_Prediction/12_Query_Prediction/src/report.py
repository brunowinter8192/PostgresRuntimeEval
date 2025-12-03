# INFRASTRUCTURE

from datetime import datetime
from pathlib import Path

# From tree.py: Query tree data structures
from src.tree import build_tree_from_dataframe, extract_pattern_node_ids


# FUNCTIONS

class ReportBuilder:
    def __init__(self, output_dir: str, strategy: str = None):
        self.output_dir = output_dir
        self.strategy = strategy or 'operator-only'
        self.lines = []
        self.timestamp = datetime.now()
        self.query_file = None
        self.query_ops = None
        self.consumed_nodes = set()
        self.pattern_assignments = {}
        self.pattern_info = {}
        self.input_summary_lines = []

    # Store input summary for reuse across queries
    def add_input_summary(self, test_file: str, operator_model_dir: str, pattern_model_dir: str = None, num_patterns: int = 0):
        self.input_summary_lines = []
        self.input_summary_lines.append('## Input Summary')
        self.input_summary_lines.append('')
        self.input_summary_lines.append(f'- **Test File:** {test_file}')
        self.input_summary_lines.append(f'- **Operator Models:** {operator_model_dir}')

        if pattern_model_dir:
            self.input_summary_lines.append(f'- **Pattern Models:** {pattern_model_dir}')
            self.input_summary_lines.append(f'- **Selected Patterns:** {num_patterns}')

        self.input_summary_lines.append('')

    # Set query data for current query
    def set_query_data(self, query_file: str, query_ops, consumed_nodes: set, pattern_assignments: dict, pattern_info: dict):
        self.query_file = query_file
        self.query_ops = query_ops
        self.consumed_nodes = consumed_nodes
        self.pattern_assignments = pattern_assignments
        self.pattern_info = pattern_info

        self.lines = []
        self.lines.append('# Query Prediction Report')
        self.lines.append('')
        self.lines.append(f'**Query:** {query_file}')
        self.lines.append(f'**Strategy:** {self.strategy}')
        self.lines.append(f'**Timestamp:** {self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}')
        self.lines.append('')
        self.lines.extend(self.input_summary_lines)

    # Add pattern assignments section
    def add_pattern_assignments_section(self):
        self.lines.append('## Pattern Assignments')
        self.lines.append('')

        if not self.pattern_assignments:
            self.lines.append('No patterns applied (operator-only mode).')
            self.lines.append('')
            return

        self.lines.append('| Pattern Hash | Root Node | Pattern Length | Consumed Nodes |')
        self.lines.append('|--------------|-----------|----------------|----------------|')

        for root_node_id, pattern_hash in self.pattern_assignments.items():
            info = self.pattern_info.get(pattern_hash, {})
            pattern_length = info.get('length', 1)

            consumed_by_pattern = [nid for nid in self.consumed_nodes if nid != root_node_id]
            consumed_str = ', '.join(str(nid) for nid in sorted(consumed_by_pattern)) or '-'

            self.lines.append(f'| {pattern_hash[:8]} | {root_node_id} | {pattern_length} | {consumed_str} |')

        self.lines.append('')

    # Add query tree section with ASCII visualization
    def add_query_tree_section(self):
        self.lines.append('## Query Tree')
        self.lines.append('')
        self.lines.append('```')

        if self.query_ops is not None and not self.query_ops.empty:
            root = build_tree_from_dataframe(self.query_ops)
            self._render_tree_node(root, 0)

        self.lines.append('```')
        self.lines.append('')

    # Render single tree node recursively
    def _render_tree_node(self, node, indent: int):
        prefix = '  ' * indent
        label = f'Node {node.node_id} ({node.node_type})'

        if node.node_id in self.pattern_assignments:
            pattern_hash = self.pattern_assignments[node.node_id]
            label += f' [PATTERN: {pattern_hash[:8]}]'
        elif node.node_id in self.consumed_nodes:
            label += ' [consumed]'

        if node.depth == 0:
            label += ' - ROOT'
        elif len(node.children) == 0:
            label += ' - LEAF'

        self.lines.append(f'{prefix}{label}')

        for child in node.children:
            self._render_tree_node(child, indent + 1)

    # Add prediction results section
    def add_prediction_results(self, predictions: list):
        self.lines.append('## Prediction Results')
        self.lines.append('')
        self.lines.append('| Node | Type | Actual (ms) | Predicted (ms) | MRE (%) | Source |')
        self.lines.append('|------|------|-------------|----------------|---------|--------|')

        total_mre = 0.0
        count = 0

        for p in sorted(predictions, key=lambda x: x['depth']):
            actual = p['actual_total_time']
            predicted = p['predicted_total_time']
            mre = abs(predicted - actual) / actual * 100 if actual > 0 else 0

            self.lines.append(f'| {p["node_id"]} | {p["node_type"]} | {actual:.2f} | {predicted:.2f} | {mre:.1f} | {p["prediction_type"]} |')

            total_mre += mre
            count += 1

        self.lines.append('')

        avg_mre = total_mre / count if count > 0 else 0
        pattern_count = sum(1 for p in predictions if p['prediction_type'] == 'pattern')
        operator_count = sum(1 for p in predictions if p['prediction_type'] == 'operator')

        self.lines.append('## Summary')
        self.lines.append('')
        self.lines.append(f'- **Average MRE:** {avg_mre:.2f}%')
        self.lines.append(f'- **Predictions by Pattern:** {pattern_count}')
        self.lines.append(f'- **Predictions by Operator:** {operator_count}')
        self.lines.append('')

    # Add prediction chain section with step-by-step details
    def add_prediction_chain(self, predictions: list, prediction_cache: dict, pattern_assignments: dict, consumed_nodes: set, pattern_info: dict):
        self.lines.append('## Prediction Chain (Bottom-Up)')
        self.lines.append('')

        sorted_predictions = sorted(predictions, key=lambda x: -x['depth'])

        for step, p in enumerate(sorted_predictions, 1):
            node_id = p['node_id']
            node_type = p['node_type']
            source = p['prediction_type']
            depth = p['depth']

            is_root = depth == 0
            is_leaf = not any(pred['depth'] > depth for pred in predictions if pred['node_id'] != node_id)
            is_pattern_root = node_id in pattern_assignments

            role = ''
            if is_root:
                role = 'ROOT'
            elif is_pattern_root:
                role = 'PATTERN ROOT'
            elif is_leaf:
                role = 'LEAF'

            self.lines.append(f'### Step {step}: Node {node_id} ({node_type}){" - " + role if role else ""}')
            self.lines.append('')
            self.lines.append(f'- **Source:** {source}')

            if node_id in pattern_assignments:
                pattern_hash = pattern_assignments[node_id]
                info = pattern_info.get(pattern_hash, {})
                length = info.get('length', 1)
                self.lines.append(f'- **Pattern:** {pattern_hash[:8]} (length={length})')

                consumed_by_this = [nid for nid in consumed_nodes if nid != node_id]
                relevant_consumed = []

                if self.query_ops is not None:
                    root = build_tree_from_dataframe(self.query_ops[self.query_ops['node_id'] == node_id])
                    if root:
                        pattern_node_ids = extract_pattern_node_ids(root, length)
                        relevant_consumed = [nid for nid in pattern_node_ids if nid != node_id]

                if relevant_consumed:
                    self.lines.append(f'- **Consumes:** Nodes {", ".join(str(nid) for nid in sorted(relevant_consumed))}')

            if node_id in prediction_cache:
                cache = prediction_cache[node_id]

                model_path = cache.get('model_path')
                if model_path:
                    self.lines.append(f'- **Model:** `{model_path}`')

                input_features = cache.get('input_features', {})

                if input_features:
                    for target_name, features in input_features.items():
                        if features:
                            self.lines.append(f'- **Input ({target_name}):**')

                            for k, v in sorted(features.items()):
                                if isinstance(v, float):
                                    self.lines.append(f'  - {k}={v:.4f}')
                                else:
                                    self.lines.append(f'  - {k}={v}')

            self.lines.append(f'- **Output:** st={p["predicted_startup_time"]:.2f}, rt={p["predicted_total_time"]:.2f}')
            self.lines.append('')

    # Save report to markdown file
    def save(self):
        if not self.query_file:
            return

        md_dir = Path(self.output_dir) / 'md'
        md_dir.mkdir(parents=True, exist_ok=True)

        timestamp_str = self.timestamp.strftime('%Y%m%d_%H%M%S')
        filename = f'12_query_prediction_{self.query_file}_{timestamp_str}.md'

        with open(md_dir / filename, 'w') as f:
            f.write('\n'.join(self.lines))
