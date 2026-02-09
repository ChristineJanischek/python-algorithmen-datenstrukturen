"""
Struktogramm-Tools für Baden-Württemberg Abitur-Standards

Dieses Paket enthält umfassende Werkzeuge zur Verwaltung von Struktogrammen
nach der offiziellen Operatorenliste des Baden-Württemberg Abiturs.

Enthält:
- Validator: Prüft Struktogramme gegen Operatorenliste
- Refactorer: Automatisches Refactoring zu korrekter Notation
- CLI: Kommandozeilen-Interface für Batch-Verarbeitung

Author: GitHub Copilot
Version: 1.0
"""

from struktogramm_validator import (
    StruktogrammValidator,
    StruktogrammAnalyzer,
    ValidationResult,
    ValidationLevel,
    validate_file,
    create_validation_report,
)

from struktogramm_refactorer import (
    StruktogrammRefactorer,
    StruktogrammFormatter,
    RefactoringChange,
    create_refactoring_report,
    apply_refactoring_batch,
)

__version__ = "1.0"
__author__ = "GitHub Copilot"

__all__ = [
    "StruktogrammValidator",
    "StruktogrammAnalyzer",
    "StruktogrammRefactorer",
    "StruktogrammFormatter",
    "ValidationResult",
    "ValidationLevel",
    "RefactoringChange",
    "validate_file",
    "create_validation_report",
    "create_refactoring_report",
    "apply_refactoring_batch",
]
