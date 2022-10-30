from tkinter import *
from tkinter import ttk
import pyttsx3

root = Tk()

root.title("Speech APP")
root.geometry("600x100")
root.resizable(False, False)
root.config(bg="#5800FF")

voices_list = {}
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    voices_list[voice.name] = voice.id

entry_text_user = StringVar()

text_label = Label(root, font=("Roboto 14"), text="Your message:", bg="#5800FF", fg="#fff")
text_label.place(x=20, y=10)

text_entry = Entry(root, font=("Roboto 14"), textvariable=entry_text_user)
text_entry.place(x=180, y=10)

action_button = Button(root, font=("Roboto 12"), text="Listen", command=lambda:speech(),bg="#5800FF", fg="#fff")
action_button.place(x = 450, y = 5)

combo = ttk.Combobox(state="readonly", values=list(voices_list.keys()), width=40)
combo.place(x=20, y=50)

def speech():
    user_text = entry_text_user.get()
    language = combo.get()

    if user_text and language:
        engine.setProperty('voice', voices_list[language])

        engine.say(user_text)

        engine.runAndWait()
    else:
        print("Please select a language and enter a text")

        

root.mainloop()