from rest_framework import serializers
from authCustom.models import Token_Custom

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token_Custom
        fields = "__all__"