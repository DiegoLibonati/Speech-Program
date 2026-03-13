from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE
from src.models.speech_engine_model import SpeechEngineModel
from src.utils.dialogs import ValidationDialogError


def make_voice(name: str, voice_id: str) -> MagicMock:
    voice: MagicMock = MagicMock()
    voice.name = name
    voice.id = voice_id
    return voice


@pytest.fixture
def speech_engine_model() -> SpeechEngineModel:
    mock_voices: list[MagicMock] = [
        make_voice("English", "voice_id_en"),
        make_voice("Spanish", "voice_id_es"),
    ]
    mock_engine: MagicMock = MagicMock()
    mock_engine.getProperty.return_value = mock_voices

    with patch("src.models.speech_engine_model.pyttsx3.init", return_value=mock_engine):
        instance: SpeechEngineModel = SpeechEngineModel()
    return instance


class TestSpeechEngineModelInit:
    def test_engine_is_initialized(self) -> None:
        mock_engine: MagicMock = MagicMock()
        mock_engine.getProperty.return_value = []

        with patch("src.models.speech_engine_model.pyttsx3.init", return_value=mock_engine) as mock_init:
            SpeechEngineModel()

        mock_init.assert_called_once()

    def test_voices_dict_is_populated(self, speech_engine_model: SpeechEngineModel) -> None:
        assert speech_engine_model.voices == {"English": "voice_id_en", "Spanish": "voice_id_es"}

    def test_voices_is_dict(self, speech_engine_model: SpeechEngineModel) -> None:
        assert isinstance(speech_engine_model.voices, dict)

    def test_voices_keys_are_voice_names(self, speech_engine_model: SpeechEngineModel) -> None:
        assert "English" in speech_engine_model.voices
        assert "Spanish" in speech_engine_model.voices

    def test_voices_values_are_voice_ids(self, speech_engine_model: SpeechEngineModel) -> None:
        assert speech_engine_model.voices["English"] == "voice_id_en"
        assert speech_engine_model.voices["Spanish"] == "voice_id_es"

    def test_voices_empty_when_no_voices_available(self) -> None:
        mock_engine: MagicMock = MagicMock()
        mock_engine.getProperty.return_value = []

        with patch("src.models.speech_engine_model.pyttsx3.init", return_value=mock_engine):
            instance: SpeechEngineModel = SpeechEngineModel()

        assert instance.voices == {}

    def test_get_property_called_with_voices(self, speech_engine_model: SpeechEngineModel) -> None:
        speech_engine_model.engine.getProperty.return_value = []
        speech_engine_model._SpeechEngineModel__get_voices()
        speech_engine_model.engine.getProperty.assert_called_with("voices")


class TestSpeechEngineModelSpeech:
    def test_raises_validation_error_when_text_is_empty(self, speech_engine_model: SpeechEngineModel) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            speech_engine_model.speech(text="", lang_name="English")
        assert exc_info.value.message == MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE

    def test_raises_validation_error_when_lang_name_is_empty(self, speech_engine_model: SpeechEngineModel) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            speech_engine_model.speech(text="Hello", lang_name="")
        assert exc_info.value.message == MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE

    def test_raises_validation_error_when_both_are_empty(self, speech_engine_model: SpeechEngineModel) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            speech_engine_model.speech(text="", lang_name="")
        assert exc_info.value.message == MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE

    def test_returns_true_on_success(self, speech_engine_model: SpeechEngineModel) -> None:
        result: bool = speech_engine_model.speech(text="Hello", lang_name="English")
        assert result is True

    def test_set_property_called_with_correct_voice_id(self, speech_engine_model: SpeechEngineModel) -> None:
        speech_engine_model.speech(text="Hello", lang_name="English")
        speech_engine_model.engine.setProperty.assert_called_once_with("voice", "voice_id_en")

    def test_say_called_with_text(self, speech_engine_model: SpeechEngineModel) -> None:
        speech_engine_model.speech(text="Hello world", lang_name="English")
        speech_engine_model.engine.say.assert_called_once_with("Hello world")

    def test_run_and_wait_called(self, speech_engine_model: SpeechEngineModel) -> None:
        speech_engine_model.speech(text="Hello", lang_name="English")
        speech_engine_model.engine.runAndWait.assert_called_once()

    def test_set_property_not_called_when_text_is_empty(self, speech_engine_model: SpeechEngineModel) -> None:
        with pytest.raises(ValidationDialogError):
            speech_engine_model.speech(text="", lang_name="English")
        speech_engine_model.engine.setProperty.assert_not_called()

    def test_say_not_called_when_lang_is_empty(self, speech_engine_model: SpeechEngineModel) -> None:
        with pytest.raises(ValidationDialogError):
            speech_engine_model.speech(text="Hello", lang_name="")
        speech_engine_model.engine.say.assert_not_called()

    def test_speech_uses_correct_voice_for_spanish(self, speech_engine_model: SpeechEngineModel) -> None:
        speech_engine_model.speech(text="Hola", lang_name="Spanish")
        speech_engine_model.engine.setProperty.assert_called_once_with("voice", "voice_id_es")
