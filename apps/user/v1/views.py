from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from apps.base.base_views import ModelBaseViewSet
from apps.user.models import User
from apps.user.v1.serializer import UserSerializer, CreateUserSerializer
from apps.user.permission import RestKeyPermission
from apps.base.permissions import IsSuperUserPermission


class UserViewSet(ModelBaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = [RestKeyPermission]
        elif self.action in ["list"]:
            self.permission_classes = [IsSuperUserPermission]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        else:
            return UserSerializer

    def create(self, request, *args, **kwargs):
        rds_id = request.data.get("rds_id")
        user = User.objects.filter(rds_id=rds_id).first()
        if user is not None:
            user_serialized = self.get_serializer_class(user)
            headers = self.get_success_headers(user_serialized.data)
            return Response(user_serialized.data, status=status.HTTP_201_CREATED, headers=headers)
        return super().create(request, *args, **kwargs)
