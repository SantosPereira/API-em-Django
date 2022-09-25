"""
ASGI config for Web_Service_Django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from http import server
import os

from django.core.asgi import get_asgi_application
from uvicorn import Config, Server

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Web_Service_Django.settings')

application = get_asgi_application()

def run():
    config = Config(app=application, port=8000)
    server = Server(config=config)
    server.run()
