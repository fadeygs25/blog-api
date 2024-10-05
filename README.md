Dưới đây là phiên bản đã chỉnh sửa của README, bao gồm phần hướng dẫn migration từ đầu đến cuối:

---

# Blog API Project

## Introduction
This project builds a Blog API with CRUD (Create, Read, Update, Delete) functionality using Django and Django REST Framework. The project applies design patterns such as Service Layer, Repository Layer, and Factory to manage business logic and is structured according to modern software development standards.

## Directory Structure
```
my_project/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   ├── testing.py
│   │   ├── ci_cd.py
│   ├── urls.py
│   ├── wsgi.py
├── apps/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── blog_service.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── blog_repository.py
│   │   ├── factories/
│   │   │   ├── __init__.py
│   │   │   ├── blog_factory.py
├── static/
├── media/
├── templates/
├── logs/
├── scripts/
├── tests/
├── docs/
├── requirements/
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── .env
├── Makefile
```

## System Requirements

- Python 3.9+
- Django 3.x+
- PostgreSQL (recommended for production environment)
- Docker and Docker Compose (optional)

## Installation

### Step 1: Create and Configure the Project Environment

1. **Create the main directory for the project:**

```bash
mkdir my_project
cd my_project
```

2. **Create and activate a virtual environment:**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install Django and required packages:**

```bash
pip install django djangorestframework
```

4. **Initialize the Django project:**

```bash
django-admin startproject config .
```

### Step 2: Create Apps and Configure the Directory Structure

1. **Create the `core` app:**

```bash
python manage.py startapp core
```

2. **Create necessary directories:**

```bash
mkdir -p config/settings apps/core/{services,repositories,factories} static/css static/js static/images media/uploads templates/core logs scripts tests docs requirements
```

### Step 3: Configure `settings.py`

1. **Create basic configuration in `config/settings/base.py`:**

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
```

2. **Configure database and environments in `development.py`, `production.py`, etc.**

### Step 4: Build the Blog API

1. **Create Blog Post model in `apps/core/models.py`:**

```python
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

2. **Create Serializer in `apps/core/serializers.py`:**

```python
from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
```

3. **Create Repository in `apps/core/repositories/blog_repository.py`:**

```python
from .models import BlogPost

class BlogPostRepository:
    def get_all_posts():
        return BlogPost.objects.all()
```

4. **Create Service in `apps/core/services/blog_service.py`:**

```python
from apps.core.repositories.blog_repository import BlogPostRepository

class BlogPostService:
    def list_all_posts():
        return BlogPostRepository.get_all_posts()
```

5. **Create Views and URL:**

```python
from rest_framework import viewsets
from .services.blog_service import BlogPostService

class BlogPostViewSet(viewsets.ViewSet):
    def list(self, request):
        posts = BlogPostService.list_all_posts()
        return Response(posts)
```

### Step 5: Set Up Database and Migrations

1. **Configure Database:**

Ensure your database configuration is correct in the `config/settings/development.py` file (or the relevant environment file). For example, with PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

2. **Run Migrations:**

Once your models are set up, it's time to apply migrations. Follow these steps:

- First, create migration files based on the changes in your models:

```bash
python manage.py makemigrations
```

- Then, apply those migrations to your database:

```bash
python manage.py migrate
```

3. **Run Migrations for Core App:**

Once your models are set up, it's time to apply migrations. Follow these steps:

- First, ensure the `core` app's models are ready for migration:

```bash
python manage.py makemigrations core
```

- Then, apply those migrations to your database:

```bash
python manage.py migrate core
```

### Step 6: Run the Project

1. **Run the development server:**

```bash
python manage.py runserver
```

2. **Access `http://127.0.0.1:8000/api/posts/` to use the Blog API.**

---

This README now includes instructions for setting up and running migrations as part of the Blog API project with Django.