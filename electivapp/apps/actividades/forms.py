from django import forms
from .models import TipoActividad

class TipoActividadForm(forms.ModelForm):
    class Meta:
        model = TipoActividad
        exclude = ['']