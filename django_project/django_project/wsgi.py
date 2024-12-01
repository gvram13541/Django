import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

application = get_wsgi_application()



# POINTS TO REMEMBER:

# The wsgi.py file is used to expose the WSGI callable as a module-level variable named application.
# The WSGI callable is used by the WSGI server to communicate with the Django application.
# The get_wsgi_application() function is used to get the WSGI application object.
# The os.environ.setdefault() function is used to set the DJANGO_SETTINGS_MODULE environment variable to the settings module of the Django project.
