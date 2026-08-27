"""Tests für den MockProvider."""

import pytest

from learning_agent.models import HintLevel, Message, MessageRole
from learning_agent.providers.mock_provider import (
    MockProvider,
    _bestimme_hilfestufe,
    _waehle_antwortliste,
)


@pytest.fixture
def provider() -> MockProvider:
    return MockProvider()


def test_generate_gibt_text_zurueck(provider: MockProvider) -> None:
    nachrichten = [
        Message(role=MessageRole.SYSTEM, content="HILFESTUFE:1"),
        Message(role=MessageRole.USER, content="Was ist eine Liste?"),
    ]
    antwort = provider.generate(nachrichten)
    assert isinstance(antwort, str)
    assert len(antwort) > 0


def test_generate_orientierungsstufe(provider: MockProvider) -> None:
    nachrichten = [
        Message(role=MessageRole.SYSTEM, content="HILFESTUFE:1"),
        Message(role=MessageRole.USER, content="Ich weiß nicht, wie ich eine Liste ergänzen kann."),
    ]
    antwort = provider.generate(nachrichten)
    # Orientierungsstufe: Frage zurück
    assert "?" in antwort


def test_generate_hilfestufe_3_erklaerung(provider: MockProvider) -> None:
    nachrichten = [
        Message(role=MessageRole.SYSTEM, content="HILFESTUFE:3"),
        Message(role=MessageRole.USER, content="Erkläre mir die Liste."),
    ]
    antwort = provider.generate(nachrichten)
    assert isinstance(antwort, str)


def test_bestimme_hilfestufe_standard() -> None:
    nachrichten = [
        Message(role=MessageRole.SYSTEM, content="Kein Hinweis auf Stufe"),
        Message(role=MessageRole.USER, content="Frage"),
    ]
    assert _bestimme_hilfestufe(nachrichten) == HintLevel.ORIENTIERUNG


def test_bestimme_hilfestufe_2() -> None:
    nachrichten = [
        Message(role=MessageRole.SYSTEM, content="HILFESTUFE:2"),
    ]
    assert _bestimme_hilfestufe(nachrichten) == HintLevel.HINWEIS


def test_bestimme_hilfestufe_3() -> None:
    nachrichten = [
        Message(role=MessageRole.SYSTEM, content="HILFESTUFE:3"),
    ]
    assert _bestimme_hilfestufe(nachrichten) == HintLevel.ERKLAERUNG


def test_waehle_antwortliste_liste() -> None:
    antworten = _waehle_antwortliste("Wie ergänze ich ein Element in die Liste?")
    assert len(antworten) == 3


def test_waehle_antwortliste_default() -> None:
    antworten = _waehle_antwortliste("Was ist ein Algorithmus?")
    assert len(antworten) == 3


def test_provider_implementiert_schnittstelle() -> None:
    from learning_agent.providers import LLMProvider
    provider = MockProvider()
    assert isinstance(provider, LLMProvider)
