from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from electivapp.apps.alumnos.models import Responsable
from .forms import EventoForm
from .models import EventoAuditorio

class EventosListView(LoginRequiredMixin, ListView):
    template_name = 'eventos/evento_list.html'
    model = EventoAuditorio
    context_object_name = 'eventos'

class EventoFormView(LoginRequiredMixin, FormView):
    template_name = 'actividades/tipoactividad_form.html'
    form_class = EventoForm
    success_url = reverse_lazy('eventos:home')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

# class EventoUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'actividades/tipoactividad_update.html'
#     form_class = TipoActividadForm
#     model = EventoAuditorio
#     success_url = reverse_lazy('eventos:home')

#     def form_valid(self, form):
#         form.save()
#         return HttpResponseRedirect(self.get_success_url())

class EventoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'actividades/tipoactividad_confirm_delete.html'
    model = EventoAuditorio
    context_object_name = 'evento'
    success_url = reverse_lazy('eventos:home')