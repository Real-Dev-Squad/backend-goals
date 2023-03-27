from .base import *

# Over writing settings from base with development settings
 
SECRET_KEY = env('SECRET_KEY', default='$_SECRET_KEY_$')

PORT = env('PORT')

DEBUG = env('DEBUG', default=True)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.realdevsquad.com']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env('DB_NAME', default=BASE_DIR / 'db.sqlite3'),
    }
}


# Over writing configs with configs from local.py, If available
# All settings that are defined in local.py will be over write the setting present in this file
try:
    from .local import *
except ImportError:
    print('"local.py" NOT-FOUND, Please create it in "django_jsonapi/settings" folder')
    
