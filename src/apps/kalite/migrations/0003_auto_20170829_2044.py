# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-29 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalite', '0002_auto_20170824_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejerciciosgrado',
            name='estudiantes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grado',
            name='minimo_esperado',
            field=models.PositiveIntegerField(default=1, verbose_name='Mínimo esperado'),
        ),
    ]
