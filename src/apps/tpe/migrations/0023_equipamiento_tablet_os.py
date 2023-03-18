# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2023-03-06 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tpe', '0022_auto_20211017_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamiento',
            name='tablet_os',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='os_tablet', to='tpe.EquipamientoOs', verbose_name='SO de las tablet'),
        ),
    ]
