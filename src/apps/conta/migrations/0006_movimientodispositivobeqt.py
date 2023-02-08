# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2023-01-11 03:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beqt', '0001_initial'),
        ('conta', '0005_auto_20220809_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimientoDispositivoBeqt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('tipo_movimiento', models.IntegerField(choices=[(-1, 'Baja'), (1, 'Alta')], default=1)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=14)),
                ('referencia', models.CharField(blank=True, max_length=30, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('creado_por', models.ForeignKey(blank=True, default=49, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beqt.DispositivoBeqt')),
            ],
            options={
                'verbose_name_plural': 'Movimientos de dispositivos Beqt',
                'verbose_name': 'Movimiento de dispositivo Beqt',
            },
        ),
    ]
