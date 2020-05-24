# Generated by Django 2.2.9 on 2020-05-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negocio_fechado', '0003_auto_20200509_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=None, max_length=160, verbose_name='Endereço'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='state',
            field=models.CharField(choices=[(1, 'Recente'), (2, 'Em negociação'), (3, 'Falta assinar'), (4, 'Assinado'), (5, 'Finalizado')], max_length=255, verbose_name='Estado'),
        ),
    ]
