"""Tests für die Prompt-Erzeugung (system_prompt.py)."""

from learning_agent.models import HintLevel, LearningContext, MessageRole
from learning_agent.prompts.system_prompt import erzeuge_nachrichten, erzeuge_systemprompt


def _kontext(hilfestufe: HintLevel = HintLevel.ORIENTIERUNG) -> LearningContext:
    return LearningContext(
        fachgebiet="Informatik",
        thema="Python-Listen",
        niveau="Einstieg",
        lernziel="Elemente hinzufügen",
        eingabe="Ich weiß nicht weiter.",
        hilfestufe=hilfestufe,
    )


def test_systemprompt_enthaelt_kontext() -> None:
    prompt = erzeuge_systemprompt(_kontext())
    assert "Informatik" in prompt
    assert "Python-Listen" in prompt
    assert "Einstieg" in prompt
    assert "Elemente hinzufügen" in prompt


def test_systemprompt_enthaelt_hilfestufe_token() -> None:
    for stufe in HintLevel:
        prompt = erzeuge_systemprompt(_kontext(stufe))
        assert f"HILFESTUFE:{stufe.value}" in prompt


def test_systemprompt_orientierung_enthaelt_fragen_anweisung() -> None:
    prompt = erzeuge_systemprompt(_kontext(HintLevel.ORIENTIERUNG))
    assert "Frage" in prompt or "frage" in prompt.lower()


def test_systemprompt_erklaerung_enthaelt_loesung_hinweis() -> None:
    prompt = erzeuge_systemprompt(_kontext(HintLevel.ERKLAERUNG))
    assert "Lösungsweg" in prompt or "Musterlösung" in prompt


def test_erzeuge_nachrichten_struktur() -> None:
    nachrichten = erzeuge_nachrichten(_kontext())
    assert len(nachrichten) == 2
    assert nachrichten[0].role == MessageRole.SYSTEM
    assert nachrichten[1].role == MessageRole.USER
    assert nachrichten[1].content == "Ich weiß nicht weiter."


def test_systemprompt_enthaelt_datenschutz_hinweis() -> None:
    prompt = erzeuge_systemprompt(_kontext())
    assert "KI" in prompt or "fehlerhaft" in prompt
