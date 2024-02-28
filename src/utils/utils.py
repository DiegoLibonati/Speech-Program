import pyttsx3

def get_voices(
    engine: pyttsx3.Engine
) -> dict:
    voices_list = {}
    voices = engine.getProperty('voices')

    for voice in voices:
        voices_list[voice.name] = voice.id

    return voices_list