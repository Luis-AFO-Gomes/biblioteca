# Biblioteca - Django Project

Project: Django project for a public library management system.
Step-by-step tutorial for Django beginners.

This repository contains a Django project prepared to work on Windows, macOS, and Linux.
Uses virtual environments to manage dependencies and ensure a consistent development environment across different operating systems.

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
Windows might restrict script running in powershell for security reasons. In this case, restrict policy should be changed to allow vertual environment start.<br>
There are to options available:
1. Current section only:
   ```
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
2. Permanent permition for current user
   ```
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   ```
- Confirm policy with:
  ```
  Get-ExecutionPolicy -List
  ```
  Minimum results for each option are:
   1. ```Process          Bypass```
   2. ```CurrentUser    RemoteSigned```
   
   

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
