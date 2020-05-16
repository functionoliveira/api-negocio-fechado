import datetime
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

from datetime import datetime, timedelta, timezone, tzinfo

USER_TYPE = (
    ('WORKER', 'Prestador de serviço.'),
    ('CONSUMER', 'Consumidor.')
)

class UserManager(BaseUserManager):
    """
        Classe que extende a BaseUserManager padrão de authenticação do django,
        a mesma sobrescreve o método de criação de usuário comum.
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField("Email", unique=True, max_length=255) 
    password = models.CharField("Senha", max_length=32)
    first_name = models.CharField("Nome", max_length=45)
    last_name = models.CharField("Sobrenome", max_length=45)
    photo = models.FileField("Foto do perfil", blank=True, null=True, max_length=255)
    birth_date = models.DateField("Data de nascimento", max_length=255)
    cpf = models.CharField("CPF", unique=True, validators=[UnicodeUsernameValidator()], max_length=14)
    type = models.CharField("Tipo", choices=USER_TYPE, max_length=255)

    USERNAME_FIELD = 'cpf'

    objects = UserManager()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)