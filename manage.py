#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from django.conf import settings
from django.core.management.commands.runserver import Command as runserver
import os
import sys
from dotenv import load_dotenv

load_dotenv()


# Defining constants
DJANGO_ENV = 'DJANGO_ENV'
PRODUCTION = 'PRODUCTION'
DEVELOPMENT = 'DEVELOPMENT'
TESTING = 'TESTING'
SETTINGS_PRODUCTION = 'django_jsonapi.settings.production'
SETTINGS_DEVELOPMENT = 'django_jsonapi.settings.development'
SETTINGS_TESTING = 'django_jsonapi.settings.testing'


def main():
    """Run administrative tasks."""

    django_env = os.getenv('DJANGO_ENV', DEVELOPMENT).upper() 
    
    # Setting it to DEVELOPMENT
    django_settings_module = SETTINGS_DEVELOPMENT

    if (django_env == PRODUCTION):
        django_settings_module = SETTINGS_PRODUCTION
    elif (django_env == TESTING):
        django_settings_module = SETTINGS_TESTING
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              django_settings_module)
    
    # Changing DJANGO PORT
    runserver.default_port = settings.__getattr__('PORT')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
