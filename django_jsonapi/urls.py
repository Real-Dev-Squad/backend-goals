from django.urls import include, path
from rest_framework import routers
from goals import views as goal_views
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'goal', goal_views.GoalViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include('authCustom.urls')),
    path("admin/", admin.site.urls)
]
