from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
# Over writing settings from base with development settings

SECRET_KEY = env('SECRET_KEY', default='$_SECRET_KEY_$')

PORT = env('PORT')

DEBUG = env('DEBUG', default=True)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.realdevsquad.com', '0.0.0.0']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# Over writing configs with configs from local.py, If available
# All settings that are defined in local.py will be over write the setting present in this file
try:
    from .local import *
except ImportError:
    print('"local.py" NOT-FOUND, Please create it in "config/settings" folder')

sentry_sdk.init(
    dsn="https://92bcf175d3f4477985131f011e405d6e@o4505162173382656.ingest.sentry.io/4505162175217664",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    # send_default_pii=True
)
