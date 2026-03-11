import pyttsx3
from pyttsx3.voice import Voice

from src.constants.messages import MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE
from src.utils.dialogs import ValidationDialogError


class SpeechEngineModel:
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.voices: dict[str, str] = {}

        self.__get_voices()

    def __get_voices(self) -> None:
        voices: list[Voice] = self.engine.getProperty("voices")

        for voice in voices:
            self.voices[voice.name] = voice.id

    def speech(self, text: str, lang_name: str) -> None:
        if not text or not lang_name:
            ValidationDialogError(message=MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE).dialog()
            return

        self.engine.setProperty("voice", self.voices[lang_name])
        self.engine.say(text)
        self.engine.runAndWait()
