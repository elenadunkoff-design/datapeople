# Skill: /video-hosting-draft

Generate 3 metadata variants for each video and write them to the Google Sheet as drafts.

---

## Paths

- Videos: `~/datapeople/DataPeople — Module 5 inputs (EN)/videos/`
- Transcripts: `~/datapeople/DataPeople — Module 5 inputs (EN)/transcripts/`
- Thumbnail template (case): `~/datapeople/DataPeople — Module 5 inputs (EN)/thumbnails/case/template.png`
- Thumbnail template (educational): `~/datapeople/DataPeople — Module 5 inputs (EN)/thumbnails/educational/template.png`
- Rendered thumbnails output: `~/datapeople/DataPeople — Module 5 inputs (EN)/thumbnails/rendered/`

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

**d) Render 3 distinct thumbnails**

Each variant gets its own rendered PNG with that variant's title overlaid on the template.
Run the following Python script (save to `/tmp/render_thumbnails.py` and execute with `python3`).
Populate `VIDEOS` with the list of `(clip_id, thumb_type, [(title, desc), ...])` tuples you generated in step (c).

```python
import os
from PIL import Image, ImageDraw, ImageFont

BASE      = os.path.expanduser("~/datapeople/DataPeople — Module 5 inputs (EN)")
FONT_PATH = "/System/Library/Fonts/HelveticaNeue.ttc"
COLOR     = (26, 26, 58)   # #1A1A3A
OUT_DIR   = f"{BASE}/thumbnails/rendered"
TEMPLATES = {
    "case":        f"{BASE}/thumbnails/case/template.png",
    "educational": f"{BASE}/thumbnails/educational/template.png",
}
# x zone as fraction of image width: (start, end)
ZONES = {
    "case":        (0.50, 0.96),
    "educational": (0.04, 0.50),
}

os.makedirs(OUT_DIR, exist_ok=True)

def render(template_path, title, out_path, thumb_type):
    img  = Image.open(template_path).convert("RGBA")
    W, H = img.size
    draw = ImageDraw.Draw(img)
    x0   = int(W * ZONES[thumb_type][0])
    x1   = int(W * ZONES[thumb_type][1])
    zone_w = x1 - x0

    # Auto-size: start at 96px, step down by 2px until title fits in ≤3 lines
    font, lines = None, []
    for size in range(96, 34, -2):
        font  = ImageFont.truetype(FONT_PATH, size, index=1)
        words = title.split()
        lines, line = [], []
        for w in words:
            test = " ".join(line + [w])
            if draw.textbbox((0, 0), test, font=font)[2] > zone_w and line:
                lines.append(" ".join(line))
                line = [w]
            else:
                line.append(w)
        if line:
            lines.append(" ".join(line))
        if len(lines) <= 3:
            break
    else:
        raise ValueError(f"Title too long to fit in 3 lines: {title!r}")

    line_h  = draw.textbbox((0, 0), "Ag", font=font)[3]
    spacing = int(line_h * 0.25)
    total_h = len(lines) * line_h + (len(lines) - 1) * spacing
    y = (H - total_h) // 2

    for ln in lines:
        draw.text((x0, y), ln, font=font, fill=COLOR)
        y += line_h + spacing

    img.convert("RGB").save(out_path, "PNG")
    return out_path

# ── Populate this list from step (c) ──
# VIDEOS = [
#   ("clip_6fbd3832", "case", [
#     ("Onboarding done right", "description 1..."),
#     ("New hire day one: what good looks like", "description 2..."),
#     ("Two onboarding stories: spot the difference", "description 3..."),
#   ]),
#   ...
# ]

rendered = {}   # clip_id -> [path_v1, path_v2, path_v3]
for clip_id, thumb_type, variants in VIDEOS:
    rendered[clip_id] = []
    for i, (title, _) in enumerate(variants, 1):
        out_path = f"{OUT_DIR}/{clip_id}_v{i}.png"
        render(TEMPLATES[thumb_type], title, out_path, thumb_type)
        rendered[clip_id].append(out_path)
        print(f"  {clip_id} v{i}: {title!r} → {out_path}")
```

After running, `rendered[clip_id][0..2]` holds the three PNG paths.
Set Thumbnail 1/2/3 in the sheet row to `rendered[clip_id][0]`, `[1]`, `[2]` respectively.

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
