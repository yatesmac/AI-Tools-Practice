# Todo Flow (Django)

Lightweight, good-looking TODO tracker with due dates and resolution state. Built for Windows 11 using Django.

## Setup
- Install Python 3.11+.
- Create and activate a virtual environment (PowerShell example):
  - `python -m venv .venv`
  - `.\.venv\Scripts\Activate.ps1`
- Install dependencies: `pip install -r requirements.txt`
- Run database migrations: `python manage.py migrate`
- (Optional) Create an admin user: `python manage.py createsuperuser`

## Run
- Start the dev server: `python manage.py runserver`
- Visit http://127.0.0.1:8000/ to add, edit, resolve, and delete todos.

## Tests
- Execute the test suite: `python manage.py test`

## App Notes
- Todos track title, description, optional due date, and resolved flag.
- Home page lets you create items inline and manage them with quick edit/resolve/delete actions.
- Styling lives in `static/css/styles.css`; templates live in `templates/`.
