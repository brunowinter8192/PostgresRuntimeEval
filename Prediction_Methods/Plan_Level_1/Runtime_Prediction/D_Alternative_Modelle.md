# Anhang D: Alternative Modelle (Random Forest, XGBoost)

Neben SVM wurden Random Forest und XGBoost als alternative FFS-Modelle getestet.

## D.1 Ergebnisübersicht

*Daten:*
- `Prediction_Methods/Plan_Level_1/Runtime_Prediction/Baseline_SVM/SVM/01_ffs_progress.csv`
- `Prediction_Methods/Plan_Level_1/Runtime_Prediction/Baseline_RandomForest/Random_Forest/01_ffs_progress.csv`
- `Prediction_Methods/Plan_Level_1/Runtime_Prediction/Baseline_XGBoost/XGBoost/01_ffs_progress.csv`

*SVM:* MRE 8.28%, 7 Features
*Random Forest:* MRE 2.66%, 8 Features
*XGBoost:* MRE 2.68%, 4 Features

Random Forest und XGBoost erzielen einen deutlich niedrigeren MRE als SVM in der Plan-Level Betrachtung.. Dennoch wurde SVM als Baseline verwendet, um Vergleichbarkeit mit dem Paper (Akdere et al. 2012) zu gewährleisten.

## D.2 Dateien

Die vollständigen Ergebnisse sind im Repository nachvollziehbar:

- *Random Forest:* `Prediction_Methods/Plan_Level_1/Runtime_Prediction/Baseline_RandomForest/`
- *XGBoost:* `Prediction_Methods/Plan_Level_1/Runtime_Prediction/Baseline_XGBoost/`

Jeder Ordner enthält:

- `FFS/` - Forward Feature Selection Ergebnisse
- `{Model}/` - Trainierte Modelle und Predictions
- `Evaluation/` - Evaluationsmetriken und Visualisierungen
