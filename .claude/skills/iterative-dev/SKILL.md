---
name: iterative-dev
description: Manages iterative workflow with plan-implement cycles. Use when user mentions "iterativer workflow".
---

# Iterative Development Skill

## Overview

This skill extends native Claude Code Plan Mode with:
- Phase indicators
- Iterative cycle structure
- Explicit file vs chat separation

Follow all native Plan Mode rules.

## Cycle

```
PLAN (Plan Mode) -> IMPLEMENT -> EVALUATE -> IMPROVE -> CLOSING -> PLAN (new cycle)
```

**Note:** Only PLAN uses Claude Code's native Plan Mode system prompt. EVALUATE, IMPROVE and CLOSING are skill-internal phases that happen after IMPLEMENT, regardless of system mode.

**Phase Detection:** System message contains "Plan mode is active" → PLAN phase is active. This is the trigger to return to PLAN from any other phase.

Every response starts with phase indicator:
- `📋 PLAN` - Planning phase (Plan Mode active)
- `🔨 IMPLEMENT` - Implementation phase
- `🔍 EVALUATE` - Report phase (not Plan Mode)
- `🛠️ IMPROVE` - Improvements phase (not Plan Mode)
- `✅ CLOSING` - Cycle completion (not Plan Mode)

---

## Planning Phase (PLAN)

### Communication

| Channel | Purpose |
|---------|---------|
| Chat | Brainstorming, asking questions |
| Plan file | Key points and implementation steps |

- One question at a time, based on previous answer, prefer multiple choice, 'aksuserquestion' tool
	- Questions building up on each other, one leads to another
- Use system-provided plan file path from Plan Mode message
- ALWAYS use Write/Edit tool to update plan file
- NEVER write plan content directly in chat

### Plan File Management

**Core Principle:** Build the plan iteratively. New plan ALWAYS overwrites old plan.

- **CRITICAL:** When starting a new plan, OVERWRITE the old plan file completely
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

### After IMPLEMENTATION

**Principle:** One phase per response. Never combine IMPLEMENT and EVALUATE in same response.

1. Verify all plan items were executed
2. **If open points remain:** Inform user: "Open items: [list]"
3. Ask: "Continue implementing or proceed to EVALUATE?"

User confirms → next response starts with 🔍 EVALUATE

---

## Evaluation Phase (EVALUATE)

**Purpose:** Evaluate the PLAN→IMPLEMENT iteration (the process), NOT the content.

**CRITICAL: NO EDITS IN EVALUATE.** Only collect and report. All edits happen in IMPROVE.

**NO:**
- Summarizing what was implemented
- Making edits or fixes (that's IMPROVE)

**YES:**
- How was the Plan Phase, did user and you were on the same page, were the user precise, did you ask questions
- How was the execution, were there flaws in the execution, misexecuted commands, unclear plan file


Claude writes a report covering:

- **Execution:** What matched the plan, what deviated
- **Process:** What could have been planned better
- **Documentation:** Does DOCS.md need updating? (new scripts, changed behavior, new parameters)
- **Improvements:** What can be improved? With reasoning. ONLY LIST, do NOT implement yet.
  - Critical: Must fix (breaks functionality, wrong behavior)
  - Important: Should fix (code quality, maintainability)
  - Optional: Nice to have (style, minor optimizations)

**COMMIT (CRITICAL):** After the report, check: Were edits made during IMPLEMENT? → Commit immediately.

After report + commit:
1. Ask: "Any remarks?"
2. Collect additional user feedback into improvement list
3. Ask: "Proceed to IMPROVE?"

User confirms → next response starts with 🛠️ IMPROVE

---

## Improve Phase (IMPROVE)

**Purpose:** Implement improvements identified in EVALUATE.

**CRITICAL:** This is where edits happen, NOT in EVALUATE.

1. Review improvement list from EVALUATE (including user feedback)
2. Implement each improvement
3. Ask: "Proceed to CLOSING?"

User confirms → next response starts with ✅ CLOSING

---

## Closing Phase (CLOSING)

Only enter when user confirms (e.g., "proceed", "close", "done").

1. Update DOCS.md (if needed)
2. Update plan file:
   - Remove completed items
   - **KEEP open items for next iteration** (deferred tasks, unverified claims, follow-up work)
   - If no open items remain: clear file (overwrite with single space)
3. Ask: "New cycle or done for now?"
