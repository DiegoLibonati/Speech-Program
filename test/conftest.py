from tkinter import Tk

from pytest import fixture

from src.models.speech_engine import SpeechEngine
from src.ui.interface_app import InterfaceApp


@fixture
def engine() -> SpeechEngine:
    return SpeechEngine()


@fixture
def interface_app(engine: SpeechEngine) -> InterfaceApp:
    root = Tk()

    return InterfaceApp(root=root, engine=engine)
