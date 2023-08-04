from django.db import models
from django.contrib.auth import get_user_model
from django.db import transaction

from utils.models import BaseModel


class Wallet(BaseModel):
    """users wallet model. used for transactions and buy cryptos."""

    amount = models.BigIntegerField(default=0)
    user = models.OneToOneField(
        to=get_user_model(),
        related_name="wallet",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user.get_full_name()} - {self.amount}"

    @transaction.atomic
    def charge_wallet(self, amount: int) -> int:
        """Charging user wallet. incresing wallet amount."""
        wallet = Wallet.objects.select_for_update().get(pk=self.pk)
        wallet.amount += amount
        wallet.save()
        return wallet.amount

    @transaction.atomic
    def decreasing_wallet(self, amount: int) -> int:
        """decoreasing wallet amount."""
        wallet = Wallet.objects.select_for_update().get(pk=self.pk)
        wallet.amount -= amount
        wallet.save()
        return wallet.amount
