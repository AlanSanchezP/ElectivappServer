from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponse, HttpResponseRedirect

from .models import TipoActividad, Actividad
from .forms import TipoActividadForm

# Create your views here.

class TiposActividadListView(LoginRequiredMixin, ListView):
    template_name = 'actividades/tipoactividad_list.html'
    model = TipoActividad
    context_object_name = 'tipos'

class TiposActividadFormView(LoginRequiredMixin, FormView):
    template_name = 'actividades/tipoactividad_form.html'
    form_class = TipoActividadForm
    success_url = reverse_lazy('actividades:lista_tipos')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

class TiposActividadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'actividades/tipoactividad_update.html'
    form_class = TipoActividadForm
    model = TipoActividad
    success_url = reverse_lazy('actividades:lista_tipos')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

class TiposActividadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'actividades/tipoactividad_confirm_delete.html'
    model = TipoActividad
    context_object_name = 'tipo'
    success_url = reverse_lazy('actividades:lista_tipos')

class RegistrarActividadView(LoginRequiredMixin, TemplateView):
    template_name = 'actividades/actividad_registrar.html'

    def post(self, request, *args, **kwargs):
        return HttpResponse('holi')

class Test(FormView):
    template_name = 'users/user_form.html'
    form_class = TipoActividadForm