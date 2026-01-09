---
name: thesis-writing
description: Thesis prose style guide and rules. (project)
---

# Writing Skill

## Overview

Style guide for academic prose. Contains rules, prohibitions, and terminology standards.

**language is German** - examples remain in German as they demonstrate correct German academic writing.

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

### ASK THE FUCKING USER

- User fragen für Referenz-Dateien (macht das Leben leichter)
- User fragen für kritische Infos zum Verständnis
- User hat breites Wissen - nutze es

### One Question at a Time

- Eine Frage auf einmal
- Fragen bauen aufeinander auf
- Multiple Choice bevorzugen (AskUserQuestion tool)
- Nur acten wenn alles klar ist

### Any Remarks vor Exit

- IMMER "Any remarks?" fragen bevor ExitPlanMode
- User kontrolliert den Übergang

### Parallel Editing Awareness

**CRITICAL:** User edits the SAME .md file in PARALLEL!

**Before EVERY Edit - ALWAYS:**
1. RE-READ affected lines (even if recently read)
2. ONLY edit what is explicitly in the plan
3. DO NOT touch surrounding text
4. NEVER revert user changes

**On Edit error "File has been modified":**
- File was changed in parallel
- Re-read and adjust edit
- DO NOT restore old version

**Rationale:** User edits simultaneously. Every edit without prior reading risks overwriting user changes.

### Edit Workflow

**Phase 1: PLAN**
- User activates Plan Mode
- User makes changes or describes what needs to be written
- Claude updates plan iteratively
- All findings and remarks collected in plan
- When enough material: ONE edit instead of many small ones

**Phase 2: IMPLEMENT**
- Plan is executed
- Edits are done together

**Phase 3: CLEANUP**
- After each complete execution: overwrite plan file completely
- Only open actions remain in plan
- Completed tasks are removed
- No baggage from previous iterations

**Rule:** In EVERY response clearly state: "Phase: PLAN" or "Phase: IMPLEMENT"

### Technical Verification

**Rule:** Before EVERY edit - think first:
- Are the statements technically correct?
- Are file paths correct, if referenced as source? (check with `ls` or `find`)
- Are citations and years correct?
- Is terminology consistent?

**When in doubt:** Confront user IMMEDIATELY, don't guess.

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

## CRITICAL WORDING

Check EVERY sentence against these rules.

### Punctuation & Formatting

**1. No colons as sentence connectors**
- WRONG: "Die Schlussfolgerung ist zweischneidig: Einerseits..."
- WRONG: "Der Grund: Die Features..."
- RIGHT: "Die Schlussfolgerung ist zweischneidig. Einerseits..."
- RIGHT: "Der Grund ist, dass die Features..."

**2. No hyphen after parenthesis**
- WRONG: "... - die Optimizer-Costs"
- RIGHT: "... . Die Optimizer-Costs"

**3. No long parenthetical explanations**
- WRONG: "(8 Basis-Features plus Operator-Zähler)"
- RIGHT: Separate sentence or reformulate

**4. No bold in thesis prose**
- WRONG: "**Warum funktioniert das?**", "**Kernfragen**"
- RIGHT: Use `##` headers or `*italic*` for emphasis

### Language

**5. Englische Wörter in deutschem Text**

a) **Großschreibung:** Englische Substantive werden großgeschrieben (deutsche Grammatik gilt)
   - RIGHT: "die Prediction", "das Pattern", "die Query"
   - Rule: Englisch im deutschen Text = Substantiv = groß

b) **Englische Komposita:** Getrennt, NIEMALS Bindestrich
   - WRONG: "Pattern-Selection", "Length-First", "Hash-Join"
   - RIGHT: "Pattern Selection", "Length First", "Hash Join"

c) **Englisch-Deutsch:** NIEMALS Bindestrich-Mischung
   - WRONG: "Prediction-Methode", "Pattern-Auswahl", "Query-Struktur"
   - RIGHT: Komplett Englisch ODER komplett Deutsch umformulieren

d) **Deutsche Komposita:** Bindestrich nur wenn es sonst schlecht klingt
   - Normal: "Datensatzstruktur", "Vorhersagemethode" (zusammen)
   - Selten: Bindestrich nur bei Lesbarkeit

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

**13. No filenames in prose**
- WRONG: "Die Details lassen sich in `01_Feature_Selection.py` nachvollziehen."
- RIGHT: "Die Details lassen sich in der Feature Selection nachvollziehen.¹"
- Rule: Filenames belong in footnotes, not in thesis text. Use descriptive German text instead.

---

# Thesis-Specific Content

Swap this section for different projects.

---

## RAG-First for Thesis Questions

**Rule:** When user talks about "the thesis":
1. ALWAYS search RAG first (Collection: `Thesis`)
2. EXCEPTION: User explicitly refers to the current .md being edited

**Examples:**
- "How did we do this in Plan-Level?" → RAG search
- "Check line 75" → Read current .md (no RAG)
- "Is this consistent with chapter 3?" → RAG search

---

## Citations

### Two Systems

| Type | Format | Example |
|------|--------|---------|
| **Literature** (external sources) | In-text citation | Akdere und Çetintemel (2011, Abschnitt 3.4) |
| **Repository** (own code/output) | Footnote with relative path | ¹ |

### Literature Citations

**3 Varianten:**

1. **Allgemeine Referenz (ganzes Werk, kein Abschnitt):**
   `Akdere und Çetintemel (2011) begegnen diesen Fragen...`

2. **Integriert mit Abschnitt (Autor = Subjekt):**
   `Akdere und Çetintemel (2011, Abschnitt 3.4) schlagen drei Strategien vor.`

3. **Separater Hinweis (nach Aussage, KEIN Komma nach Autor!):**
   `Diese Definition folgt dem Paper (Akdere und Çetintemel 2011, Abschnitt 3.2).`

**Komma-Regel:**
- Integriert (Variante 1+2): `Autor (Jahr, Abschnitt)` ← Komma vor Abschnitt
- Separat (Variante 3): `(Autor Jahr, Abschnitt)` ← KEIN Komma nach Autor!

**"Das Paper" im Text:**
- OK wenn Zitation am Satzende folgt
- Sonst Inline-Zitation verwenden

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

### Appendix

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
| Modellierungsansatz | Modeling approach (Plan-Level, Operator-Level, Hybrid) | Paper: "modeling approach" | Vorhersagemethode, Methode, Ansatz |
| Methoden | Overarching procedures | Paper | Methodiken, Vorgehensweisen |
| MRE | Mean Relative Error | Paper | |
| Prediction | Forecast/prediction | User | Vorhersage |
| Query | Database query | User | Abfrage, Datenbankabfrage |
| Optimizer Cost Model | Cost-based prediction model of the optimizer | (Akdere und Çetintemel, 2011) | |
| Tech-Stack | Technology stack (hardware, software, config) | User | |
| Pattern Selection | Selection of patterns for model training | User | Greedy Pattern Selection |
| Plan | Tree structure of Nodes/Operators | Thesis 3.1 | Planbaum |
| Frequency | Anzahl Vorkommen eines Patterns in Trainingsdaten | User | Occurrence |

---

## Word Formatting

### Code Blocks (Appendix)

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

[PNG centered]

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

| Source | Integriert | Separat (kein Komma nach Autor!) |
|--------|------------|----------------------------------|
| Paper | Akdere und Çetintemel (2011) | (Akdere und Çetintemel 2011, Abschnitt X.X) |
| TPC-H Spec | TPC (2022) | (TPC 2022, S. X) |
| PostgreSQL Docs | PostgreSQL (2025) | (PostgreSQL 2025, S. X) |
| GitHub Repo | — | Footnotes only |

**Note:** Paper PDF has no page numbers → use section references ("Abschnitt X.X")

### Word Formatting

- Alphabetical by surname
- Hanging indent: Paragraph → Special indent → Hanging, 1.25 cm
