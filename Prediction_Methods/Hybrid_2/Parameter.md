# Hybrid_7 Parameter

## Pattern Selection Method

**Wert:** Error-based Selection

**Herleitung:**

Evaluation auf Test.csv mit Full-Training Models:

| Methode | Overall MRE |
|---------|-------------|
| Operator Only | 18.87% |
| Pattern + Size | 4.87% |
| Pattern + Frequency | 4.86% |
| **Pattern + Error** | **4.72%** |

**Entscheidung:** Error-based Selection liefert den niedrigsten MRE.

---

## Epsilon Threshold

**Wert:** 0.01% (0.0001)

**Zweck:** Minimale MRE-Verbesserung damit ein Pattern selektiert wird.

**Herleitung:**

Analyse der Delta-Verteilung ueber 3 Selection-Methoden:

| Methode | Median Delta | Min Delta |
|---------|--------------|-----------|
| Size | 0.005% | ~0 |
| Frequency | 0.002% | ~0 |
| Error | 0.009% | ~0 |

- Median liegt bei 0.002-0.009%
- Viele Patterns bringen faktisch keine Verbesserung (Delta ~0)
- Ein einzelnes Pattern liefert ~10.6% Verbesserung (Grossteil des Gewinns)

**Entscheidung:** Epsilon = 0.01% filtert Patterns die weniger als den Median beitragen, behaelt aber alle signifikanten Verbesserungen.

---

## Early-Stopping Threshold (Online)

**Wert:** TARGET_MRE = 10%

**Zweck:** Stoppe Pattern-Evaluation wenn MRE unter Threshold faellt.

**Herleitung:**

Convergence-Analyse zeigt:

| Strategie | Final MRE | 90% Verbesserung bei |
|-----------|-----------|----------------------|
| Error | 6.06% | Iteration 65 |
| Frequency | 6.15% | Iteration 103 |
| Size | 6.17% | Iteration 71 |

- Offline-Optimum liegt bei ~6%
- 90% der Verbesserung wird frueh erreicht, letzte 10% ineffizient
- 10% Threshold bietet Puffer ueber Optimum

**Anwendung:**
```
Online: Wenn aktuelle_MRE < 10% → STOPPE Pattern-Evaluation
```

**Quelle:** `Runtime_Prediction/A_02b_Convergence_Analysis.py`
**Daten:** `Evaluation/Pattern_Test_Full_*/Convergenz/A_02b_summary.csv`

---

## Occurrence vs Impact

**Erkenntnis:** Hohe Occurrence != Hoher Impact

| Occurrence | Selection Rate | Avg Delta |
|------------|----------------|-----------|
| 1-10 | 3% | 0.000008 |
| 11-50 | 4% | 0.0024 |
| **51-100** | 20% | **0.0226** |
| 101-200 | 45% | 0.0057 |
| 200+ | 100% | 0.0001 |

**Fazit:** Patterns mit 51-100 Occurrences haben hoechsten Impact. "Genug Samples" allein ist kein guter Indikator fuer Pattern-Qualitaet.

**Quelle:** `Runtime_Prediction/A_02c_Occurrence_Analysis.py`
**Daten:** `Evaluation/Pattern_Test_Full_Freq/Occurrence/A_02c_occurrence.csv`

---

## Pattern Feature Set (Online)

**Wert:** 14 Base Features (alle verwenden)

**Features:**
- `nt` - Node Type
- `nt1`, `nt2` - Child Node Types
- `np` - Number of Parallel Workers
- `plan_width` - Plan Width
- `rt1`, `rt2` - Child Runtime (actual)
- `st1`, `st2` - Child Startup Time (actual)
- `sel` - Selectivity
- `reltuples` - Relation Tuples
- `parallel_workers` - Parallel Workers
- `startup_cost`, `total_cost` - Cost Estimates

**Zweck:** Festes Feature-Set fuer Online-Pattern-Modelle (keine Zeit fuer FFS).

**Herleitung:**

Frequenzanalyse ueber alle 370 Patterns zeigt: Alle 14 Features haben aehnlich hohe Frequenz (249-391 Vorkommen). Kein klarer Cutoff - alle Features relevant.

**Quelle:** `Runtime_Prediction/A_03a_Feature_Frequency.py`
**Daten:** `Evaluation/Pattern_Feature_Set/A_03a_feature_frequency_*.csv`
