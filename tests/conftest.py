import tkinter as tk
from collections.abc import Iterator

import pytest


@pytest.fixture(scope="session")
def root() -> Iterator[tk.Tk]:
    instance: tk.Tk = tk.Tk()
    instance.withdraw()
    yield instance
    instance.destroy()
