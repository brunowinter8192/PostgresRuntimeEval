---
description: Check if README.md and DOCS.md need updates after code changes
---

# DOCUMENTATION UPDATE CHECK

## OVERVIEW

Documentation updates are OPTIONAL - only required when changes affect the documented contract or workflow.

**Projekt-Kontext:** Standalone Pipeline ohne workflow.py.
Jedes Modul ist unabhaengig mit argparse. User orchestriert manuell.

**Two separate files, two separate concerns:**
- **README.md:** Meta-Workflow (WHAT) - Wie Module zusammenhaengen, Phasen, Shared Infrastructure
- **DOCS.md:** Modul-Details (HOW) - Workflow im Modul, was Funktionen tun, Inputs/Outputs

---

## README.md CHECK

**Purpose:** README dokumentiert den Meta-Workflow: Phasen, Module, Shared Infrastructure.

### Update Required When:

1. **Phase-Struktur aendert sich**
   - Neue Phase hinzugefuegt (z.B. Phase 4)
   - Phase-Reihenfolge aendert sich
   - Phase entfernt oder zusammengefuehrt

2. **Module aendern sich**
   - Neuer Ordner/Modul hinzugefuegt
   - Modul umbenannt oder entfernt
   - Modul-Abhaengigkeiten aendern sich

3. **Shared Infrastructure aendert sich**
   - mapping_config.py: Neue Konstanten/Funktionen
   - Neue Config-Datei hinzugefuegt
   - Bestehende Config-Exports aendern sich

4. **Dataset-Varianten aendern sich**
   - Neue Dataset-Variante (z.B. State_2)
   - Train/Test Split aendert sich
   - Feature-Anzahl aendert sich

5. **External Dependencies aendern sich**
   - Neue externe Abhaengigkeit zu anderem Workflow
   - Pfade zu externen Modellen/Daten aendern sich

### Update NOT Required When:

- Bug fixes in implementation (HOW)
- Internal refactoring
- Performance improvements
- Code reorganization without behavioral changes
- Variable/function renaming

### Decision Workflow:

1. **Read README** - Locate sections describing changed functionality
2. **Identify Impact** - Does user-visible behavior change?
3. **Decision:**
   - If workflow/usage/output changes: Update README section
   - If only internal implementation changes: Document reason for skipping
   - **If uncertain: ASK THE USER**

---

## DOCS.md CHECK

**Purpose:** DOCS dokumentiert Modul-Details: Script-Workflow, Funktionen, Inputs/Outputs.

### Update Required When:

1. **Neues Script hinzugefuegt**
   - Neues 0N_Script.py im Modul
   - Script Documentation Section hinzufuegen (Purpose, Workflow, Inputs, Outputs, Usage)

2. **Script-Workflow aendert sich**
   - Reihenfolge aendert sich (01 → 02 → 03)
   - Script entfernt oder zusammengefuehrt
   - Neue Abhaengigkeiten zwischen Scripts

3. **Argparse Parameter aendern sich**
   - Neue positional/optional Arguments
   - Argument entfernt oder umbenannt
   - Default-Werte aendern sich

4. **Output-Format aendert sich**
   - CSV Spalten aendern sich
   - Neuer Output-Ordner
   - Dateinamens-Konvention aendert sich

5. **Modul-spezifische Config aendert sich**
   - ffs_config.py: Neue Parameter
   - Konstanten aus mapping_config.py verwendet

### Update NOT Required When:

- Bug fixes in implementation (HOW)
- Internal refactoring within function body
- Performance improvements
- Code reorganization without changing responsibilities
- Variable/function renaming (internal only)
- Algorithm changes that don't affect contract

### Decision Workflow:

1. **Read DOCS** - Locate sections describing changed functions/modules
2. **Identify Impact** - Does the WHAT change, or only the HOW?
3. **Check call sequence** - Did orchestrator order change?
4. **Decision:**
   - If WHAT changed: Update DOCS section
   - If only HOW changed: Document reason for skipping update
   - **If uncertain: ASK THE USER**

---

## COMPREHENSIVE REVIEW PROTOCOL

### Step 1: Analyze Changes
List all files modified and nature of changes:
- Which files changed?
- What changed in each file?
- Are changes behavioral or implementation-only?

### Step 2: README Impact Assessment
Ask these questions:
1. Aendert sich die Phase-Struktur?
2. Werden Module hinzugefuegt/entfernt/umbenannt?
3. Aendert sich mapping_config.py oder andere Shared Infrastructure?
4. Aendern sich Dataset-Varianten oder External Dependencies?

**If YES to any: README update likely required**

### Step 3: DOCS.md Impact Assessment
Ask these questions:
1. Wurden neue Scripts (0N_xxx.py) hinzugefuegt?
2. Aendert sich der Script-Workflow (01 → 02 → 03)?
3. Aendern sich Argparse Parameter?
4. Aendert sich das Output-Format (CSV Spalten, Ordner)?
5. Aendert sich modul-spezifische Config?

**If YES to any: DOCS.md update likely required**

### Step 4: Document Decisions
For each file (README.md, DOCS.md), document:
```
FILE: README.md / DOCS.md
CHANGE: <brief description>
SECTION: <which section would be affected>
DECISION: UPDATE REQUIRED / NO UPDATE / UNCERTAIN
REASON: <why WHAT changed or why only HOW changed>
ACTION: <if update required, what to update>
RECOMMENDATION: <formulate question + YES/NO recommendation for user>
```

**IMPORTANT:**
- If DECISION is UNCERTAIN: Ask the user with your recommendation
- If DECISION is UPDATE REQUIRED: Present recommendation to user for confirmation
- If DECISION is NO UPDATE: Present recommendation to user for confirmation

---

## RECOMMENDATION FORMAT

**CRITICAL:** Present a single, consolidated recommendation.

After completing Step 4, summarize:

```
GESAMTEMPFEHLUNG:
- README.md: UPDATE / KEIN UPDATE
- DOCS.md: UPDATE / KEIN UPDATE

FRAGE (falls relevant): [Spezifische Unsicherheit]
EMPFEHLUNG: [z.B. "In DOCS.md ja, in README nein"]
BEGRUENDUNG: [Kurze Erklaerung]
```

**Rules:**
1. One consolidated overview, not per-change
2. Only formulate question if uncertain
3. User makes final decision

---

## EXECUTION CHECKLIST

After running this command, complete the following:

- [ ] List all files modified in this session
- [ ] For each change, identify if WHAT or HOW changed
- [ ] Check README.md sections affected by WHAT changes
- [ ] Check DOCS.md sections affected by WHAT changes
- [ ] Document update decisions for both files
- [ ] **Formulate recommendations for each decision**
- [ ] **Present recommendations to user:**
  - UNCERTAIN: Ask user with YES/NO recommendation
  - UPDATE REQUIRED: Confirm with user before updating
  - NO UPDATE: Document reasoning only
- [ ] Wait for user approval before making any documentation changes
- [ ] If approved, update sections as recommended
