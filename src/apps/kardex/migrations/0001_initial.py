# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('factura', models.IntegerField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoEquipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_del_equipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('direccionn', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('observacion', models.TextField(blank=True, null=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kardex.Equipo')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kardex.EstadoEquipo')),
                ('no_entrada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kardex.Entrada')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEntrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_entrada', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_proveedor', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSalida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_salida', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='salida',
            name='tipo_salida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kardex.TipoSalida'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='tipo_de_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kardex.TipoProveedor'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kardex.Equipo'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kardex.EstadoEquipo'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kardex.Proveedor'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='tipo_entrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kardex.TipoEntrada'),
        ),
    ]
