from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('buyer_home/', views.buyer_home, name='buyer_home'),
    path('seller_home/', views.seller_home, name='seller_home'),
    path('password-reset/', 
        PasswordResetView.as_view(template_name="customers/password_reset.html"), 
        name='password_reset'),
    path('password-reset/done/',
        PasswordResetDoneView.as_view(template_name="customers/password_reset_done.html"), 
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name="customers/password_reset_confirm.html"), 
        name='password_reset_confirm'),
    path('password-reset-complete/',
        PasswordResetCompleteView.as_view(template_name="customers/password_reset_complete.html"), 
        name='password_reset_complete'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('place_order/', views.place_order, name='place_order'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)