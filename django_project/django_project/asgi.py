import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

application = get_asgi_application()


## KEY POINTS ABOUT ASGI:

# ASGI stands for Asynchronous Server Gateway Interface.
# ASGI is a standard interface between web servers and Python web applications or frameworks.
# ASGI is a successor to WSGI (Web Server Gateway Interface).
# ASGI is designed to handle asynchronous I/O operations.
# ASGI is a specification, not a server or framework.
# It exposes the ASGI callable as module-level variable named application. This is used by the ASGI server to communicate with the application.
