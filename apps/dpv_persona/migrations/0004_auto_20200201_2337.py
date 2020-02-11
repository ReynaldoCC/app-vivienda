# Generated by Django 2.2 on 2020-02-01 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_persona', '0003_auto_20200119_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personajuridica',
            name='cpopular',
            field=models.ForeignKey(blank=True, default='', help_text='Consejo popular donde recide la persona', null=True, on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.ConsejoPopular', verbose_name='Consejo Popular'),
        ),
        migrations.AlterField(
            model_name='personanatural',
            name='cpopular',
            field=models.ForeignKey(blank=True, default='', help_text='Consejo popular donde recide la persona', null=True, on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.ConsejoPopular', verbose_name='Consejo Popular'),
        ),
    ]
