# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-10-16 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_auto_20171013_0751'),
        ('escuela', '0008_auto_20171016_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completa', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Computadora',
                'verbose_name_plural': 'Computadoras',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('red', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('fotos_link', models.URLField(blank=True, null=True)),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.Escuela')),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laboratorios', to='users.Organizacion', verbose_name='Organización')),
                ('poblacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laboratorios', to='escuela.EscPoblacion', verbose_name='Población')),
            ],
            options={
                'verbose_name': 'Laboratorio',
                'verbose_name_plural': 'Laboratorios',
            },
        ),
        migrations.CreateModel(
            name='MarcaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name': 'Marca de item',
                'verbose_name_plural': 'Marcas de items',
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='ie.Computadora')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ie.Item')),
            ],
            options={
                'verbose_name': 'Serie',
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='TipoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Tipo de Item',
                'verbose_name_plural': 'Tipos de Items',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ie.MarcaItem'),
        ),
        migrations.AddField(
            model_name='item',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ie.TipoItem'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='items',
            field=models.ManyToManyField(related_name='computadoras', through='ie.Serie', to='ie.Item'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='laboratorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computadoras', to='ie.Laboratorio'),
        ),
    ]