from .base import *
import dj_database_url
import os

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost").split(",")

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
