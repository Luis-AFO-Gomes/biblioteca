# Biblioteca - Django Project

This repository contains a Django project prepared to work on Windows, macOS, and Linux.

## Project structure

```text
biblioteca/
├── .gitignore
├── README.md
├── requirements.txt
├── db.sqlite3
├── manage.py
├── biblioteca/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── books/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

## Requirements

- Python 3
- Git

## Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

## Create and activate a virtual environment

The recommended virtual environment folder name is `.venv`.

### Windows

Create the virtual environment:

```bash
py -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

If `py` is not available, use:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

### Linux

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

## Install dependencies

With the virtual environment activated, run:

```bash
pip install -r requirements.txt
```

## Apply migrations

```bash
python manage.py migrate
```

## Run the development server

```bash
python manage.py runserver
```

Open in the browser:

```text
http://127.0.0.1:8000/
```

## Notes

- The file `db.sqlite3` is intentionally kept in the repository.
- The virtual environment folder `.venv` is ignored by Git.
- After adding new Python packages, update `requirements.txt`.

## Update requirements

```bash
pip freeze > requirements.txt
```