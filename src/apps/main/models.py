import os
import json
import math
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

from django.test import Client
from django.core.files import File
from django.contrib.auth.models import User

class Departamento(models.Model):
    """
    Description: Departamento de Guatemala
    """
    nombre = models.CharField(max_length=30)
    main_dep_creada_por =models.ForeignKey(User, on_delete=models.CASCADE,default=User.objects.get(username="Admin").pk)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    """
    Description: Municipio de Guatemala
    """
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=150)
    main_mun_creada_por =models.ForeignKey(User, on_delete=models.CASCADE,default=User.objects.get(username="Admin").pk)
    def __str__(self):
        return self.nombre + " (" + str(self.departamento) + ")"


class Coordenada(models.Model):
    lat = models.CharField(max_length=25, verbose_name="Latitud")
    lng = models.CharField(max_length=25, verbose_name="Longitud")
    descripcion = models.CharField(max_length=70, null=True, blank=True, verbose_name="Descripción")
    main_coo_creada_por =models.ForeignKey(User, on_delete=models.CASCADE,default=User.objects.get(username="Admin").pk)
    def __str__(self):
        if self.descripcion:
            return self.descripcion
        else:
            return self.lat + ", " + self.lng


    def calcular_distancia(self):
        #lat_destino = float(self.lat)
        #lng_destino = float(self.lng)
        lat_destino = 14.69121
        lng_destino = -91.11679
        #lat_funsepa = 14.65402
        #lng_funsepa = -90.53823
        
        lat_funsepa = 6.28331696378
        lng_funsepa = -75.5689742567
        rad = math.pi / 180
        dlat = float(lat_destino) - lat_funsepa
        dlon = float(lng_destino) - lng_funsepa
        R = 6372.795477598
        a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat_destino)*math.cos(rad*lat_funsepa)*(math.sin(rad*dlon/2))**2
          
        distancia=2*R*math.asin(math.sqrt(a))
        return distancia

class ArchivoGenerado(models.Model):
    nombre = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    ultima_actualizacion = models.DateTimeField(default=timezone.now)
    archivo = models.FileField(upload_to='generados/')
    descripcion = models.TextField(null=True, blank=True)

    input_url = models.CharField(max_length=50, null=True, blank=True)
    activo = models.BooleanField(default=True, blank=True)
    main_arch_creada_por =models.ForeignKey(User, on_delete=models.CASCADE,default=User.objects.get(username="Admin").pk)
    class Meta:
        verbose_name = "Archivo fijo"
        verbose_name_plural = "Archivos fijos"

    def __str__(self):
        return self.nombre

    def generar_slug(self):
        fecha = timezone.now()
        return slugify('{}_{}'.format(self.nombre, fecha.strftime('%Y-%m-%d-%H-%M-%S')))

    def get_absolute_url(self):
        return settings.MEDIA_URL + self.archivo.name

    def generar(self):
        c = Client()
        res = c.get(reverse(self.input_url))
        slug = self.generar_slug()
        with open(settings.MEDIA_ROOT + '{}.json'.format(slug), "w") as f:
            json.dump(res.json(), f, ensure_ascii=False)

        with open(settings.MEDIA_ROOT + '{}.json'.format(slug), "r") as file:
            self.archivo.save('{}.json'.format(slug), File(file))
        os.remove(f.name)
