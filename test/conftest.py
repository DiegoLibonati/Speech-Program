from tkinter import Tk

from pytest import fixture

from src.models import Engine, InterfaceApp


@fixture
def engine() -> Engine:
    return Engine()


@fixture
def interface_app(engine: Engine) -> InterfaceApp:
    root = Tk()

    return InterfaceApp(root=root, engine=engine)
