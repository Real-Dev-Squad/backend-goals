from rest_framework import permissions
from .utils import env

class RestKeyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        key = request.headers.get('Rest-Key')
        return key == env('REST_KEY')