import tkinter as tk

import pytest

from src.ui.styles import Styles


@pytest.fixture(scope="session")
def root() -> tk.Tk:
    instance: tk.Tk = tk.Tk()
    instance.withdraw()
    yield instance
    instance.destroy()


@pytest.fixture
def styles() -> Styles:
    return Styles()
