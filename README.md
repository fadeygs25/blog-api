# Blog API Project

## Introduction
This project builds a Blog API with CRUD (Create, Read, Update, Delete) functionality using Django and Django REST Framework. The project applies design patterns such as Service Layer, Repository Layer, and Factory to manage business logic and is structured according to modern software development standards.

## System Requirements

- Python 3.9+
- Django 3.x+
- PostgreSQL (recommended for production environment)
- Docker and Docker Compose (optional)

## Installation

### Step 1: Set Up Project Environment

1. **Create and activate a virtual environment:**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. **Install required packages:**

```bash
pip install -r requirements.txt
```

3. **Initialize the Django project:**

```bash
django-admin startproject config .
```

### Step 2: Set Up the Database

1. **Ensure your database is correctly configured in the `settings.py` file (e.g., using PostgreSQL).**

### Step 3: Run Migrations

1. **Apply migrations to set up your database schema:**

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Run the Project

1. **Start the development server:**

```bash
python manage.py runserver
```

2. **Access the API at `http://127.0.0.1:8000/api/posts/`.**

---
