---
description: Structured planning workflow for clarifying user intent before implementation
argument-hint: [User Prompt]
---

# Plan Workflow

**Initial User Prompt (WHAT):** $ARGUMENTS

---

## Step Indicator Rule

**MANDATORY:** Every response in this workflow MUST start with:
`Phase X, Step Y: [Step-Name]`

---

## Phase 1: Determine Prompt Type

Analyze the user's initial prompt:

| Type | Example | Approach in Phase 2 |
|------|---------|---------------------|
| Too broad/vague | "How can I optimize MCP output?" | NARROW |
| Too narrow/specific | "Look at module X, function Y" | EXPAND |
| Seems clear | "Refactor module A to use pattern B" | VERIFY |

**ALWAYS go to Phase 2.** Even if the goal seems clear, verify understanding before proceeding.

→ Go to Phase 2

---

## Phase 2: Clarify WHAT (User Prompt)

**Goal:** Clarify WHAT the user wants to achieve in this session

### Step 1: Summarize Understanding
Summarize what I understood from the prompt

### Step 2: Ask Clarification Question
Ask MULTIPLE, but ONE QUESTION AT A TIME that narrows (if too broad) or expands (if too narrow):
- Too broad: Which component? What specific problem? Expected outcome?
- Too narrow: What should happen? How does this fit? What's the goal?

**🛑 STOP** - Wait for user answer

### Step 3: Iterate
Analyze user's answer → repeat Step 1-2 until WHAT is clear

### Step 4: WHAT Confirmation
1. Explain WHAT in my own words
    - Examples:
        - 'In this session you want to build a Leave one template out (LOTO) Modular workflow using scripts from directory X'
        - 'In this session you want to explore the Reddit API, documented in the files x y z for the purpose of building a MCP server which can search in subreddits and gives out a certain number of posts based on a certain criteria'
        - 'In this session you want to further build a web scraper optimization pipeline, goal is to carefully monitor the output and create benchmarks for the scraping' 
2. **🛑 STOP** - Ask the user if he wants to proceed to Phase 3 or if he has remarks based on the summary or if there are more things to clarify
    2.1 **CRITICAL** if the user does not clearly state in his response the he wants to proceed to Phase 3, go back to ### Step 2: Ask Clarification Question and execute again from there

→ Go to Phase 3

---

## Phase 3: Clarify HOW

**Goal:** Based on the now clear WHAT, clarify implementation details before writing Plan.md

### Step 1: Analysis
1. Based on Phase 1, now Analyse in detail the Modules or Doc- Files that you are building on or from
2. Propose 2-3 different approaches with trade-offs, for Achieving the WHAT
3. Present options conversationally with your recommendation and reasoning
4. Lead with your recommended option and explain why

5.  **🛑 STOP** - Ask the user if he is fine with that approach and wants to proceed to Phase 4
 5.1 **CRITICAL** if the user does not clearly state in his response the he wants to proceed to Phase 4, brainstorm and refine the HOW until the user clearly states he wants to proceed to Phase 4

→ Go to Phase 4

---

## Phase 4: Write Plan

### Step 1: Write Plan.md
Write the Plan.md with:
- Clear implementation steps
- Files to modify
- Expected outcome

Call ExitPlanMode

---

## Core Principles

- One question at a time, based on previous answer
- Multiple choice preferred - easier to answer than open-ended
- ALWAYS summarize understanding IN CHAT before writing Plan.md
- YAGNI ruthlessly - remove unnecessary features from all designs
- State current phase and step in every response: `Phase X, Step Y`
