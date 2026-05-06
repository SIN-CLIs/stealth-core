# anti-learn.md — Anti-Patterns (stealth-core)

> **Zweck**: Fehlermuster die NIE WIEDER auftreten dürfen.

---

## ❌ Absolute Verbote

1. **NIE webauto-nodriver** verwenden — ABSOLUT BANNED in der Stealth Suite
2. **skylight-cli ist RE-ACTIVATED** — `skylight-cli snapshot-compact` und `skylight-cli batch` sind ERLAUBT (NEMO Architektur)
3. **NIE CDP für Navigation/Klicks** — nur JS execute/evaluate erlaubt
4. **NIE pyautogui/pynput** — Mausbewegung ist verboten
5. **NIE `pkill -f "heypiggy-bot"`** — killt ALLE Chrome-Instanzen

## ❌ Doc-System

- **NIE** Dateien ohne W-Fragen-Kommentare erstellen
- **NIE** fehlende Pflichtdateien ignorieren — Doc-Health-Check läuft

> **See SIN-CLIs/stealth-runner/learn.md for authoritative documentation (NEMO is PRIMARY as of 2026-05-06).**
