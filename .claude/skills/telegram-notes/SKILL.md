---
name: telegram-notes
description: "Runs a three-step cycle: (1) Fetch — pulls pending text messages from a personal Telegram bot via the Bot API; (2) Classify — splits each message into an idea (thought, concept, observation) or a task (actionable item with a verb); (3) Save — appends ideas to telegram-notes/ideas.md and tasks to telegram-notes/tasks.md. Use when the user runs /telegram-notes, asks to pull telegram notes, sync telegram ideas, fetch bot messages, or process notes from Telegram."
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(curl *)
  - Bash(mkdir *)
  - Bash(chmod *)
---

# /telegram-notes — Fetch and Classify Telegram Notes

Pulls pending messages from a personal Telegram bot, classifies each as an
**idea** or a **task**, and appends them to dated files in `telegram-notes/`.

Arguments passed: `$ARGUMENTS`

Config lives at `~/.claude/telegram-notes.json`.

---

## Dispatch on arguments

### No args — fetch, analyze, save

Run the full pipeline (steps below).

### `configure <token> <chat_id>`

1. Parse `$ARGUMENTS`: first word is the bot token, second word is the chat ID
   (numeric, may be negative for groups).
2. Write `~/.claude/telegram-notes.json`:
   ```json
   {
     "token": "<token>",
     "chatId": "<chat_id>",
     "lastUpdateId": 0
   }
   ```
3. `chmod 600 ~/.claude/telegram-notes.json` — the token is a credential.
4. Confirm: *"Configured. Run `/telegram-notes` to fetch your first batch."*

If only one arg is given: tell the user the format is
`/telegram-notes configure <token> <chat_id>` and explain where to find each.

### `status`

Read `~/.claude/telegram-notes.json` and show:
- Token: set/not set (first 10 chars masked if set)
- Chat ID
- Last processed update ID
- Paths of `telegram-notes/ideas.md` and `telegram-notes/tasks.md` (exist/not)

---

## Full pipeline (no-args flow)

### Step 1 — Load config

Read `~/.claude/telegram-notes.json`.

If missing or token not set:
> "Not configured yet. Run `/telegram-notes configure <token> <chat_id>` to
> set up. Get a token from @BotFather; get your chat ID by messaging
> @userinfobot on Telegram."

Stop.

### Step 2 — Fetch updates

Call the Telegram Bot API:

```
curl -s "https://api.telegram.org/bot{TOKEN}/getUpdates?offset={lastUpdateId+1}&limit=100&timeout=0"
```

Where `{lastUpdateId+1}` is `config.lastUpdateId + 1` (use `0` if it is `0`,
which fetches all pending).

Parse the JSON response. Check `result.ok`. If not ok, show the error and stop.

Filter `result.result` to messages where `message.chat.id == config.chatId`
(as strings or numbers — compare both). Collect `message.text` values, skipping
empty or media-only messages.

If no matching messages: *"No new messages from your chat. Nothing to process."*
Stop (do not update lastUpdateId).

### Step 3 — Mark as read

From all updates in `result.result` (not just filtered), find the highest
`update_id`. Update `config.lastUpdateId` to that value and write back to
`~/.claude/telegram-notes.json`.

This acknowledges all updates so they won't be returned again.

### Step 4 — Classify messages

For each collected message text, decide:

- **Task** — something to do: has a verb in imperative or contains action words
  (buy, call, fix, write, send, check, book, research, schedule, remind, etc.),
  or is phrased as a to-do ("need to", "don't forget", "remember to").
- **Idea** — a thought, observation, question, concept, or note that isn't
  directly actionable right now (reflections, "what if", "I wonder", quotes,
  inspirations, project concepts).

When ambiguous, lean toward **idea** unless it has a clear action verb.

Preserve the message text verbatim. Do not summarize or rewrite.

### Step 5 — Save

Target directory: `telegram-notes/` relative to the current working directory.

```
mkdir -p telegram-notes
```

Date header to use: today's date in `## YYYY-MM-DD` format.

**`telegram-notes/ideas.md`** — append:
```markdown
## YYYY-MM-DD

- <idea text>
- <idea text>
```

**`telegram-notes/tasks.md`** — append:
```markdown
## YYYY-MM-DD

- [ ] <task text>
- [ ] <task text>
```

If either file has no entries for that type, skip appending to it (don't write
an empty section).

If the file already ends with a section for today's date, append items under
it rather than adding a duplicate date header.

### Step 6 — Report

Tell the user:
- How many messages were fetched
- How many classified as ideas vs tasks
- Which files were updated

Example:
> Fetched 7 messages. Saved 4 ideas → `telegram-notes/ideas.md`,
> 3 tasks → `telegram-notes/tasks.md`.

---

## Implementation notes

- The Telegram Bot API `getUpdates` returns only *unacknowledged* updates.
  Once you advance the offset, those messages are gone from the API — the
  source of truth becomes your markdown files.
- `chatId` may be a number or a string; coerce both sides to string for
  comparison.
- If `curl` is not available, tell the user and stop.
- Never log or display the full token. If you need to show it, mask everything
  after the first 10 characters.
- The config file stores a credential — always `chmod 600` after writing.
