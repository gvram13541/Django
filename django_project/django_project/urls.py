from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("blog.urls")),
    path("users/", include("users.urls")),
    path("admin/", admin.site.urls),
]

# POINTS TO REMEMBER:
# For a Django project, the URL configuration is defined in the urls.py file.
# The urlpatterns list is a list of URL patterns that Django will try to match with the requested URL.
# The path() function is used to define a URL pattern.
# The first argument to the path() function is the URL pattern to match.
# The second argument is the view function that should be called when the URL pattern is matched.
# The view function can be a function or a class-based view.
# The path() function can also take optional arguments like name, kwargs, and converters.
