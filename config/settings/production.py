from .base import *

# Over writing settings from base with production settings

SECRET_KEY = env('SECRET_KEY')

PORT = env('PORT')

DEBUG = env('DEBUG', default=False)

DEFAULT_ALLOWED_HOSTS_STRING = '.realdevsquad.com'

ALLOWED_HOSTS = env(
    'ALLOWED_HOSTS', default=DEFAULT_ALLOWED_HOSTS_STRING).split(' ')

