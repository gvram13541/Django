from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', 
        PasswordResetView.as_view(template_name = "customers/password_reset.html"), 
        name='password_reset'),
    path('password-reset/done/',
        PasswordResetDoneView.as_view(template_name = "customers/password_reset_done.html"), 
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name = "customers/password_reset_confirm.html"), 
        name='password_reset_confirm'),
    path('password-reset-complete/',
        PasswordResetCompleteView.as_view(template_name = "customers/password_reset_complete.html"), 
        name='password_reset_complete'),
]