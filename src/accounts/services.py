from accounts.models import User
from django.db.models import QuerySet


def create_user(phone_number, password) -> QuerySet:
    """
    Creating user
    """
    return User.objects.create_user(
        phone_number=phone_number,
        password=password,
    )
