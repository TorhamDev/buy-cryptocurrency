from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from cryptos.models import Crypto


class CryptosListAPI(APIView):
    """API to reciveing list of all sellable cryptos"""

    class CryptosListOutputSerializer(serializers.ModelSerializer):
        """
        Input serializer for cryptos list API.
        **only responseble for serializing input data.**
        """

        class Meta:
            model = Crypto
            fields = "__all__"

    @extend_schema(responses=CryptosListOutputSerializer)
    def get(self, request) -> Response:
        """
        This api is responsible of listing all cryptocurrencies that can be purchased to users.
        """

        cryptos = Crypto.objects.all()
        serializer = self.CryptosListOutputSerializer(
            instance=cryptos,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)
