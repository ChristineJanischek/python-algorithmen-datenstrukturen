#!/usr/bin/env python3
"""
Markdown Reviewer Installation & Setup Guide

Dieses Skript installiert und konfiguriert die automatische Markdown-Überprüfung.
"""

import os
import sys
import subprocess
from pathlib import Path


def install_markdown_reviewer():
    """Installiere und konfiguriere den Markdown Reviewer."""
    
    repo_root = Path(__file__).parent.parent.parent
    tools_dir = repo_root / "apps" / "tools"
    git_hooks_dir = repo_root / ".git" / "hooks"
    
    print("\n" + "="*70)
    print("📋 MARKDOWN REVIEWER - INSTALLATION")
    print("="*70 + "\n")
    
    # Überprüfe Dateien
    reviewer_script = tools_dir / "markdown_reviewer.py"
    pre_push_hook = git_hooks_dir / "pre-push"
    
    if not reviewer_script.exists():
        print("❌ Fehler: markdown_reviewer.py nicht gefunden!")
        return False
    
    if not git_hooks_dir.exists():
        git_hooks_dir.mkdir(parents=True, exist_ok=True)
        print(f"✓ Git hooks Verzeichnis erstellt: {git_hooks_dir}")
    
    if pre_push_hook.exists():
        print(f"✓ Git Pre-Push Hook vorhanden: {pre_push_hook}")
    
    # Mache Hook ausführbar
    try:
        os.chmod(pre_push_hook, 0o755)
        print(f"✓ Pre-Push Hook ist ausführbar\n")
    except Exception as e:
        print(f"❌ Fehler beim Setzen der Ausführungsrechte: {e}\n")
        return False
    
    # Zeige Zusammenfassung
    print("="*70)
    print("✅ INSTALLATION ERFOLGREICH")
    print("="*70)
    print("\n📝 VERWENDUNG:\n")
    print("1. Normale Git Workflow:")
    print("   $ git add .")
    print("   $ git commit -m 'Deine Nachricht'")
    print("   $ git push")
    print("\n2. Beim Git Push wird automatisch gefragt:")
    print("   📋 GIT PRE-PUSH HOOK - Markdown Review")
    print("   Möchtest Du die Markdown-Dateien überprüfen lassen? (ja/Ja/j/J oder Enter)")
    print("\n3. Bei 'ja' werden folgende Prüfungen gemacht:")
    print("   ✓ Ungültige Datei-Referenzen")
    print("   ✓ Tote Links / Verwaiste Dateien")
    print("   ✓ Struktur-Konsistenz (fehlende INDEX-Einträge)")
    print("   ✓ Dokumentations-Synchronisation")
    print("\n4. Manual Review (ohne Push):")
    print("   $ python3 apps/tools/markdown_reviewer.py")
    print("   $ python3 apps/tools/setup_markdown_reviewer.py")  # This script
    print("\n" + "="*70)
    print("💡 TIPPS:\n")
    print("• Der Hook fragt IMMER vor dem Push")
    print("• Du kannst mit 'Enter' überspringen (für dringende Pushes)")
    print("• Der Report wird auch als JSON gespeichert: .github/markdown_review_report.json")
    print("• Warnungen sollten trotzdem überprüft werden, sind aber nicht-kritisch")
    print("• Im dev-Container ist python3 bereits installiert")
    print("\n" + "="*70 + "\n")
    
    return True


if __name__ == "__main__":
    success = install_markdown_reviewer()
    sys.exit(0 if success else 1)
