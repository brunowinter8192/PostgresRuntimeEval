#!/usr/bin/env python3
import sys
import pandas as pd
from pathlib import Path
from datetime import datetime

def analyze_warm_first_run_effect(warm_df):
    results = []
    
    for _, row in warm_df.iterrows():
        query = row['query']
        run1 = row['run_1_ms']
        
        runs_2_5 = [row['run_2_ms'], row['run_3_ms'], 
                    row['run_4_ms'], row['run_5_ms']]
        mean_2_5 = sum(runs_2_5) / len(runs_2_5)
        
        diff_abs = run1 - mean_2_5
        diff_pct = (diff_abs / mean_2_5) * 100
        
        results.append({
            'query': query,
            'run_1_ms': run1,
            'runs_2_5_mean_ms': mean_2_5,
            'diff_abs_ms': diff_abs,
            'diff_pct': diff_pct
        })
    
    return pd.DataFrame(results)

def compare_cold_warm_means(cold_df, warm_df):
    merged = cold_df.merge(warm_df, on='query', suffixes=('_cold', '_warm'))
    
    results = []
    for _, row in merged.iterrows():
        cold_mean = row['mean_ms_cold']
        warm_mean = row['mean_ms_warm']
        
        diff_abs = cold_mean - warm_mean
        diff_pct = (diff_abs / cold_mean) * 100
        speedup = cold_mean / warm_mean
        
        results.append({
            'query': row['query'],
            'cold_mean_ms': cold_mean,
            'warm_mean_ms': warm_mean,
            'diff_abs_ms': diff_abs,
            'diff_pct': diff_pct,
            'speedup_factor': speedup
        })
    
    return pd.DataFrame(results)

def main():
    cold_path = Path(sys.argv[1])
    warm_path = Path(sys.argv[2])
    
    cold_df = pd.read_csv(cold_path)
    warm_df = pd.read_csv(warm_path)
    
    cold_df['query'] = cold_df['template']
    
    first_run_df = analyze_warm_first_run_effect(warm_df)
    cold_warm_df = compare_cold_warm_means(cold_df, warm_df)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(__file__).parent / 'csv'
    output_dir.mkdir(exist_ok=True)
    
    first_run_file = output_dir / f'warm_first_run_effect_{timestamp}.csv'
    cold_warm_file = output_dir / f'cold_vs_warm_{timestamp}.csv'
    
    first_run_df.to_csv(first_run_file, index=False)
    cold_warm_df.to_csv(cold_warm_file, index=False)
    
    print(f"{first_run_file}")
    print(f"{cold_warm_file}")

if __name__ == "__main__":
    main()
