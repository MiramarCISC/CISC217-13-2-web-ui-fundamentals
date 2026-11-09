# CISC 217 Week 13 — Web UI Fundamentals

This lab adds a browser-based user interface to a working FastAPI character API.

## Learning goals

You will practice:

- rendering HTML with Jinja2
- serving CSS and JavaScript as static files
- building accessible HTML forms
- using CSS selectors and the box model
- calling FastAPI endpoints with JavaScript `fetch()`
- updating the page using the DOM
- keeping UI code separate from API logic

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
python -m pytest -q
```

Several tests should fail initially.

## Required work

Complete the TODOs in:

- `src/cisc217_week13/main.py`
- `src/cisc217_week13/templates/index.html`
- `src/cisc217_week13/static/styles.css`
- `src/cisc217_week13/static/app.js`

Do not modify the provided tests unless instructed by your instructor.

## Run the application

```bash
uvicorn cisc217_week13.main:app --reload
```

Open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

## Run tests

```bash
python -m pytest -q
```

Individual files:

```bash
python -m pytest -q tests/test_api.py
python -m pytest -q tests/test_ui_route.py
python -m pytest -q tests/test_html.py
python -m pytest -q tests/test_static.py
python -m pytest -q tests/test_javascript.py
```

Push your completed work and confirm the Classroom50 autograder passes.
