from tkinter import Frame, Tk, ttk

from pyttsx3.voice import Voice

from src.ui.components.speech_input import SpeechInput
from src.ui.styles import Styles


class MainView(Frame):
    def __init__(
        self,
        root: Tk,
        styles: Styles,
        voices: list[Voice],
        on_listen: callable,
    ) -> None:
        super().__init__(root, bg=styles.PRIMARY_COLOR)
        self._styles = styles
        self._voices = voices
        self._on_listen = on_listen

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.columnconfigure(0, weight=1)

        self._speech_input = SpeechInput(
            parent=self,
            styles=self._styles,
            on_listen=self._on_listen,
        )
        self._speech_input.grid(row=0, column=0, sticky="ew", padx=20, pady=(10, 5))

        self._combo = ttk.Combobox(
            self,
            state="readonly",
            values=self._voices,
            width=40,
        )
        self._combo.grid(row=1, column=0, sticky="w", padx=20, pady=10)

    def get_text(self) -> str:
        return self._speech_input.get_text()

    def get_lang(self) -> str:
        return self._combo.get()
