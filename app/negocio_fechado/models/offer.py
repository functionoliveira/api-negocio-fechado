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
    (1, "Recente"),
    (2, "Com proposta"),
    (3, "Em negociação"),
    (4, "Falta assinar"),
    (5, "Em execução"),
    (6, "Finalizado"),
)

class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Título", max_length=255)
    description = models.CharField("Descrição", max_length=255)
    worker = models.ForeignKey("User", on_delete=models.PROTECT)
    price = models.CharField("Valor", max_length=255)
    state = models.CharField("Estado", choices=STATE, max_length=255)
    files = models.FileField("Anexos", upload_to='attachments/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.title