# For the coding agent

Read README.md (build, deploy, editing) and HANDOFF.md (state, open items, legal) before touching anything.

- `build_pages.py` is the source of truth. Edit the Python, run `python build_pages.py`, never edit the HTML.
- Verify before saying done: preview over HTTP at desktop width and with real mobile emulation at 390 px. After a deploy, wait a few minutes before concluding a change did not land.
- The rules in README under "Rules from the owners" are not yours to relax. Neither is anything in HANDOFF under "Legal pages".
- `STATS_KEY` lives only in the Cloudflare secret store. Never write it to a file, a commit or a message. Never paste signup addresses anywhere.
- Deploy only when the owners ask. Report the version id and what you verified live.
