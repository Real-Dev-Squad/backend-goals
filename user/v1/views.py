from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.v1.serializer import UserSerializer
from base.utils import env
from user.permission import RestKeyPermission

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [RestKeyPermission]

    