# A_ Scripts Evaluation - Online_1

## Scope

Alle 3 A_ scripts für alle 3 Strategies (Error, Size, Frequency) ausführen.

## Execution Plan

### 1. A_01a_Query_Evaluation.py (MRE per template + plot)

```bash
cd Prediction_Methods/Online_1/Runtime_Prediction

python3 A_01a_Query_Evaluation.py Evaluation/Error --output-dir Evaluation/Analysis/Error
python3 A_01a_Query_Evaluation.py Evaluation/Size --output-dir Evaluation/Analysis/Size
python3 A_01a_Query_Evaluation.py Evaluation/Frequency --output-dir Evaluation/Analysis/Frequency
```

### 2. A_02_Pattern_Analysis.py (selected vs used patterns)

```bash
python3 A_02_Pattern_Analysis.py Evaluation/Error --output-dir Evaluation/Analysis/Error
python3 A_02_Pattern_Analysis.py Evaluation/Size --output-dir Evaluation/Analysis/Size
python3 A_02_Pattern_Analysis.py Evaluation/Frequency --output-dir Evaluation/Analysis/Frequency
```

### 3. A_03_Method_Comparison.py (Hybrid_1 vs Hybrid_2 vs Online_1)

```bash
python3 A_03_Method_Comparison.py \
  ../../Hybrid_1/Runtime_Prediction/Baseline_SVM/Evaluation/approach_3 \
  ../../Hybrid_2/Runtime_Prediction/Evaluation/Size/Epsilon \
  Evaluation/Analysis/Size \
  --output-dir Evaluation/Analysis/Comparison
```

## Verified Paths

- Hybrid_1: `../../Hybrid_1/Runtime_Prediction/Baseline_SVM/Evaluation/approach_3`
- Hybrid_2: `../../Hybrid_2/Runtime_Prediction/Evaluation/Size/Epsilon`
- Online_1: `Evaluation/Analysis/Size`
