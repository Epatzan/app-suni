# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2023-08-07 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mye', '0015_auto_20211017_1040'),
        ('inventario', '0087_solicitudbitacora_observaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='proyecto',
            field=models.ManyToManyField(blank=True, null=True, related_name='proyecto_inventario', to='mye.Cooperante'),
        ),
        migrations.AddField(
            model_name='entradadetalle',
            name='proyecto',
            field=models.ManyToManyField(blank=True, null=True, related_name='proyecto_inventario_detalle', to='mye.Cooperante'),
        ),
    ]
