# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-05 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tpe', '0016_auto_20170424_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipamientoos',
            options={'verbose_name': 'Software para equipo', 'verbose_name_plural': 'Software para equipo'},
        ),
        migrations.AlterField(
            model_name='equipamiento',
            name='equipo_os',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tpe.EquipamientoOs', verbose_name='SO de las PC'),
        ),
        migrations.AlterField(
            model_name='equipamiento',
            name='fotos_link',
            field=models.URLField(blank=True, null=True, verbose_name='Link a fotos'),
        ),
        migrations.AlterField(
            model_name='equipamiento',
            name='observacion',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='equipamiento',
            name='poblacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escuela.EscPoblacion', verbose_name='Población'),
        ),
        migrations.AlterField(
            model_name='equipamiento',
            name='servidor_os',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servidores', to='tpe.EquipamientoOs', verbose_name='SO del servidor'),
        ),
    ]
