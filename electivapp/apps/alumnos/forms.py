from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Responsable

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        exclude = ['']