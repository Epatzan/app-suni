# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2022-08-09 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_perfil_externo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='cargo',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
