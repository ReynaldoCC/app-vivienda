# Generated by Django 2.2 on 2020-02-11 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0014_auto_20200211_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasificacionrespuesta',
            name='codigo',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*[a-zA-Z ]$', message='Este campo solo puede contener letras')], verbose_name='Código'),
        ),
    ]
