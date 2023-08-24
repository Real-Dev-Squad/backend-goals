from .models import Token_Custom
from rest_framework import authentication
from rest_framework import exceptions


class UserAuthenticationExtender():
    def __init__(self, auth_token, userId, created):
        self.auth_token = auth_token
        self.user_id = userId
        self.token_created = created
        self.is_authenticated = True


class TokenCustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            goal_token = request.COOKIES['goal-site-session']
        except Exception:
            return None

        try:
            token = Token_Custom.objects.get(auth_token=goal_token)
            if token.is_invalid():
                raise exceptions.AuthenticationFailed(
                    "Token is expired or invalid")
        except Token_Custom.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                'Token is expired or invalid')

        user = UserAuthenticationExtender(
            token.auth_token, token.user_id, token.token_created)
        return (user, None)
