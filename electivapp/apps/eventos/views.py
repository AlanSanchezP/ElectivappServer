from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from electivapp.apps.alumnos.models import Responsable
from .models import EventoAuditorio

class EventosListView(LoginRequiredMixin, ListView):
    template_name = 'eventos/evento_list.html'
    model = EventoAuditorio
    context_object_name = 'eventos'