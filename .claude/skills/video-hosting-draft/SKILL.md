# Skill: /video-hosting-draft

Generate 3 metadata variants for each video and write them to the Google Sheet as drafts.

---

## Paths

- Videos: `~/datapeople/DataPeople — Module 5 inputs (EN)/videos/`
- Transcripts: `~/datapeople/DataPeople — Module 5 inputs (EN)/transcripts/`
- Thumbnail (case): `~/datapeople/DataPeople — Module 5 inputs (EN)/thumbnails/case/template.png`
- Thumbnail (educational): `~/datapeople/DataPeople — Module 5 inputs (EN)/thumbnails/educational/template.png`

## Google Sheet

- Sheet ID: `12jd1KZ_wDrLNtalcMPcq5JXhc8KxlbHWEF83-bSdBL0`
- Tab: `Sheet1`
- Column layout (write header row first if sheet is empty):
  - A: Video File
  - B: Title 1 | C: Description 1 | D: Thumbnail 1
  - E: Title 2 | F: Description 2 | G: Thumbnail 2
  - H: Title 3 | I: Description 3 | J: Thumbnail 3
  - K: Approved Title | L: Approved Description | M: Approved Thumbnail
  - N: Status

---

## Steps

### 1. Inventory

List all `.mp4` files in the videos/ folder. List all `.txt` files in the transcripts/ folder.

### 2. For each video

**a) Read content**
- If a matching transcript exists (same clip ID, e.g. `clip_6fbd3832.mp4` → `clip_6fbd3832.txt`), read it in full.
- If no transcript exists, note "no transcript — filename only" and use the clip ID as the only signal.

**b) Classify thumbnail type**

Pick one thumbnail template per video based on content:
- `case/template.png` — use for role-play scenarios, client stories, real-world workplace demonstrations (e.g. onboarding walkthrough acting out a real scenario)
- `educational/template.png` — use for explainer content, interviews, how-to guides, concept breakdowns (e.g. "what is HR analytics", "how to resolve conflict")

When no transcript is available, default to `educational/template.png`.

**c) Generate 3 variants**

For each video, generate 3 distinct variants. Each variant has:
- **Title** — for the thumbnail overlay (also used as the video title)
- **Description** — 2–4 sentences for the video page

**Title rules (from thumbnail SPEC):**
- Length: 12–55 characters (including spaces). Sweet spot: 30–50 chars.
- Sentence case — first letter capitalized, rest lowercase.
- No emojis, no `!`, `?`, or `…` at end, no periods at end, no ALL CAPS words (acronyms like `HR`, `LLM`, `SQL` are fine).
- No "Case:" or "Learning:" at the start — these pills are already baked into the thumbnail.
- No "DataPeople" brand in title — logo is already in the thumbnail.
- No episode numbers.
- A colon works well as a divider: `Topic: refinement` or `Client: result`.
- Max 3 lines after word wrap. Avoid words longer than 14 characters.

Make the 3 variants meaningfully different:
- Variant 1: punchy/short hook
- Variant 2: descriptive with colon structure
- Variant 3: outcome-focused or question-framing

**Description rules:**
- 2–4 sentences, plain prose, no bullet points.
- Summarize what the viewer will learn or see.
- No marketing fluff ("game-changing", "revolutionary").

**d) Thumbnail path**

All 3 variants for one video use the same thumbnail template (the one you classified in step b). Set the Thumbnail column to the absolute path of that template.

### 3. Write to Google Sheet

Use `gws` to write all rows.

First, check if the sheet already has a header row. If not, write the header:
```
Video File | Title 1 | Description 1 | Thumbnail 1 | Title 2 | Description 2 | Thumbnail 2 | Title 3 | Description 3 | Thumbnail 3 | Approved Title | Approved Description | Approved Thumbnail | Status
```

Then append one row per video with:
- Column A: video filename (e.g. `clip_6fbd3832.mp4`)
- Columns B–D: Variant 1 (title, description, thumbnail path)
- Columns E–G: Variant 2
- Columns H–J: Variant 3
- Columns K–M: leave blank (filled in by human reviewer)
- Column N: `draft`

Use `gws sheets spreadsheets values append` with `valueInputOption: USER_ENTERED`.

### 4. Report

After writing, print a summary:
- How many videos processed
- Which had transcripts vs filename-only
- Which thumbnail type was assigned to each
- Confirm rows written to the sheet
