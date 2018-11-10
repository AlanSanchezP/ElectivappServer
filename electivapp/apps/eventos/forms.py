import time
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import EventoAuditorio

class EventoForm(forms.ModelForm):
    class Meta:
        model = EventoAuditorio
        exclude = ['validado']