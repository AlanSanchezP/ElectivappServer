from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from electivapp.apps.alumnos.models import Responsable
from .forms import EventoForm, EventoUpdateForm
from .models import EventoAuditorio
from .serializers import EventoSerializer

class EventosListView(LoginRequiredMixin, ListView):
    template_name = 'eventos/evento_list.html'
    model = EventoAuditorio
    context_object_name = 'eventos'

class EventoFormView(LoginRequiredMixin, FormView):
    template_name = 'eventos/evento_form.html'
    form_class = EventoForm
    success_url = reverse_lazy('eventos:home')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

class EventoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'eventos/evento_update.html'
    form_class = EventoUpdateForm
    model = EventoAuditorio
    success_url = reverse_lazy('eventos:home')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

class EventoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'eventos/evento_confirm_delete.html'
    model = EventoAuditorio
    context_object_name = 'evento'
    success_url = reverse_lazy('eventos:home')

@api_view(['GET'])
def eventos_list(request):
    if request.method == 'GET':
        eventos = EventoAuditorio.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)