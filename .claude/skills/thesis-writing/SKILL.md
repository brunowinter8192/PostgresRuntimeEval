---
name: thesis-writing
description: Thesis prose style guide and rules. (project)
---

# Thesis Writing Skill

## Overview

Style guide for academic thesis prose. Contains rules, prohibitions, and terminology standards.

**Thesis language is German** - all writing examples remain in German.

---

## Core Principles

### Precision Transformation

User input is colloquial, imprecise, shorthand. Claude transforms into precise technical academic German.

**Examples:**
- "helfen" → "den MRE reduzieren" / "die Vorhersagegenauigkeit verbessern"
- "besser" → "niedrigere Fehlerrate" / "geringerer MRE"
- "funktioniert" → "erzielt signifikant bessere Ergebnisse"
- "das Pattern matched" → "das Pattern wird dem Subtree zugewiesen"

### Stay in User Scope

**Rule:**
- Execute ONLY what user explicitly requested
- If scope unclear → ASK before acting
- One step at a time
- Wait for user confirmation before proceeding

### Parallel Editing Awareness

**Rule:** User macht parallel Edits im MD. Vor jedem Edit:
1. Wenn User Zeilennummern nennt → diese Zeilen LESEN
2. Aktuellen Stand der Datei prüfen bevor Edit
3. Nur das editieren was explizit angefragt wurde
4. NIEMALS User-Edits rückgängig machen

**Rationale:** User editiert gleichzeitig. Ohne vorheriges Lesen werden User-Änderungen überschrieben.

### Edit Workflow

**Phase 1: PLAN**
- User aktiviert Plan Mode
- User macht Changes oder sagt was geschrieben werden soll
- Claude aktualisiert iterativ den Plan
- Alle Findings und Remarks werden im Plan gesammelt
- Wenn genug Material: EIN Edit statt viele kleine

**Phase 2: IMPLEMENT**
- Plan wird ausgeführt
- Edits werden zusammen gemacht

**Phase 3: CLEANUP**
- Nach jeder vollständigen Ausführung: Plan-Datei komplett überschreiben
- Nur offene Aktionen bleiben im Plan
- Erledigte Aufgaben werden entfernt
- Kein Ballast aus vorherigen Iterationen

**Rule:** In JEDER Response klar angeben: "Phase: PLAN" oder "Phase: IMPLEMENT"

### Fachliche Verifikation

**Rule:** Vor JEDEM Edit - Kopf einschalten:
- Sind die Aussagen fachlich korrekt?
- Stimmen Dateipfade? (mit `ls` oder `find` prüfen)
- Stimmen Zitate und Jahreszahlen?
- Stimmt die Terminologie?

**Bei Zweifel:** User SOFORT konfrontieren, nicht raten.

**Beispiele für Prüfung:**
- Pfad im Plan → `ls` ausführen, existiert die Datei?
- Paper-Zitat "(Akdere et al. 2012)" → Sources in SKILL.md prüfen → 2011, zwei Autoren
- Technische Aussage → RAG durchsuchen oder User fragen

**Pattern:** LESEN → EDITIEREN
- Vor jedem Edit: Zeile lesen
- Wenn User keine Zeile nennt → FRAGEN
- NIEMALS blind editieren

**Prohibited:**
- Running additional analyses "while we're at it"
- Checking related things "just in case"
- Suggesting next steps without being asked
- Assuming what user wants next

**Rationale:** User has full context and knows exactly what they need. Jumping ahead wastes time and pollutes context.

---

## Style Guide

### Academic Prose Standards

- Short, clear sentences (max 1.5 lines)
- Passive voice common ("wurde bestätigt", "wurden widerlegt")
- English technical terms standalone (Feature Pool, Feature Set, Operators)
- Formal register, no colloquialisms
- Technical details embedded in flowing prose (not bullet lists)

### Tense Rules

| Section | Tense | Example |
|---------|-------|---------|
| Introduction | Present | "Diese Arbeit untersucht..." |
| Methods | Past | "Es wurden Modelle trainiert..." |
| Results | Past | "Die Analyse zeigte..." |
| Discussion | Mix | Results past, conclusions present |
| Citing sources | Present | "Akdere und Çetintemel (2011) zeigen..." |

**General rule:**
- Present: What the thesis does, general truths, citing other authors
- Past: What was concretely done/measured (methods, results)

---

## Prohibitions

Check EVERY sentence against these rules.

### Punctuation & Formatting

**1. No colons as sentence connectors**
- WRONG: "Die Schlussfolgerung ist zweischneidig: Einerseits..."
- WRONG: "Der Grund: Die Features..."
- RIGHT: "Die Schlussfolgerung ist zweischneidig. Einerseits..."
- RIGHT: "Der Grund ist, dass die Features..."

**2. No hyphen after parenthesis**
- WRONG: "(`predictions.csv`) - die Optimizer-Costs"
- RIGHT: "(`predictions.csv`). Die Optimizer-Costs"

**3. No long parenthetical explanations**
- WRONG: "(8 Basis-Features plus Operator-Zähler)"
- RIGHT: Separate sentence or reformulate

**4. No bold sub-headings inside sections**
- WRONG: "**Warum funktioniert das?**"
- RIGHT: Use `##` headers or topic sentences
- EXCEPTION: Structural bold text like `**Kernfragen**` is allowed (becomes bold in Word)

### Language

**5. English only for introduced terms**

English words only if the term is in the Terminology table. Otherwise German.
- WRONG: "Operator-Typen", "Disk-Pages", "Passthrough-Ratio"
- RIGHT: "Arten von Operators", "Tech-Stack" (introduced term)

**6. Always use proper umlauts**
- WRONG: "fuehren", "wuerde", "aendern", "Ueberblick"
- RIGHT: "führen", "würde", "ändern", "Überblick"
- Rule: ä ö ü ß - never ae oe ue ss substitutes

**7. No first person pronouns**
- WRONG: "wir haben zwei Variablen", "Ich analysiere"
- RIGHT: "es liegen zwei Variablen vor", "die Analyse zeigt"
- Rule: Use passive voice or impersonal constructions

**8. No "adressieren" in any form**
- WRONG: "adressiert", "adressieren", "adressierte"
- RIGHT: "behandelt", "behebt", "löst", "zielt auf"
- Rule: Always replace with context-appropriate German verb

### Content

**9. No academic fillers**
- WRONG: "Zu beachten ist", "Es ist zu beachten"
- RIGHT: Formulate directly

**10. No text-comparison tables**
- Tables with numeric data (MRE values, counts) → OK
- Tables with text comparisons (Aspekt/Status, Ja/Nein, Beschreibung) → WRONG

WRONG:
```
| Aspekt | Paper | Diese Arbeit | Status |
|--------|-------|--------------|--------|
| FFS    | Ja    | Ja           | Bestätigt |
```

RIGHT: "FFS wurde bestätigt. Sowohl das Paper als auch diese Arbeit setzen FFS erfolgreich ein."

Rule: If a table cell contains prose/categories instead of numbers, convert to sentences.

**11. No bullet points in thesis prose**
- WRONG: `- Item`
- RIGHT: Numbered lists (`1.`, `2.`, `3.`) or flowing prose
- Rule: Avoid bullet points, numbering is acceptable (per guidelines)

**12. No code snippets in thesis**
- WRONG: `df_sorted = df.sort_values(...)` or `if len(pattern_assignments) == 1:`
- RIGHT: Explain algorithms in prose or numbered steps
- Allowed: References to .py files in parentheses, e.g., `(tree.py:158-161)`
- Rule: Code stays in repo, thesis explains what the code does

---

# Thesis-Specific Content

Swap this section for different projects.

---

## RAG Collections

See `RAG_MCP` skill for available collections and search patterns.

**Key collections for thesis:**
- `Thesis` - existing chapters (use `document=` filter for specific chapter)
- `Learning-based_Query_Performance_Modeling_and_Pred` - base paper
- `postgresql-17-US` - PostgreSQL docs
- `specification` - TPC-H spec

---

## Citations

### Two Systems

| Type | Format | Example |
|------|--------|---------|
| **Literature** (external sources) | In-text citation | (Akdere und Çetintemel, 2011, S. 5) |
| **Repository** (own code/output) | Footnote with relative path | ¹ |

### Literature Citations

**Without section** (reference to entire work):
...orientiert sich an den Methoden von Akdere und Çetintemel (2011)...

**With section** (specific passage):
- In sentence: Akdere und Çetintemel (2011, Abstract) definieren...
- Separate: ...(Akdere und Çetintemel, 2011, Abschnitt 3.2).

**Comma rule:** Comma after author only in parenthetical (separate) reference.

### Repository References (Footnotes)

Footnotes for scripts, CSVs, PNGs from the repository.

**In text:**
```
Das Script trainiert die Modelle.¹
```

**In footnote:**
```
¹ Hybrid_2/Runtime_Prediction/02_Train.py
```

**Path format:** Relative from repo root, e.g.:
- `Hybrid_2/Runtime_Prediction/02_Train.py`
- `Hybrid_2/Dataset/Operators/Training_Training/`
- `Prediction_Methods/Dynamic/Runtime_Prediction/A_01a_overview.png`

### Appendix (Anhang)

Appendix files live in repo as `.md` files and get copy-pasted into Word.

**Different rules than main text:**

| Aspect | Main Text | Appendix |
|--------|-----------|----------|
| Repo references | Footnotes | Inline `*Bezug:*` paths |
| Formatting | — | `*kursiv*` only (no `**fett**`) |

**Rationale:** Appendix = technical reference documentation, read alongside open repo. Footnotes would reduce readability.

**Source reference:** Single footnote at appendix title pointing to source file:
```
# Anhang A: Technisches Setup¹

---
¹ Misc/Setup/A_Setup.md.
```

**MD preparation:** Convert `**text**` → `*text*` before Word import (Richtlinien 3.8.2: no bold in Fließtext).

---

## Terminology

Consistent terms throughout the thesis. List is iteratively extended.

| Correct | Meaning | Source | Forbidden |
|---------|---------|--------|-----------|
| Modellierungsansatz | Ansatz zur Modellierung (Plan-Level, Operator-Level, Hybrid) | Paper: "modeling approach" | Vorhersagemethode, Methode, Ansatz |
| Methoden | Übergeordnete Vorgehensweisen | Paper | Methodiken, Vorgehensweisen |
| MRE | Mean Relative Error / Mittlerer relativer Fehler | Paper | |
| Prediction | Vorhersage | User | |
| Query | Datenbankabfrage | User | Abfrage, Datenbankabfrage |
| Optimizer Cost Model | Kostenbasiertes Vorhersagemodell des Optimizers | (Akdere und Çetintemel, 2011) | |
| Tech-Stack | Technologie-Stack (Hardware, Software, Konfiguration) | User | |
| Pattern Selection | Auswahl von Patterns für Modelltraining | User | Greedy Pattern Selection |
| Plan | Baumstruktur aus Nodes/Operators | Thesis 3.1 | Planbaum |

---

## Word Formatting

### Code Blocks

- Font: Courier New
- Size: 10pt
- Optional: light gray background

### Figures (Richtlinien 3.6)

**Structure:**
- Figure centered
- Title + number **below** figure: `Abbildung 3.1: Beschreibung`
- Source **below** title: `Quelle: Eigene Darstellung.¹⁹`
- Numbering: `Abbildung {Kapitel}.{Zähler}` (independent from tables)

**Formatting (all centered):**
- Font: Times, 10pt, italic
- Title: `Abbildung 3.1: Beschreibender Titel`
- Source: `Quelle: Eigene Darstellung.` + footnote

**Requirements:**
- Every figure must be mentioned in text before it appears
- Reference: "siehe Abbildung 3.1" or "Abbildung 3.1 zeigt..."

**Example in Word:**

[PNG zentriert]

*Abbildung 3.1: MRE pro Template bei Plan-Level Modellierung*

*Quelle: Eigene Darstellung.*¹⁹

**Note:** Footnote ¹⁹ points to repo PNG path.

---

### Tables (Richtlinien 3.6)

**Structure:**
- Title + number **above** table: `Tabelle 3.1: Beschreibung`
- Source **below** table: `Quelle: Eigene Darstellung.²⁰`
- Numbering: `Tabelle {Kapitel}.{Zähler}` (independent from figures)

**Formatting (all centered):**
- Font: Times, 10pt, italic
- Title: `Tabelle 3.1: Beschreibender Titel`
- Source: `Quelle: Eigene Darstellung.` + footnote

**Requirements:**
- Every table must be mentioned and explained in text
- Place table in immediate proximity to text reference

**Difference to Figures:**
- Figures: Title **below**
- Tables: Title **above**

**Example in Word:**

*Tabelle 3.1: MRE der Templates mit der schlechtesten Performance*

| Rank | Template | Mean Actual | Mean Predicted | MRE   |
|------|----------|-------------|----------------|-------|
| 1    | Q18      | 3163ms      | 1590ms         | 49.7% |
| 2    | Q11      | 211ms       | 241ms          | 14.2% |
| 3    | Q16      | 200ms       | 227ms          | 13.7% |

*Quelle: Eigene Darstellung.*²⁰

**Note:** Footnote ²⁰ points to repo CSV path.

---

## Sources

PDF sources used throughout thesis. Internet sources managed in Word bibliography.

### PDF Sources (in RAG)

```
Akdere, M. und Çetintemel, U. (2011). Learning-based Query Performance
    Modeling and Prediction. CS-11-01. Brown University.
The PostgreSQL Global Development Group. (2025). PostgreSQL 17 Documentation.
TPC. (2022). TPC Benchmark H (TPC-H) Standard Specification. Revision 3.0.1.
```

### Short Citations

| Source | In sentence | Separate |
|--------|-------------|----------|
| Paper | Akdere und Çetintemel (2011) | (Akdere und Çetintemel, 2011, Abschnitt X.X) |
| TPC-H Spec | TPC (2022) | (TPC, 2022, S. X) |
| PostgreSQL Docs | PostgreSQL (2025) | (PostgreSQL, 2025, S. X) |
| GitHub Repo | — | Footnotes only |

**Note:** Paper PDF has no page numbers → use section references ("Abschnitt X.X")

### Word Formatting

- Alphabetical by surname
- Hanging indent: Paragraph → Special indent → Hanging, 1.25 cm
