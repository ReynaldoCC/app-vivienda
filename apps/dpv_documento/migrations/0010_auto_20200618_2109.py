# Generated by Django 2.2.2 on 2020-06-18 21:09

import apps.dpv_documento.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_documento', '0009_auto_20200618_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipodpvdocumento',
            name='con_respuesta',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dpvdocumento',
            name='archivo_digital',
            field=models.FileField(blank=True, help_text='Solo puede subir archivos PDF o imagen del documento', upload_to=apps.dpv_documento.models.scramble_upload_doc, verbose_name='Copia en Digital'),
        ),
    ]
