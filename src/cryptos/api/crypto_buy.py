from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from cryptos.selectors import calcualte_crypto_price


class BuyCryptoAPI(APIView):
    permission_classes = (IsAuthenticated,)

    class InputSerializer(serializers.Serializer):
        crypto_id = serializers.IntegerField()
        amount = serializers.IntegerField()

    @extend_schema(request=InputSerializer)
    def post(self, request) -> Response:
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        price_to_buy = calcualte_crypto_price(
            crypto_id=serializer.validated_data.get("crypto_id"),
            amount=serializer.validated_data.get("amount"),
        )

        return Response({"data": price_to_buy})
