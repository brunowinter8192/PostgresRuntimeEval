# Anhang C: SVM Parameter

Dieser Anhang dokumentiert die Konfiguration der SVM und zeigt den Einfluss einer Variation des nu Parameters.

## C.1 Verwendete Parameter

*Bezug:* `Prediction_Methods/Plan_Level_1/Runtime_Prediction/ffs_config.py`

Die SVM verwendet NuSVR aus sklearn mit folgenden Parametern:

- *nu:* 0.65
  - Untere Schranke für den Anteil der Support Vectors (scikit-learn, 2025)
  - Höherer Wert = mehr Support Vectors = glattere Anpassung

- *C:* 5.0
  - Regularisierungsparameter
  - Höherer Wert = weniger Regularisierung = engere Anpassung an Trainingsdaten

- *gamma:* 'scale'
  - Kernel-Koeffizient
  - 'scale' bedeutet: 1 / (n_features * X.var())

- *kernel:* 'rbf'
  - Radial Basis Function Kernel
  - Standard für nicht-lineare Zusammenhänge

## C.2 Skalierung

*Bezug:* `Prediction_Methods/Plan_Level_1/Runtime_Prediction/Baseline_SVM/Evaluation/A_01c_Outlier_Analysis.py`

*MaxAbsScaler* (scikit-learn, 2025) wird verwendet, da SVM normalisierte Features benötigt. MaxAbsScaler skaliert jedes Feature auf den Bereich [-1, 1] basierend auf dem absoluten Maximalwert. Im Gegensatz zu StandardScaler erhält MaxAbsScaler Sparsity, da Nullwerte Null bleiben.

## C.3 Parameter-Exploration

*Bezug:* `Misc/FFS_Comparison/Plan_Level/`

Eine explorative Variation des nu-Parameters wurde durchgeführt:

- *nu=0.65 (Baseline):* MRE 8.28%, 7 Features selektiert
- *nu=0.5:* MRE 8.42%, 7 Features selektiert

Der Unterschied beträgt ~0.14% und ist damit marginal. Die selektierten Features unterscheiden sich teilweise:

*Baseline (nu=0.65):*
initplan_count, subplan_count, Index_Scan_cnt, op_count, Seq_Scan_rows, Index_Only_Scan_cnt, jit_functions

*Nu=0.5:*
initplan_count, subplan_count, group_key_count, jit_functions, Index_Only_Scan_cnt, workers_planned, Gather_cnt

## C.4 Optimierungspotential

Eine systematische Optimierung der Hyperparameter wurde nicht durchgeführt. Mögliche Ansätze wären die Variation von C, die Variation von nu sowie die Variation von gamma.
