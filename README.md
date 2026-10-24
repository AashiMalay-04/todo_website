
# To-Do List

A beginner-friendly full-stack to-do website built with Python and Flask. It lets users add, complete, undo, edit, and delete tasks through a clean checklist interface.

## Features

- Add new tasks
- Mark tasks complete with a checkbox
- Undo completed tasks
- Edit task text
- Delete tasks
- Reveal task actions by double-clicking a task
- Store tasks locally with SQLite
- Save project history with Git and GitHub
- Deploy the Flask app with Render

## Built With

- **Python** — application logic
- **Flask** — routes, forms, and HTML template rendering
- **SQLite** — local task database
- **HTML, CSS, and JavaScript** — interface and interactions
- **Gunicorn** — production server used by Render

## Run Locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
