from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'today',
        'USER': 'today',
        'PASSWORD': 'today',
        'HOST': 'db',
        'PORT': '5432',
    }
}
