from rest_framework_simplejwt.tokens import RefreshToken

def get_user_token(user):
    return f'Bearer {str(RefreshToken.for_user(user).access_token)}'