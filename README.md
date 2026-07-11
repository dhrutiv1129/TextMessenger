# AI Text Reply Bot

**TL;DR:** A bot that watches for incoming iMessages and auto-replies in my own voice — tone and style adapt depending on who's texting me.

🚧 **Work in progress** — actively being built out, expect rough edges.

---

## Why This Project Exists

I wanted to see how far I could push an LLM to actually sound like *me* over text, not just a generic AI assistant voice, and to explore what it takes to make that adapt naturally depending on who's on the other end of the conversation.

## What It Does

Monitors incoming iMessages in real time and generates a reply written in my texting style, then sends it back automatically.

## Key Features

- **Real-time message monitoring** — watches for new incoming texts as they arrive
- **AI-generated replies** — uses an LLM to draft a response instead of a canned auto-reply
- **Personality matching** — aims to sound like my own texting voice rather than a generic assistant
- **Contact-aware tone** — designed to adjust style depending on who's texting

## How It Works

1. Watch for new incoming messages
2. Pass the message to an AI model along with context on how I'd typically respond
3. Generate a reply in my voice
4. Send the reply back automatically

## Tech Stack

- **Python**
- **OpenAI API** — reply generation
- **AppleScript / macOS Messages integration** — reading and sending iMessages

## Next Steps

Still actively shaping the personality-matching and per-contact logic. More to come.
