from django.core.asgi import get_asgi_application
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
from ws.middleware import websockets

application = get_asgi_application()
application = websockets(application)
