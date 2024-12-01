# from django.urls import path
# from . import views
# from django.contrib.auth.views import (
#         LoginView, 
#         LogoutView, 
#         PasswordResetView,
#         PasswordResetDoneView,
#         PasswordResetConfirmView,
#         PasswordResetCompleteView,
# )
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
#     path('verify-otp/', views.verify_otp, name='verify_otp'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('profile/', views.profile, name='profile'),
#     path('password_reset/', 
#          PasswordResetView.as_view(template_name="users/password_reset.html"), 
#          name='password_reset'),
#     path('password_reset/done/', 
#          PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), 
#          name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', 
#          PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), 
#          name='password_reset_confirm'),
#     path('reset/done/', 
#          PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), 
#          name='password_reset_complete'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

## to test wheather the email is working or not
# from django.urls import path
# from .views import test_email

# urlpatterns = [
#     path('test_email/', test_email, name='test_email'),
# ]

from django.urls import path
from . import views
from django.contrib.auth.views import (
        LogoutView, 
        PasswordResetView,
        PasswordResetDoneView,
        PasswordResetConfirmView,
        PasswordResetCompleteView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Use custom login_view
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_reset/', 
         PasswordResetView.as_view(template_name="users/password_reset.html"), 
         name='password_reset'),
    path('password_reset/done/', 
         PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), 
         name='password_reset_confirm'),
    path('reset/done/', 
         PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), 
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)