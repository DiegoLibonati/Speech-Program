import tkinter as tk
from unittest.mock import MagicMock

import pytest

from src.ui.components.speech_input import SpeechInput
from src.ui.styles import Styles


@pytest.fixture
def styles() -> Styles:
    return Styles()


@pytest.fixture
def on_listen() -> MagicMock:
    return MagicMock()


@pytest.fixture
def speech_input(root: tk.Tk, styles: Styles, on_listen: MagicMock) -> SpeechInput:
    return SpeechInput(parent=root, styles=styles, on_listen=on_listen)


class TestSpeechInput:
    def test_instantiation(self, speech_input: SpeechInput) -> None:
        assert speech_input is not None

    def test_is_frame_subclass(self, speech_input: SpeechInput) -> None:
        assert isinstance(speech_input, tk.Frame)

    def test_get_text_returns_empty_string_by_default(self, speech_input: SpeechInput) -> None:
        assert speech_input.get_text() == ""

    def test_get_text_returns_value_after_set(self, speech_input: SpeechInput) -> None:
        speech_input._entry_text_user.set("Hello world")
        assert speech_input.get_text() == "Hello world"

    def test_get_text_returns_empty_after_clear(self, speech_input: SpeechInput) -> None:
        speech_input._entry_text_user.set("Something")
        speech_input._entry_text_user.set("")
        assert speech_input.get_text() == ""

    def test_on_listen_callback_is_stored(self, speech_input: SpeechInput, on_listen: MagicMock) -> None:
        assert speech_input._on_listen is on_listen

    def test_entry_text_user_is_string_var(self, speech_input: SpeechInput) -> None:
        assert isinstance(speech_input._entry_text_user, tk.StringVar)
