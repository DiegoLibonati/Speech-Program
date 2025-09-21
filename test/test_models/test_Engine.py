import pytest
import pyttsx3

from src.models.Engine import Engine
from src.utils.constants import ERROR_NOT_TEXT_OR_LANGUAGE


def test_init_engine(engine: Engine) -> None:
    assert engine.engine
    assert isinstance(engine.engine, pyttsx3.Engine)

    assert engine.voices
    assert isinstance(engine.voices, dict)


def test_speech_without_text_or_lang_name(engine: Engine) -> None:
    with pytest.raises(ValueError) as exc_info:
        engine.speech(text="", lang_name="asd")

    assert str(exc_info.value) == ERROR_NOT_TEXT_OR_LANGUAGE


def test_speech(engine: Engine) -> None:
    engine.speech(text="David", lang_name=list(engine.voices.keys())[0])
