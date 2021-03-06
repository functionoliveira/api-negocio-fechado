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
    (1, "Enviada"),
    (2, "Aceita"),
    (3, "Recusada")
)

class Tender(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Título", max_length=255)
    description = models.CharField("Descrição", max_length=255)
    offer = models.ForeignKey("Offer", on_delete=models.PROTECT, blank=True, null=True)
    needs = models.ForeignKey("Needs", on_delete=models.PROTECT, blank=True, null=True)
    proposer = models.ForeignKey("User", on_delete=models.PROTECT)
    price = models.CharField("Valor", max_length=255)
    state = models.CharField("Senha", choices=STATE, max_length=255)
  
    def __str__(self):
        return self.title