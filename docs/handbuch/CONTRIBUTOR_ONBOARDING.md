# Contributor Onboarding Anleitung

**Dokumentstand:** 2026-02-06

---

## 🎯 Warum diese Checkliste?

Dieses Repository ist ein **Lehr- und Lernmaterial-Verwaltungssystem**. Bevor du neue Inhalte hinzufügst oder das System erweiterst, musst du folgende Grundprinzipien verstehen:

1. **Versionskontrolle** - Damit Änderungen sicher und nachverfolgbar sind
2. **Branching & Backup** - Damit es immer einen stabilen Zustand gibt
3. **Content Management** - Damit Inhalte strukturiert und automatisiert verwaltet werden
4. **Struktogramme** - Das ist eine Abitur-Anforderung in Baden-Württemberg
5. **Zusammenarbeit** - Damit mehrere Personen ohne Konflikte arbeiten können

Diese Checkliste stellt sicher, dass **alle Contributor** diese Grundlagen verstehen, **bevor** sie zum ersten Mal Code oder Inhalte committen.

---

## 📋 Schritt-für-Schritt Übersicht

| **Todo** | **Beschreibung** | **Link zu Anleitung** | **Warum?** |
|---------|---------|---------|---------|
| 1️⃣ Git Basics | Git und unser Branching-Modell verstehen | [Siehe unten: Set 1](#set-1-git--versionskontrolle) | Damit Änderungen nicht in Konflikt kommen |
| 2️⃣ Environment Setup | Python, Tools lokal installieren & testen | [DEVELOPEMENT.MD](DEVELOPEMENT.MD) | Zum Lokaltesten vor dem Push |
| 3️⃣ Backup Strategy | Unser Tag/Release/Hotfix-System verstehen | [BACKUP_STRATEGY.md](BACKUP_STRATEGY.md) | Damit es immer einen stabilen Rollback gibt |
| 4️⃣ Struktogramme | BW-Abitur-Standard für Programmlogik | [STRUKTOGRAMM_GUIDE.md](STRUKTOGRAMM_GUIDE.md) | Pflichtanforderung für Aufgaben |
| 5️⃣ Content Management | Wie man Aufgaben/Infos/Lösungen erstellt | [ELEARNING_TEMPLATE_GUIDE.md](ELEARNING_TEMPLATE_GUIDE.md) | Das ist unser zentrales System |
| 6️⃣ First Contribution | Dein erster Workflow: Branch → Edit → Commit → Test → PR | [Siehe unten: Set 2](#set-2-dein-erster-contribution) | Praktische Übung aller vorherigen Punkte |

---

## ✅ Interaktive Checklisten

### Set 1: Git & Versionskontrolle

**Lernziel:** Du verstehst unser Git-Workflow und kannst sicher mit Branches arbeiten.

- [ ] Ich habe `git --version` aus der Kommandozeile aufgerufen
- [ ] Ich verstehe, was ein **Branch** ist (unabhängiges Arbeiten)
- [ ] Ich verstehe, was ein **Commit** ist (Snapshot der Änderungen)
- [ ] Ich verstehe, was ein **Tag** ist (Labels für stabile Versionen)
- [ ] Ich habe die [BACKUP_STRATEGY.md](BACKUP_STRATEGY.md) gelesen
- [ ] Ich verstehe: `main` ist IMMER stabil und produktiv
- [ ] Ich verstehe: Neuer Content → **Feature-Branch** → **PR** → **main**
- [ ] Ich kann einen Feature-Branch erstellen: `git switch -c feature/mein-feature`
- [ ] Ich kann Commits erstellen: `git commit -m "Aussagekräftige Nachricht"`
- [ ] Ich habe mindestens 1x mit Branches in einem anderen Projekt gearbeitet

**Falls blockiert:** Git Tutorial anschauen (z.B. https://git-scm.com/book/de/v2/Git-Grundlagen)

---

### Set 2: Environment & Lokales Setup

**Lernziel:** Du kannst das System lokal starten und das sollte funktionieren.

- [ ] Python 3.8+ ist installiert (`python --version`)
- [ ] Ich habe das Repository geklont: `git clone <repo-url>`
- [ ] Ich bin im Projekt-Root-Verzeichnis: `/workspaces/python-algorithmen-datenstrukturen`
- [ ] Ich habe die [DEVELOPEMENT.MD](DEVELOPEMENT.MD) Anweisungen gelesen
- [ ] Ich verstehe die Verzeichnisstruktur (docs/, src/, apps/, ...)
- [ ] Ich habe einen Python venv / Umgebung eingerichtet (falls nötig)
- [ ] Ich kann Python-Dateien in `src/utils/` ausführen
- [ ] Ich habe versucht, `elearning_manager.py` zu importieren (kein Fehler!)
- [ ] Ich habe versucht, `struktogramm_helper.py` zu importieren (kein Fehler!)

**Falls blockiert:** Siehe [DEVELOPEMENT.MD](DEVELOPEMENT.MD)

---

### Set 3: Backup & Versionierung verstehen

**Lernziel:** Du weißt, wie wir stabile Versionen sichern und wie Rollback funktioniert.

- [ ] Ich habe [BACKUP_STRATEGY.md](BACKUP_STRATEGY.md) gelesen
- [ ] Ich verstehe: **main = stabil**, Features in separaten Branches
- [ ] Ich verstehe den Workflow: Feature → PR → Tests → Merge → **Tag setzen**
- [ ] Ich kenne die Tag-Konvention: `v2026.02.06`en (sortierbar, sprechend)
- [ ] Ich verstehe: Release-Branches für **Hotfixes** auf älteren Versionen
- [ ] Ich weiß, wie man auf eine alte Version zurückspringt: `git checkout <tag>`
- [ ] Ich verstehe: **Nur getestete & validierte Änderungen** gehen in `main`

**Falls blockiert:** Die Backup-Strategy ist kurz, mach einen `git tag -l` um alte Versionen zu sehen

---

### Set 4: Struktogramme (BW-Abitur Standard)

**Lernziel:** Du kannst Struktogramme nach Baden-Württemberg-Standard erstellen und validieren.

- [ ] Ich habe [STRUKTOGRAMM_GUIDE.md](STRUKTOGRAMM_GUIDE.md) gelesen
- [ ] Ich kenne die Operatorenliste: `struktogramme/Operatorenliste-Struktogramme.md`
- [ ] Ich verstehe: `Deklaration`, `Initialisierung`, `Zuweisung`
- [ ] Ich verstehe: `Wenn-dann-sonst`, `Wiederhole`, `Zähle`
- [ ] Ich kann mindestens ein Pattern anwenden (z.B. Array-Durchlauf)
- [ ] Ich kann `StruktogrammBuilder` in Python verwenden
- [ ] Ich habe ein eigenes Struktogramm erstellt oder validiert
- [ ] Ich verstehe: Struktogramme sind **Pflicht** für alle Aufgaben (Abitur!)

**Falls blockiert:** Siehe Pattern-Beispiele in [STRUKTOGRAMM_GUIDE.md](STRUKTOGRAMM_GUIDE.md#häufige-patterns)

---

### Set 5: Content Management System

**Lernziel:** Du kannst Aufgaben, Informationen und Lösungen korrekt erstellen und veröffentlichen.

- [ ] Ich habe [ELEARNING_TEMPLATE_GUIDE.md](ELEARNING_TEMPLATE_GUIDE.md) gelesen
- [ ] Ich verstehe die Dateistruktur: `docs/aufgaben/L*/`, `docs/loesungen/L*/`, etc.
- [ ] Ich kenne die Naming-Konvention: `LX_Y_Z_Thema.md`
- [ ] Ich verstehe: **Python Manager MUSS verwendet werden** (nicht manuell!)
- [ ] Ich kann `ELearningManager` in Python verwenden
- [ ] Ich kann `create_aufgabe_quick()` verwenden
- [ ] Ich kann `create_information_quick()` verwenden
- [ ] Ich kann `create_loesung_quick()` verwenden
- [ ] Ich weiß, dass danach `generate_all_indices()` aufgerufen werden muss
- [ ] Ich verstehe Metadaten: Titel, Level, Kategorie, Nummer, Autor

**Falls blockiert:** Siehe Beispiele in [ELEARNING_TEMPLATE_GUIDE.md](ELEARNING_TEMPLATE_GUIDE.md#workflows)

---

### Set 6: Dein erster Contribution

**Lernziel:** Du hast deinen ersten Feature-Branch erstellt, geändert, getestet und einen PR eingereicht.

- [ ] Ich habe einen Feature-Branch erstellt: `git switch -c feature/meine-erste-aufgabe`
- [ ] Ich habe eine kleine Änderung gemacht (z.B. eine Aufgabe hinzugefügt)
- [ ] Ich habe lokal getestet, dass keine Fehler entstehen
- [ ] Ich habe meine Änderungen committed: `git commit -m "sprechende Nachricht"`
- [ ] Ich habe meinen Branch gepusht: `git push -u origin feature/...`
- [ ] Ich habe einen **PR (Pull Request)** erstellt
- [ ] Ich habe auf Code-Review / Feedback warten können
- [ ] Mein PR wurde gemergt nach Code-Review
- [ ] Danach wurde ein **Tag gesetzt** (falls Milestone erreicht)
- [ ] Ich verstehe: FÜR ZUKÜNFTIGE FEATURES WIEDERHOLE ICH DIESE SCHRITTE

**Falls blockiert:** Kontaktiere die Repository-Betreuer für Hilfe beim ersten PR

---

## 🎓 Rollen & Spezielle Checklisten

### 👨‍🏫 Rolle: Lehrer / Content-Ersteller

**Zusätzlich zu Set 1-6, wenn du Aufgaben/Informationen erstellst:**

- [ ] Ich lese die [ELEARNING_TEMPLATE_GUIDE.md](ELEARNING_TEMPLATE_GUIDE.md)
- [ ] Ich verstehe die Zielgruppe (Schüler, Level L1/L2/L3)
- [ ] Meine Aufgabe hat ein Struktogramm (Abitur-Anforderung!)
- [ ] Meine Aufgabe hat Testfälle / Beispiele
- [ ] Meine Lösung ist ebenfalls dokumentiert
- [ ] Ich verwende den Python Manager, **nicht** manuelle Dateien
- [ ] Ich regeneriere Indices: `manager.generate_all_indices()`
- [ ] Ich teste alles lokal, BEVOR ich committen
- [ ] Ich erstelle einen PR mit aussagekräftiger Beschreibung
- [ ] Mein PR wird von mindestens 1 anderen Person reviewed

---

### 👨‍💻 Rolle: Entwickler / System-Erweiterung

**Zusätzlich zu Set 1-6, wenn du das System erweitern möchtest:**

- [ ] Ich lese die [ARCHITECTURE.MD](ARCHITECTURE.MD)
- [ ] Ich verstehe die bestehende Code-Struktur (apps/, src/, docs/)
- [ ] Ich habe ein Issue oder Feature-Request erstellt (nicht einfach Code schreiben!)
- [ ] Ich dokumentiere meine API / neue Funktionen
- [ ] Ich schreibe Unit Tests (falls sinnvoll)
- [ ] Ich aktualisiere die [ROUTINEN.md](ROUTINEN.md) mit neuen Funktionen
- [ ] Ich aktualisiere relevante .md-Dateien in docs/handbuch/
- [ ] Mein Code folgt den Coding Standards (Type Hints, Docstrings)
- [ ] Ich teste alles lokal mit verschiedenen Szenarien
- [ ] Mein PR wird von mindestens einem Maintainer reviewed
- [ ] Nach Merge wird ein **neuer Tag** gesetzt

---

## 📚 Ressourcen & Links

### Zentrale Handbücher
- [SYSTEM_INDEX.md](SYSTEM_INDEX.md) - Übersicht aller Routinen
- [BACKUP_STRATEGY.md](BACKUP_STRATEGY.md) - Versionierung & Backups
- [DEVELOPEMENT.MD](DEVELOPEMENT.MD) - Lokalsetup & Entwicklung
- [STRUKTOGRAMM_GUIDE.md](STRUKTOGRAMM_GUIDE.md) - Struktogramme BW-Standard
- [ELEARNING_TEMPLATE_GUIDE.md](ELEARNING_TEMPLATE_GUIDE.md) - Content Management
- [ROUTINEN.md](ROUTINEN.md) - Alle verfügbaren Funktionen

### Externe Ressourcen
- [Git Dokumentation](https://git-scm.com/book/de/v2)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Python Dokumentation](https://docs.python.org/3/)

---

## ❓ Häufig gestellte Fragen

**F: Ich bin neu und weiß nicht, wo ich anfangen soll.**  
**A:** Starte mit Set 1 & 2. Wenn diese erledigt sind, gehe zu Set 3-5 je nach deiner Rolle.

**F: Muss ich ALLE Checkboxen abhaken?**  
**A:** Ja, es gibt keine Ausnahmen. Diese Checkliste ist ein Onboarding-Prozess, nicht optional.

**F: Was, wenn ich nicht weiterkommen?**  
**A:** Erstelle ein Issue im Repository oder kontaktiere ein Maintainer-Team.

**F: Wie lange dauert das alles?**  
**A:** Für Lehrer/Content-Ersteller: **2-4 Stunden**. Für Entwickler: **4-8 Stunden** (abhängig vom Erfahrungslevel).

**F: Muss ich das jedes Mal wiederholen?**  
**A:** Nein, nur beim ersten Beitrag. Danach ist Set 6 der Standard-Workflow.

---

## 📝 Bestätigung

Nach Abschluss **aller Checklisten-Sets** (1-6 + deine Rolle):

1. Erstelle einen PR mit der Beschreibung: "Contributor Onboarding abgeschlossen"
2. Ein Maintainer wird dich als **verified Contributor** markieren
3. Du kannst ab sofort ohne weitere Genehmigung PRs einreichen (unter Einhaltung des Workflows)

**Willkommen an Bord! 🚀**

---

*Diese Anleitung wird regelmäßig aktualisiert. Letzte Aktualisierung: 2026-02-06*
