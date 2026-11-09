# CISC 217 Week 13 — Web UI Fundamentals

This lab adds a browser-based user interface to a working FastAPI character API.

## Learning Goals

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

## Required Work

Complete the TODOs in:

- `src/cisc217_week13/main.py`
- `src/cisc217_week13/templates/index.html`
- `src/cisc217_week13/static/styles.css`
- `src/cisc217_week13/static/app.js`

Do not modify the provided tests unless instructed by your instructor.

## One-Time JupyterHub Setup

Check whether `jupyter-server-proxy` is installed:

```bash
/opt/conda/bin/python -m pip show jupyter-server-proxy
```

If it is not installed:

```bash
/opt/conda/bin/python -m pip install --user jupyter-server-proxy
```

Enable it:

```bash
/opt/conda/bin/jupyter server extension enable \
  --py jupyter_server_proxy \
  --user
```

Verify:

```bash
/opt/conda/bin/jupyter server extension list | grep -i -A3 proxy
```

You should see `jupyter_server_proxy enabled`.

If you just installed or enabled it, restart your JupyterHub server/session before continuing.

## Run the Application in JupyterHub

Activate the project environment:

```bash
source .venv/bin/activate
```

Start the application:

```bash
uvicorn cisc217_week13.main:app \
  --host 127.0.0.1 \
  --port 8000 \
  --root-path "${JUPYTERHUB_SERVICE_PREFIX}proxy/8000"
```

Leave that terminal running.

Open the application:

https://sdccd-jupyterhub.nrp-nautilus.io/hub/user-redirect/proxy/8000

API documentation:

https://sdccd-jupyterhub.nrp-nautilus.io/hub/user-redirect/proxy/8000/docs

## Troubleshooting

Verify that FastAPI itself is responding:

```bash
curl -i http://127.0.0.1:8000/
```

A working application should return:

```text
HTTP/1.1 200 OK
```

If FastAPI responds but the browser displays a Jupyter 404 page, verify:

```bash
/opt/conda/bin/jupyter server extension list | grep -i -A3 proxy
```

If the extension was just installed or enabled, restart your JupyterHub server/session and start Uvicorn again.

## Run Tests

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