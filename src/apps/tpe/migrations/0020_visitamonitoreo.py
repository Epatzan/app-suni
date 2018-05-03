# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-08 15:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escuela', '0010_auto_20171117_0807'),
        ('tpe', '0019_auto_20171005_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitaMonitoreo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_visita', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de Visita')),
                ('hora_inicio', models.TimeField(default=django.utils.timezone.now)),
                ('hora_final', models.TimeField(default=django.utils.timezone.now)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('fotos_link', models.URLField(blank=True, null=True, verbose_name='Imagen')),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitas_contactos', to='escuela.EscContacto')),
                ('encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitas_encargado', to=settings.AUTH_USER_MODEL)),
                ('equipamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitas_monitoreo', to='tpe.Equipamiento')),
                ('otras_personas', models.ManyToManyField(blank=True, related_name='visitas_varias', to=settings.AUTH_USER_MODEL, verbose_name='Otras personas que visitan')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitas_soporte', to='tpe.TicketSoporte')),
            ],
            options={
                'verbose_name': 'Visita de monitoreo',
                'verbose_name_plural': 'Visitas de monitoreo',
            },
        ),
    ]