# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-20 14:24
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tpe', '0003_auto_20170130_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipamientoSeguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('equipamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tpe.Equipamiento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Garantia',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_vencimiento', models.DateField()),
                ('equipamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tpe.Equipamiento')),
            ],
            options={
                'verbose_name_plural': 'Garantías',
                'verbose_name': 'Garantía',
            },
        ),
        migrations.CreateModel(
            name='TicketRegistro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('descripcion', models.TextField()),
                ('costo_reparacion', models.DecimalField(decimal_places=2, default=Decimal('0.0000'), max_digits=7)),
                ('costo_envio', models.DecimalField(decimal_places=2, default=Decimal('0.0000'), max_digits=7)),
            ],
            options={
                'verbose_name_plural': 'Soporte - Registro de tickets',
                'verbose_name': 'Soporte - Registro de ticket',
            },
        ),
        migrations.CreateModel(
            name='TicketRegistroTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.TextField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Soporte - Tipos de registro',
                'verbose_name': 'Soporte - Tipo de registro',
            },
        ),
        migrations.CreateModel(
            name='TicketSoporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_abierto', models.DateField(default=django.utils.timezone.now)),
                ('fecha_cierre', models.DateField()),
                ('abierto_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('garantia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tpe.Garantia')),
            ],
            options={
                'verbose_name_plural': 'Soporte - Tickets',
                'verbose_name': 'Soporte - Ticket',
            },
        ),
        migrations.AddField(
            model_name='ticketregistro',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='tpe.TicketSoporte'),
        ),
        migrations.AddField(
            model_name='ticketregistro',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tpe.TicketRegistroTipo'),
        ),
        migrations.AddField(
            model_name='ticketregistro',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
