import os

if "RENDER" in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
