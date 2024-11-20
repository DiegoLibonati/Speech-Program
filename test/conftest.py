from tkinter import Tk

from pytest import fixture

from src.models.Engine import Engine
from src.models.InterfaceApp import InterfaceApp

@fixture
def engine() -> Engine:
    return Engine()

@fixture
def interface_app(engine: Engine) -> InterfaceApp:
    root = Tk()

    return InterfaceApp(root=root, engine=engine)