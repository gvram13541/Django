from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from Users.views import UsersListView, UserDetailsView

urlpatterns = [
    path('users/', UsersListView.as_view()),
    path('user_details/<int:pk>', UserDetailsView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)





# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from Users import views

# urlpatterns = [
#     path('listusers/', views.ListAllUsers),
#     path('listusers/<int:pk>/', views.UserView),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
