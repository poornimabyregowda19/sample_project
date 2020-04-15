"""
WSGI config for cmms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

if os.getenv("SIMPLE_SETTINGS") and not os.getenv("SIMPLE_SETTINGS") in ["cmms.settings.development", "cmms.settings.production"]:
    os.environ.setdefault("SIMPLE_SETTINGS", "cmms.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmms.settings.development")


application = get_wsgi_application()
