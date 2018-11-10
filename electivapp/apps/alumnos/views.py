from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render 
from django.views.generic import View, TemplateView, FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect

from .models import Alumno, Responsable
from .forms import AlumnoForm, ResponsableForm, ResponsableUpdateForm
import electivapp.apps.alumnos.utils as _utils
from electivapp.apps.actividades.models import Actividad

# Create your views here.
class AlumnosSearchView(LoginRequiredMixin, View):
    template_name = 'alumnos/alumno_search.html'

    def post(self, request, **kwargs):
        print(request.POST)
        boleta = request.POST.get('boleta')
        try:
            alumno = Alumno.objects.get(boleta=boleta)
            return render(
                request, 
                self.template_name, 
                context={
                    "alumno": alumno, 
                    "boleta": boleta,
                },
            )
        except Alumno.DoesNotExist:
            messages.add_message(
                request, 
                messages.INFO, 
                "No se encontro un alumno con la boleta {0}".format(boleta),
            )
            return render(
                request, 
                self.template_name, 
                context={"boleta": boleta},
            )

    def get(self, request, **kwargs):
        if "pk" in kwargs:
            mutable = request.POST._mutable
            request.POST._mutable = True
            request.POST["boleta"] = kwargs["pk"]
            request.POST._mutable = mutable
            return self.post(request)
        else:
            return render(
                request, 
                self.template_name
            )

class AlumnoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'alumnos/alumno_update.html'
    form_class = AlumnoForm
    model = Alumno

    def form_valid(self, form):
        boleta = form.save().boleta
        return HttpResponseRedirect(
            reverse_lazy('alumnos:consulta_boleta', kwargs={"pk": boleta})
        )

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