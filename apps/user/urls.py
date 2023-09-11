from django.urls import include, path
from rest_framework import routers
from django.urls import path
from apps.user.v1.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
