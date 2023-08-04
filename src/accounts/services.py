from accounts.models import User, Wallet
from django.db.models import QuerySet


def create_user(phone_number, password) -> QuerySet:
    """
    Creating user and a wallt for it
    """
    user = User.objects.create_user(
        phone_number=phone_number,
        password=password,
    )

    Wallet.objects.create(user=user)

    return user
