from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import serializers
from drf_spectacular.utils import extend_schema

from accounts.models import User
from accounts.services import create_user


class UserRegisterAPI(APIView):
    """
    Registering user with phone number and password into db.
    """

    class UserRegisterInputSerializer(serializers.ModelSerializer):
        """
        Input serializer for register user.
        **only responseble for serializing input data.**
        """

        password = serializers.CharField()
        confirm_password = serializers.CharField()

        class Meta:
            model = User
            fields = ("phone_number", "password", "confirm_password")

    class UserRegisterOutputSerializer(serializers.ModelSerializer):
        """
        Output serializer for register user.
        **only responseble for serializing output data, without password infos**
        """

        class Meta:
            model = User
            fields = ("phone_number",)

    @extend_schema(
        request=UserRegisterInputSerializer, responses=UserRegisterOutputSerializer
    )
    def post(self, request: Request) -> Response:
        """
        *notice*: **this view is only for test and it's need a lot of validations!**

        Create a User with post method
        """

        input_serializer = self.UserRegisterInputSerializer(data=request.data)

        input_serializer.is_valid(raise_exception=True)
        validated_data = input_serializer.validated_data

        user = create_user(
            phone_number=validated_data.get("phone_number"),
            password=validated_data.get("password"),
        )

        output_serializer = self.UserRegisterOutputSerializer(instance=user)

        return Response(output_serializer.data)
