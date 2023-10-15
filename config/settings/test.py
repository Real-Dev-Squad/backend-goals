from .base import *

# Over writing settings from base with development settings

SECRET_KEY = env('SECRET_KEY')

PORT = env('PORT')

DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = ['localhost', '.realdevsquad.com', '0.0.0.0']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
