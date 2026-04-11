import tkinter as tk
from unittest.mock import MagicMock

import pytest

from src.configs.default_config import DefaultConfig
from src.models.speech_engine_model import SpeechEngineModel
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


@pytest.fixture
def mock_engine() -> MagicMock:
    engine: MagicMock = MagicMock(spec=SpeechEngineModel)
    engine.voices = {"Voice English": "voice_en", "Voice Spanish": "voice_es"}
    return engine


@pytest.fixture
def config() -> DefaultConfig:
    return DefaultConfig()


@pytest.fixture
def styles() -> Styles:
    return Styles()


@pytest.fixture
def interface_app(root: tk.Tk, mock_engine: MagicMock, config: DefaultConfig, styles: Styles) -> InterfaceApp:
    return InterfaceApp(root=root, engine=mock_engine, config=config, styles=styles)


class TestInterfaceApp:
    def test_engine_attribute_is_set(self, interface_app: InterfaceApp, mock_engine: MagicMock) -> None:
        assert interface_app.engine is mock_engine

    def test_main_view_is_created(self, interface_app: InterfaceApp) -> None:
        assert interface_app._main_view is not None

    def test_window_title_is_speech_app(self, root: tk.Tk, interface_app: InterfaceApp) -> None:
        assert root.title() == "Speech APP"

    def test_config_attribute_is_set(self, interface_app: InterfaceApp, config: DefaultConfig) -> None:
        assert interface_app._config is config

    def test_styles_attribute_is_set(self, interface_app: InterfaceApp, styles: Styles) -> None:
        assert interface_app._styles is styles

    def test_perform_speech_calls_engine_speech(self, interface_app: InterfaceApp, mock_engine: MagicMock) -> None:
        interface_app._main_view.get_text = MagicMock(return_value="Hello")
        interface_app._main_view.get_lang = MagicMock(return_value="Voice English")
        interface_app._perform_speech()
        mock_engine.speech.assert_called_once_with(text="Hello", lang_name="Voice English")
