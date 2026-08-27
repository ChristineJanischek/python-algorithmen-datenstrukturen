# Einrichtungsanleitung für Schülerinnen und Schüler

Diese Anleitung erklärt Schritt für Schritt, wie du die Entwicklungsumgebung einrichtest
und mit der Arbeit am Lernagenten beginnst.

---

## Voraussetzungen

- GitHub-Konto (kostenlos unter https://github.com)
- Python 3.11 oder neuer
- Git installiert
- VS Code oder Thonny (empfohlen)

---

## Schritt 1: GitHub-Konto verwenden

Melde dich unter https://github.com an.
Falls du noch kein Konto hast, erstelle eines (kostenlos).

---

## Schritt 2: Repository klonen

**Bash / macOS / Linux:**
```bash
git clone https://github.com/DEIN-USERNAME/python-algorithmen-datenstrukturen.git
cd python-algorithmen-datenstrukturen
```

**Windows PowerShell:**
```powershell
git clone https://github.com/DEIN-USERNAME/python-algorithmen-datenstrukturen.git
cd python-algorithmen-datenstrukturen
```

> Ersetze `DEIN-USERNAME` durch deinen GitHub-Benutzernamen (nach dem Fork).

---

## Schritt 3: Python-Version prüfen

**Bash:**
```bash
python3 --version
```

**Windows PowerShell:**
```powershell
python --version
```

Es muss mindestens `Python 3.11.x` angezeigt werden.

---

## Schritt 4: Virtuelle Umgebung erstellen

**Bash:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> Die virtuelle Umgebung isoliert die Projektabhängigkeiten vom Rest des Systems.
> Du erkennst eine aktive Umgebung am `(.venv)` am Anfang der Befehlszeile.

---

## Schritt 5: Projekt installieren

**Bash und Windows PowerShell:**
```bash
pip install -e .
```

Oder ohne Installation (direkt aus dem Quellverzeichnis):
```bash
pip install pytest
```

---

## Schritt 6: Tests ausführen

```bash
pytest tests/learning_agent/
```

Alle Tests sollten bestehen (grüne Ausgabe).

---

## Schritt 7: Konsolenanwendung starten

**Bash:**
```bash
python -m learning_agent.main
```

**Alternativ:**
```bash
python src/learning_agent/main.py
```

Du wirst nach Lerngebiet, Thema, Niveau und Lernziel gefragt.
Dann kannst du Fragen stellen.

> **Kein API-Schlüssel erforderlich!** Die Anwendung funktioniert vollständig ohne externen Dienst.

---

## Schritt 8: Issue übernehmen

1. Öffne das Repository auf GitHub.
2. Klicke auf **Issues**.
3. Wähle eine Aufgabe, die noch nicht übernommen wurde.
4. Kommentiere: „Ich übernehme diese Aufgabe."
5. Lies die Beschreibung in `student_tasks/`.

---

## Schritt 9: Branch erstellen

```bash
git checkout -b feature/aufgabe-01-dein-name
```

Nutze das Format: `feature/aufgabe-NR-kurzbeschreibung`

---

## Schritt 10: Änderungen committen

```bash
git add src/learning_agent/learning/hint_levels.py
git commit -m "feat: waehle_hilfestufe implementiert (Aufgabe 01)"
```

Schreibe kleine, nachvollziehbare Commits.
Jeder Commit soll eine abgeschlossene Änderung beschreiben.

---

## Schritt 11: Branch pushen

```bash
git push origin feature/aufgabe-01-dein-name
```

---

## Schritt 12: Pull Request erstellen

1. Öffne das Repository auf GitHub.
2. Klicke auf **Pull Requests → New pull request**.
3. Wähle deinen Branch aus.
4. Schreibe eine verständliche Beschreibung.
5. Verknüpfe das Issue: `Closes #42` (Nummer anpassen).
6. Klicke auf **Create Pull Request**.

---

## Häufige Probleme

### „python" wird nicht gefunden (Windows)
Versuche `python3` oder `py` statt `python`.

### Virtuelle Umgebung wird nicht aktiviert (Windows)
Führe in PowerShell aus:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Tests schlagen fehl
Stelle sicher, dass die virtuelle Umgebung aktiviert ist und `pip install -e .` ausgeführt wurde.

### VS Code erkennt den Python-Interpreter nicht
Drücke `Ctrl+Shift+P` → `Python: Select Interpreter` → wähle `.venv`.
