# Operator-Level Features (Static)

## Core Features from Paper (Table 2)

### np - Estimated I/O in Number of Pages

Geschätzter I/O-Aufwand in Anzahl Disk-Pages.

**Extraktion:**
- Hat Node `"Relation Name"`? → Query `SELECT relpages FROM pg_class WHERE relname = '{relation_name}'`
- Kein `"Relation Name"`? → np = 0

**Node Types mit I/O:** Seq Scan, Index Scan, Index Only Scan, Bitmap Heap Scan

**Beispiel:** Seq Scan auf lineitem → relation_name = "lineitem" → pg_class.relpages = 112600 → np = 112600

---

### nt - Estimated Number of Output Tuples

Geschätzte Anzahl Output-Tupel des Operators.

**Extraktion:** `Plan Rows` aus EXPLAIN JSON

**Beispiel:** `"Plan Rows": 6001215` → nt = 6001215

---

### nt1 - Estimated Number of Input Tuples from Left Child

Geschätzte Anzahl Input-Tupel vom linken Kind (Outer).

**Extraktion:**
```python
for child in plan_node.get("Plans", []):
    if child.get("Parent Relationship") == "Outer":
        nt1 = child.get("Plan Rows", 0)
```

**Beispiel:** Hash Join mit Outer Child (Plan Rows: 150000) → nt1 = 150000

**Sonderfall:** Keine Children oder kein Outer Child → nt1 = 0

---

### nt2 - Estimated Number of Input Tuples from Right Child

Geschätzte Anzahl Input-Tupel vom rechten Kind (Inner).

**Extraktion:**
```python
for child in plan_node.get("Plans", []):
    if child.get("Parent Relationship") == "Inner":
        nt2 = child.get("Plan Rows", 0)
```

**Beispiel:** Hash Join mit Inner Child (Plan Rows: 10000) → nt2 = 10000

**Sonderfall:** Keine Children oder kein Inner Child → nt2 = 0

---

### sel - Estimated Operator Selectivity

Selectivity = Anteil der Rows die durchgelassen werden (0 bis 1).

**Extraktion (operator-spezifisch):**

**Scans (Filter Selectivity):**
```python
if node_type in ["Seq Scan", "Index Scan", "Index Only Scan"]:
    reltuples = SELECT reltuples FROM pg_class WHERE relname = relation_name
    sel = nt / reltuples if reltuples > 0 else 0
```

**Joins (Join Selectivity):**
```python
elif node_type in ["Hash Join", "Merge Join", "Nested Loop"]:
    sel = nt / (nt1 * nt2) if (nt1 * nt2) > 0 else 0
```

**Unbinäre Operatoren (Data Reduction):**
```python
elif nt1 > 0:
    sel = nt / nt1
else:
    sel = 0
```

**Beispiel Seq Scan:** nt=1000, reltuples=1,000,000 → sel = 0.001 (0.1% gefiltert)

**Beispiel Hash Join:** nt=5000, nt1=10,000, nt2=1,000 → sel = 0.0005 (sehr selektiver Join)

---

## Zusätzliche Features aus EXPLAIN Output

### startup_cost - Estimated Startup Cost

Geschätzte Kosten bis zum ersten Output-Tupel.

**Extraktion:** `Startup Cost` aus EXPLAIN JSON

**Beispiel:** `"Startup Cost": 170311.11` → startup_cost = 170311.11

---

### total_cost - Estimated Total Cost

Geschätzte Gesamtkosten für alle Output-Tupel.

**Extraktion:** `Total Cost` aus EXPLAIN JSON

**Beispiel:** `"Total Cost": 170315.88` → total_cost = 170315.88

---

### plan_width - Estimated Average Output Tuple Width

Durchschnittliche Breite eines Output-Tupels in Bytes.

**Extraktion:** `Plan Width` aus EXPLAIN JSON

**Beispiel:** `"Plan Width": 236` → plan_width = 236

---

### reltuples - Actual Number of Tuples in Referenced Tables

Tatsächliche Anzahl Tupel in referenzierten Tabellen.

**Extraktion:**
- Hat Node `"Relation Name"`? → Query `SELECT reltuples FROM pg_class WHERE relname = '{relation_name}'`
- Kein `"Relation Name"`? → reltuples = 0

**Beispiel Scan:** Seq Scan auf lineitem → reltuples = 6,001,215

**Sonderfall:** Non-Scan-Operatoren → reltuples = 0

---

### parallel_workers - Number of Parallel Workers

Anzahl paralleler Worker-Prozesse.

**Extraktion:** `Workers Planned` aus EXPLAIN JSON (nur bei Gather/Gather Merge)

**Beispiel:** `"Workers Planned": 4` → parallel_workers = 4

**Sonderfall:** Nicht-parallele Operatoren → parallel_workers = 0
