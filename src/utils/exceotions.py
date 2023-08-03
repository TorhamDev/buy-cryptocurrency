from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidCryptoID(APIException):
    default_detail = "Invalid crypto id We cannot find any crypto with this id."
    status_code = status.HTTP_400_BAD_REQUEST
