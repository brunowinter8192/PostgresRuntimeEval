import argparse
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# INFRASTRUCTURE

PHASE_THRESHOLDS = [0, 25, 50, 75, 90, 100]
CONVERGENCE_POINTS = [50, 90, 95]

# ORCHESTRATOR

def analyze_convergence(selection_log: str, output_dir: str) -> None:
    df = load_selection_log(selection_log)
    mre_curve = extract_mre_curve(df)
    baseline_mre, final_mre = mre_curve[0], mre_curve[-1]
    total_improvement = baseline_mre - final_mre
    phases = compute_phases(mre_curve, baseline_mre, total_improvement)
    convergence = compute_convergence_points(mre_curve, baseline_mre, total_improvement)
    export_results(phases, convergence, baseline_mre, final_mre, total_improvement, len(mre_curve), output_dir)
    export_plot(mre_curve, output_dir)

# FUNCTIONS

# Load selection log CSV
def load_selection_log(path: str) -> pd.DataFrame:
    return pd.read_csv(path, delimiter=';')

# Extract MRE values per iteration
def extract_mre_curve(df: pd.DataFrame) -> list:
    mre_values = []
    current_mre = df['baseline_mre'].iloc[0]
    for _, row in df.iterrows():
        if row['status'] == 'SELECTED':
            current_mre = row['new_mre']
        mre_values.append(current_mre)
    return mre_values

# Compute phases based on percent of total improvement
def compute_phases(mre_curve: list, baseline_mre: float, total_improvement: float) -> list:
    phases = []
    for i in range(len(PHASE_THRESHOLDS) - 1):
        pct_start = PHASE_THRESHOLDS[i]
        pct_end = PHASE_THRESHOLDS[i + 1]
        target_start = baseline_mre - (pct_start / 100) * total_improvement
        target_end = baseline_mre - (pct_end / 100) * total_improvement
        iter_start = find_iteration_for_mre(mre_curve, target_start)
        iter_end = find_iteration_for_mre(mre_curve, target_end)
        phases.append({
            'phase': i + 1,
            'pct_start': pct_start,
            'pct_end': pct_end,
            'iter_start': iter_start,
            'iter_end': iter_end,
            'iterations_needed': iter_end - iter_start,
            'mre_at_start': round(mre_curve[iter_start], 6),
            'mre_at_end': round(mre_curve[min(iter_end, len(mre_curve) - 1)], 6)
        })
    return phases

# Find first iteration where MRE drops to or below target
def find_iteration_for_mre(mre_curve: list, target: float) -> int:
    for i, mre in enumerate(mre_curve):
        if mre <= target:
            return i
    return len(mre_curve) - 1

# Compute convergence points (iterations at X% improvement)
def compute_convergence_points(mre_curve: list, baseline_mre: float, total_improvement: float) -> dict:
    convergence = {}
    for pct in CONVERGENCE_POINTS:
        target = baseline_mre - (pct / 100) * total_improvement
        convergence[f'iter_at_{pct}pct'] = find_iteration_for_mre(mre_curve, target)
    return convergence

# Export results to CSV
def export_results(phases: list, convergence: dict, baseline_mre: float, final_mre: float, total_improvement: float, total_iterations: int, output_dir: str) -> None:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    df_phases = pd.DataFrame(phases)
    df_summary = pd.DataFrame([{
        'baseline_mre': round(baseline_mre, 6),
        'final_mre': round(final_mre, 6),
        'total_improvement': round(total_improvement, 6),
        'total_iterations': total_iterations,
        **{k: v for k, v in convergence.items()}
    }])
    df_phases.to_csv(out_path / 'A_02b_phases.csv', sep=';', index=False)
    df_summary.to_csv(out_path / 'A_02b_summary.csv', sep=';', index=False)

# Export MRE progression plot
def export_plot(mre_curve: list, output_dir: str) -> None:
    out_path = Path(output_dir)
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(mre_curve)), mre_curve, linewidth=1.5)
    plt.xlabel('Iteration')
    plt.ylabel('MRE')
    plt.title('MRE Progression over Pattern Selection')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path / 'A_02b_mre_progression.png', dpi=150)
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("selection_log", help="Path to selection_log.csv")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()
    analyze_convergence(args.selection_log, args.output_dir)
