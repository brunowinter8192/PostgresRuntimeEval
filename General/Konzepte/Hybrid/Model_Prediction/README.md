
--> ok jetzt lass uns mal rein theoretisch überlegen wie ein pattern modell funktionnieren müsste.
    --> erstmal müssten alle patterns als solche erkannt werden und es muss klar sein welche patterns leaf patterns sind und welche non leaf
--> ah ich verstehe jetzt, man geht am normalen exeplan durch. 
Hash	9
Seq Scan	10
--> haben wir dazu ein pattern modell, ja, ist das pattern modell ein leaf pattern modell, ja, check, dann ausführen

Hash	10
Seq Scan	11

--> haben wir dazu ein pattern modell, ja, ist das pattern modell ein leaf pattern modell, ja, check, dann ausführen

Nested Loop	10
Seq Scan	11
Index Scan	11

--> haben wir dazu ein pattern modell, ja, ist das pattern modell ein leaf pattern modell, ja, check, dann ausführen


Hash Join	9
Nested Loop	10
Hash	10

-->  haben wir dazu ein pattern modell, ja, ist das pattern modell ein leaf pattern modell, nein
    --> was will das modell? predictions für nested loop und hash
    --> haben wir pattern predictions für nested loop und hash die auf 10 enden, ja, dann reingeben
    
Hash Join	8
Hash Join	9
Hash	9

-->  haben wir dazu ein pattern modell, ja, ist das pattern modell ein leaf pattern modell, nein
    --> was will das modell? predictions für hash join und hash
    --> haben wir pattern predictions für hash join und hash die auf 9 enden?
    --> ja , dann reingeben
    
Hash	7
Hash Join	8 

-->  haben wir dazu ein pattern modell, ja, ist das pattern modell ein leaf pattern modell, nein
    --> was will das modell? predictions für hash join 
    --> haben wir pattern predictions für hash join die auf 8 enden?
    --> ja , dann reingeben



# Execution Plan Generation Script (04_create_execution_plan.py)

## Übersicht
Das Script erstellt einen Execution Plan für Query Plans, der festlegt ob für jeden Operator ein Pattern-Modell oder ein Operator-Level-Modell verwendet wird. Der Plan wird bottom-up von der tiefsten Depth (Leaf-Nodes) zur Root (depth 0) aufgebaut.

## Kernkonzepte

### 1. Pattern vs. Operator-Level
- **Pattern-Modelle:** Trainiert auf mehreren zusammenhängenden Operatoren (z.B. Hash → Seq Scan)
- **Operator-Modelle:** Trainiert auf einzelnen Operatoren

### 2. Leaf vs. Non-Leaf Patterns
- **Leaf Pattern:** Alle Children sind Leaf-Operatoren ohne eigene Children (z.B. Seq Scan, Index Scan)
- **Non-Leaf Pattern:** Mindestens ein Child hat selbst Children → braucht Child-Predictions

### 3. Consumed States
- **consumed_by_pattern:** Operator war PARENT in einem Pattern → keine separaten Child-Predictions für ihn erstellt
- **consumed_by_operator:** Operator wurde einzeln predicted → Child-Predictions verfügbar

**Wichtig:** Ein consumed_by_pattern Operator kann NICHT als direktes Child/Sibling in neuem Pattern verwendet werden (fehlende Predictions). Er KANN aber als Grandchild in Non-Leaf Patterns verwendet werden (Predictions werden in missing_child_features erwartet).

## Algorithmus

### Bottom-Up Iteration
Das Script iteriert von max_depth bis 0 und verarbeitet jeden Operator auf der aktuellen Depth.

### Zwei-Pass System pro Depth

**Pass 1: Pattern-Suche**
Für jeden nicht-consumed Operator auf aktueller Depth:
1. Finde Parent-Operator (depth - 1)
2. Prüfe ob Pattern zwischen aktuellem Operator und Parent existiert
3. Wenn Pattern gefunden und valide → konsumiere Parent + alle Children durch Pattern

**Pass 2: Operator-Level Fallback**  
Für jeden noch nicht-consumed Operator auf aktueller Depth:
1. Kein Pattern möglich → verwende Operator-Level Modell
2. Konsumiere Operator durch Operator-Level

### Pattern-Validierung

Ein Pattern ist valide wenn:
1. Pattern-Key in PATTERNS Liste existiert
2. Pattern in pattern_features (trained models) existiert
3. Für Non-Leaf Patterns: Alle Grandchildren (Children der Children) haben Predictions

### Critical Rules

**Regel 1: Consumed-Check**
- consumed_by_pattern Operatoren als direkte Children/Siblings: BLOCKIERT (keine Child-Predictions vorhanden)
- consumed_by_pattern Operatoren als Grandchildren: ERLAUBT (Predictions in missing_child_features erwartet)
- consumed_by_operator Operatoren: BLOCKIERT in allen Patterns (bereits final predicted)

**Beispiel:**
```
Depth 9-8: Pattern → beide consumed_by_pattern
Depth 8-7: Neuer Pattern-Versuch mit Child auf 8 (consumed_by_pattern) → BLOCKIERT
Depth 7-6: Non-Leaf Pattern mit Grandchildren auf 8 (consumed_by_pattern) → OK
```

**Regel 2: Keine Depth-Übersprünge**
- Jede Depth muss verarbeitet werden
- Zwei-Pass System stellt sicher dass alle Operatoren behandelt werden

**Regel 3: Parent-Child Beziehung**
- Pattern-Suche erfolgt immer zwischen Child (aktuelle Depth) und Parent (Depth - 1)
- find_parent_operator geht rückwärts im DataFrame und findet ersten Operator mit depth - 1

**Regel 4: Grandchildren für Non-Leaf**
- Non-Leaf Patterns brauchen Predictions der GRANDCHILDREN, nicht der direkten Children
- check_child_features_available holt Children DER Children und prüft deren Predictions

## Beispiel-Ablauf

```
Depth 11: Seq Scan, Index Scan
→ Leaf Operatoren, keine Pattern-Suche als Child
→ Pass 2: Operator-Level für beide

Depth 10: Nested Loop
→ Pass 1: Pattern 10-11? → Nested_Loop_Seq_Scan_Outer_Index_Scan_Inner
→ Leaf Pattern → Valid → consumed_by_pattern (10, 11, 11)

Depth 10: Hash  
→ Pass 1: Pattern 10-11? → Hash_Seq_Scan_Outer
→ Leaf Pattern → Valid → consumed_by_pattern (10, 11)

Depth 9: Hash Join
→ Pass 1: Pattern 9-10? → Hash_Join_Nested_Loop_Outer_Hash_Inner
→ Non-Leaf Pattern → check Grandchildren (11, 11)
→ Grandchildren consumed_by_pattern → KEINE separaten Predictions
→ Pattern NICHT valid
→ Pass 2: Operator-Level → consumed_by_operator (9)

Depth 8: Hash Join
→ Pass 1: Pattern 8-9? → Exists but Parent 9 consumed_by_operator
→ Continue
→ Pass 2: Operator-Level → consumed_by_operator (8)
```

## Output

Das Script generiert eine Markdown-Datei mit:
- Overview: Anzahl Pattern vs. Operator Steps
- Detaillierte Steps bottom-up sortiert
- Für Pattern: Name, Leaf/Non-Leaf, Operatoren, Required Features
- Für Operator: Operator, Depth, Children, Required Child Predictions

## Verwendung

```bash
python 04_create_execution_plan.py \
    <operator_dataset.csv> \
    <query_name> \
    <pattern_overview.csv> \
    <output_dir>
```

Beispiel:
```bash
python 04_create_execution_plan.py \
    /path/to/operator_dataset_cleaned.csv \
    Q9_100_seed_812199069 \
    /path/to/two_step_evaluation_overview.csv \
    execution_plans
```
