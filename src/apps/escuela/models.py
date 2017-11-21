import requests
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

from apps.main.models import Municipio, Coordenada
from apps.main.utils import get_telefonica


class EscArea(models.Model):
    area = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

    def __str__(self):
        return self.area


class EscJornada(models.Model):
    """
    Description: Jornada de la escuela
    """
    jornada = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'

    def __str__(self):
        return self.jornada


class EscModalidad(models.Model):
    """
    Description: Modalidad de la escuela
    """
    modalidad = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        return self.modalidad


class EscNivel(models.Model):
    """
    Description: Nivel de la escuela
    """
    nivel = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'

    def __str__(self):
        return self.nivel


class EscPlan(models.Model):
    """
    Description: Plan de la escuela (diario, fin de semana, etc.)
    """
    plan = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    def __str__(self):
        return self.plan


class EscSector(models.Model):
    """
    Description: Sector de la escuela (oficial, privado, etc.)
    """
    sector = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def __str__(self):
        return self.sector


class EscStatus(models.Model):
    """
    Description: Status de la escuela (Abierta, cerrada)
    """
    status = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statues'

    def __str__(self):
        return self.status


class Escuela(models.Model):
    """
    Description: Escuela
    """
    codigo = models.CharField(max_length=15, unique=True)
    distrito = models.CharField(max_length=10, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, related_name='escuelas')
    nombre = models.CharField(max_length=250)
    direccion = models.TextField(verbose_name='Dirección')
    telefono = models.CharField(max_length=12, null=True, blank=True, verbose_name='Teléfono')
    nivel = models.ForeignKey(EscNivel, on_delete=models.PROTECT)
    sector = models.ForeignKey(EscSector, on_delete=models.PROTECT)
    area = models.ForeignKey(EscArea, on_delete=models.PROTECT, verbose_name='Área')
    status = models.ForeignKey(EscStatus, on_delete=models.PROTECT)
    modalidad = models.ForeignKey(EscModalidad, on_delete=models.PROTECT)
    jornada = models.ForeignKey(EscJornada, on_delete=models.PROTECT)
    plan = models.ForeignKey(EscPlan, on_delete=models.PROTECT)
    mapa = models.ForeignKey(Coordenada, null=True, blank=True)

    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('escuela_detail', kwargs={'pk': self.id})

    def get_poblacion(self):
        if self.poblaciones.count() > 0:
            return self.poblaciones.latest('fecha').total_alumno
        else:
            return None
    poblacion = property(get_poblacion)

    def es_equipada(self):
        return True if self.equipamiento.count() > 0 else False
    equipada = property(es_equipada)

    def get_ficha_escolar(self):
        return 'https://public.tableau.com/views/1-FichaEscolarDatosGenerales/DatosGenerales?CODUDI={}'.format(
            self.codigo)

    def get_matricula_url(self):
        return 'https://public.tableau.com/views/2-FichaaEscolaraMatriculaHistorica/DetallePromovidosRetirados?CODUDI={}&%3AshowVizHome=no'.format(
            self.codigo)

    def get_rendimiento_url(self):
        return 'https://public.tableau.com/views/6-Fichaescolarpruebasestandarizadas/Pruebasestandarizadas?CODUDI={}&%3AshowVizHome=no'.format(
            self.codigo)

    def get_capacitacion(self):
        """Establece una conexión al servidor del SUNI1 para
        obtener datos de capacitación. Esta función será eliminada en futuras versiones.

        Returns:
            dict: Diccionario con el nombre de la escuela y el listado de participantes
        """
        url = settings.LEGACY_URL['cyd_informe']
        if url is not '':
            params = {'udi': self.codigo}
            resp = requests.post(url=url, data=params)
            return resp.json()
        else:
            return [[], []]

    @property
    def capacitacion(self):
        data = self.get_capacitacion()
        respuesta = {'capacitada': True if len(data[1]) > 0 else False}
        if respuesta['capacitada'] is True:
            respuesta['participantes'] = data[1]
        return respuesta

    @property
    def equipada(self):
        return self.equipamiento.count() > 0


class EscContactoRol(models.Model):
    """
    Description: Rol para el contacto de escuela
    """
    rol = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Rol de contacto"
        verbose_name_plural = "Roles de contacto"

    def __str__(self):
        return self.rol


class EscContacto(models.Model):
    escuela = models.ForeignKey(Escuela, related_name="contacto")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.ForeignKey(EscContactoRol, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos de escuela"

    def __str__(self):
        return self.nombre + " " + self.apellido


class EscContactoTelefono(models.Model):
    contacto = models.ForeignKey(EscContacto, related_name="telefono", null=True)
    telefono = models.IntegerField()

    def get_empresa(self):
        return get_telefonica(self.telefono)
    empresa = property(get_empresa)

    def __str__(self):
        return str(self.telefono)


class EscContactoMail(models.Model):
    """
    Description: Correo de contacto
    """
    contacto = models.ForeignKey(EscContacto, related_name="mail", null=True)
    mail = models.EmailField(max_length=125)

    def __str__(self):
        return self.mail


class EscPoblacion(models.Model):
    escuela = models.ForeignKey(Escuela, related_name="poblaciones")
    fecha = models.DateField(default=timezone.now)

    alumna = models.PositiveIntegerField(
        default=0, verbose_name='Estudiantes mujeres')
    alumno = models.PositiveIntegerField(
        default=0, verbose_name='Estudiantes varones')
    maestra = models.PositiveIntegerField(
        default=0, verbose_name='Docentes mujeres')
    maestro = models.PositiveIntegerField(
        default=0, verbose_name='Dicentes varones')

    total_alumno = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Total de estudiantes')
    total_maestro = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Total de docentes')

    class Meta:
        verbose_name = "Población de escuela"
        verbose_name_plural = "Poblaciones de escuela"

    def __str__(self):
        return str(self.escuela)[:15] + " - " + str(self.fecha)

    def save(self, *args, **kwargs):
        """En caso de que no se hubiera ingresado el total, suma las cantidades
        detalladas para establecerlo.
        """
        if self.total_alumno is None or self.total_alumno == 0:
            self.total_alumno = self.alumna + self.alumno
        if self.total_maestro is None or self.total_maestro == 0:
            self.total_maestro = self.maestra + self.maestro
        super(EscPoblacion, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.escuela.get_absolute_url()


class EscMatricula(models.Model):

    """Registro histórico de la matrícula de la escuela.
    Cuántos promovidos, retirados y reprobados.
    """
    escuela = models.ForeignKey(Escuela, related_name='matriculas')
    ano = models.PositiveIntegerField(verbose_name='Año')
    m_promovido = models.PositiveIntegerField(default=0, verbose_name='Mujeres promovidas')
    m_no_promovido = models.PositiveIntegerField(default=0, verbose_name='Mujeres no promovidas')
    m_retirado = models.PositiveIntegerField(default=0, verbose_name='Mujeres retiradas')
    h_promovido = models.PositiveIntegerField(default=0, verbose_name='Hombres promovidos')
    h_no_promovido = models.PositiveIntegerField(default=0, verbose_name='Hombres no promovidos')
    h_retirado = models.PositiveIntegerField(default=0, verbose_name='Hombres retirados')

    class Meta:
        verbose_name = "Matrícula de escuela"
        verbose_name_plural = "Matrículas de escuelas"
        ordering = ['escuela', '-ano']

    def __str__(self):
        return '{escuela} - {ano}'.format(
            escuela=self.escuela,
            ano=self.ano)

    @property
    def t_promovido(self):
        return self.m_promovido + self.h_promovido

    @property
    def t_no_promovido(self):
        return self.m_no_promovido + self.h_no_promovido

    @property
    def t_retirado(self):
        return self.m_retirado + self.h_retirado

    @property
    def m_total(self):
        return self.m_promovido + self.m_no_promovido + self.m_retirado

    @property
    def h_total(self):
        return self.h_promovido + self.h_no_promovido + self.h_retirado

    @property
    def m_promovido_p(self):
        return int(self.m_promovido / self.m_total * 100)

    @property
    def m_no_promovido_p(self):
        return int(self.m_no_promovido / self.m_total * 100)

    @property
    def m_retirado_p(self):
        return int(self.m_retirado / self.m_total * 100)

    @property
    def h_promovido_p(self):
        return int(self.h_promovido / self.h_total * 100)

    @property
    def h_no_promovido_p(self):
        return int(self.h_no_promovido / self.h_total * 100)

    @property
    def h_retirado_p(self):
        return int(self.h_retirado / self.h_total * 100)

    @property
    def t_promovido_p(self):
        return int(self.t_promovido / (self.t_promovido + self.t_retirado + self.t_no_promovido) * 100)

    def get_absolute_url(self):
        return self.escuela.get_absolute_url()


class EscRendimientoMateria(models.Model):

    """Materia a evaluar en una prueba de rendimiento académico.
    """

    materia = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Materia de rendimiento"
        verbose_name_plural = "Materias de rendimiento"

    def __str__(self):
        return self.materia


class EscRendimientoAcademico(models.Model):

    """Pruebas estandarizadas del rendimiento académico de la escuela.
    """

    escuela = models.ForeignKey(Escuela, related_name='rendimientos')
    materia = models.ForeignKey(EscRendimientoMateria, related_name='registros')
    ano = models.PositiveIntegerField(verbose_name='Año')
    insatisfactorio = models.DecimalField(max_digits=5, decimal_places=2)
    debe_mejorar = models.DecimalField(max_digits=5, decimal_places=2)
    satisfactorio = models.DecimalField(max_digits=5, decimal_places=2)
    excelente = models.DecimalField(max_digits=5, decimal_places=2)
    no_evaluado = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Rendimiento académico"
        verbose_name_plural = "Rendimientos académicos"
        ordering = ['escuela', '-ano']

    def __str__(self):
        return '{escuela} - {ano}'.format(
            escuela=self.escuela,
            ano=self.ano)

    def get_absolute_url(self):
        return self.escuela.get_absolute_url()

    @property
    def porcentaje_logro(self):
        return self.excelente + self.satisfactorio
