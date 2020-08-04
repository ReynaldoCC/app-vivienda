# Generated by Django 2.2.2 on 2020-03-27 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_respuesta', '0003_respuestarechazada'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='respuesta',
            options={'verbose_name': 'Respuesta', 'verbose_name_plural': 'Respuestas'},
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='codigo',
            field=models.CharField(max_length=16, verbose_name='Código de la Respuesta'),
        ),
    ]
