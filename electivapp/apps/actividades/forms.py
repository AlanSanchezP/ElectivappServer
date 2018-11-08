from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import TipoActividad

class TipoActividadForm(forms.ModelForm):
    class Meta:
        model = TipoActividad
        exclude = ['']
        labels = {
            'valorHoras': _('Value per hour'),
        }