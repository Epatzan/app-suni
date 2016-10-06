# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
                ('direccion', models.CharField(blank=True, max_length=150, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('puesto', models.CharField(max_length=75)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactoMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=100)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mail', to='fr.Contacto')),
            ],
        ),
        migrations.CreateModel(
            name='ContactoTelefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=12)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefono', to='fr.Contacto')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=12, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etiqueta', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('color', models.CharField(choices=[('navy', 'azul'), ('aqua', 'aqua'), ('purple', 'Morado'), ('yellow', 'Amarillo'), ('teal', 'turquesa'), ('red', 'rojo'), ('green', 'verde')], default='purple', max_length=10)),
            ],
            options={
                'ordering': ('etiqueta',),
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('color', models.CharField(choices=[('navy', 'azul'), ('aqua', 'aqua'), ('purple', 'Morado'), ('yellow', 'Amarillo'), ('teal', 'turquesa'), ('red', 'rojo'), ('green', 'verde')], default='green', max_length=10)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_evento', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo_de_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fr.TipoEvento'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fr.Empresa'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='etiquetas',
            field=models.ManyToManyField(to='fr.Etiqueta'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='evento',
            field=models.ManyToManyField(to='fr.Evento'),
        ),
    ]
