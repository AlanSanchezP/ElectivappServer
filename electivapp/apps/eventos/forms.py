import time
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import EventoAuditorio

class EventoForm(forms.ModelForm):
    class Meta:
        model = EventoAuditorio
        exclude = ['validado', 'asistentes']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={
                'class': 'datetimepicker-input',
                'data-target': '#datetimepicker1'},
                format='%d/%m/%Y %H:%M')

        }
        labels = {
            'fecha': _('Fecha (dd/mm/aaaa HH:MM)'),
            'duracion': _('Duración (HH:MM:ss)')
        }

class EventoUpdateForm(EventoForm):
    class Meta(EventoForm.Meta):
        model = EventoForm.Meta.model
        exclude = ['asistentes']