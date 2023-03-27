# Sample format for local.py

# Change all necessary settings to overwrite in development.py

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Settings

SECRET_KEY = 'secret_key'

PORT = 5000

DEBUG = True

ALLOWED_HOSTS = ['localhost','.realdevsquad.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
