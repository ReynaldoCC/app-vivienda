# Generated by Django 2.2.2 on 2020-01-11 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0004_auto_20191218_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedencia',
            name='tipo',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='dpv_nomencladores.TipoProcedencia'),
        ),
        migrations.AlterField(
            model_name='consejopopular',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='dpv_nomencladores.Municipio'),
        ),
    ]
