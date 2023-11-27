from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from apps.goals.views import GoalViewSet
from apps.user.v1.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'goal', GoalViewSet)

urlpatterns = [
    path("admin/", admin.site.urls)
]

# apps urls
urlpatterns += [
    path("api/v1/", include(router.urls)),
]
