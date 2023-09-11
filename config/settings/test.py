from .base import *

# Over writing settings from base with development settings

SECRET_KEY = env('SECRET_KEY')

PORT = env('PORT')

DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = ['localhost', '.realdevsquad.com']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env('DB_NAME', default=BASE_DIR / 'db.sqlite3'),
    }
}
