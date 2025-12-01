# LOTO: Leave-One-Template-Out Evaluation

## Konzept

LOTO (Leave-One-Template-Out) ist das **Dynamic Workload** Szenario aus dem Paper.
Es testet, wie gut das Hybrid-Modell auf **komplett ungesehene Query-Templates** generalisiert.

## Split

```
Alle 14 TPC-H Templates: Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q18, Q19

Fuer jedes Template T:
    TRAINING = 13 Templates (alle ausser T)
    TEST = 1 Template (nur T)

    -> 14 separate Evaluationen
```

## Unterschied zu 5-Fold CV (Static Workload)

| Aspekt | 5-Fold CV (Static) | LOTO (Dynamic) |
|--------|-------------------|----------------|
| Split | Zufaellig ueber alle Templates | Template-basiert |
| Test sieht | Queries aus bekannten Templates | Queries aus unbekanntem Template |
| Fragestellung | Wie gut auf bekannten Strukturen? | Wie gut auf NEUEN Strukturen? |
| Paper Section | 5.3 | 5.4 |

## Paper-Zitat (Section 5.4)

> "For this experiment, we used the 12 templates shown in Figure 9, with 11 of them used in training and the remaining for testing. That is for each template we build and test separate prediction models based on the training data of the other templates."

## Warum LOTO wichtig ist

In der Praxis kommen neue Queries, die das Modell noch nie gesehen hat. LOTO simuliert dieses Szenario:
- Training kennt Template Q1 nicht
- Test besteht nur aus Q1-Queries
- Kann das Modell trotzdem gut predicten?

Das Paper zeigt: **Size-Based** und **Online** performen hier am besten, weil kleine Patterns und on-the-fly gebaute Patterns besser auf neue Strukturen generalisieren.

## Unterordner

| Ordner | Strategie | Beschreibung |
|--------|-----------|--------------|
| Hybrid_7/ | Size-Based | Kleinere Patterns zuerst (Offline) |
| Hybrid_8/ | Error-Based | Hoechster freq x error zuerst (Offline) |
| Hybrid_9/ | Frequency-Based | Haeufigste zuerst (Offline) |
| Online/ | Online Building | Patterns zur Laufzeit fuer spezifische Query gebaut |

## Paper-Referenz

`/Users/brunowinter2000/Documents/Thesis/Thesis_Final/Misc/Learning-based_Query_Performance_Modeling_and_Pred.md`

Akdere et al., "Learning-based Query Performance Modeling and Prediction", ICDE 2012
