from tkinter import Tk

from src.configs.default_config import DefaultConfig
from src.models.speech_engine_model import SpeechEngineModel
from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class InterfaceApp:
    def __init__(self, root: Tk, engine: SpeechEngineModel, config: DefaultConfig, styles: Styles = Styles()) -> None:
        self._styles = styles
        self._config = config
        self._root = root
        self._root.title("Oratio")
        self._root.geometry("600x100")
        self._root.resizable(False, False)
        self._root.config(background=self._styles.PRIMARY_COLOR)

        self.engine = engine

        self._main_view = MainView(
            root=self._root,
            styles=self._styles,
            voices=list(self.engine.voices.keys()),
            on_listen=self._perform_speech,
        )
        self._main_view.grid(row=0, column=0, sticky="nsew")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

    def _perform_speech(self) -> None:
        text = self._main_view.get_text()
        lang_name = self._main_view.get_lang()

        self.engine.speech(text=text, lang_name=lang_name)
