# Operator-Level Targets and Metadata

## Target Variables

### actual_startup_time - Actual Startup Time (ms)

Wall-clock-Zeit bis zum ersten Output-Tupel des Operators.

**Extraktion:** `Actual Startup Time` aus EXPLAIN ANALYSE JSON

**Beispiel:** 
```json
"Actual Startup Time": 938.592
```
→ actual_startup_time = 938.592

**Wichtig:** Dies ist die echte Wall-Clock-Zeit, keine Adjustments für Loops oder Parallelität.

---

### actual_total_time - Actual Total Time (ms)

Wall-clock-Zeit bis der Operator komplett fertig ist (alle Output-Tupel produziert).

**Extraktion:** `Actual Total Time` aus EXPLAIN ANALYSE JSON

**Beispiel:**
```json
"Actual Total Time": 944.985
```
→ actual_total_time = 944.985

**Wichtig:** Dies ist die echte Wall-Clock-Zeit nach Operator-Completion. Unabhängig von `Actual Loops` - keine Multiplikation, keine Adjustments.

**Verifikation:**
- Root-Operator: actual_total_time ≈ Execution Time (minus Overhead)
- Alle Queries: actual_total_time < 3000ms

---

## Metadata

### query_file - Query Identifier

Eindeutige Identifikation der Query basierend auf dem SQL-Filename.

**Extraktion:** Filename ohne Extension aus dem SQL-File

**Beispiel:**
- SQL-File: `Q1_100_seed_812199069.sql`
- query_file = `"Q1_100_seed_812199069"`

**Format:** `Q{template}_{variant}_seed_{seed}`

---

### node_type - Operator Type

Typ des Operators im Query Plan.

**Extraktion:** `Node Type` aus EXPLAIN ANALYSE JSON

**Beispiel:**
```json
"Node Type": "Aggregate"
```
→ node_type = "Aggregate"

**Häufige Node Types:**
- Seq Scan
- Index Scan
- Hash Join
- Nested Loop
- Merge Join
- Aggregate
- Sort
- Hash
- Gather / Gather Merge
- Materialize
- Limit

---

### node_id - Global Node Identifier

Eindeutige, global hochzählende ID für jeden Operator über alle Queries hinweg.

**Extraktion:** Globaler Counter bei depth-first Traversierung aller Queries

**Traversierungsreihenfolge:**
1. Templates: Q1, Q2, ..., Q22 (ascending, skip Q15)
2. Innerhalb Template: SQL-Files sortiert nach Filename (ascending)
3. Innerhalb Query: Depth-first durch Plan-Tree

**Beispiel:**
```
Query 1 (Q1_100_seed_1.sql):
  Aggregate    → node_id = 1
  Gather Merge → node_id = 2
  Sort         → node_id = 3
  Aggregate    → node_id = 4
  Seq Scan     → node_id = 5

Query 2 (Q1_100_seed_2.sql):
  Aggregate    → node_id = 6  ← Zählt weiter
  Sort         → node_id = 7
  ...
```

**Wichtig:** 
- node_id ist über alle Queries eindeutig
- Startet bei 1
- Inkrementiert bei jedem besuchten Node
- Deterministische Reihenfolge durch sortierte Traversierung

---

### depth - Tree Depth Level

Tiefe des Operators im Query Plan Tree.

**Extraktion:** Rekursiv bei Traversierung

**Berechnung:**
- Root-Operator: depth = 0
- Jedes Child: parent_depth + 1

**Beispiel:**
```
Aggregate (depth=0)
└─ Gather Merge (depth=1)
   └─ Sort (depth=2)
      └─ Aggregate (depth=3)
         └─ Seq Scan (depth=4)
```

**InitPlans/SubPlans:** Werden als normale Children behandelt
```
Sort (depth=0)
├─ Aggregate [InitPlan 1] (depth=1)
│  └─ Gather (depth=2)
└─ Aggregate [Outer] (depth=1)
   └─ Gather (depth=2)
```

---

### parent_relationship - Parent Relationship Type

Beziehung des Operators zu seinem Parent-Operator.

**Extraktion:** `Parent Relationship` aus EXPLAIN ANALYSE JSON

**Beispiel:**
```json
"Parent Relationship": "Outer"
```
→ parent_relationship = "Outer"

**Mögliche Werte:**
- `"Outer"` - Linkes Kind bei binären Operatoren (z.B. Join Outer-Side)
- `"Inner"` - Rechtes Kind bei binären Operatoren (z.B. Join Inner-Side)
- `"InitPlan"` - InitPlan Subquery
- `"SubPlan"` - SubPlan Subquery
- `null` - Root-Operator (hat keinen Parent)

**Beispiel Hash Join:**
```
Hash Join (parent_relationship=null)
├─ Seq Scan (parent_relationship="Outer")
└─ Hash (parent_relationship="Inner")
   └─ Seq Scan (parent_relationship="Outer")
```

---

### subplan_name - Subplan Identifier

Name des SubPlans/InitPlans falls vorhanden.

**Extraktion:** `Subplan Name` aus EXPLAIN ANALYSE JSON

**Beispiel:**
```json
"Subplan Name": "InitPlan 1"
```
→ subplan_name = "InitPlan 1"

**Sonderfall:** Reguläre Operatoren → subplan_name = null

**Beispiel mit InitPlan:**
```
Sort (subplan_name=null)
├─ Aggregate (subplan_name="InitPlan 1", parent_relationship="InitPlan")
│  └─ Gather (subplan_name=null)
└─ Aggregate (subplan_name=null, parent_relationship="Outer")
```

---