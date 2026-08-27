"""Provider-Basisklasse mit gemeinsamen Hilfsmethoden."""

from learning_agent.models import Message


class BaseProvider:
    """Optionale Basisklasse für Provider-Implementierungen.

    Enthält gemeinsame Hilfsmethoden. Die Verwendung ist freiwillig –
    auch eine Klasse, die nur ``generate`` implementiert, genügt der
    ``LLMProvider``-Schnittstelle.
    """

    def format_messages(self, messages: list[Message]) -> str:
        """Wandelt eine Nachrichtenliste in einen lesbaren Text um.

        Args:
            messages: Liste der Nachrichten.

        Returns:
            Formatierter Text.
        """
        lines = []
        for msg in messages:
            lines.append(f"[{msg.role.value.upper()}]: {msg.content}")
        return "\n".join(lines)
