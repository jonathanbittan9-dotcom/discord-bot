# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Bot

Set the `DISCORD_BOT_TOKEN` environment variable, then run:

```bash
DISCORD_BOT_TOKEN=your_token_here python main.py
```

## Architecture

This is a multi-file Discord bot built with `discord.py` using the `commands.Bot` subclass pattern with slash commands via `app_commands`.

**File structure:**
- `main.py` — bot setup, data loading, moderation (`on_message`), and calls each file's `setup()` function
- `info.py` — static info commands: `/serverhelp`, `/stem`, `/steam`, `/physics`, `/biology`, `/chemistry`
- `games.py` — game commands: `/game`, `/gamble`
- `xp.py` — XP commands: `/xp`, `/shop`, `/rank`

**How files are connected:** Each file (`info.py`, `games.py`, `xp.py`) exposes a `setup(bot, ...)` function. `main.py` calls them after creating the bot:
```python
info.setup(Bot)
games.setup(Bot, user_xp)
xp_commands.setup(Bot, user_xp, user_rank)
```

**Key globals (defined in `main.py`):**
- `Bot` — the bot instance (prefix `!`, default + message_content intents)
- `GUILD_ID` — hardcoded guild object (`1468209555761532980`); all slash commands are guild-scoped
- `user_xp` — in-memory dict loaded from/saved to `xp.json`, keyed by user ID string; passed to `games.py` and `xp.py`
- `user_rank` — in-memory dict loaded from/saved to `rank.json`; passed to `xp.py`

**Slash commands registered:**
- `/serverhelp`, `/stem`, `/steam`, `/physics`, `/biology`, `/chemistry` — static info responses (`info.py`)
- `/calculator` — takes `num1`, `operator`, `num2` args (`main.py`)
- `/game` — number guessing game (1–10, 10s timeout) (`games.py`)
- `/gamble` — XP gambling via dice/coin/number sub-choices (10s message wait) (`games.py`)
- `/xp` — shows user's current XP (`xp.py`)
- `/shop` — stub, not yet implemented (`xp.py`)
- `/rank` — stub, not yet implemented (`xp.py`)

**XP persistence:** Every XP change writes the full `user_xp` dict back to `xp.json` immediately.

**Moderation:** `warn_words` and `instant_ban_words` lists exist in `on_message` (`main.py`) but the enforcement logic is commented out.

## Known Issues / Bugs

- `/shop` and `/rank` are stubs with no implementation yet
- **Moderation enforcement is disabled:** `warn_words` and `instant_ban_words` lists exist but the enforcement logic in `on_message` is commented out
