# Generated by Django 2.2.9 on 2020-05-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negocio_fechado', '0005_auto_20200517_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='files',
        ),
        migrations.AddField(
            model_name='offer',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='attachments/%Y/%m/%d/', verbose_name='Anexo'),
        ),
    ]
