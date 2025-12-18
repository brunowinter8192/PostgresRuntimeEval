# Thesis Prediction Methods - Justfile
# Usage: just <recipe> [args]

set shell := ["bash", "-cu"]

# Default: show available commands
default:
    @just --list --unsorted

# ═══════════════════════════════════════════════════════════════════════════════
# GIT SHORTCUTS
# ═══════════════════════════════════════════════════════════════════════════════

# Quick commit with message
commit msg:
    git add -A
    git commit -m "{{msg}}"

# Commit with scope prefix
commit-scope scope msg:
    git add -A
    git commit -m "{{scope}}: {{msg}}"

# Show recent commits
log n="5":
    git log --oneline -{{n}}


