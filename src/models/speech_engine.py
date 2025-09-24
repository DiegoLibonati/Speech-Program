import pyttsx3

from src.utils.constants import ERROR_NOT_TEXT_OR_LANGUAGE


class SpeechEngine:
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.voices: dict[str, str] = {}

        self.__get_voices()

    def __get_voices(self) -> None:
        voices: list[pyttsx3.voice.Voice] = self.engine.getProperty("voices")

        for voice in voices:
            self.voices[voice.name] = voice.id

    def speech(self, text: str, lang_name: str) -> None:
        if not text or not lang_name:
            raise ValueError(ERROR_NOT_TEXT_OR_LANGUAGE)

        self.engine.setProperty("voice", self.voices[lang_name])
        self.engine.say(text)
        self.engine.runAndWait()
