from unittest.mock import MagicMock, patch

import pytest

from src.models.speech_engine_model import SpeechEngineModel
from src.utils.dialogs import ValidationDialogError


def _make_mock_voice(name: str, voice_id: str) -> MagicMock:
    voice: MagicMock = MagicMock()
    voice.name = name
    voice.id = voice_id
    return voice


@pytest.fixture
def mock_pyttsx3_engine() -> MagicMock:
    engine: MagicMock = MagicMock()
    engine.getProperty.return_value = [
        _make_mock_voice("Voice English", "voice_en"),
        _make_mock_voice("Voice Spanish", "voice_es"),
    ]
    return engine


@pytest.fixture
def speech_engine(mock_pyttsx3_engine: MagicMock) -> SpeechEngineModel:
    with patch("pyttsx3.init", return_value=mock_pyttsx3_engine):
        return SpeechEngineModel()


class TestSpeechEngineModel:
    def test_voices_is_populated_on_init(self, speech_engine: SpeechEngineModel) -> None:
        assert len(speech_engine.voices) == 2

    def test_voices_maps_name_to_id(self, speech_engine: SpeechEngineModel) -> None:
        assert speech_engine.voices["Voice English"] == "voice_en"
        assert speech_engine.voices["Voice Spanish"] == "voice_es"

    def test_voices_is_dict(self, speech_engine: SpeechEngineModel) -> None:
        assert isinstance(speech_engine.voices, dict)

    def test_speech_raises_when_text_is_empty(self, speech_engine: SpeechEngineModel) -> None:
        with pytest.raises(ValidationDialogError):
            speech_engine.speech(text="", lang_name="Voice English")

    def test_speech_raises_when_lang_name_is_empty(self, speech_engine: SpeechEngineModel) -> None:
        with pytest.raises(ValidationDialogError):
            speech_engine.speech(text="Hello", lang_name="")

    def test_speech_raises_when_both_inputs_are_empty(self, speech_engine: SpeechEngineModel) -> None:
        with pytest.raises(ValidationDialogError):
            speech_engine.speech(text="", lang_name="")

    def test_speech_sets_voice_property(self, speech_engine: SpeechEngineModel, mock_pyttsx3_engine: MagicMock) -> None:
        speech_engine.speech(text="Hello", lang_name="Voice English")
        mock_pyttsx3_engine.setProperty.assert_called_once_with("voice", "voice_en")

    def test_speech_calls_say(self, speech_engine: SpeechEngineModel, mock_pyttsx3_engine: MagicMock) -> None:
        speech_engine.speech(text="Hello world", lang_name="Voice English")
        mock_pyttsx3_engine.say.assert_called_once_with("Hello world")

    def test_speech_calls_run_and_wait(self, speech_engine: SpeechEngineModel, mock_pyttsx3_engine: MagicMock) -> None:
        speech_engine.speech(text="Hello", lang_name="Voice English")
        mock_pyttsx3_engine.runAndWait.assert_called_once()

    def test_speech_returns_true(self, speech_engine: SpeechEngineModel) -> None:
        result: bool = speech_engine.speech(text="Hello", lang_name="Voice English")
        assert result is True
