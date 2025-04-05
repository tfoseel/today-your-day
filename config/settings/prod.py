from .base import *
import dj_database_url
import os

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["web-production-2f16.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ["https://web-production-2f16.up.railway.app"]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
