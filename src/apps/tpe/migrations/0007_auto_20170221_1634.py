# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-21 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpe', '0006_auto_20170221_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketsoporte',
            name='fecha_cierre',
            field=models.DateField(blank=True, null=True),
        ),
    ]