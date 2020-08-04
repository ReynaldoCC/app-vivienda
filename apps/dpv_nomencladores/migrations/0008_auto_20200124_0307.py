# Generated by Django 2.2 on 2020-01-24 03:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0007_auto_20200119_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedencia',
            name='tipo',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='procedencias', to='dpv_nomencladores.TipoProcedencia'),
        ),
        migrations.AlterField(
            model_name='procedencia',
            name='tipo_contenido',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(('app_label', 'dpv_nomencladores'), ('model', 'organismo')), models.Q(('app_label', 'dpv_nomencladores'), ('model', 'organizacion')), models.Q(('app_label', 'dpv_nomencladores'), ('model', 'prensaescrita')), models.Q(('app_label', 'dpv_nomencladores'), ('model', 'telefono')), models.Q(('app_label', 'dpv_nomencladores'), ('model', 'email')), models.Q(('app_label', 'dpv_persona'), ('model', 'personanatural')), models.Q(('app_label', 'dpv_persona'), ('model', 'personajuridica')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Contenido de Procedencia'),
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Eliminado')),
                ('numero', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.RegexValidator('[a-zA-Z0-9 ]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Teléfono')),
            ],
            options={
                'verbose_name': 'Teléfono',
                'verbose_name_plural': 'Teléfonos',
                'ordering': ['numero'],
                'unique_together': {('numero', 'deleted_at')},
            },
        ),
        migrations.CreateModel(
            name='PrensaEscrita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Eliminado')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.RegexValidator('[a-zA-Z0-9 ]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Prensa Escrita')),
                ('siglas', models.CharField(max_length=10, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.RegexValidator('[a-zA-Z0-9 ]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Siglas')),
            ],
            options={
                'verbose_name': 'Prensa Escrita',
                'verbose_name_plural': 'Prensas Escritas',
                'ordering': ['nombre'],
                'unique_together': {('nombre', 'deleted_at')},
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Eliminado')),
                ('email', models.EmailField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.EmailValidator()], verbose_name='Correo Electrónico')),
            ],
            options={
                'verbose_name': 'Correo Electrónico',
                'verbose_name_plural': 'Correos Electrónicos',
                'ordering': ['email'],
                'unique_together': {('email', 'deleted_at')},
            },
        ),
    ]
