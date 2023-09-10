from rest_framework import permissions


class IsSuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return False
