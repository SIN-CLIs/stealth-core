# banned.md — Verbotene Methoden (stealth-core)

> **← [stealth-runner/banned.md](https://github.com/OpenSIN-AI/stealth-runner/blob/main/banned.md) für vollständige Liste**

---

## ABSOLUT BANNED

| Tool/Methode | Grund | Ersatz |
|-------------|-------|--------|
| `webauto-nodriver` | MCP-Server, CDP-Missbrauch | NEMO (cua-driver LEGACY fallback) |
| `skylight-cli` | RE-ACTIVATED (snapshot-compact + batch) | NEMO Batch Executor |
| CDP Navigation/Klicks | Chrome blockiert, unsicher | NEMO Batch Executor |
| `pyautogui` | Mausbewegung | NEMO Batch Executor |
| `pynput` | Mausbewegung | NEMO Batch Executor |
| `pkill -f "heypiggy-bot"` | Killt USER Chrome mit! | `SessionManager.close_all()` |

## BEDINGT ERLAUBT

| Tool | Bedingung |
|------|-----------|
| CDP JS evaluate | NUR für `Runtime.evaluate()` — keine Navigation |
| macos-ax-cli | NUR für System-Scan — nicht für Klicks |

**Letztes Update**: 2026-05-06

> **See SIN-CLIs/stealth-runner/learn.md for authoritative documentation (NEMO is PRIMARY as of 2026-05-06).**
