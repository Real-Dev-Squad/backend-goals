from rest_framework import permissions
from apps.base.constants import SUPER_USER_ROLE, MEMBER_ROLE


def AuthorizationPermissions(roles=[]):
    class AuthorizationPermission:
        def has_permission(self, request, view):
            if not request.user.is_authenticated:
                return False

            user_roles = request.user.roles
            for role in roles:
                if user_roles.get(role, False) is True:
                    return True
                else:
                    continue
            return False

    return AuthorizationPermission
