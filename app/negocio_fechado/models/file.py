import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

class File(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField("Arquivo", upload_to='attachments/%Y/%m/%d/')
