#!/usr/bin/env python3

# INFRASTRUCTURE
from datetime import datetime
from pathlib import Path


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
        self.lines.append('| Hash | Pattern String | Length | Occurrences | Error Score |')
        self.lines.append('|------|----------------|--------|-------------|-------------|')

        for r in ranking[:10]:
            pattern_str = r['pattern_string'][:40] + '...' if len(r['pattern_string']) > 40 else r['pattern_string']
            self.lines.append(f'| {r["pattern_hash"][:8]} | {pattern_str} | {r["pattern_length"]} | {r["occurrence_count"]} | {r["error_score"]:.4f} |')

        self.lines.append('')
        self.lines.append('## Phase D: Pattern Selection')
        self.lines.append('')
        self.lines.append('| Iter | Pattern | Error Score | Delta | Status | MRE After |')
        self.lines.append('|------|---------|-------------|-------|--------|-----------|')

    def add_selection_iteration(self, iteration, pattern_hash, candidate, delta, status, mre_after):
        delta_str = f'{delta*100:.4f}%' if delta else 'N/A'
        self.lines.append(f'| {iteration} | {pattern_hash[:8]} | {candidate["error_score"]:.4f} | {delta_str} | {status} | {mre_after*100:.2f}% |')

    def add_final_prediction(self, predictions, final_mre, baseline_mre):
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

    def save(self):
        md_dir = Path(self.output_dir) / 'md'
        md_dir.mkdir(parents=True, exist_ok=True)

        timestamp_str = self.timestamp.strftime('%Y%m%d_%H%M%S')
        filename = f'02_online_prediction_{self.query_file}_{timestamp_str}.md'

        with open(md_dir / filename, 'w') as f:
            f.write('\n'.join(self.lines))
