---
name: meeting-analysis
description: Analyze work meeting transcripts from calls/ folder. Extracts key decisions, problems, action items with owners, recurring patterns across files, and always adds CEO-level recommendations. Saves a dated report.md.
argument-hint: "[filename or 'all']"
user-invocable: true
---

# Skill: meeting-analysis

You are analyzing work meeting transcripts for a company. Follow these steps exactly.

---

## Step 1 — Locate the calls/ folder

Look for a `calls/` folder in this order:
1. Current working directory
2. Common project roots relative to cwd (e.g., `../calls/`, subdirectories)

If `calls/` is not found, ask the user to provide the path before proceeding.

---

## Step 2 — Ask scope

Before reading any files, ask the user:

> "Should I analyze all transcript files in calls/, or a specific one? If specific, please give me the filename or path."

Wait for the answer. If they say a specific file, confirm it exists. If it doesn't, tell them and ask again.

---

## Step 3 — Read the transcripts

Read every relevant `.md` file fully before doing any analysis. Do not skim. Take note of:
- Date and participants (name + role)
- Every topic discussed, no matter how briefly
- Who said what — attribute everything

---

## Step 4 — Analyze

For **each file**, extract the following categories. Under each item record: what exactly happened or was decided, who raised or owns it, and the relevant context (client name, dollar amount, deadline, etc.).

### Categories

**Key Decisions**
Concrete conclusions the group reached — things that were agreed, approved, or confirmed. Include who made the call and any conditions attached.

**Open Questions / Problems**
Issues raised but not resolved in the meeting. Include how serious the problem is and whether an owner was assigned.

**Action Items**
Specific commitments made by named individuals. Format as: _Person → what they committed to → by when (if stated)_.

**Resolved Incidents**
Issues that were raised and confirmed resolved within the same meeting (e.g., a server incident that was already fixed). Keep these separate so they don't inflate the problems list.

---

## Step 5 — Cross-file patterns (only when analyzing all files)

After the per-file breakdowns, add a section: **Recurring Patterns Across Meetings**.

- Identify problems, themes, or tensions that appear in 3 or more meetings
- For each: name the pattern, list every meeting where it appeared with a one-line summary of how it showed up, explain why it keeps recurring based on what participants said, and quantify the impact where possible (lost deals, missed deadlines, dollar amounts)
- Rank them by business impact, highest first
- Cap at 5 patterns unless there are clearly more

---

## Step 6 — Recommendations

Always add a **Recommended Actions** section at the end — never skip this, even if not asked.

For each major problem identified (per-file or cross-file), provide recommendations in three tiers:
- **Immediate** — actions the CEO or team lead can take this week, no dependencies
- **Short-term** — actions for the coming month
- **Structural** — process or tooling changes that fix the root cause

Be specific: name the person who should own each action, reference actual details from the transcripts (client names, amounts, deadlines), and avoid generic advice.

---

## Step 7 — Save the report

- Filename: `report-YYYY-MM-DD.md` using today's date
- Save location: the project root (parent of `calls/`)
- If a file with that name already exists, append a suffix: `report-YYYY-MM-DD-2.md`, etc.
- After saving, tell the user the full path of the file created

---

## Report structure

```
# Meeting Analysis Report
**Generated:** YYYY-MM-DD
**Source:** [N file(s) analyzed — list filenames]

---

## [Filename or "All Files" if cross-analysis]

### Key Decisions
...

### Open Questions / Problems
...

### Action Items
...

### Resolved Incidents
...

---

## Recurring Patterns Across Meetings  ← only when analyzing all files
...

---

## Recommended Actions
...
```

---

## Style rules

- Every item must be attributed to a named person with their role
- Include specific details: dollar amounts, company names, dates, deadlines — never generalize away from what the transcript says
- Do not editorialize beyond what the transcript supports
- Keep summaries tight — one to three sentences per item, more only if the complexity demands it
- If something is ambiguous in the transcript, note the ambiguity rather than resolving it
