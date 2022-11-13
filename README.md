# Speech-Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Install requirements.txt
4. Use `python speech_program.py` to execute program

## Description

I made a program in Python, using Tkinter as user interface that allows to reproduce a text entered by the user in voice. The user will enter by the input of this program any message, then he will have to choose a voice that reproduces what he wrote, by default it only brings 2 voices, one in Spanish and another in English. Once this is done the user will touch the Listen button to play the message and listen to it.

## Technologies used

1. Python

## Libraries used

1. Tkinter
2. pyttsx3

## Galery

![Speech-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/speechpython-0.jpg)

![Speech-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/speechpython-1.jpg)

![Speech-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/speechpython-2.jpg)

![Speech-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/speechpython-3.jpg)

![Speech-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/speechpython-4.jpg)

## Portfolio Link

`https://diegolibonati.github.io/DiegoLibonatiWeb/#/projects?q=Speech%20Program`

## Video

https://user-images.githubusercontent.com/99032604/198900310-d3260a5c-7158-4a7f-abc5-b64f2e6d7ac0.mp4

## Documentation

In this variable we are going to store all the voices that we have in our system:

```
voices_list = {}
```

With the `engine` variable we initialize the `pyttsx3` library to be able to use it:

```
engine = pyttsx3.init()
```

In this variable we are going to obtain all the voices that we have in our system:

```
voices = engine.getProperty('voices')
```

Here what we do is to go through voice by voice the voices that we obtained from the system and we are going to save them in our dictionary of `voices_list` with a key that will be the name of the voice and an id as value that is what we will use later to reproduce the voice:

```
for voice in voices:
    voices_list[voice.name] = voice.id
```

To the combo that we make in `tkinter` we are going to add only the keys, that is to say, the names that we had set as key:

```
combo = ttk.Combobox(state="readonly", values=list(voices_list.keys()), width=40)
```

This function will be in charge of reproducing the text we entered with the voice we selected from the combo. We get what the user entered and the language selected by the user to reproduce the voice. In case of not choosing a text will be skipped. Then it will execute the voice with what it has to say, based on what the user wrote:

```
def speech():
    user_text = entry_text_user.get()
    language = combo.get()

    if user_text and language:
        engine.setProperty('voice', voices_list[language])

        engine.say(user_text)

        engine.runAndWait()
    else:
        print("Please select a language and enter a text")
```
