[![CI](https://github.com/swe-students-spring2026/3-package-sand_cat/actions/workflows/ci.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-sand_cat/actions)

# 🐱 Sand Cat

**Sand Cat** is a lighthearted and fun Python package designed to bring a little bit of joy, levity, and cuteness to developers' terminals. Inspired by the adorable sand cat, this package generates ASCII cat art, delivers cute greetings, predicts fortunes, reacts dramatically to everyday programming events, and offers comforting words when you're stuck on a bug.

**PyPI**: [sand-cat on PyPI](https://pypi.org/project/sand-cat/)

---

## Team Members
* [Hollan Yuan](https://github.com/hwyuanzi)
* [Tuo Zhang](https://github.com/TuoZhang0902)
* [Yecheng Yue](https://github.com/YechengYueEddy)

---

## Features

| Function | Description | Example |
|---|---|---|
| `cat_greeting(name, mood)` | Playful greeting based on name and mood | `cat_greeting("Tuo", "happy")` |
| `get_fortune(treats)` | Fortune prediction based on treats given | `get_fortune(5)` |
| `cat_comfort(level)` | Comforting words for bug-stuck devs (1–5) | `cat_comfort(3)` |
| `draw_cat(style)` | ASCII cat art in different poses | `draw_cat("ninja")` |
| `cat_energy(weather, energy_level)` | Weather + energy based fortune | `cat_energy("sunny", 8)` |
| `cat_reaction(event, intensity)` | Dramatic reaction to coding events (1–3) | `cat_reaction("deploy", 3)` |

---

## Installation

To use this package in your own Python projects, install it via `pipenv`:

```bash
pipenv install sand-cat
```

Then import it in your code:

```python
from sandcat_fun import cat_greeting, draw_cat, cat_reaction, cat_energy, cat_comfort, get_fortune
```

---

## Usage & Code Examples

### Example Program
We have a complete example program that demonstrates all functions:
**[Example Program (`demo.py`)](./demo.py)**

Run it with:
```bash
python demo.py
```

### Function Details

#### 1. `cat_greeting(name: str, mood: str)`
Return a playful cat-style greeting based on the user's name and mood.

```python
from sandcat_fun import cat_greeting

greeting = cat_greeting("Hollan", mood="happy")
print(greeting)
# "Meow, Hollan! This sand cat is thrilled to see your happy paws today."

greeting = cat_greeting("Hollan", mood="grumpy")
print(greeting)
# "Hiss... just kidding, Hollan. Even grumpy humans deserve a soft sand cat hello."
```

Valid moods: `happy`, `sleepy`, `grumpy`, `excited`, `calm`

#### 2. `get_fortune(treats: int = 1)`
The magical sand cat predicts your fortune. More treats = better fortune!

```python
from sandcat_fun import get_fortune

fortune = get_fortune(treats=5)
print(fortune)
# "Purrr! The Sand Cat is pleased. A bug you've been chasing for days will suddenly make sense today!"
```

#### 3. `cat_comfort(level: int = 1)`
Comforting words for developers stuck on a bug. Level ranges from 1 (mild) to 5 (emergency comfort).

```python
from sandcat_fun import cat_comfort

comfort_msg = cat_comfort(level=5)
print(comfort_msg)
# "PURRRR... developer emergency comfort activated. ..."
```

#### 4. `draw_cat(style: str = "sleeping")`
Generates cute ASCII cat text art in various poses.

```python
from sandcat_fun import draw_cat

art = draw_cat(style="coding")
print(art)
#    /\_/\
#   ( @.@ )  [Bug]
#    > ^ <   /
#   / [___] \
```

Valid styles: `sleeping`, `stretching`, `sitting`, `playing`, `coding`, `ninja`, `loaf`

#### 5. `cat_energy(weather: str, energy_level: int)`
Returns a cat-style fortune based on the current weather and your energy level (1–10).

```python
from sandcat_fun import cat_energy

fortune = cat_energy("sunny", 8)
print(fortune)
# "This is a zoomie-powered cat fortune for a Sunny day: ..."

fortune = cat_energy("rainy", 2)
print(fortune)
# "This is a nap-friendly cat fortune for a Rainy day: ..."
```

Valid weather options: `sunny`, `rainy`, `cloudy`, `snowy`, `windy`

#### 6. `cat_reaction(event: str, intensity: int = 1)`
Returns a dramatic cat reaction to common programming events. Intensity goes from 1 (mild) to 3 (maximum drama).

```python
from sandcat_fun import cat_reaction

reaction = cat_reaction("bug_fixed", 2)
print(reaction)
# "Purrr! The sand cat does a little victory stretch! That bug never stood a chance!"

reaction = cat_reaction("deploy", 3)
print(reaction)
# "MROW!! *hides under desk* IS IT FRIDAY?! WHY ARE WE DEPLOYING?! ROLLBACK PLAN READY?!"
```

Valid events: `bug_fixed`, `code_review`, `deploy`, `merge_conflict`, `friday`, `monday`

---

## Project Structure

```
3-package-sand_cat/
├── sandcat_fun/             # Main package source code
│   ├── __init__.py          # Package exports
│   ├── cat.py               # cat_greeting, cat_comfort, cat_energy
│   ├── draw.py              # draw_cat (ASCII art)
│   ├── fortune.py           # get_fortune
│   └── reaction.py          # cat_reaction
├── tests/                   # Unit tests (pytest)
│   ├── test_cat.py
│   ├── test_draw.py
│   ├── test_fortune.py
│   └── test_reaction.py
├── demo.py                  # Example program using all functions
├── Pipfile                  # pipenv dependency management
├── Pipfile.lock
├── pyproject.toml           # Build configuration
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI workflow
├── LICENSE
└── README.md
```

---

## Contributor Guide

If you want to contribute to the project, follow these steps to set up the development environment on any platform.

### 1. Prerequisites
Make sure you have Python 3.10+ and `pipenv` installed.
```bash
pip install --user pipenv
```

### 2. Clone and Setup
```bash
git clone https://github.com/swe-students-spring2026/3-package-sand_cat.git
cd 3-package-sand_cat

# Create virtual environment and install all dependencies
pipenv install --dev

# Activate the virtual environment
pipenv shell
```

### 3. Running Tests
We use `pytest` for unit testing. Every function has at least 3 assertions covering normal usage, edge cases, and invalid inputs.

```bash
pipenv run pytest -v
```

### 4. Building the Package
Build the wheel and source distribution using `build`:

```bash
python -m build
```
This generates the built files in the `dist/` directory.

### 5. Publishing to PyPI
Upload the package to PyPI using `twine`:

```bash
# For TestPyPI (testing)
python -m twine upload --repository testpypi dist/*

# For PyPI (production)
python -m twine upload dist/*
```

---

## CI/CD Overview

This project uses **GitHub Actions** for continuous integration. The CI workflow (`.github/workflows/ci.yml`) automatically runs on every push and pull request:

- **Builds and tests** the package on **two Python versions** (3.10 and 3.11)
- Uses `pipenv` to install dependencies in an isolated environment
- Runs the full `pytest` test suite to catch regressions early

---

## License

GNU General Public License v3. See `LICENSE` for details.