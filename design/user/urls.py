from django.urls import path, include
from .views import user_login, user_logout, register, profile, create_request

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('create-request/', create_request, name='create_request'),
]
