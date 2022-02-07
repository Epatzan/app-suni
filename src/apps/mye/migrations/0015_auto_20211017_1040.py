# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2021-10-17 16:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mye', '0014_usuariocooperante'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperante',
            name='creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='medio',
            name='creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requisito',
            name='creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitudversion',
            name='creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='validacion',
            name='creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, related_name='mye_creada_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='validaciontipo',
            name='creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='validacionversion',
            name='creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
