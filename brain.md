# brain.md — Architektur (stealth-core)

> **← [stealth-runner/brain.md](https://github.com/OpenSIN-AI/stealth-runner/blob/main/brain.md) für Gesamtarchitektur**

---

## Repo-Architektur

- **Layer**: ⚙️ Core
- **Beschreibung**: Core Stealth Engine — Browser Fabric + CDP Layer
- **Technologie**: (Dokumentation folgt)

## Stealth Suite Integration

Dieses Repo ist Teil der Stealth Suite und MUSS:
1. NEMO Architektur (CUA-ONLY ist LEGACY/DEPRECATED) respektieren
2. Pipeline (perceive→plan→guard→execute→critique) einhalten
3. BANNED Tools vermeiden

## Abhängigkeiten

- [stealth-runner](https://github.com/OpenSIN-AI/stealth-runner) — Orchestrator
- DOC-HEALTH: `python3 /Users/jeremy/dev/stealth-runner/scripts/check_doc_health.py --repo stealth-core`

**Letztes Update**: 2026-05-06

> **See SIN-CLIs/stealth-runner/learn.md for authoritative documentation (NEMO is PRIMARY as of 2026-05-06).**
