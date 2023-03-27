from django.urls import path
from .views import goal_auth_token

urlpatterns = [
    path('get_token/<str:userId>', goal_auth_token),
]
