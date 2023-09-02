from base.base_views import ModelBaseViewSet

from user.models import User
from user.v1.serializer import UserSerializer
from base.utils import env
from user.permission import RestKeyPermission

class UserViewSet(ModelBaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [RestKeyPermission]

    