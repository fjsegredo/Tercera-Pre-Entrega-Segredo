"""
ASGI config for Tercera_Pre_Entrega_Segredo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tercera_Pre_Entrega_Segredo.settings')

application = get_asgi_application()
