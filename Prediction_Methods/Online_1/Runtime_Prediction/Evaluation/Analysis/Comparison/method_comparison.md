# Method Comparison Report

**Ordering (Dumb -> Intelligent):** Hybrid_1 -> Hybrid_2 -> Online_1

## Input Paths

- **Hybrid_1:** `../../Hybrid_1/Runtime_Prediction/Baseline_SVM/Evaluation/approach_3`
- **Hybrid_2:** `../../Hybrid_2/Runtime_Prediction/Evaluation/Size/Epsilon`
- **Online_1:** `Evaluation/Analysis/Size`

## Summary

**Overall MRE:** H1=6.25% ✓-> H2=3.48% ≈-> O1=3.15%

- **H1 -> H2:** 6 templates improved, 8 templates worsened (overall: -2.77%)
- **H2 -> O1:** 8 templates improved, 5 templates worsened (overall: -0.33%)

## Template MRE Comparison

### Q1

- **MRE:** H1=4.7% ≈-> H2=4.73% ✗-> O1=10.06%
- **H1 Patterns:** f8231c4d
- **H2 Patterns:** 52c5ec81
- **O1 Patterns:** -

### Q3

- **MRE:** H1=2.57% ≈-> H2=2.32% ✓-> O1=1.4%
- **H1 Patterns:** 25df29b5,f4cb205a
- **H2 Patterns:** 25df29b5,3aab37be
- **O1 Patterns:** 25df29b5

### Q4

- **MRE:** H1=4.8% ✓-> H2=2.99% ≈-> O1=3.12%
- **H1 Patterns:** c53c4396,f8231c4d
- **H2 Patterns:** 2724c080
- **O1 Patterns:** -

### Q5

- **MRE:** H1=4.24% ✗-> H2=5.22% ✓-> O1=3.16%
- **H1 Patterns:** 460af52c,a95bee4e
- **H2 Patterns:** 2724c080,3aab37be
- **O1 Patterns:** -

### Q6

- **MRE:** H1=4.08% ≈-> H2=4.48% ✗-> O1=5.33%
- **H1 Patterns:** a5f39f08
- **H2 Patterns:** a5f39f08
- **O1 Patterns:** a5f39f08

### Q7

- **MRE:** H1=1.33% ≈-> H2=1.75% ≈-> O1=1.25%
- **H1 Patterns:** 9d0e407c,a54055ce,b149ff28
- **H2 Patterns:** 2724c080,3aab37be
- **O1 Patterns:** -

### Q8

- **MRE:** H1=1.81% ✗-> H2=3.73% ✓-> O1=2.92%
- **H1 Patterns:** 53f9aa07,a95bee4e
- **H2 Patterns:** 2724c080,3aab37be
- **O1 Patterns:** -

### Q9

- **MRE:** H1=9.82% ✓-> H2=9.3% ✓-> O1=5.43%
- **H1 Patterns:** 2873b8c3,3aab37be,a5f39f08,bd9dfa7b,ec92bdaa
- **H2 Patterns:** 3aab37be,a5f39f08
- **O1 Patterns:** a5f39f08

### Q10

- **MRE:** H1=1.96% ≈-> H2=2.2% ✓-> O1=1.15%
- **H1 Patterns:** 25df29b5,7a51ce50
- **H2 Patterns:** 25df29b5,3aab37be
- **O1 Patterns:** 25df29b5

### Q12

- **MRE:** H1=2.77% ✗-> H2=5.53% ✓-> O1=4.17%
- **H1 Patterns:** 460af52c,c53c4396
- **H2 Patterns:** 2724c080
- **O1 Patterns:** -

### Q13

- **MRE:** H1=12.96% ✓-> H2=1.82% ≈-> O1=1.84%
- **H1 Patterns:** 1d35fb97,422ae017
- **H2 Patterns:** 35ffb644
- **O1 Patterns:** 35ffb644

### Q14

- **MRE:** H1=2.29% ✓-> H2=1.5% ≈-> O1=1.93%
- **H1 Patterns:** 310134da
- **H2 Patterns:** 3aab37be,a5f39f08
- **O1 Patterns:** a5f39f08

### Q18

- **MRE:** H1=32.61% ✓-> H2=0.48% ≈-> O1=0.48%
- **H1 Patterns:** 7bcfec22,895c6e8c
- **H2 Patterns:** fd858367
- **O1 Patterns:** fd858367

### Q19

- **MRE:** H1=1.55% ✗-> H2=2.63% ✓-> O1=1.82%
- **H1 Patterns:** 310134da
- **H2 Patterns:** 3aab37be,a5f39f08
- **O1 Patterns:** a5f39f08
