# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Bot

Set the `DISCORD_BOT_TOKEN` environment variable, then run:

```bash
DISCORD_BOT_TOKEN=your_token_here python main.py
```

## Architecture

This is a single-file Discord bot (`main.py`) built with `discord.py` using the `commands.Bot` subclass pattern with slash commands via `app_commands`.

**Key globals:**
- `Bot` — the bot instance (prefix `!`, default + message_content intents)
- `GUILD_ID` — hardcoded guild object (`1468209555761532980`); all slash commands are guild-scoped
- `user_xp` — in-memory dict loaded from/saved to `xp.json`, keyed by user ID string

**Slash commands registered:**
- `/serverhelp`, `/stem`, `/steam`, `/physics`, `/biology`, `/chemistry` — static info responses
- `/calculator` — takes `num1`, `operator`, `num2` args
- `/game` — number guessing game (1–10, 10s timeout)
- `/gamble` — XP gambling via dice/coin/number sub-choices (10s message wait)
- `/xp` — shows user's current XP
- `/shop` — stub, not yet implemented
- `/rank` — stub, not yet implemented (has a bug: uses `{user_rank}` instead of `f-string`)

**XP persistence:** Every XP change writes the full `user_xp` dict back to `xp.json` immediately.

**Moderation:** `warn_words` and `instant_ban_words` lists exist in `on_message` but the enforcement logic is commented out.

## Known Issues / Bugs

- `rank.json` loading uses `f` before it is defined (line 17) — will silently fall back to `{}` via the except, but the intent was to load rank data
- `/rank` command uses `{user_rank}` without an `f` prefix, so it always prints the literal string
- `/shop` and `/physics`/`biology`/`chemistry` pass `guild=GUILD_ID` as a keyword arg to the function signature instead of to the decorator — this is a parameter mismatch
- The bot token was committed in `.vscode/launch.json` — that token should be rotated
