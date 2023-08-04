from django.db.models import QuerySet
from accounts.models import User, Wallet


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
