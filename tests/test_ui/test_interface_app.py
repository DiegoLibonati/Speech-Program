import tkinter as tk
from collections.abc import Iterator
from unittest.mock import MagicMock, patch

import pytest

from src.configs.testing_config import TestingConfig
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


@pytest.fixture
def mock_engine() -> MagicMock:
    engine: MagicMock = MagicMock()
    engine.voices = {"Microsoft David": "voice-id-david"}
    return engine


@pytest.fixture
def interface_app(root: tk.Tk, mock_engine: MagicMock) -> Iterator[InterfaceApp]:
    config: TestingConfig = TestingConfig()
    app: InterfaceApp = InterfaceApp(root=root, engine=mock_engine, config=config)
    yield app
    app._main_view.destroy()


class TestInterfaceApp:
    @pytest.mark.unit
    def test_initializes_without_error(self, interface_app: InterfaceApp) -> None:
        assert interface_app is not None

    @pytest.mark.unit
    def test_title_is_oratio(self, root: tk.Tk, interface_app: InterfaceApp) -> None:
        assert root.title() == "Oratio"

    @pytest.mark.unit
    def test_uses_custom_styles_when_provided(self, root: tk.Tk, mock_engine: MagicMock) -> None:
        styles: Styles = Styles()
        config: TestingConfig = TestingConfig()

        app: InterfaceApp = InterfaceApp(
            root=root, engine=mock_engine, config=config, styles=styles
        )
        app._main_view.destroy()

        assert app._styles is styles

    @pytest.mark.unit
    def test_uses_default_styles_when_none_provided(self, interface_app: InterfaceApp) -> None:
        assert isinstance(interface_app._styles, Styles)

    @pytest.mark.unit
    def test_perform_speech_delegates_to_engine(
        self, interface_app: InterfaceApp, mock_engine: MagicMock
    ) -> None:
        with patch.object(interface_app._main_view, "get_text", return_value="Hello"):
            with patch.object(interface_app._main_view, "get_lang", return_value="Microsoft David"):
                interface_app._perform_speech()

        mock_engine.speech.assert_called_once_with(text="Hello", lang_name="Microsoft David")
