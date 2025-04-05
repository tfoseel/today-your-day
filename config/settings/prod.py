from .base import *
import dj_database_url
import os

DEBUG = False

host = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
ALLOWED_HOSTS = [host] if host else ["localhost"]

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# whitenoise static 설정
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 보안 설정
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
