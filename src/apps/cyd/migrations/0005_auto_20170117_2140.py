# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-17 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0003_auto_20161115_1406'),
        ('cyd', '0004_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Asignaciones',
                'verbose_name': 'Asignacion',
            },
        ),
        migrations.CreateModel(
            name='ParEscolaridad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Escolaridades de participante',
                'verbose_name': 'Escolaridad de participante',
            },
        ),
        migrations.CreateModel(
            name='ParEtnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Etnias de participante',
                'verbose_name': 'Etnia de participante',
            },
        ),
        migrations.CreateModel(
            name='ParRol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Roles de participante',
                'verbose_name': 'Rol de participante',
            },
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('genero', models.IntegerField(choices=[(1, 'Hombre'), (2, 'Mujer')])),
                ('direccion', models.TextField(blank=True, null=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('tel_casa', models.CharField(blank=True, max_length=11, null=True)),
                ('tel_movil', models.CharField(blank=True, max_length=11, null=True)),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('avatar', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='avatar_participante')),
                ('escolaridad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cyd.ParEscolaridad')),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='escuela.Escuela')),
                ('etnia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cyd.ParEtnia')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cyd.ParRol')),
            ],
            options={
                'verbose_name_plural': 'Participantes',
                'verbose_name': 'Participante',
            },
        ),
        migrations.AlterModelOptions(
            name='grupo',
            options={'verbose_name': 'Grupo de capacitación', 'verbose_name_plural': 'Grupos de capacitación'},
        ),
        migrations.AddField(
            model_name='asignacion',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyd.Grupo'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyd.Participante'),
        ),
    ]
