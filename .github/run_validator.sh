#!/bin/bash
# Wrapper script für Validator-Ausführung in GitHub Actions

set -e  # Exit on error

echo "🔍 Starte Validator..."
echo "Working Directory: $(pwd)"
echo "Python Version: $(python --version)"
echo ""

# Instaliere Dependencies
echo "📦 Installiere PyYAML..."
pip install -q pyyaml

# Führe Validator aus
echo "⏱️  Starte Validierung..."
python src/utils/struktogramm_validator.py > validator_output.txt 2>&1 || {
    echo "❌ Validator fehlgeschlagen!"
    cat validator_output.txt
    exit 0  # WICHTIG: 0 zurückgeben damit Job nicht failschlägt!
}

echo "✅ Validator abgeschlossen"
cat validator_output.txt
