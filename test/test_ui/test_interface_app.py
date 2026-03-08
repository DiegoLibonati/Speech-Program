from unittest.mock import MagicMock, patch

import pytest

from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock, mock_engine: MagicMock) -> InterfaceApp:
    with (
        patch("src.ui.interface_app.MainView") as mock_main_view_class,
    ):
        mock_main_view: MagicMock = MagicMock()
        mock_main_view.grid = MagicMock()
        mock_main_view_class.return_value = mock_main_view
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._root = mock_root
        instance._config = MagicMock()
        instance._main_view = mock_main_view
        instance.engine = mock_engine
        return instance


class TestInterfaceAppInit:
    def test_stores_styles(self, interface_app: InterfaceApp, mock_styles: MagicMock) -> None:
        assert interface_app._styles == mock_styles

    def test_stores_root(self, interface_app: InterfaceApp, mock_root: MagicMock) -> None:
        assert interface_app._root == mock_root

    def test_stores_engine(self, interface_app: InterfaceApp, mock_engine: MagicMock) -> None:
        assert interface_app.engine == mock_engine

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock, mock_engine: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, engine=mock_engine, config=MagicMock(), styles=mock_styles)

        mock_root.title.assert_called_once_with("Speech APP")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock, mock_engine: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, engine=mock_engine, config=MagicMock(), styles=mock_styles)

        mock_root.geometry.assert_called_once_with("600x100")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock, mock_engine: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, engine=mock_engine, config=MagicMock(), styles=mock_styles)

        mock_root.resizable.assert_called_once_with(False, False)

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock, mock_engine: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, engine=mock_engine, config=MagicMock())

        assert isinstance(app._styles, Styles)

    def test_main_view_created_with_voice_keys(self, mock_root: MagicMock, mock_styles: MagicMock, mock_engine: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, engine=mock_engine, config=MagicMock(), styles=mock_styles)

        _, kwargs = mock_main_view_class.call_args
        assert kwargs.get("voices") == list(mock_engine.voices.keys())

    def test_main_view_on_listen_is_bound(self, mock_root: MagicMock, mock_styles: MagicMock, mock_engine: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, engine=mock_engine, config=MagicMock(), styles=mock_styles)

        _, kwargs = mock_main_view_class.call_args
        assert callable(kwargs.get("on_listen"))


class TestInterfaceAppPerformSpeech:
    def test_engine_speech_called_with_text_and_lang(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_text.return_value = "Hello"
        interface_app._main_view.get_lang.return_value = "English"

        interface_app._perform_speech()

        interface_app.engine.speech.assert_called_once_with(text="Hello", lang_name="English")

    def test_get_text_is_called(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_text.return_value = "Hello"
        interface_app._main_view.get_lang.return_value = "English"

        interface_app._perform_speech()

        interface_app._main_view.get_text.assert_called_once()

    def test_get_lang_is_called(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_text.return_value = "Hello"
        interface_app._main_view.get_lang.return_value = "English"

        interface_app._perform_speech()

        interface_app._main_view.get_lang.assert_called_once()

    def test_engine_speech_called_with_spanish(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_text.return_value = "Hola"
        interface_app._main_view.get_lang.return_value = "Spanish"

        interface_app._perform_speech()

        interface_app.engine.speech.assert_called_once_with(text="Hola", lang_name="Spanish")
