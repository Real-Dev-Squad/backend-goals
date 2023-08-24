from rest_framework import permissions
from .utils import env

class RestKeyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        key = request.META.get('REST_KEY')  # Replace with your actual header key name
        # Check if the key is correct (you can replace 'YOUR_CORRECT_KEY' with your actual key)
        return key == env('REST_KEY')