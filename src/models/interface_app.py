from tkinter import Button, Entry, Label, StringVar, Tk, ttk

from src.models import Engine
from src.utils.constants import PRIMARY, ROBOTO_12, ROBOTO_14, TEXT_YOUR_MESSAGE, WHITE


class InterfaceApp:
    def __init__(self, root: Tk, engine: Engine, bg: str = PRIMARY) -> None:
        self.root = root
        self.root.title = "Speech APP"
        self.root.geometry("600x100")
        self.root.resizable(False, False)
        self.root.config(bg=bg)

        self.engine = engine

        self.__create_widgets()

    def __create_widgets(self) -> None:
        self.entry_text_user = StringVar()

        text_label = Label(
            self.root, font=(ROBOTO_14), text=TEXT_YOUR_MESSAGE, bg=PRIMARY, fg=WHITE
        )
        text_label.place(x=20, y=10)

        text_entry = Entry(
            self.root, font=(ROBOTO_14), textvariable=self.entry_text_user
        )
        text_entry.place(x=180, y=10)

        action_button = Button(
            self.root,
            font=(ROBOTO_12),
            text="Listen",
            command=lambda: self._perform_speech(),
            bg=PRIMARY,
            fg=WHITE,
        )
        action_button.place(x=450, y=5)

        self._combo = ttk.Combobox(
            state="readonly", values=list(self.engine.voices.keys()), width=40
        )
        self._combo.place(x=20, y=50)

    def _perform_speech(self) -> None:
        text = self.entry_text_user.get()
        lang_name = self._combo.get()

        self.engine.speech(text=text, lang_name=lang_name)
