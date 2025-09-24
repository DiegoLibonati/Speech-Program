from tkinter import Tk

from src.models.speech_engine import SpeechEngine
from src.ui.interface_app import InterfaceApp


def main():
    root = Tk()
    engine = SpeechEngine()

    app = InterfaceApp(root=root, engine=engine)
    root.mainloop()

    print(f"App: {app}")


if __name__ == "__main__":
    main()
