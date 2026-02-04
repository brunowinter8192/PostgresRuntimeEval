# Anhang B: Cold Cache Validierung

Dieser Anhang dokumentiert das Cold Cache Protokoll und dessen Validierung für reproduzierbare Runtime Messungen.

## B.1 Motivation

Ohne Cold Cache würden gecachte Daten die Messungen verfälschen. PostgreSQL nutzt Shared Buffers als RAM Cache für zuletzt gelesene Tables und Indexes. Zusätzlich speichert das Betriebssystem Disk Reads im OS Page Cache.

Die erste Ausführung einer Query ist langsam (Daten von Disk), folgende Ausführungen sind schnell (Daten aus Cache). Für reproduzierbare, vergleichbare Messungen muss jede Query unter identischen Bedingungen starten.

## B.2 Cold Cache Protokoll

*Bezug: cold_cache_validation/restart_docker/execute_queries.py*

Für jede Ausführung einer Query wird folgendes Protokoll durchlaufen:

1. OrbStack (Docker VM) vollständig beenden
2. System Memory Cache leeren: sudo purge
3. OrbStack neu starten
4. Docker Container starten
5. Warten bis PostgreSQL Verbindungen akzeptiert
6. Query ausführen und Zeit messen mit time.perf_counter()

Es werden keine Warm-up Queries ausgeführt. Jede Query wird isoliert ausgeführt. Die Messung erfolgt als Wall Clock Zeit.

## B.3 Validierung

### B.3.1 Vergleich zweier Cold Cache Läufe

*Bezug: Plan_Level_CC/A_01_Runtime_Variance.py*
*Daten: Plan_Level_CC/csv/A_01_comparison.csv*

Um die Konsistenz des Protokolls zu validieren, wurden zwei unabhängige Läufe mit Cold Cache über die gesamten Datasets durchgeführt (Baseline und State_1, jeweils 150 Seeds pro Template).

Als Metrik dient der Coefficient of Variation (CV) = Standardabweichung / Mittelwert × 100.

Die meisten Templates zeigen einen CV von 1.5-5%, was auf konsistente Messungen hindeutet. Wie Abbildung B.1 zeigt, liegt Q13 mit circa 10% CV deutlich über dem Durchschnitt und wird in B.4 untersucht.

*Abbildung B.1: Vergleich CV innerhalb Template*
*Quelle: Eigene Darstellung (Plan_Level_CC/csv/A_01_cv_comparison.png)*

### B.3.2 Vergleich Cold vs Warm Cache

*Bezug: Comparison_Cold_Warm/compare_cold_warm.py*
*Daten: Comparison_Cold_Warm/csv/cold_vs_warm_20251006_184219.csv*

Um den Einfluss des Cachings zu quantifizieren, wurden Messungen mit Cold Cache und Warm Cache verglichen. Der Speedup liegt zwischen 1.89x und 21.24x. Q1 weist das Minimum auf mit 1.89x (1120ms → 591ms), Q4 das Maximum mit 21.24x (1066ms → 50ms). Diese Ergebnisse bestätigen, dass Caching einen deutlichen Einfluss auf die Laufzeiten von Queries hat, was die Notwendigkeit des Protokolls für Cold Cache unterstreicht.

## B.4 Auffällige Schwankungen bei Q13

### B.4.1 Beobachtung

Q13 zeigt in beiden Validierungsläufen deutlich höhere Schwankungen in der Runtime als andere Templates:

- CV von Q13: circa 10% (Baseline: 9.79%, State_1: 11.22%)
- CV anderer Templates: circa 2-5%

Diese Anomalie ist konsistent über beide unabhängigen Läufe.

### B.4.2 Erklärungsansatz 1: Row-Count Schwankung

*Bezug: Q13_Analyse/A_01_Q13_Variance.py*
*Daten: Q13_Analyse/A_01_q13_variance.csv*

Q13 enthält eine LIKE Bedingung (o_comment not like '%special%packages%'), deren Substitution Parameter pro Seed variieren (siehe Misc/Generated_Queries/Q13/Q13_1_seed_0101000000.sql). Dies könnte zu unterschiedlichen Ergebnismengen führen und somit die erhöhten Schwankungen verursachen. Die Analyse zeigt jedoch einen CV des Row Count von nur 0.33%. Bei nahezu konstanter Ergebnismenge (6.78M - 6.86M Rows) können variable Row Counts die 10% Schwankung in der Runtime nicht erklären. Dieser Erklärungsansatz scheidet damit aus.

### B.4.3 Erklärungsansatz 2: Seq-Scan Dauer

*Bezug: Q13_Analyse/A_01_Q13_Variance.py*
*Daten: Q13_Analyse/A_01_q13_variance.csv*

Der initiale Seq Scan könnte basierend auf dem LIKE Matching Kriterium unterschiedlich lange dauern. Die Analyse der Daten auf Operator Level zeigt einen CV des Seq Scan von 3.31%. Auch dieser Wert liegt deutlich unter dem CV der Runtime des Templates von circa 10% und erklärt die beobachteten Schwankungen nicht. Der Seq Scan selbst weist geringe Schwankungen auf.

### B.4.4 Fazit

Die Ursache für die erhöhten Schwankungen in der Runtime von Q13 konnte nicht abschließend geklärt werden. Für die Evaluation der ML-Modelle zur Runtime Prediction ist dies jedoch nicht hinderlich. Erhöhte Schwankungen in einzelnen Templates spiegeln vielmehr reale Szenarien wider, mit denen ein Modell umgehen können muss.
