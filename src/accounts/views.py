from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from accounts.models import User
from accounts.serializers import RegisterUserSerializer


class RegisterUserView(APIView):
    """
    Registering user with phone number and password into db.
    """

    serializer_class = RegisterUserSerializer

    def post(self, request: Request) -> Response:
        """
        *notice*: **this view is only for test and it's need a lot of validations!**

        Create User with post method

        param : `phone_number` : user phone number

        param : `password` : user password

        param : `confirm_password` : confirm password

        ### retrun :
        ```json
            {
                "message":"success"
            }
        ```

        """

        req_data = request.data

        serializer = self.serializer_class(data=req_data)

        serializer.is_valid(raise_exception=True)

        User.objects.create_user(
            phone_number=serializer.validated_data["phone_number"],
            password=serializer.validated_data["password"],
            is_active=False,
        )

        return Response({"message": "success"})
