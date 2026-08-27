"""Provider-Schnittstelle für LLM-Anbieter.

Definiert die abstrakte Schnittstelle, die alle LLM-Provider
implementieren müssen. Dadurch bleibt der Agent unabhängig vom
konkreten Modellanbieter.
"""

from typing import Protocol, runtime_checkable

from learning_agent.models import Message


@runtime_checkable
class LLMProvider(Protocol):
    """Austauschbare Schnittstelle für Sprachmodell-Anbieter.

    Jeder Provider – ob Mock, lokales Modell oder externe API –
    muss diese Schnittstelle erfüllen.

    Beispiel für eine eigene Implementierung::

        class MeinProvider:
            def generate(self, messages: list[Message]) -> str:
                # Eigene Logik
                return "Antwort"
    """

    def generate(self, messages: list[Message]) -> str:
        """Erzeugt eine Antwort auf Basis der Gesprächshistorie.

        Args:
            messages: Liste der bisherigen Nachrichten (Kontext).

        Returns:
            Die generierte Antwort als Text.
        """
        ...
