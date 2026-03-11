from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.components.speech_input import SpeechInput


@pytest.fixture
def speech_input(mock_styles: MagicMock, mock_on_listen: MagicMock) -> SpeechInput:
    with (
        patch("src.ui.components.speech_input.Frame.__init__", return_value=None),
        patch("src.ui.components.speech_input.Label"),
        patch("src.ui.components.speech_input.Entry"),
        patch("src.ui.components.speech_input.Button"),
        patch("src.ui.components.speech_input.StringVar"),
        patch.object(SpeechInput, "columnconfigure"),
    ):
        instance: SpeechInput = SpeechInput.__new__(SpeechInput)
        instance._styles = mock_styles
        instance._on_listen = mock_on_listen
        instance._entry_text_user = MagicMock(spec=StringVar)
        return instance


class TestSpeechInputInit:
    def test_stores_styles(self, speech_input: SpeechInput, mock_styles: MagicMock) -> None:
        assert speech_input._styles == mock_styles

    def test_stores_on_listen(self, speech_input: SpeechInput, mock_on_listen: MagicMock) -> None:
        assert speech_input._on_listen == mock_on_listen

    def test_button_command_is_on_listen(self, mock_styles: MagicMock, mock_on_listen: MagicMock) -> None:
        with (
            patch("src.ui.components.speech_input.Frame.__init__", return_value=None),
            patch("src.ui.components.speech_input.Label") as mock_label,
            patch("src.ui.components.speech_input.Entry") as mock_entry,
            patch("src.ui.components.speech_input.Button") as mock_button,
            patch("src.ui.components.speech_input.StringVar"),
            patch.object(SpeechInput, "columnconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            mock_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: SpeechInput = SpeechInput.__new__(SpeechInput)
            instance._styles = mock_styles
            SpeechInput.__init__(instance, parent=MagicMock(), styles=mock_styles, on_listen=mock_on_listen)

        _, kwargs = mock_button.call_args
        assert kwargs.get("command") == mock_on_listen

    def test_button_text_is_listen(self, mock_styles: MagicMock, mock_on_listen: MagicMock) -> None:
        with (
            patch("src.ui.components.speech_input.Frame.__init__", return_value=None),
            patch("src.ui.components.speech_input.Label") as mock_label,
            patch("src.ui.components.speech_input.Entry") as mock_entry,
            patch("src.ui.components.speech_input.Button") as mock_button,
            patch("src.ui.components.speech_input.StringVar"),
            patch.object(SpeechInput, "columnconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            mock_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: SpeechInput = SpeechInput.__new__(SpeechInput)
            instance._styles = mock_styles
            SpeechInput.__init__(instance, parent=MagicMock(), styles=mock_styles, on_listen=mock_on_listen)

        _, kwargs = mock_button.call_args
        assert kwargs.get("text") == "Listen"

    def test_label_text_is_your_message(self, mock_styles: MagicMock, mock_on_listen: MagicMock) -> None:
        with (
            patch("src.ui.components.speech_input.Frame.__init__", return_value=None),
            patch("src.ui.components.speech_input.Label") as mock_label,
            patch("src.ui.components.speech_input.Entry") as mock_entry,
            patch("src.ui.components.speech_input.Button") as mock_button,
            patch("src.ui.components.speech_input.StringVar"),
            patch.object(SpeechInput, "columnconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            mock_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: SpeechInput = SpeechInput.__new__(SpeechInput)
            instance._styles = mock_styles
            SpeechInput.__init__(instance, parent=MagicMock(), styles=mock_styles, on_listen=mock_on_listen)

        _, kwargs = mock_label.call_args
        assert kwargs.get("text") == "Your message:"

    def test_entry_created_with_variable(self, mock_styles: MagicMock, mock_on_listen: MagicMock) -> None:
        with (
            patch("src.ui.components.speech_input.Frame.__init__", return_value=None),
            patch("src.ui.components.speech_input.Label") as mock_label,
            patch("src.ui.components.speech_input.Entry") as mock_entry,
            patch("src.ui.components.speech_input.Button") as mock_button,
            patch("src.ui.components.speech_input.StringVar") as mock_string_var,
            patch.object(SpeechInput, "columnconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            mock_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            mock_var: MagicMock = MagicMock(spec=StringVar)
            mock_string_var.return_value = mock_var
            instance: SpeechInput = SpeechInput.__new__(SpeechInput)
            instance._styles = mock_styles
            SpeechInput.__init__(instance, parent=MagicMock(), styles=mock_styles, on_listen=mock_on_listen)

        _, kwargs = mock_entry.call_args
        assert kwargs.get("textvariable") == mock_var

    def test_columnconfigure_called_three_times(self, mock_styles: MagicMock, mock_on_listen: MagicMock) -> None:
        with (
            patch("src.ui.components.speech_input.Frame.__init__", return_value=None),
            patch("src.ui.components.speech_input.Label") as mock_label,
            patch("src.ui.components.speech_input.Entry") as mock_entry,
            patch("src.ui.components.speech_input.Button") as mock_button,
            patch("src.ui.components.speech_input.StringVar"),
            patch.object(SpeechInput, "columnconfigure") as mock_columnconfigure,
        ):
            mock_label.return_value.grid = MagicMock()
            mock_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: SpeechInput = SpeechInput.__new__(SpeechInput)
            instance._styles = mock_styles
            SpeechInput.__init__(instance, parent=MagicMock(), styles=mock_styles, on_listen=mock_on_listen)

        assert mock_columnconfigure.call_count == 3


class TestSpeechInputGetText:
    def test_returns_entry_value(self, speech_input: SpeechInput) -> None:
        speech_input._entry_text_user.get.return_value = "Hello world"
        result: str = speech_input.get_text()
        assert result == "Hello world"

    def test_returns_empty_string_when_empty(self, speech_input: SpeechInput) -> None:
        speech_input._entry_text_user.get.return_value = ""
        result: str = speech_input.get_text()
        assert result == ""

    def test_calls_entry_get(self, speech_input: SpeechInput) -> None:
        speech_input._entry_text_user.get.return_value = "test"
        speech_input.get_text()
        speech_input._entry_text_user.get.assert_called_once()
