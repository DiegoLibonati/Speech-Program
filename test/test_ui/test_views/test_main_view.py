from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.main_view import MainView


@pytest.fixture
def main_view(mock_root: MagicMock, mock_styles: MagicMock, mock_on_listen: MagicMock) -> MainView:
    with (
        patch("src.ui.views.main_view.Frame.__init__", return_value=None),
        patch("src.ui.views.main_view.SpeechInput"),
        patch("src.ui.views.main_view.ttk.Combobox"),
        patch.object(MainView, "columnconfigure"),
    ):
        instance: MainView = MainView.__new__(MainView)
        instance._styles = mock_styles
        instance._voices = ["English", "Spanish"]
        instance._on_listen = mock_on_listen
        instance._speech_input = MagicMock()
        instance._combo = MagicMock()
        return instance


class TestMainViewInit:
    def test_stores_styles(self, main_view: MainView, mock_styles: MagicMock) -> None:
        assert main_view._styles == mock_styles

    def test_stores_voices(self, main_view: MainView) -> None:
        assert main_view._voices == ["English", "Spanish"]

    def test_stores_on_listen(self, main_view: MainView, mock_on_listen: MagicMock) -> None:
        assert main_view._on_listen == mock_on_listen

    def test_speech_input_receives_on_listen(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_listen: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.SpeechInput") as mock_speech_input,
            patch("src.ui.views.main_view.ttk.Combobox") as mock_combo,
            patch.object(MainView, "columnconfigure"),
        ):
            mock_speech_input.return_value.grid = MagicMock()
            mock_combo.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(
                instance,
                root=mock_root,
                styles=mock_styles,
                voices=["English", "Spanish"],
                on_listen=mock_on_listen,
            )

        _, kwargs = mock_speech_input.call_args
        assert kwargs.get("on_listen") == mock_on_listen

    def test_combobox_created_with_voices(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_listen: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.SpeechInput") as mock_speech_input,
            patch("src.ui.views.main_view.ttk.Combobox") as mock_combo,
            patch.object(MainView, "columnconfigure"),
        ):
            mock_speech_input.return_value.grid = MagicMock()
            mock_combo.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(
                instance,
                root=mock_root,
                styles=mock_styles,
                voices=["English", "Spanish"],
                on_listen=mock_on_listen,
            )

        _, kwargs = mock_combo.call_args
        assert kwargs.get("values") == ["English", "Spanish"]

    def test_combobox_state_is_readonly(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_listen: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.SpeechInput") as mock_speech_input,
            patch("src.ui.views.main_view.ttk.Combobox") as mock_combo,
            patch.object(MainView, "columnconfigure"),
        ):
            mock_speech_input.return_value.grid = MagicMock()
            mock_combo.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(
                instance,
                root=mock_root,
                styles=mock_styles,
                voices=["English", "Spanish"],
                on_listen=mock_on_listen,
            )

        _, kwargs = mock_combo.call_args
        assert kwargs.get("state") == "readonly"


class TestMainViewGetText:
    def test_delegates_to_speech_input(self, main_view: MainView) -> None:
        main_view._speech_input.get_text.return_value = "Hello"
        result: str = main_view.get_text()
        assert result == "Hello"

    def test_calls_speech_input_get_text(self, main_view: MainView) -> None:
        main_view._speech_input.get_text.return_value = "test"
        main_view.get_text()
        main_view._speech_input.get_text.assert_called_once()


class TestMainViewGetLang:
    def test_delegates_to_combo(self, main_view: MainView) -> None:
        main_view._combo.get.return_value = "English"
        result: str = main_view.get_lang()
        assert result == "English"

    def test_returns_empty_string_when_nothing_selected(self, main_view: MainView) -> None:
        main_view._combo.get.return_value = ""
        result: str = main_view.get_lang()
        assert result == ""

    def test_calls_combo_get(self, main_view: MainView) -> None:
        main_view._combo.get.return_value = "Spanish"
        main_view.get_lang()
        main_view._combo.get.assert_called_once()
