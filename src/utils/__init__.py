"""
Utilities für python-algorithmen-datenstrukturen Repository

Dieses Paket enthält Tools und Helper für:
- Struktogramm-Validierung und -Rendering (struktogramm_*)
- E-Learning Content Management (elearning_manager)
- Prüfungsdokument-Verwaltung (pruefungen_namenskonvention)
- DOCX-Markdown Optimierung (docx_markdown_optimizer)
- Versionsmanagement (version_manager)
"""

from src.utils.struktogramm_helper import (
    StruktogrammValidator,
    StruktogrammElement,
    OperatorType,
)

from src.utils.docx_markdown_optimizer import (
    DocxOptimizer,
    DocxMetadata,
    StruktogrammOptimizer,
    CodeBlockOptimizer,
    FooterVersionOptimizer,
    optimize_pruefungen_directory,
)

from src.utils.elearning_manager import ELearningManager

__version__ = "1.0"
__all__ = [
    # Struktogramm
    "StruktogrammValidator",
    "StruktogrammElement",
    "OperatorType",
    
    # DOCX Optimizer
    "DocxOptimizer",
    "DocxMetadata",
    "StruktogrammOptimizer",
    "CodeBlockOptimizer",
    "FooterVersionOptimizer",
    "optimize_pruefungen_directory",
    
    # E-Learning
    "ELearningManager",
]
