# Speech Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Execute: `python -m venv venv`
4. Execute in Windows: `venv\Scripts\activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Use `python -m src.app` to execute program

## Description

I made a program in Python, using Tkinter as user interface that allows to reproduce a text entered by the user in voice. The user will enter by the input of this program any message, then he will have to choose a voice that reproduces what he wrote, by default it only brings 2 voices, one in Spanish and another in English. Once this is done the user will touch the Listen button to play the message and listen to it.

## Technologies used

1. Python

## Libraries used

#### Requirements.txt

```
pyttsx3==2.90
```

#### Requirements.test.txt

```
pytest
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/Speech-Program`](https://www.diegolibonati.com.ar/#/project/Speech-Program)

## Video

https://user-images.githubusercontent.com/99032604/198900310-d3260a5c-7158-4a7f-abc5-b64f2e6d7ac0.mp4

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`