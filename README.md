# Oratio

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.dev.txt`
7. Execute: `pip install -r requirements.test.txt`
8. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

**Oratio** is a desktop application built in Python that converts any written text into spoken audio using the system's text-to-speech engine. It provides a clean and minimal graphical interface powered by Tkinter, making it straightforward to use without any technical knowledge.

The user opens the application and is presented with a simple form: a text input field where any message can be typed, and a dropdown list that displays all the available voices installed on the operating system. By default, at least two voices are available — one in Spanish and one in English — though the list will automatically include any additional voices installed on the system, allowing for a broader range of languages and accents. Once the user has typed their message and selected a preferred voice, they click the **Listen** button to play the speech back immediately through the system's audio output.

Under the hood, the application uses `pyttsx3`, a cross-platform text-to-speech library that interfaces directly with native speech engines: SAPI5 on Windows, NSSpeechSynthesizer on macOS, and espeak on Linux. This means no internet connection is required — everything runs fully offline on the local machine.

The application also includes robust error handling: if the text field is left empty or an invalid voice is selected, a descriptive dialog is shown to the user instead of crashing. All configuration is managed through environment variables, and the codebase is organized following a clear MVC-inspired architecture with a config system, a model layer, and a UI layer — making it easy to extend or modify.

The app can be run directly with Python or packaged into a standalone executable using PyInstaller, making distribution simple without requiring the end user to have Python installed.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

#### Requirements.txt

```
pyttsx3==2.90
python-dotenv==1.0.1
```

#### Requirements.dev.txt
```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Requirements.test.txt

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/oratio`](https://www.diegolibonati.com.ar/#/project/oratio)

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -r requirements.dev.txt`
4. Execute: `pip-audit -r requirements.txt`

## Env Keys

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.

```
ENVIRONMENT=development
```

## Known Issues

None at the moment.