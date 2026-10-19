# HireTrack — Placement Tracker

Django job-application tracker with responsive HTML, CSS, and JavaScript frontend.

## Features
- Registration and sign-in
- Dashboard statistics
- Add, edit, search, filter, and delete applications
- Add and manage companies
- User-specific records and SQLite database

## Run on Windows CMD
```bat
cd path\to\placement_tracker_full_project
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py makemigrations applications
python manage.py migrate
python manage.py runserver
```
Open `http://127.0.0.1:8000/`, then create an account.

Optional admin account:
```bat
python manage.py createsuperuser
```
Open `http://127.0.0.1:8000/admin/`.

This project is configured for local development. Review Django deployment security settings before putting it on the public internet.
