from tkinter import StringVar
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles


@pytest.fixture
def mock_root() -> MagicMock:
    root: MagicMock = MagicMock()
    root.title = MagicMock()
    root.geometry = MagicMock()
    root.resizable = MagicMock()
    root.config = MagicMock()
    root.columnconfigure = MagicMock()
    root.rowconfigure = MagicMock()
    return root


@pytest.fixture
def mock_styles() -> MagicMock:
    styles: MagicMock = MagicMock()
    styles.PRIMARY_COLOR = "#5800FF"
    styles.WHITE_COLOR = "#FFFFFF"
    styles.BLACK_COLOR = "#000000"
    styles.FONT_ROBOTO_12 = "Roboto 12"
    styles.FONT_ROBOTO_14 = "Roboto 14"
    return styles


@pytest.fixture
def real_styles() -> Styles:
    return Styles()


@pytest.fixture
def mock_on_listen() -> MagicMock:
    return MagicMock()


@pytest.fixture
def mock_engine() -> MagicMock:
    engine: MagicMock = MagicMock()
    engine.voices = {"English": "voice_id_en", "Spanish": "voice_id_es"}
    return engine


@pytest.fixture
def variable() -> MagicMock:
    return MagicMock(spec=StringVar)
