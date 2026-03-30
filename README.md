[![Build Status](https://github.com/swe-students-spring2026/3-package-sand_cat/actions/workflows/ci.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-sand_cat/actions)

# Sand Cat

**Sand Cat** is a lighthearted and fun Python package designed to bring a little bit of joy, levity, and cuteness to developers' terminals. Inspired by the adorable sand cat, this package generates ASCII cat art, delivers cute greetings, predicts fortunes, and offers comforting words to developers when they face bugs. 

**PyPI Package Link**: [sand-cat on PyPI](https://pypi.org/project/sand-cat/)

---

## Team Members
* [Hollan Yuan](https://github.com/hwyuanzi)
* [Tuo Zhang](https://github.com/TuoZhang0902)
* [Team Member 3 Name](https://github.com/username3)
* [Team Member 4 Name](https://github.com/username4)
* [Team Member 5 Name](https://github.com/username5)

---

## Installation & User Guide

To import and use this package in your own Python projects, simply install it via `pip`:

```bash
pip install sand-cat
```

### Example Program
We have created a complete example program that utilizes all the functions provided by `sandcat_fun`. 
You can view and run the full demonstration here: **Example Program (`demo.py`)**

### Core Functions and Code Examples

Our package comes with four core interactive functions. Here is how you can use them:

#### 1. `cat_greeting(name: str, mood: str)`
Return a playful cat-style greeting based on the user's name and mood.

```python
from sandcat_fun import cat_greeting

# Happy mood
greeting = cat_greeting("Hollan", mood="happy")
print(greeting)

# Grumpy mood
greeting = cat_greeting("Hollan", mood="grumpy")
print(greeting)
```

#### 2. `get_fortune(treats: int = 1)`
The magical sand cat predicts your fortune. The more treats (fish) you offer, the better your fortune might be!

```python
from sandcat_fun import get_fortune

# Give the cat 5 treats
fortune = get_fortune(treats=5)
print(fortune)
# Output example: "Meow! Thank you! Your code will compile flawlessly today!"
```

#### 3. `cat_comfort(level: int = 1)`
A function for developers who are stuck on a bug. The sand cat provides comforting words.

```python
from sandcat_fun import cat_comfort

# High level of comfort needed
comfort_msg = cat_comfort(level=3)
print(comfort_msg)
# Output example: "Purrrr... Everything will be okay. Take a break, drink some water. <3"
```

#### 4. `draw_cat(style: str = "sleeping")`
Generates and returns various cute ASCII cat text arts depending on the style parameter.

```python
from sandcat_fun import draw_cat

# Draw a stretching cat
art = draw_cat(style="stretching")
print(art)
```

---

## Contributor Guide

If you want to contribute to the project, follow these instructions to set up the development environment, install dependencies, run tests, and build the project on any platform.

### 1. Prerequisites
Make sure you have Python 3.9+ and `pipenv` installed on your machine.
```bash
pip install --user pipenv
```

### 2. Setup the Environment
Clone this repository and use `pipenv` to install all dependencies (including development tools like `pytest`, `build`, and `twine`).

```bash
git clone https://github.com/swe-students-spring2026/3-package-sand_cat.git
cd 3-package-sand_cat

# Create virtual environment and install dependencies
pipenv install --dev

# Activate the virtual environment
pipenv shell
```

### 3. Environment Variables & Configuration
If the project requires any specific environment variables to run properly, please refer to the `.env.example` file provided in the root directory.

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```
2. Open the `.env` file and replace the dummy values with your actual configuration keys.

### 4. Running Tests
We use `pytest` for unit testing to ensure our functions behave as expected (with a minimum of 3 assertions per function).

To run the test suite:
```bash
pytest -v
```

### 5. Building the Package
To build the distribution artifacts (wheel and source distribution) using `build`:

```bash
python -m build
```
This will generate the built files in the `dist/` directory.

### 6. Distributing / Publishing to PyPI
To upload the newly built package to PyPI (or TestPyPI) using `twine`:

```bash
# For TestPyPI
python -m twine upload --repository testpypi dist/*

# For actual PyPI
python -m twine upload dist/*
```

---

# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.