# Missing Child Features Analysis

Child features checked: st1, rt1, st2, rt2, nt1, nt2

## Index_Scan

| Target | Template | Missing Features |
|--------|----------|------------------|
| execution_time | Q1 | st1, rt1, st2, rt2 |
| execution_time | Q10 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q12 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q13 | st1, rt1, st2, rt2 |
| execution_time | Q14 | st1, rt1, st2, rt2 |
| execution_time | Q18 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q19 | st1, rt1, st2, rt2 |
| execution_time | Q3 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q4 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q5 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q6 | st1, rt1, st2, rt2 |
| execution_time | Q7 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q8 | st1, rt1, st2, rt2 |
| execution_time | Q9 | st1, rt1, st2, rt2 |
| start_time | Q1 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q10 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q12 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q13 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q14 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q18 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q19 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q3 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q4 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q5 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q6 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q7 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q8 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q9 | st1, rt1, st2, rt2, nt1, nt2 |

## Seq_Scan

| Target | Template | Missing Features |
|--------|----------|------------------|
| execution_time | Q1 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q10 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q12 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q13 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q14 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q18 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q19 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q3 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q4 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q5 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q6 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q7 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q8 | st1, rt1, st2, rt2, nt1, nt2 |
| execution_time | Q9 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q1 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q10 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q12 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q14 | st1, rt1, st2, rt2, nt2 |
| start_time | Q18 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q19 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q3 | st1, rt1, st2, rt2, nt2 |
| start_time | Q4 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q5 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q6 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q7 | st1, rt1, st2, rt2 |
| start_time | Q8 | st1, rt1, st2, rt2, nt1, nt2 |
| start_time | Q9 | st1, rt1, st2, rt2, nt1, nt2 |

## Summary

### Missing count per feature

- st1: 55 times missing
- rt1: 55 times missing
- st2: 55 times missing
- rt2: 55 times missing
- nt1: 45 times missing
- nt2: 47 times missing

### Operators with missing child features

- Index_Scan: 28 entries with missing features
- Seq_Scan: 27 entries with missing features