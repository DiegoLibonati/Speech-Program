from tkinter import Button, Entry, Frame, Label, Misc, StringVar

from src.ui.styles import Styles


class SpeechInput(Frame):
    def __init__(
        self,
        parent: Misc,
        styles: Styles,
        on_listen: callable,
    ) -> None:
        super().__init__(parent, bg=styles.PRIMARY_COLOR)
        self._styles = styles
        self._on_listen = on_listen

        self._entry_text_user = StringVar()

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)

        Label(
            self,
            font=self._styles.FONT_ROBOTO_14,
            text="Your message:",
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
        ).grid(row=0, column=0, padx=(0, 10), sticky="w")

        Entry(
            self,
            font=self._styles.FONT_ROBOTO_14,
            textvariable=self._entry_text_user,
        ).grid(row=0, column=1, sticky="ew", padx=(0, 10))

        Button(
            self,
            font=self._styles.FONT_ROBOTO_12,
            text="Listen",
            command=self._on_listen,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
        ).grid(row=0, column=2, sticky="e")

    def get_text(self) -> str:
        return self._entry_text_user.get()
