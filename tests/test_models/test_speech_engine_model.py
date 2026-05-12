from unittest.mock import MagicMock, patch

import pytest

from src.models.speech_engine_model import SpeechEngineModel
from src.utils.dialogs import ValidationDialogError


def _make_voice(name: str, voice_id: str) -> MagicMock:
    voice: MagicMock = MagicMock()
    voice.name = name
    voice.id = voice_id
    return voice


@pytest.fixture
def mock_engine() -> MagicMock:
    engine: MagicMock = MagicMock()
    engine.getProperty.return_value = [
        _make_voice("Microsoft David", "voice-id-david"),
        _make_voice("Microsoft Zira", "voice-id-zira"),
    ]
    return engine


@pytest.fixture
def speech_model(mock_engine: MagicMock) -> SpeechEngineModel:
    with patch("src.models.speech_engine_model.pyttsx3.init", return_value=mock_engine):
        model: SpeechEngineModel = SpeechEngineModel()
    return model


class TestSpeechEngineModel:
    @pytest.mark.unit
    def test_voices_populated_on_init(self, speech_model: SpeechEngineModel) -> None:
        assert "Microsoft David" in speech_model.voices
        assert "Microsoft Zira" in speech_model.voices

    @pytest.mark.unit
    def test_voices_maps_name_to_id(self, speech_model: SpeechEngineModel) -> None:
        assert speech_model.voices["Microsoft David"] == "voice-id-david"
        assert speech_model.voices["Microsoft Zira"] == "voice-id-zira"

    @pytest.mark.unit
    def test_speech_raises_validation_error_when_text_is_empty(
        self, speech_model: SpeechEngineModel
    ) -> None:
        with pytest.raises(ValidationDialogError):
            speech_model.speech(text="", lang_name="Microsoft David")

    @pytest.mark.unit
    def test_speech_raises_validation_error_when_lang_is_empty(
        self, speech_model: SpeechEngineModel
    ) -> None:
        with pytest.raises(ValidationDialogError):
            speech_model.speech(text="Hello", lang_name="")

    @pytest.mark.unit
    def test_speech_raises_validation_error_when_both_empty(
        self, speech_model: SpeechEngineModel
    ) -> None:
        with pytest.raises(ValidationDialogError):
            speech_model.speech(text="", lang_name="")

    @pytest.mark.unit
    def test_speech_sets_voice_property(
        self, speech_model: SpeechEngineModel, mock_engine: MagicMock
    ) -> None:
        speech_model.speech(text="Hello", lang_name="Microsoft David")

        mock_engine.setProperty.assert_called_once_with("voice", "voice-id-david")

    @pytest.mark.unit
    def test_speech_calls_say_with_text(
        self, speech_model: SpeechEngineModel, mock_engine: MagicMock
    ) -> None:
        speech_model.speech(text="Hello world", lang_name="Microsoft David")

        mock_engine.say.assert_called_once_with("Hello world")

    @pytest.mark.unit
    def test_speech_calls_run_and_wait(
        self, speech_model: SpeechEngineModel, mock_engine: MagicMock
    ) -> None:
        speech_model.speech(text="Hello", lang_name="Microsoft David")

        mock_engine.runAndWait.assert_called_once()

    @pytest.mark.unit
    def test_speech_returns_true_on_success(self, speech_model: SpeechEngineModel) -> None:
        result: bool = speech_model.speech(text="Hello", lang_name="Microsoft David")

        assert result is True
