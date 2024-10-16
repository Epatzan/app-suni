from django import forms
from django.contrib.auth.models import User

from apps.naat import models as naat_m
from apps.cyd import forms as cyd_f
from apps.cyd import models as cyd_m


class AsignacionNaatForm(cyd_f.ParticipanteBaseForm):
    """Formulario para crear un :class:`Participante` y asignarlo a un capacitador por medio
    de :class:`AsignacionNaat` (esta lógica para en la vista, el formulario únicamente sirve para
    tomar los datos).
    La lógica para filtrar al capacitador se realizará en la vista.
    """
    capacitador = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='naat_facilitador'),
        empty_label=None)

    class Meta:
        model = cyd_m.Participante
        fields = [
            'udi', 'nombre', 'apellido', 'dpi', 'genero', 'rol',
            'mail', 'tel_movil']
        exclude = ('slug',)

    def __init__(self, *args, **kwargs):
        super(AsignacionNaatForm, self).__init__(*args, **kwargs)
        self.fields['capacitador'].label_from_instance = lambda obj: '{}'.format(obj.get_full_name())


class CalendarFilterForm(forms.Form):
    """Formulario para filtrar los eventos mostrados en el calendario con base en el capacitador."""
    capacitador = forms.ModelChoiceField(
        queryset=User.objects.filter(id__in=naat_m.SesionPresencial.objects.values('capacitador').distinct()),
        required=False)

    def __init__(self, *args, **kwargs):
        super(CalendarFilterForm, self).__init__(*args, **kwargs)
        self.fields['capacitador'].label_from_instance = lambda obj: '{}'.format(obj.get_full_name())
