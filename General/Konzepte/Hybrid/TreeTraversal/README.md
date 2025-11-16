# CSV Tree-Traversal Logic

## Core Principle: DFS-Order Guarantee

PostgreSQL EXPLAIN JSON liefert Query Plans als verschachtelte Baumstruktur. Die CSV ist **garantiert in Depth-First Search (DFS) Order** durch rekursives Durchlaufen der JSON `"Plans"` Arrays.

**DFS-Order bedeutet:**
```
Parent (depth=3)
├─ Child 1 (depth=4)
│  └─ Grandchild (depth=5)
└─ Child 2 (depth=4)
   └─ Grandchild (depth=5)
```

**In CSV (DFS-traversiert):**
```
Row 1: Parent       (depth=3)
Row 2: Child 1      (depth=4)
Row 3: Grandchild   (depth=5)
Row 4: Child 2      (depth=4)
Row 5: Grandchild   (depth=5)
```

---

## build_children_map(): Die Basis-Logik

**Verwendet in:**
- `bottom_up_prediction.py` (Operator-Level Runtime Prediction)
- `find_all_patterns_v2.py` (Plan-Level Pattern Extraction)

**Funktion:** Für jeden Node die direkten Children identifizieren.

```python
def build_children_map(query_ops):
    children_map = {}
    
    for idx in range(len(query_ops)):
        current_row = query_ops.iloc[idx]
        current_depth = current_row['depth']
        current_node_id = current_row['node_id']
        
        children = []
        
        for j in range(idx + 1, len(query_ops)):
            next_row = query_ops.iloc[j]
            
            if next_row['depth'] == current_depth + 1:
                children.append({
                    'node_id': next_row['node_id'],
                    'node_type': next_row['node_type'],
                    'relationship': next_row['parent_relationship']
                })
            elif next_row['depth'] <= current_depth:
                break
        
        children_map[current_node_id] = children
    
    return children_map
```

---

## Wie es funktioniert

**Für jeden Node (bei Index `idx`):**

1. Starte bei `j = idx + 1` (nächster Node nach current)
2. Iteriere durch alle folgenden Nodes
3. **Wenn `depth == current_depth + 1`:** Es ist ein direktes Child → speichern
4. **Wenn `depth <= current_depth`:** Zurück zum gleichen oder höheren Level → BREAK (Subtree beendet)
5. **Sonst:** Weiter iterieren (Grandchild oder tieferer Nachfahre)

**Kritisch:** KEIN `skip_subtree()` - wir iterieren durch ALLE Zeilen bis `depth <= current_depth`.

---

## Beispiel-Walkthrough

**CSV-Daten:**
```
idx  node_id  node_type    depth  parent_rel
0    8841     Sort         0      
1    8842     Aggregate    1      Outer
2    8843     Gather       2      Outer
3    8844     Aggregate    3      Outer
4    8845     Sort         4      Outer
5    8846     Hash Join    5      Outer
6    8847     Nested Loop  6      Outer
7    8848     Hash Join    7      Outer
8    8849     Seq Scan     8      Outer
9    8850     Hash         8      Inner
```

**build_children_map() für Hash Join (idx=5, depth=5):**

```
idx=5: Hash Join (depth=5)
  j=6: Nested Loop (depth=6)
    depth=6 == 5+1 ✓ → Child gefunden
    children.append({node_id: 8847, node_type: 'Nested Loop', relationship: 'Outer'})
  
  j=7: Hash Join (depth=7)
    depth=7 > 5+1 → Grandchild, continue
  
  j=8: Seq Scan (depth=8)
    depth=8 > 5+1 → Great-grandchild, continue
  
  j=9: Hash (depth=8)
    depth=8 > 5+1 → Great-grandchild, continue
  
  j=10: out of bounds → Ende
```

**Resultat:** `children_map[8846] = [{node_id: 8847, node_type: 'Nested Loop', relationship: 'Outer'}]`

---

## Warum KEIN skip_subtree()?

**Unterschied zur README-Version:**

**Alte Version (mit skip_subtree):**
```python
if current_depth == parent_depth + 1:
    children.append({...})
    i = skip_subtree(df, i, current_depth)  # SKIP Subtree
```

**Aktuelle Version (ohne skip_subtree):**
```python
if next_row['depth'] == current_depth + 1:
    children.append({...})
# Kein Skip → continue Iteration durch Subtree
elif next_row['depth'] <= current_depth:
    break
```

**Grund:** 
- Für Pattern-Extraktion müssen wir **jeden** Node als potenziellen Pattern-Parent betrachten
- Grandchildren können eigene Patterns bilden
- Wir wollen alle Parent-Child Patterns im kompletten Tree, nicht nur direkte Children des Root

---

## Pattern Extraction Logic

**Nach `build_children_map()` erfolgt Pattern-Extraktion:**

```python
for idx, row in query_ops.iterrows():
    parent_depth = row['depth']
    parent_type = row['node_type']
    parent_node_id = row['node_id']
    
    # Skip Root-Node (depth=0)
    if parent_depth < 1:
        continue
    
    children = children_map[parent_node_id]
    
    # Skip Leaf-Operatoren (keine Children)
    if len(children) == 0:
        continue
    
    # Filter: Mindestens ein REQUIRED_OPERATOR
    pattern_operators = {parent_type} | {child['node_type'] for child in children}
    if not pattern_operators.intersection(REQUIRED_OPERATORS):
        continue
    
    # Leaf Pattern Check
    is_leaf_pattern = any(len(children_map[child['node_id']]) == 0 for child in children)
    
    # Pattern Key erstellen
    pattern_key = format_pattern_key(parent_type, children)
```

---

## Leaf Pattern Definition

**Leaf Operator:** Node ohne Children (`len(children_map[node_id]) == 0`)

**Leaf Pattern:** Pattern wo mindestens einer der Children ein Leaf Operator ist

**Beispiele:**

```python
# Leaf Pattern (Seq Scan hat keine Children)
"Hash Join → [Hash (Inner), Seq Scan (Outer)]"

# Leaf Pattern (Hash Kind hat keine Children)
"Nested Loop → [Hash Join (Outer), Index Scan (Inner)]"

# Non-Leaf Pattern (beide Children haben eigene Children)
"Sort → Aggregate (Outer)"  # wenn Aggregate Children hat
```

---

## Pattern Key Format

**Sortierung der Children:**
1. Outer zuerst, dann Inner, dann Unknown
2. Innerhalb gleicher Relationship: alphabetisch nach node_type

**Ein Child:**
```
"Hash Join → Seq Scan (Outer)"
```

**Mehrere Children:**
```
"Hash Join → [Hash (Inner), Nested Loop (Outer)]"
```

---

## DFS-Order Garantien

**3 kritische Garantien:**

1. **Alle Children kommen direkt nach dem Parent**
   - Keine Children vor Parent
   - Keine Children nach Rückkehr zu `depth <= parent_depth`

2. **Subtrees sind zusammenhängend**
   - Alle Nachfahren zwischen Operator und nächstem Operator auf gleichem Level

3. **depth ist monoton bis Subtree-Ende**
   - Innerhalb Subtree: depth kann nur steigen oder gleich bleiben
   - Sobald `depth <= parent_depth`: Subtree beendet

**Diese Garantien ermöglichen die lineare Iteration ohne explizite Parent-Referenzen.**
