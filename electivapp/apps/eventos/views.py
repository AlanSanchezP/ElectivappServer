from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from electivapp.apps.alumnos.models import Responsable
from .models import Evento

class EventosListView(LoginRequiredMixin, ListView):
    template_name = 'pages/submenu.html'
    model = Evento
    context_object_name = 'eventos'