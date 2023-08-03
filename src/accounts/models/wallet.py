from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model


class Wallet(BaseModel):
    amount = models.BigIntegerField(default=0)
    user = models.OneToOneField(
        to=get_user_model(),
        related_name="wallet",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user.get_full_name()} - {self.amount}"
