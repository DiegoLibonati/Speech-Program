from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE
from src.models.speech_engine_model import SpeechEngineModel


@pytest.fixture
def speech_engine_model() -> SpeechEngineModel:
    mock_voice_en: MagicMock = MagicMock()
    mock_voice_en.name = "English"
    mock_voice_en.id = "voice_id_en"

    mock_voice_es: MagicMock = MagicMock()
    mock_voice_es.name = "Spanish"
    mock_voice_es.id = "voice_id_es"

    with patch("src.models.speech_engine_model.pyttsx3.init") as mock_init:
        mock_engine: MagicMock = MagicMock()
        mock_engine.getProperty.return_value = [mock_voice_en, mock_voice_es]
        mock_init.return_value = mock_engine
        model: SpeechEngineModel = SpeechEngineModel()
        return model


class TestSpeechEngineModelInit:
    def test_voices_dict_is_populated(self, speech_engine_model: SpeechEngineModel) -> None:
        assert len(speech_engine_model.voices) == 2

    def test_voices_contains_english_key(self, speech_engine_model: SpeechEngineModel) -> None:
        assert "English" in speech_engine_model.voices

    def test_voices_contains_spanish_key(self, speech_engine_model: SpeechEngineModel) -> None:
        assert "Spanish" in speech_engine_model.voices

    def test_voices_english_maps_to_correct_id(self, speech_engine_model: SpeechEngineModel) -> None:
        assert speech_engine_model.voices["English"] == "voice_id_en"

    def test_voices_spanish_maps_to_correct_id(self, speech_engine_model: SpeechEngineModel) -> None:
        assert speech_engine_model.voices["Spanish"] == "voice_id_es"

    def test_engine_get_property_called_with_voices(self, speech_engine_model: SpeechEngineModel) -> None:
        speech_engine_model.engine.getProperty.assert_called_with("voices")


class TestSpeechEngineModelSpeech:
    def test_validation_dialog_called_when_text_is_empty(self, speech_engine_model: SpeechEngineModel) -> None:
        with patch("src.models.speech_engine_model.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            speech_engine_model.speech(text="", lang_name="English")

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE)
        mock_dialog_class.return_value.dialog.assert_called_once()

    def test_validation_dialog_called_when_lang_name_is_empty(self, speech_engine_model: SpeechEngineModel) -> None:
        with patch("src.models.speech_engine_model.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            speech_engine_model.speech(text="Hello", lang_name="")

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE)
        mock_dialog_class.return_value.dialog.assert_called_once()

    def test_set_property_not_called_when_lang_name_is_empty(self, speech_engine_model: SpeechEngineModel) -> None:
        with patch("src.models.speech_engine_model.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            speech_engine_model.speech(text="Hello", lang_name="")

        speech_engine_model.engine.setProperty.assert_not_called()

    def test_set_property_not_called_when_text_is_empty(self, speech_engine_model: SpeechEngineModel) -> None:
        with patch("src.models.speech_engine_model.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            speech_engine_model.speech(text="", lang_name="English")

        speech_engine_model.engine.setProperty.assert_not_called()

    def test_set_property_called_with_correct_voice_id(self, speech_engine_model: SpeechEngineModel) -> None:
        speech_engine_model.speech(text="Hello", lang_name="English")
        speech_engine_model.engine.setProperty.assert_called_once_with("voice", "voice_id_en")

    def test_say_called_with_text(self, speech_engine_model: SpeechEngineModel) -> None:
        speech_engine_model.speech(text="Hello world", lang_name="English")
        speech_engine_model.engine.say.assert_called_once_with("Hello world")

    def test_run_and_wait_is_called(self, speech_engine_model: SpeechEngineModel) -> None:
        speech_engine_model.speech(text="Hello", lang_name="English")
        speech_engine_model.engine.runAndWait.assert_called_once()

    def test_speech_uses_correct_voice_for_spanish(self, speech_engine_model: SpeechEngineModel) -> None:
        speech_engine_model.speech(text="Hola", lang_name="Spanish")
        speech_engine_model.engine.setProperty.assert_called_once_with("voice", "voice_id_es")
