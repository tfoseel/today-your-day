from .base import *
import dj_database_url
import os

DEBUG = False

# Render 외부에서 접속 허용
ALLOWED_HOSTS = [os.environ.get("RENDER_EXTERNAL_HOSTNAME", "localhost")]

# PostgreSQL DATABASE_URL 환경변수 기반 설정
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# Static 파일 관련 설정 (whitenoise 사용)
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 보안 설정 (배포 시 추가 고려)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
