# Oratio

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

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

Dependencies are declared in `pyproject.toml` and grouped by purpose. The `requirements*.txt` files are thin wrappers that delegate to the corresponding extras.

#### Runtime (`[project.dependencies]`)

```
pyttsx3==2.90
python-dotenv==1.2.2
```

#### Dev (`[project.optional-dependencies]` dev)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
mypy==1.13.0
python-semantic-release==9.21.0
```

#### Test (`[project.optional-dependencies]` test)

```
pytest==9.0.3
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Build (`[project.optional-dependencies]` build)

```
pyinstaller==6.16.0
```

## Getting Started

Follow these steps to set up the project locally for development.

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e ".[dev,test]"`
6. Copy `.env.example.dev` to `.env` so the application can load its configuration
7. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Env Keys

The `.env` file you copied during setup defines the runtime environment for the application.

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.

```
ENVIRONMENT=development
```

## Testing

With the environment set up, you can verify everything is working by running the test suite.

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e ".[test]"`
6. Execute: `pytest --log-cli-level=INFO`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -e ".[dev]"`
4. Execute: `pip-audit -r requirements.txt`

## Build

Once tests pass and the dependencies are clean, you can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -e ".[build]"`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -e ".[build]"`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Continuous Integration

The repository ships with a **GitHub Actions** pipeline defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml). It runs automatically on every `push` and `pull_request` targeting the `main` branch. On `push` to `main`, the same workflow continues with three additional jobs that produce an automated release.

### Pipeline overview

```
                      ┌─── PR or push to main ───┐
                      ▼                          ▼
┌──────────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│   lint-and-audit     │─▶│       test       │─▶│      build       │
│ ruff · mypy · audit  │  │ pytest (headless)│  │ pyinstaller (lnx)│
└──────────────────────┘  └──────────────────┘  └──────────────────┘
                                                          │
                                       (only on push to main, sequentially)
                                                          ▼
                                                ┌──────────────────────┐
                                                │   prepare-release    │
                                                │ bump · changelog · tag│
                                                └──────────────────────┘
                                                          │
                                                          ▼
                                                ┌──────────────────────┐
                                                │  build-windows-exe   │
                                                │ pyinstaller (windows)│
                                                └──────────────────────┘
                                                          │
                                                          ▼
                                                ┌──────────────────────┐
                                                │   publish-release    │
                                                │ GitHub Release + .exe│
                                                └──────────────────────┘
```

### Validation jobs (run on every PR and push)

1. **`lint-and-audit`** — `ruff check`, `ruff format --check`, `mypy`, `pip-audit --skip-editable`.
2. **`test`** — installs Tkinter + `xvfb` on Ubuntu and runs `pytest --tb=short` headlessly.
3. **`build`** — smoke test that `pyinstaller app.spec` produces a binary on Linux.

### Release jobs (only on push to `main`)

4. **`prepare-release`** — runs [`python-semantic-release`](https://python-semantic-release.readthedocs.io/) which inspects the commits since the latest tag, decides the next SemVer version using [Conventional Commits](#conventional-commits-required-for-releases), updates `CHANGELOG.md` and the `version` field in `pyproject.toml`, then commits, tags and pushes back to `main`. Skipped automatically when the head commit is the bot's own `chore(release): vX.Y.Z [skip release]` commit, to avoid loops.
5. **`build-windows-exe`** — checks out the freshly created tag on a `windows-latest` runner, runs `pyinstaller app.spec`, and renames the artifact to `oratio-vX.Y.Z-windows.exe`.
6. **`publish-release`** — uses `python-semantic-release/publish-action` to create the GitHub Release for the new tag, attach the Windows `.exe`, and use the generated changelog section as the release notes.

### Conventional Commits (required for releases)

Commits merged into `main` must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) so the pipeline can compute the next version and group the changelog entries.

| Commit prefix | Version bump | Example |
|---|---|---|
| `feat:` / `feat(scope):` | **MINOR** | `feat(ui): add dark mode toggle` |
| `fix:` / `fix(scope):`, `perf:` / `perf(scope):` | **PATCH** | `fix: prevent crash on empty username` |
| `refactor:`, `docs:`, `build:`, `ci:`, `chore:`, `style:`, `test:` | **No release** | `refactor: extract auth helper` |
| `feat!:` / `fix!:` or `BREAKING CHANGE:` in the body | **MAJOR** | `feat!: rewrite auth API` |

When a push contains multiple commits, the highest applicable bump wins (a single `feat:` among many `fix:` triggers a MINOR bump). If only release-neutral types (`refactor`, `docs`, `chore`, etc.) are present, no new version is published. If you squash-merge PRs, configure the repo to use the PR title as the squash commit message and write the **PR title** following the convention.

### Skipping a release

If you need to push a change to `main` without producing a release (e.g. tweaking job names in the workflow, fixing a typo in the README), append `[skip release]` to the commit message. The validation jobs (lint, test, build) still run; only `prepare-release`, `build-windows-exe` and `publish-release` are skipped.

```bash
git commit -m "ci: rename build job for clarity [skip release]"
```

To skip **everything** including validation, use GitHub's standard `[skip ci]` marker instead.

### Where the build outputs live

| Output | Location |
|---|---|
| Validation logs (lint, tests) | **Actions** tab on GitHub |
| Linux smoke-build binary | Ephemeral, inside the runner |
| Windows `.exe` per version | **Releases** page (sidebar of the repo) |
| Version history & notes | [`CHANGELOG.md`](CHANGELOG.md) + Releases page |

> **Note:** GitHub's **Packages** section is for package registries (npm, PyPI, Docker, etc.) and does not host PyInstaller executables. Standalone binaries always live under **Releases**.

### Repository setup required for releases

For the release jobs to push tags and commits back to `main`, the repository needs:

1. **Settings → Actions → General → Workflow permissions**: set to *Read and write permissions*.
2. **Branch protection on `main`**: if enabled, allow the `github-actions[bot]` to bypass the PR requirement, or disable the protection for the bot. Otherwise `prepare-release` will fail when pushing the version bump.

### Running the same checks locally

```bash
# lint-and-audit
ruff check .
ruff format --check .
mypy --config-file=pyproject.toml .
pip-audit --skip-editable

# test
pytest --tb=short

# build
pyinstaller app.spec
```

## Production

The `app.spec` file bundles the repository-level `.env` directly into the final executable. This means whatever values are in `.env` at build time will be shipped to end users. Before building a production artifact:

1. Set production values directly in `.env` (e.g. `ENVIRONMENT=production`).
2. Treat any binary built with a development `.env` as non-distributable.

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/oratio`](https://www.diegolibonati.com.ar/#/project/oratio)
