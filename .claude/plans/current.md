# Plan: Fix Single-Pattern-Constraint für echtes Hybrid

**Bead:** Thesis_Final-d0l

## Problem

Single-Pattern-Constraint ist falsch implementiert:

**Aktuell (falsch):**
- Constraint wird NACH dem Pattern-Matching geprüft
- Wenn 1 Pattern alles konsumiert → ALLE Assignments werden verworfen → Pure Operator-Prediction

**Gewollt:**
- Constraint wird WÄHREND des Pattern-Matching geprüft
- Wenn 1 Pattern alles konsumieren WÜRDE → dieses Pattern ÜBERSPRINGEN
- Nächst-kürzeres Pattern probieren
- Ziel: mindestens 1 Pattern UND mindestens 1 Operator-Node übrig

## Betroffene Dateien

### Static Hybrid_1
- `Prediction_Methods/Hybrid_1/Runtime_Prediction/03_Predict_Queries/src/tree.py`
  - `build_pattern_assignments()` (Zeile 135-161): Constraint einbauen
- `Prediction_Methods/Hybrid_1/Runtime_Prediction/03_Predict_Queries/src/prediction.py`
  - Zeile 75-77: Post-hoc Constraint ENTFERNEN

### Dynamic Hybrid_1
- `Prediction_Methods/Dynamic/Runtime_Prediction/Hybrid_1/03_Predict.py`
  - `build_pattern_assignments()` (Zeile 232-258): Constraint einbauen
  - Zeile 321-324: Post-hoc Constraint ENTFERNEN

### Dynamic Dataset
- `Prediction_Methods/Dynamic/Dataset/Dataset_Hybrid_1/00_Dry_Prediction.py`
  - `build_pattern_assignments()` (Zeile 285-311): Constraint einbauen
  - Zeile 87-90: Post-hoc Constraint ENTFERNEN

## Implementierung

In `build_pattern_assignments()` VOR dem Hinzufügen eines Pattern-Matches:

```python
computed_hash = compute_pattern_hash(node, pattern_length)
if computed_hash == pattern_hash:
    # Single-Pattern-Constraint: Skip wenn dieses Pattern ALLE Nodes konsumieren würde
    would_consume_all = (len(consumed_nodes) == 0 and len(pattern_node_ids) == len(all_nodes))
    if would_consume_all:
        continue

    consumed_nodes.update(pattern_node_ids)
    pattern_assignments[node.node_id] = pattern_hash
```

## Tasks

1. [ ] Static `tree.py`: Constraint in `build_pattern_assignments()` einbauen
2. [ ] Static `prediction.py`: Post-hoc Constraint entfernen (Zeile 75-77)
3. [ ] Dynamic `03_Predict.py`: Constraint einbauen + Post-hoc entfernen
4. [ ] Dynamic `00_Dry_Prediction.py`: Constraint einbauen + Post-hoc entfernen
5. [ ] Verifizieren: Test mit Q14 (bekannter Fall mit 7-Node-Tree)
