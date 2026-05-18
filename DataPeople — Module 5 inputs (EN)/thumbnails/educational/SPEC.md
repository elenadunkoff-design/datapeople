# Thumbnail Template: Learning

## File
- `template.png` — ready background, 1280×720 (16:9). **The `LEARNING` pill is already baked in** to the top-left corner, **and the `DataPeople` logo into the top-right**. You don't need to overlay them yourself.
- Palette: pink background (gradient `#fde0f6` → `#fdc0ce`), brand magenta `#df1882` (logo, pill), white text inside the pill, dark navy `#1A1A3A` (for the overlay text).
- Hero: a unicorn with charts and an analytics panel on the right side of the frame — takes up roughly the right 50% of the width. The text zone is the **left half**.

## What gets overlaid
**The title, and only the title.** Large, bold, in `#1A1A3A` (dark navy neutral), no shadow. Centered vertically across the full height, left-aligned within the zone **4%–50% of the frame width** (left half). Font size is auto-tuned to the line length.

Dark navy neutral, not brand magenta — magenta is already taken by the `LEARNING` pill and the `DataPeople` logo. Repeating the color flattens the hierarchy and hurts readability.

---

## Title brief

### Length
- **Sweet spot: 30–50 characters** (including spaces). In that range the font sits around 50–78px on 3 lines — the most readable and dramatic look.
- **Minimum: 12 characters.** Anything shorter and the text balloons up (96px max) — it reads more like a "bold caption" than a thumbnail title. OK for short, punchy hooks like `HR analytics`.
- **Maximum: 55 characters.** Anything longer pushes the font under 50px and reads small in the YouTube feed. **Hard limit for the generator.**

### Structure
- A **colon** works well as a "topic: refinement" divider — it gives a natural break onto two lines. Example: `New-hire onboarding: first 30 days`.
- Long words (>14 characters) break the wrap — the model should avoid them or pick synonyms.
- No more than **3 lines** after word wrapping. If you end up with 4, the title is too long — rewrite it.

### Tone and style
- **Declarative or implicit-question (no punctuation).** "HR analytics", "New-hire onboarding: first 30 days", "What CRM actually is".
- **Don't use:** emojis, exclamation/question marks at the end, periods at the end, ALL CAPS, opening/closing quote marks.
- **OK to use:** colons, dashes, numbers, acronyms (`LLM`, `API`, `SQL`).
- **Case:** Sentence case — first letter capitalized, the rest lowercase. Not Title Case, not ALL CAPS.

### Forbidden
- The word "Learning" / "Lesson" at the start — the `LEARNING` pill is already baked into the top-left, and duplication wastes characters.
- The channel brand (`DataPeople: …`) — the logo is already in the top-right corner.
- Episode numbers (`Lesson 27`, `Video #3`).

### Good examples
- `HR analytics` (12 chars) — at the lower bound, reads as a tight term-hook
- `New-hire onboarding: first 30 days` (34 chars) — sweet spot, colon gives rhythm
- `Goal setting: keeping the team focused` (38 chars) — declarative, no question mark needed

### Bad examples
- `Learning: HR analytics` — duplicates the `LEARNING` pill
- `HOW TO ONBOARD NEW HIRES IN 30 DAYS!!!` — CAPS + exclamation marks
- `📊 HR analytics by DataPeople` — emoji + duplicates the logo

---

## Contract for the overlay script

The script takes a `title` string and **must**:
1. Check the length: 12 ≤ len(title) ≤ 55. If it doesn't fit, return an error with a specific note for re-generation — don't try to truncate.
2. Reject characters: `!`, `?`, `…` at the end; emojis; ALL-CAPS tokens longer than 3 letters (acronyms like `LLM`, `API`, `SQL` are fine).
3. Font: `HelveticaNeue.ttc` index 1 (Bold), color `#1A1A3A`, no shadow.
4. Starting size: 96px. Step down by 2px. Minimum: 36px. Max lines: 3.
5. Render zone: x ∈ [4% W, 50% W], y centered across the full height.
6. If it doesn't fit in 3 lines at any size — error, don't render.
