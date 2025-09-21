from tkinter import Tk

from src.models import Engine, InterfaceApp


def main():
    root = Tk()
    engine = Engine()

    app = InterfaceApp(root=root, engine=engine)

    root.mainloop()

    print(f"App: {app}")


if __name__ == "__main__":
    main()



