import tkinter as tk
from collections.abc import Iterator
from unittest.mock import MagicMock

import pytest

from src.ui.components.speech_input import SpeechInput
from src.ui.styles import Styles


@pytest.fixture
def on_listen() -> MagicMock:
    return MagicMock()


@pytest.fixture
def speech_input(root: tk.Tk, on_listen: MagicMock) -> Iterator[SpeechInput]:
    styles: Styles = Styles()
    component: SpeechInput = SpeechInput(parent=root, styles=styles, on_listen=on_listen)
    yield component
    component.destroy()


class TestSpeechInput:
    @pytest.mark.unit
    def test_initializes_without_error(self, speech_input: SpeechInput) -> None:
        assert speech_input is not None

    @pytest.mark.unit
    def test_get_text_returns_empty_string_initially(self, speech_input: SpeechInput) -> None:
        result: str = speech_input.get_text()

        assert result == ""

    @pytest.mark.unit
    def test_get_text_returns_typed_value(self, speech_input: SpeechInput) -> None:
        speech_input._entry_text_user.set("Hello world")

        result: str = speech_input.get_text()

        assert result == "Hello world"

    @pytest.mark.unit
    def test_get_text_returns_empty_after_clear(self, speech_input: SpeechInput) -> None:
        speech_input._entry_text_user.set("Something")
        speech_input._entry_text_user.set("")

        result: str = speech_input.get_text()

        assert result == ""

    @pytest.mark.unit
    def test_get_text_preserves_unicode(self, speech_input: SpeechInput) -> None:
        speech_input._entry_text_user.set("Héllo wörld 日本語")

        result: str = speech_input.get_text()

        assert result == "Héllo wörld 日本語"
