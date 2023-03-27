from .models import Token_Custom
from rest_framework import authentication
from rest_framework import exceptions


class UserAuthenticationExtender():
    def __init__(self, auth_token, userId, created):
        self.auth_token = auth_token
        self.userId = userId
        self.created = created
        self.is_authenticated = True


class TokenCustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            goal_token = request.COOKIES['goal-site-session']
        except Exception:
            return None

        try:
            token = Token_Custom.objects.get(auth_token=goal_token)
            if token.is_invalid(token.created.timestamp()):
                raise exceptions.AuthenticationFailed(
                    "Token is expired or invalid")
        except Token_Custom.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                'Token is expired or invalid')

        user = UserAuthenticationExtender(
            token.auth_token, token.userId, token.created)
        return (user, None)
