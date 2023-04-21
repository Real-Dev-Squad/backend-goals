from django.urls import path, include
from authCustom.v1.views import GoalAuthTokenViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'auth_token', GoalAuthTokenViewSet, basename='auth_token')

urlpatterns = [
    path('', include(router.urls)),
]
