from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from electivapp.apps.alumnos.models import Responsable
from .forms import EventoForm, EventoUpdateForm
from .models import EventoAuditorio

class EventosListView(LoginRequiredMixin, ListView):
    template_name = 'eventos/evento_list.html'
    model = EventoAuditorio
    context_object_name = 'eventos'

class EventoFormView(LoginRequiredMixin, FormView):
    template_name = 'eventos/evento_form.html'
    form_class = EventoForm
    success_url = reverse_lazy('eventos:home')

    def form_valid(self, form):
        try:
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        except ValidationError as e:
            form.add_error(None, e)
            return super(EventoFormView, self).form_invalid(form)

class EventoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'eventos/evento_update.html'
    form_class = EventoUpdateForm
    model = EventoAuditorio
    success_url = reverse_lazy('eventos:home')

    def form_valid(self, form):
        try:
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        except ValidationError as e:
            form.add_error(None, e)
            return super(EventoFormView, self).form_invalid(form)

class EventoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'eventos/evento_confirm_delete.html'
    model = EventoAuditorio
    context_object_name = 'evento'
    success_url = reverse_lazy('eventos:home')