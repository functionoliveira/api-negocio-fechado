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

class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Senha", max_length=255)
    description = models.CharField("Senha", max_length=255)
    worker = models.CharField("Senha", max_length=255)
    price = models.CharField("Senha", max_length=255)
    state = models.CharField("Senha", max_length=255)
  
    def __str__(self):
        return self.title