from rest_framework_json_api import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "rds_id", "created_at", "modified_at", "roles"]


class CreateUserSerializer(UserSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "rds_id", "token",
                  "created_at", "modified_at", "roles"]

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "exp": refresh.payload["exp"],
            "access": str(refresh.access_token)
        }

    def create(self, validated_data):
        if self.is_valid():
            return User.objects.create_user(**validated_data)
