from django.urls import include, path
from rest_framework import routers
from django.urls import path
from apps.goals.views import GoalViewSet

router = routers.DefaultRouter()
router.register(r'goal', GoalViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
