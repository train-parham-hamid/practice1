

from rest_framework import serializers
from users.models import User


class InputUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

class OutputUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)
