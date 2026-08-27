# Git- und GitHub-Workflow

Dieser Workflow gilt für alle Beiträge zum Lernagenten-Projekt.

---

## Grundregeln

1. **Keine direkten Änderungen auf `main`.**
2. **Ein Issue pro abgegrenzter Aufgabe.**
3. **Ein Branch pro Issue.**
4. **Kleine, nachvollziehbare Commits.**
5. **Pull Request für jede Aufgabe.**

---

## Ablauf im Überblick

```
main
 │
 │  git checkout -b feature/aufgabe-01-name
 ├──────────────────────────────► feature/aufgabe-01-name
 │                                         │
 │                                    Commits...
 │                                         │
 │                                  Pull Request
 │◄─────────────────────────────────────────
 │  Merge nach Review
```

---

## Schritt für Schritt

### 1. Issue erstellen oder übernehmen

Jede Aufgabe beginnt mit einem GitHub Issue.
Das Issue beschreibt die Aufgabe, das Ziel und die Akzeptanzkriterien.

### 2. Branch erstellen

```bash
git checkout main
git pull origin main
git checkout -b feature/aufgabe-01-hint-levels
```

**Namensformat:** `feature/aufgabe-NR-kurzbeschreibung`

Beispiele:
- `feature/aufgabe-01-hint-levels`
- `feature/aufgabe-03-error-analysis`
- `fix/test-mock-provider`

### 3. Arbeiten und committen

Committe oft – nach jeder abgeschlossenen Teilaufgabe:

```bash
git add src/learning_agent/learning/hint_levels.py
git commit -m "feat: Funktion waehle_hilfestufe hinzugefügt"
```

**Commit-Nachricht Format:**
```
typ: kurze Beschreibung (max. 72 Zeichen)
```

Typen:
- `feat:` – neue Funktion
- `fix:` – Fehlerbehebung
- `test:` – Tests hinzugefügt
- `docs:` – Dokumentation
- `refactor:` – Code umstrukturiert

### 4. Branch pushen

```bash
git push origin feature/aufgabe-01-hint-levels
```

### 5. Pull Request erstellen

1. GitHub öffnen → **Pull Requests → New pull request**
2. Branch auswählen
3. Titel: `feat: Hilfestufen-Auswahl implementiert (#1)`
4. Beschreibung: Was wurde gemacht? Was wurde getestet?
5. Verknüpfung: `Closes #1` (Issue-Nummer)
6. Reviewerin oder Reviewer zuweisen

### 6. Code Review

- Eine andere Gruppe prüft den Code.
- Feedback respektvoll geben und empfangen.
- Bei Änderungswünschen: committen und pushen (PR aktualisiert sich automatisch).

### 7. Merge

Nach erfolgreichem Review merged die Lehrkraft oder eine berechtigte Person den PR.

---

## Häufige Fehler

| Problem | Lösung |
|---------|--------|
| Direkter Commit auf `main` | Branch erstellen und PR nutzen |
| Viele unzusammenhängende Änderungen in einem Commit | Kleinere, fokussierte Commits |
| Fehlende Commit-Nachricht | Immer eine aussagekräftige Nachricht schreiben |
| PR ohne Issue-Verknüpfung | `Closes #NR` in die PR-Beschreibung |

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
