import tkinter as tk
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


@pytest.fixture
def styles() -> Styles:
    return Styles()


@pytest.fixture
def voices() -> list[str]:
    return ["Voice English", "Voice Spanish"]


@pytest.fixture
def on_listen() -> MagicMock:
    return MagicMock()


@pytest.fixture
def main_view(root: tk.Tk, styles: Styles, voices: list[str], on_listen: MagicMock) -> MainView:
    return MainView(root=root, styles=styles, voices=voices, on_listen=on_listen)


class TestMainView:
    def test_instantiation(self, main_view: MainView) -> None:
        assert main_view is not None

    def test_is_frame_subclass(self, main_view: MainView) -> None:
        assert isinstance(main_view, tk.Frame)

    def test_get_text_returns_empty_string_by_default(self, main_view: MainView) -> None:
        assert main_view.get_text() == ""

    def test_get_lang_returns_empty_string_by_default(self, main_view: MainView) -> None:
        assert main_view.get_lang() == ""

    def test_get_lang_returns_selected_value(self, main_view: MainView) -> None:
        main_view._combo.set("Voice English")
        assert main_view.get_lang() == "Voice English"

    def test_combo_has_voices_values(self, main_view: MainView, voices: list[str]) -> None:
        combo_values: tuple[str, ...] = main_view._combo.cget("values")
        assert list(combo_values) == voices

    def test_speech_input_is_created(self, main_view: MainView) -> None:
        assert main_view._speech_input is not None

    def test_get_text_delegates_to_speech_input(self, main_view: MainView) -> None:
        main_view._speech_input._entry_text_user.set("Delegated text")
        assert main_view.get_text() == "Delegated text"
