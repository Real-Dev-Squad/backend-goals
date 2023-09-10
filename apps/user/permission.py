from rest_framework import permissions
from django.conf import LazySettings

settings = LazySettings()


class RestKeyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        key = request.headers.get('Rest-Key')
        return key == settings.RDS_BACKEND_SECRET_KEY
