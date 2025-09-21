# Speech Program

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

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
pytest==8.4.2
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/Speech-Program`](https://www.diegolibonati.com.ar/#/project/Speech-Program)

## Video

https://user-images.githubusercontent.com/99032604/198900310-d3260a5c-7158-4a7f-abc5-b64f2e6d7ac0.mp4

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Join to the correct path of the clone
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller --onefile --windowed src/app.py` 

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Join to the correct path of the clone
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller --onefile --windowed src/app.py` 

Alternatively, you can run the helper script: `./build.sh`

## Known Issues
