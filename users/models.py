
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from .model_managers import CustomUserAccountManager

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # User model supporting email instead of username
    email = models.EmailField(_("Your correct email"),
                              max_length=255, unique=True)
    name = models.CharField(_("Your full name"), max_length=100)
    gender = models.CharField(
        _("Your Gender"), max_length=6, choices=GENDER_CHOICES)
    phone_number = models.CharField(_("Your phone number"), max_length=40)
    country = CountryField(_("Your country"), default="KE")
    net_worth = models.CharField(_("Your estimated net worth"), max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # Overiding the default model manager to user our Custom model manager
    objects = CustomUserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.name.split()[0]
