from ._base import *
import os

DEBUG = False

ALLOWED_HOSTS += []

WSGI_APPLICATION = 'config.wsgi.prod.application'

INSTALLED_APPS += [
]

MIDDLEWARE += [
]


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("SQL_HOST"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "NAME": os.environ.get("SQL_NAME"),
        "PORT": os.environ.get("SQL_PORT")
    }
}