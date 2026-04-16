---
name: telegram-notes
description: "Runs a three-step cycle: (1) Fetch — pulls pending text and voice messages from a personal Telegram bot via the Bot API; (2) Transcribe & Classify — transcribes voice messages via Whisper, then splits all messages into ideas (thoughts, concepts, observations) or tasks (actionable items with a verb); (3) Save — appends ideas to telegram-notes/ideas.md and tasks to telegram-notes/tasks.md. Use when the user runs /telegram-notes, asks to pull telegram notes, sync telegram ideas, fetch bot messages, transcribe voice notes, or process notes from Telegram."
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(curl *)
  - Bash(mkdir *)
  - Bash(chmod *)
  - Bash(rm *)
---

# /telegram-notes — Fetch, Transcribe, and Classify Telegram Notes

Pulls pending messages from a personal Telegram bot — both **text** and
**voice** — transcribes voice via Whisper, classifies everything as an
**idea** or a **task**, and appends to dated files in `telegram-notes/`.

Arguments passed: `$ARGUMENTS`

Config lives at `~/.claude/telegram-notes.json`.

---

## Dispatch on arguments

### No args — fetch, transcribe, classify, save

Run the full pipeline (steps below).

### `configure <token> <chat_id>`

1. Parse `$ARGUMENTS`: first word is the bot token, second word is the chat ID
   (numeric, may be negative for groups).
2. Write `~/.claude/telegram-notes.json`:
   ```json
   {
     "token": "<token>",
     "chatId": "<chat_id>",
     "lastUpdateId": 0,
     "whisperKey": ""
   }
   ```
3. `chmod 600 ~/.claude/telegram-notes.json` — the token is a credential.
4. Confirm, then remind the user to set a Whisper key for voice support:
   *"Configured. For voice messages, run `/telegram-notes whisper-key <openai_key>`."*

If only one arg is given: tell the user the format is
`/telegram-notes configure <token> <chat_id>`.

### `whisper-key <key>`

1. Read `~/.claude/telegram-notes.json` (create default if missing).
2. Set `whisperKey` to the provided key.
3. Write back. `chmod 600`.
4. Confirm: *"Whisper key saved. Voice messages will now be transcribed."*

### `status`

Read `~/.claude/telegram-notes.json` and show:
- Token: set/not set (first 10 chars masked if set)
- Chat ID
- Whisper key: set/not set
- Last processed update ID
- Paths of `telegram-notes/ideas.md` and `telegram-notes/tasks.md` (exist/not)

---

## Full pipeline (no-args flow)

### Step 1 — Load config

Read `~/.claude/telegram-notes.json`.

If missing or token not set:
> "Not configured yet. Run `/telegram-notes configure <token> <chat_id>`."

Stop.

### Step 2 — Fetch updates

Call the Telegram Bot API:

```
curl -s "https://api.telegram.org/bot{TOKEN}/getUpdates?offset={lastUpdateId+1}&limit=100&timeout=0"
```

Use `offset=1` when `lastUpdateId` is `0`.

Parse the JSON response. If `ok` is false, show the error and stop.

Filter `result.result` to updates where `message.chat.id == config.chatId`
(compare as strings). For each matching message, collect:

- **Text messages**: `message.text` — store as `{ type: "text", content: "..." }`
- **Voice messages**: `message.voice.file_id` — store as `{ type: "voice", fileId: "..." }`

Skip messages that are neither (photos, stickers, etc.).

If no matching messages: *"No new messages from your chat. Nothing to process."*
Stop (do not advance lastUpdateId).

### Step 3 — Mark as read

Find the highest `update_id` across all updates in `result.result`.
Update `config.lastUpdateId` and write back to `~/.claude/telegram-notes.json`.

### Step 4 — Transcribe voice messages

For each `{ type: "voice", fileId }` item:

**4a. Get the file path:**
```
curl -s "https://api.telegram.org/bot{TOKEN}/getFile?file_id={fileId}"
```
Extract `result.file_path` from the response.

**4b. Download the audio:**
```
curl -s "https://api.telegram.org/file/bot{TOKEN}/{file_path}" -o /tmp/tg_voice_{fileId}.ogg
```

**4c. Transcribe via Whisper:**

If `config.whisperKey` is set (or `$OPENAI_API_KEY` is in the environment):
```
curl -s https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer {whisperKey}" \
  -F file=@/tmp/tg_voice_{fileId}.ogg \
  -F model=whisper-1
```
Extract `text` from the JSON response. Replace the voice item with
`{ type: "voice", content: "<transcribed text>" }`.

If local `whisper` CLI is available (check with `which whisper`):
```
whisper /tmp/tg_voice_{fileId}.ogg --model base --output_format txt --output_dir /tmp
```
Read the resulting `.txt` file as the transcription.

If neither is available: replace the item with
`{ type: "voice", content: "[voice message — no Whisper key configured]" }`.
Tell the user to run `/telegram-notes whisper-key <key>`.

**4d. Cleanup:**
```
rm /tmp/tg_voice_{fileId}.ogg
```

### Step 5 — Classify all messages

For each item (text or transcribed voice), classify the content:

- **Task** — actionable: imperative verb or action words (buy, call, fix,
  write, send, check, book, research, schedule, remind, review, create,
  prepare, update, etc.), or phrased as a to-do ("need to", "don't forget",
  "remember to").
- **Idea** — a thought, observation, concept, question, or note not directly
  actionable right now.

When ambiguous, lean **idea** unless there is a clear action verb.

For voice messages, prefix the saved content with `🎙` so it's clear it was
transcribed from audio. Preserve text verbatim.

### Step 6 — Save

Target directory: `telegram-notes/` relative to the current working directory.

```
mkdir -p telegram-notes
```

Date header: today's date as `## YYYY-MM-DD`.

**`telegram-notes/ideas.md`** — append:
```markdown
## YYYY-MM-DD

- <idea text>
- 🎙 <transcribed voice idea>
```

**`telegram-notes/tasks.md`** — append:
```markdown
## YYYY-MM-DD

- [ ] <task text>
- [ ] 🎙 <transcribed voice task>
```

Skip a file if there are no entries of that type.
If the file already has today's date header at the end, append items under it
without a duplicate header.

### Step 7 — Report

Tell the user:
- How many messages processed (text vs voice)
- How many classified as ideas vs tasks
- Which files were updated

Example:
> Fetched 5 messages (3 text, 2 voice). Saved 3 ideas → `telegram-notes/ideas.md`,
> 2 tasks → `telegram-notes/tasks.md`.

---

## Implementation notes

- Telegram voice messages are sent as `.ogg` (Opus). The Whisper API accepts
  `.ogg` directly — no conversion needed.
- Whisper key lookup order: `config.whisperKey` → `$OPENAI_API_KEY` env var →
  local `whisper` CLI → skip with placeholder.
- Never log or display tokens or API keys. Mask after the first 10 chars if
  you must show them.
- Always `chmod 600` after writing the config file.
- Clean up `/tmp/tg_voice_*.ogg` files after transcription.
- `chatId` comparison: coerce both sides to string.
