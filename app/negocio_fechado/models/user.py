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

USER_TYPE = (
    ('WORKER', 'Prestador de serviço.'),
    ('CONSUMER', 'Consumidor.')
)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField("Email", max_length=255) 
    password = models.CharField("Senha", max_length=32)
    first_name = models.CharField("Nome", max_length=45)
    last_name = models.CharField("Sobrenome", max_length=45)
    photo = models.FileField("Foto do perfil", max_length=255)
    birth_date = models.DateField("Idade", max_length=255)
    cpf = models.CharField("CPF", max_length=14)
    type = models.CharField("Tipo", choices=USER_TYPE, max_length=255)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)