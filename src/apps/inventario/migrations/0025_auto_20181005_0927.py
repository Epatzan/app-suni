# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-05 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0024_paquete_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquetetipo',
            name='tipo_dispositivo',
        ),
        migrations.AddField(
            model_name='paquetetipo',
            name='tipo_dispositivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoTipo', verbose_name='Tipos de dispositivo'),
        ),
    ]
