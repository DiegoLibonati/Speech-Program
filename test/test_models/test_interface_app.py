import logging

import pyttsx3

from src.models import InterfaceApp
from src.utils.constants import PRIMARY

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

CUSTOM_BG = "" or PRIMARY


def test_initial_config_tk_app(interface_app: InterfaceApp) -> None:
    root = interface_app.root
    root.update()

    title = root.title
    geometry = root.geometry().split("+")[0]
    resizable = root.resizable()
    config_bg = root.cget("bg")

    engine = interface_app.engine

    assert title == "Speech APP"
    assert geometry == "600x100"
    assert resizable == (False, False)
    assert config_bg == CUSTOM_BG

    assert engine
    assert isinstance(engine.engine, pyttsx3.Engine)


def test_call_perform_speech(interface_app: InterfaceApp) -> None:
    lang_name = list(interface_app.engine.voices.keys())[0]

    interface_app.entry_text_user.set("David")
    interface_app._combo.set(lang_name)

    interface_app._perform_speech()
