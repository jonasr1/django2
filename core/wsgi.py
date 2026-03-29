"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from decouple import config
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()


if config("RENDER") == "true":
    try:
        from core.create_superuser import *  # noqa: F403
    except Exception as e:  # noqa: BLE001
        print("Error creating superuser:", e)
