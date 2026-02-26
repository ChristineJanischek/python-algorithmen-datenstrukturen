#!/bin/bash
#
# Setup Script für Markdown Reviewer
# Dieses Skript installiert die automatische Markdown-Überprüfung
#
# Verwendung: bash SETUP_MARKDOWN_REVIEWER.sh

set -e

echo ""
echo "========================================================================="
echo "📋 MARKDOWN REVIEWER - SETUP"
echo "========================================================================="
echo ""

REPO_ROOT="$(git rev-parse --show-toplevel)"
GIT_HOOKS_DIR="$REPO_ROOT/.git/hooks"
GITHOOKS_SOURCE="$REPO_ROOT/.githooks/pre-push"
PRE_PUSH_HOOK="$GIT_HOOKS_DIR/pre-push"

# Überprüfe ob Git Repo
if [ ! -d "$GIT_HOOKS_DIR" ]; then
    echo "❌ Fehler: .git/hooks Verzeichnis nicht gefunden!"
    echo "   Stelle sicher, dass Du im Root des Git-Repositories bist."
    exit 1
fi

echo "📍 Repository-Pfad: $REPO_ROOT"
echo "🔗 Git Hooks Verzeichnis: $GIT_HOOKS_DIR"
echo ""

# Kopiere Hook von .githooks zu .git/hooks
if [ ! -f "$GITHOOKS_SOURCE" ]; then
    echo "❌ Fehler: $GITHOOKS_SOURCE nicht gefunden!"
    exit 1
fi

echo "▶ Kopiere Pre-Push Hook..."
cp "$GITHOOKS_SOURCE" "$PRE_PUSH_HOOK"
echo "  ✓ Hook kopiert"

echo "▶ Mache Hook ausführbar..."
chmod +x "$PRE_PUSH_HOOK"
echo "  ✓ Hook ist ausführbar"

echo ""
echo "========================================================================="
echo "✅ INSTALLATION ERFOLGREICH!"
echo "========================================================================="
echo ""
echo "📝 VERWENDUNG:"
echo ""
echo "  1. Normaler Git Workflow:"
echo "     $ git add ."
echo "     $ git commit -m 'Deine Nachricht'"
echo "     $ git push  ← Hook wird automatisch ausgeführt"
echo ""
echo "  2. Du wirst dann gefragt:"
echo "     📋 GIT PRE-PUSH HOOK - Markdown Review"
echo "     Möchtest Du die Markdown-Dateien überprüfen lassen?"
echo "     Review durchführen? (ja/Ja/j/J oder Enter zum Überspringen):"
echo ""
echo "  3. Bei 'ja' werden folgende Prüfungen gemacht:"
echo "     ✓ Ungültige Datei-Referenzen"
echo "     ✓ Tote Links / Verwaiste Dateien"
echo "     ✓ Struktur-Konsistenz (fehlende INDEX-Einträge)"
echo "     ✓ Dokumentations-Synchronisation"
echo "     ✓ Prüfungs-Dateinamensschema (Klausur_Thema_Typ_VersionX.md)"
echo ""
echo "  4. Manual Review (ohne Push):"
echo "     $ python3 apps/tools/markdown_reviewer.py"
echo ""
echo "  5. Nur Prüfungsdateien prüfen/normalisieren:"
echo "     $ python3 apps/tools/pruefungen_dateinamen_manager.py"
echo "     $ python3 apps/tools/pruefungen_dateinamen_manager.py --fix"
echo ""
echo "💡 TIPPS:"
echo "  • Mit 'Enter' können Sie den Review überspringen (für dringende Pushes)"
echo "  • Mit 'git push --no-verify' wird der Hook komplett umgangen"
echo "  • Der Report wird auch als JSON gespeichert: .github/markdown_review_report.json"
echo "  • Siehe apps/tools/MARKDOWN_REVIEWER_README.md für Details"
echo ""
echo "========================================================================="
echo ""
