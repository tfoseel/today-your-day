import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise  # 🔹 추가

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(
    os.path.dirname(__file__), 'staticfiles'))  # 🔹 추가
