---
name: iterative-dev
description: (project)
---

# Iterative Development Skill

## Overview

This skill extends native Claude Code Plan Mode with:
- Phase indicators
- Iterative cycle structure
- Explicit file vs chat separation

Follow all native Plan Mode rules.

## Task Management Hierarchy

- **Beads** (`.beads/`) - Cross-session (weeks/months)
- **Plan-File** (`.claude/plans/`) - Within a session (hours)
- **TodoWrite** - Within an iteration (minutes)

## CRITICAL CYCLE

```
PLAN (Plan Mode) -> IMPLEMENT -> RECAP -> IMPROVE -> CLOSING -> PLAN (new cycle)
```

EVERY RESPONSE STARTS WITH A PHASE INDICATOR:
- `📋 PLAN` - Planning phase (Plan Mode active)
- `🔨 IMPLEMENT` - Implementation phase
- `🔍 RECAP` - Report phase (Plan Mode active - read-only enforced)
- `🛠️ IMPROVE` - Improvements phase
- `✅ CLOSING` - Cycle completion

**Plan Mode Usage:**
- PLAN: Native Plan Mode for implementation planning
- RECAP: Plan Mode for read-only protection (prevents accidental edits)

**Phase Detection:** System message contains "Plan mode is active" → Check context to determine if PLAN or RECAP.

---

## Planning Phase (PLAN)

### Scoping (BEFORE Exploration)

BEFORE you explore, clarify with the user:

**1. SCOPE - What is the end goal?**
→ "What should the output be?"
→ File? Script? Documentation? Analysis?

**2. SOURCES - Which files/folders are relevant?**
→ "Which folders should I look at?"
→ "Is there a reference script?"
→ User knows the structure better than you

**3. CONNECTIONS - How do the sources relate?**
→ "How does X use data from Y?"
→ Only when connections are clear: read DOCS.md

**THEN:** Explore with direction (DOCS.md → relevant scripts → structures)

### Exploration

**Documentation First (MANDATORY):**

BEFORE any action in a directory (running scripts, editing files, exploring code):
1. STOP
2. READ the DOCS.md in that directory
3. ONLY THEN proceed

This is NON-NEGOTIABLE. Skipping DOCS.md leads to: wrong paths, wrong arguments, wrong understanding.

**Path Verification (MANDATORY):**

BEFORE executing scripts with relative paths:
1. Verify paths with `ls` command
2. NEVER assume paths are correct just because script exists
3. One wrong path = entire workflow fails silently

**ASK THE FUCKING USER**
- the user knows best, ask him for reference scripts, 
	- REFERENCE SCRIPTS OR SOURCE CODE IS A GAME CHANGER, MAKES LIFE MUCH EASIER
- ask him for things which are critical to understand in order to be able to make a Plan file
	- USER HAS A BROAD KNOWLEDGE, TAKE ADVANTAGE OF IT

### Communication

| Channel | Purpose |
|---------|---------|
| Chat | Brainstorming, asking questions |
| Plan file | Key points and implementation steps |

**Proactivity (CRITICAL):**
- On skill start: Ask context questions IMMEDIATELY, don't wait
- Clarify SCOPE, SOURCES, CONNECTIONS first
- THEN explore with clear direction

**Questions:**
- One question at a time, based on previous answer, prefer multiple choice, 'askuserquestion' tool
- Questions building up on each other, one leads to another

**Plan-File:**
- Use system-provided plan file path from Plan Mode message
- ALWAYS use Write/Edit tool to update plan file
- NEVER write plan content directly in chat

### Plan File Management

**Core Principle:** Build the plan ITERATIVELY.

- **CRITICAL:**
- After each chat exchange: UPDATE the plan file
- Never write the complete plan at once
- Plan grows organically through conversation
- Only call ExitPlanMode when plan reflects current understanding

### Execution During Planning

If the planning session requires module execution to refine the plan:
1. Call ExitPlanMode
2. Execute only what is needed to refine the plan
3. Ask user to manually return to plan mode

### Before ExitPlanMode

- Plan file MUST reflect current implementation approach
- NEVER call ExitPlanMode with stale plan

---

## Implementation Phase (IMPLEMENT)

- execute whats stated in the PLAN file

### After IMPLEMENTATION

**Principle:** One phase per response. Never combine IMPLEMENT and RECAP in same response.

1. Verify all plan items were executed
2. **If open points remain:** Inform user: "Open items: [list]"
3. Ask: "Continue implementing or proceed to RECAP?"

User confirms → next response starts with 🔍 RECAP

### Ad-hoc Window

After completing plan edits, BEFORE transition to RECAP:

1. Claude: "Plan edits completed. Proceed to RECAP?"
2. User can request ad-hoc edits
3. Claude executes ad-hoc edits
4. Back to step 1 until user says "eval"

**CRITICAL:** This window is the ONLY place for ad-hoc edits.

---

## Recap Phase (RECAP)

### Phase Entry

1. Ask user: "Activate Plan Mode for RECAP (`/plan`)"
2. Wait for Plan Mode system message
3. Proceed with evaluation report (read-only enforced by Plan Mode)

### Plan File Handling

**CRITICAL:** Report OVERWRITES plan file completely.

- **Executed tasks:** Only mentioned in Execution summary
- **Open items:** Listed in "## Open Items" section → handled in CLOSING phase (Bead or discard)
- **No "ORIGINAL PLAN" section** - plan is consumed by execution

### Report

Claude writes a report that OVERWRITES the plan file:

#### 1. Execution

- What matched the Plan File, what deviated from the Plan File
- Does DOCS.md need updating? (new scripts, changed behavior, new parameters)

#### 2. Process Reflection

Explicitly analyze the planning phase across two dimensions:

##### 2.1 Efficiency

###### Questions During Planning
- Were my questions focused or scattered?
- Did we iterate too much? Could we have reached the finished plan faster?
- Did I correctly understand the user's answers?
- Did the user give insightful answers?

###### Red Flags
- More than 3 back-and-forth exchanges before stable plan
- User had to correct my assumptions multiple times
- I proposed solutions before understanding the problem
- Execution Path Errors (Most IMPLEMENT failures trace back to skipped verification in PLAN)
- User did not explicitly state what he wants, gave bad directions
- User did not understand you

###### References
- Did I explicitly ask for references early enough?
- Were the references helpful or did they lead me astray?
  - Should the references have been more granular or broader?

##### 2.2 Assumptions/Hallucinations

###### Questions
- Did I make assumptions that needed correction?
- Was the user's intent clear from the start?
- Did I verify assumptions or just proceed?

###### Categories
- **Structural:** Directory layout, file locations, naming conventions
- **Semantic:** What columns mean, what functions do, data flow
- **Behavioral:** Expected output format, error handling, edge cases

###### Rule
Every assumption should be either:
1. Verified by reading code/docs
2. Explicitly confirmed with user
3. Documented as "ASSUMPTION: ..." in plan file

#### 3. Hooks Evaluation

Evaluate current hooks for improvements:

**Questions:**
- Did a hook block something it shouldn't have?
- Did a hook allow something it should have blocked?
- Is output silencing helping or hiding problems?
- Should a recurring command pattern become a hook rule?

**Improvement Candidates:**
- Commands that failed due to missing hook rules
- Verbose output that polluted context
- Security patterns that should be blocked

**Reference:** `~/.claude/scripts/README.md`

#### 4. Improvements

Improvements are based on the execution and process reflection.

Two categories - BOTH are very important:

**Content Improvements (Code/Docs):**
- Critical: Must fix (breaks functionality, wrong behavior)
- Important: Should fix (code quality, maintainability)
- Optional: Nice to have (style, minor optimizations)

**Process Improvements (Workflow):**
- What would make the next PLAN phase more efficient?
- Which questions should I ask earlier?
- Which assumptions should I verify before proposing?

#### 5. Open Items

List any tasks from the original plan that were NOT executed.
- These will be handled in CLOSING phase (create Bead or discard)

### Collecting Improvements

After report:
1. Ask: "Any remarks?"
2. User gives remark → Add to Improvements section
3. Ask: "More remarks?"
4. Repeat until user says "done" or "improve"

### Phase Exit

1. Ensure all improvements are written to plan file
2. Call ExitPlanMode
3. Next response starts with 🛠️ IMPROVE

---

## Improve Phase (IMPROVE)

**Purpose:** Execute improvements from plan file (like IMPLEMENT, but for improvements).

**Workflow:**
1. Read plan file "## Improvements" section
2. Execute each improvement (Edit, Write, Bash)
3. Commit changes
4. Ask: "Proceed to CLOSING?"

User confirms → next response starts with ✅ CLOSING

---

## Closing Phase (CLOSING)

Only enter when user confirms (e.g., "proceed", "close", "done").

1. Update DOCS.md (if needed)
2. Handle open items:
   - For each open item, ASK: "Should [Item X] go to Beads? (cross-session)"
   - User confirms → `bd create --title "..." --body "..."`
   - User declines → Keep in plan file for next iteration
   - If no open items remain: clear plan file (overwrite with single space)
3. Ask: "New cycle or done for now?"
