# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-31 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20161115_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='color',
            field=models.CharField(choices=[('tile', 'aqua'), ('green', 'green'), ('yellow', 'yellow'), ('red', 'red'), ('purple', 'purple')], default='tile', max_length=20),
        ),
    ]
