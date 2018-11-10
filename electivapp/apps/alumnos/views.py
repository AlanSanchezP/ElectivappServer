from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import View, TemplateView, FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect

from .models import Alumno, Responsable
from .forms import ResponsableForm, ResponsableUpdateForm
import electivapp.apps.alumnos.utils as _utils

# Create your views here.
class AlumnosSearchView(LoginRequiredMixin, TemplateView):
    template_name = 'alumnos/alumno_search.html'

class ResponsablesListView(LoginRequiredMixin, ListView):
    template_name = 'alumnos/responsable_list.html'
    model = Responsable
    context_object_name = 'responsables'

class ResponsableFormView(LoginRequiredMixin, FormView):
    template_name = 'alumnos/responsable_form.html'
    form_class = ResponsableForm
    success_url = reverse_lazy('alumnos:lista_responsables')

    def form_valid(self, form):
        passw = form.save()
        messages.add_message(
            self.request, 
            messages.INFO, 
            "La contraseña del responsable es {0}".format(passw),
        )
        return HttpResponseRedirect(self.get_success_url())

class ResponsableUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'alumnos/responsable_update.html'
    form_class = ResponsableUpdateForm
    model = Responsable
    success_url = reverse_lazy('alumnos:lista_responsables')

    def get(self, request, **kwargs):
        self.object = Responsable.objects.get(id=kwargs['pk'])
        alumno = self.object.alumno
        form = self.form_class(data={
            "boleta":alumno.boleta,
            "nombre":alumno.nombre,
            "carrera":alumno.carrera
        })
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

class ResponsableDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'alumnos/responsable_confirm_delete.html'
    model = Responsable
    context_object_name = 'responsable'
    success_url = reverse_lazy('alumnos:lista_responsables')

class ResponsablePasswordView(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        responsable = Responsable.objects.get(id = kwargs["pk"])
        password = _utils.generarPassword()
        responsable.password = password
        responsable.save()
        return HttpResponse(password)