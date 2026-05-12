import tkinter as tk
from collections.abc import Iterator
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


@pytest.fixture
def on_listen() -> MagicMock:
    return MagicMock()


@pytest.fixture
def main_view(root: tk.Tk, on_listen: MagicMock) -> Iterator[MainView]:
    styles: Styles = Styles()
    view: MainView = MainView(
        root=root,
        styles=styles,
        voices=["Voice A", "Voice B"],
        on_listen=on_listen,
    )
    yield view
    view.destroy()


class TestMainView:
    @pytest.mark.unit
    def test_initializes_without_error(self, main_view: MainView) -> None:
        assert main_view is not None

    @pytest.mark.unit
    def test_get_text_returns_empty_string_initially(self, main_view: MainView) -> None:
        result: str = main_view.get_text()

        assert result == ""

    @pytest.mark.unit
    def test_get_lang_returns_empty_string_initially(self, main_view: MainView) -> None:
        result: str = main_view.get_lang()

        assert result == ""

    @pytest.mark.unit
    def test_get_lang_returns_selected_voice(self, main_view: MainView) -> None:
        main_view._combo.set("Voice A")

        result: str = main_view.get_lang()

        assert result == "Voice A"

    @pytest.mark.unit
    def test_get_text_returns_typed_value(self, main_view: MainView) -> None:
        main_view._speech_input._entry_text_user.set("Test message")

        result: str = main_view.get_text()

        assert result == "Test message"

    @pytest.mark.unit
    def test_get_lang_after_changing_selection(self, main_view: MainView) -> None:
        main_view._combo.set("Voice A")
        main_view._combo.set("Voice B")

        result: str = main_view.get_lang()

        assert result == "Voice B"
