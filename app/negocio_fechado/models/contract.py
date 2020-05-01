import datetime
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from datetime import datetime, timedelta, timezone, tzinfo

STATE = (
    (1, "Aberto"),
    (2, "Fechado"),
    (3, "Aceito pelo consumidor"),
    (4, "Aceito pelo prestador"),
    (5, "Aceito por ambos")
)

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    offer = models.ForeignKey("Offer", on_delete=models.PROTECT, blank=True, null=True)
    needs = models.ForeignKey("Needs", on_delete=models.PROTECT, blank=True, null=True)
    rules = models.TextField("Regras", null=True, blank=True)
    state = models.CharField("Estado", choices=STATE, max_length=255)