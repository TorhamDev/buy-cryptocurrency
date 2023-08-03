from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from accounts.models import User
from rest_framework import serializers
from accounts.services import create_user
from drf_spectacular.utils import extend_schema


class UserRegisterAPI(APIView):
    """
    Registering user with phone number and password into db.
    """

    class InputSerializer(serializers.ModelSerializer):
        password = serializers.CharField()
        confirm_password = serializers.CharField()

        class Meta:
            model = User
            fields = ("phone_number", "password", "confirm_password")

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ("phone_number",)

    @extend_schema(request=InputSerializer, responses=OutputSerializer)
    def post(self, request: Request) -> Response:
        """
        *notice*: **this view is only for test and it's need a lot of validations!**

        Create a User with post method
        """

        req_data = request.data

        input_serializer = self.InputSerializer(data=req_data)

        input_serializer.is_valid(raise_exception=True)
        data = input_serializer.validated_data

        output_serializer = self.OutputSerializer(
            instance=create_user(
                phone_number=data.get("phone_number"),
                password=data.get("password"),
            )
        )

        return Response(output_serializer.data)
