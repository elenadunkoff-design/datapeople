# Thumbnail Template: Case

## File
- `template.png` — ready background, 1280×720 (16:9). **The `DataPeople` logo is already baked in** to the top-left corner, **and the `CASE` pill into the top-right**. You don't need to overlay them yourself.
- Palette: pink background (gradient `#fdf5ea` → `#fcb2c3`), brand magenta `#c61c64` (logo, pill), white text inside the pill, dark navy `#1A1A3A` (for the overlay text).
- Hero: a unicorn on the left side of the frame — takes up roughly the left 50% of the width. The text zone is the **right half**.

## What gets overlaid
**The title, and only the title.** Large, bold, in `#1A1A3A` (dark navy neutral), no shadow. Centered vertically across the full height, left-aligned within the zone **50%–96% of the frame width** (right half). Font size is auto-tuned to the line length.

Dark navy neutral, not brand magenta — magenta is already taken by the `CASE` pill and the `DataPeople` logo. Repeating the color flattens the hierarchy and hurts readability.

---

## Title brief

### Length
- **Sweet spot: 30–50 characters** (including spaces). In that range the font sits around 60–78px on 3 lines — the most readable and dramatic look.
- **Minimum: 12 characters.** Anything shorter and the text balloons up (96px max) — it reads more like a "bold caption" than a thumbnail title. OK for short, punchy hooks.
- **Maximum: 55 characters.** Anything longer pushes the font under 50px and reads small in the YouTube feed. **Hard limit for the generator.**

### Structure
- A **colon** works well as a "client: result" divider — it gives a natural break onto two lines. Example: `LogisPro: 23% less churn in one quarter`.
- Long words (>14 characters) break the wrap — the model should avoid them or pick synonyms.
- No more than **3 lines** after word wrapping. If you end up with 4, the title is too long — rewrite it.

### Tone and style
- **Declarative or implicit-question (no punctuation).**
- **Don't use:** emojis, exclamation/question marks at the end, periods at the end, ALL CAPS, opening/closing quote marks.
- **OK to use:** colons, dashes, numbers, percentages, client and team names.
- **Case:** Sentence case — first letter capitalized, the rest lowercase. Not Title Case, not ALL CAPS.

### Forbidden
- The word "Case" at the start (`Case: …`) — the `CASE` pill is already baked into the top-right, and duplication wastes characters.
- The channel brand (`DataPeople: …`) — the logo is already in the top-left corner.
- Episode numbers in the title itself (`Case 27`, `Video #3`).

### Good examples
- `LogisPro story` (14 chars) — short, client name, reads as a tag
- `LogisPro: 23% less churn in one quarter` (39 chars) — sweet spot: client + concrete result + window
- `SteelVault Group: HR analytics for 12k staff` (44 chars) — client + service + scale

### Bad examples
- `Case: LogisPro cut churn` — duplicates the `CASE` pill
- `HOW LOGISPRO CUT CHURN !!!` — CAPS + exclamation marks
- `🚀 SteelVault and DataPeople rolled out HR analytics` — emoji + duplicates the logo

---

## Contract for the overlay script

The script takes a `title` string and **must**:
1. Check the length: 12 ≤ len(title) ≤ 55. If it doesn't fit, return an error with a specific note for re-generation — don't try to truncate.
2. Reject characters: `!`, `?`, `…` at the end; emojis; ALL-CAPS tokens longer than 3 letters (acronyms like `LLM`, `VIP`, `B2B` are fine).
3. Font: `HelveticaNeue.ttc` index 1 (Bold), color `#1A1A3A`, no shadow.
4. Starting size: 96px. Step down by 2px. Minimum: 36px. Max lines: 3.
5. Render zone: x ∈ [50% W, 96% W], y centered across the full height.
6. If it doesn't fit in 3 lines at any size — error, don't render.
