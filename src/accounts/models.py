from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager

phone_regex = RegexValidator(
    regex=r"^\+{1}989\d{9}$",
    message="Phone number must be entered in the format: "
    "'+989xxxxxxxxx'. Up to 14 digits allowed.",
)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Users within the system are represented by this model.

    phone_number and password are required. Other fields are optional.
    """

    phone_number = models.CharField(
        _("phone number"),
        validators=[phone_regex],
        max_length=20,
        unique=True,
    )
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    update_at = models.DateTimeField(_("update date"), auto_now=True)
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("is staff"), default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self) -> str:
        return f"{self.phone_number} - {self.get_full_name()}"

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name or ""} {self.last_name or ""}'
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name
