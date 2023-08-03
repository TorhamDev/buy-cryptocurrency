from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from accounts.models import User


class RegisterUserSerializer(ModelSerializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = (
            "phone_number",
            "password",
            "confirm_password",
        )
