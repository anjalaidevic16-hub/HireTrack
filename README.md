# HireTrack — Placement Tracker

A Django-based job application tracking web application with a responsive HTML, CSS, and JavaScript frontend. HireTrack helps users organize job applications, manage company information, and monitor their placement progress.

## Features

- **User Authentication:** Registration and sign-in.
- **Dashboard Statistics:** View job application statistics.
- **Application Management:** Add, edit, search, filter, and delete job applications.
- **Company Management:** Add and manage company information.
- **User-Specific Records:** Keep application records associated with individual users.
- **Database Integration:** Store application data using SQLite.
- **Responsive Frontend:** User interface built with HTML, CSS, and JavaScript.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Page structure |
| CSS3 | Styling and responsive layout |
| JavaScript | Frontend interactions |
| SQLite | Database |
| Git and GitHub | Version control and project hosting |

## Project Structure

```text
HireTrack/
├── manage.py
├── config/
├── applications/
├── templates/
├── static/
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The directory structure above is illustrative. Your actual folders may differ.*

## Getting Started

### Prerequisites

- Python installed on your computer
- Git installed if cloning the repository
- A terminal such as Windows Command Prompt

### 1. Clone the Repository

```bash
git clone https://github.com/anjalaidevic16-hub/HireTrack.git
cd HireTrack
```

If `manage.py` is inside a nested project folder, navigate into that folder before continuing.

### 2. Create and Activate a Virtual Environment

```bat
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bat
python -m pip install -r requirements.txt
```

### 4. Configure the Django Secret Key

The application requires the `DJANGO_SECRET_KEY` environment variable if your Django settings use `os.environ["DJANGO_SECRET_KEY"]`.

Generate a new key:

```bat
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Set the generated key in your current Command Prompt session:

```bat
set "DJANGO_SECRET_KEY=YOUR_GENERATED_SECRET_KEY"
```

Replace the placeholder with the generated key. Never publish the actual key on GitHub.

### 5. Set Up the Database

```bat
python manage.py migrate
```

If you have changed the models and need to create new migrations, run:

```bat
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Application

```bat
python manage.py runserver 8001
```

Open the application in your browser:

- **Application:** http://127.0.0.1:8001/
- **Admin panel:** http://127.0.0.1:8001/admin/

Register a user account to get started.

### 7. Create an Administrator (Optional)

```bat
python manage.py createsuperuser
```

Follow the prompts to create an administrator account, then visit the admin panel.

## Security Notes

- Keep the Django secret key private.
- Exclude `.env`, virtual environments, and local database files from Git where appropriate.
- Do not commit passwords or other sensitive information.
- Configure production security settings before deploying the application publicly.

## Future Enhancements

Possible improvements include:

- Application deadline reminders
- Visual analytics and placement reports
- Application status history
- Online deployment

These are potential enhancements, not claims about existing functionality.

## Learning Outcomes

This project demonstrates practical experience with Django development, user authentication, database integration, CRUD operations, frontend development, and GitHub version control.

## Author

**Devi**  
B.Tech — Artificial Intelligence and Data Science

GitHub: [anjalaidevic16-hub](https://github.com/anjalaidevic16-hub)

---

*HireTrack is a portfolio project developed to demonstrate web application development skills.*
