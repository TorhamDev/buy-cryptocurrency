from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from utils.exceotions import InsufficientWalletBalance
from cryptos.selectors import calcualte_crypto_price, is_user_balance_enough
from cryptos.services import buy_crypto_for_user


class BuyCryptoAPI(APIView):
    """API to buy cryptos"""

    permission_classes = (IsAuthenticated,)

    class BuyCryptoInputSerializer(serializers.Serializer):
        """
        Input serializer for buy cryptos API.
        **only responseble for serializing input data.**
        """

        crypto_name = serializers.CharField()
        amount = serializers.IntegerField()

    @extend_schema(request=BuyCryptoInputSerializer)
    def post(self, request) -> Response:
        """
        This api is responsible for purchasing cryptocurrency for users.
        After the purchase,
        the balance will be deducted from the user's account
        and a purchase record will be created so that it can be dealt with as soon as possible.
        """

        serializer = self.BuyCryptoInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        crypto_name = serializer.validated_data.get("crypto_name")
        amount = serializer.validated_data.get("amount")

        price_to_buy = calcualte_crypto_price(
            crypto_name=crypto_name,
            amount=amount,
        )

        if is_user_balance_enough(self.request.user, price_to_buy):
            buy_crypto_for_user(
                user=self.request.user,
                c_name=crypto_name,
                c_amount=amount,
                price=price_to_buy,
            )
            return Response({"price": price_to_buy})

        raise InsufficientWalletBalance
