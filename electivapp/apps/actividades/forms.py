from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Categoria, TipoActividad

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ['']

class TipoActividadForm(forms.ModelForm):
    class Meta:
        model = TipoActividad
        exclude = ['']
        labels = {
            'horasRequeridas': _('Required hours for 1 credit'),
        }