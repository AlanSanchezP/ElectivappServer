import time
from datetime import datetime
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView, ListView
from django.http import HttpResponseRedirect

from electivapp.core.mixins import AdminStaffRequiredMixin
from electivapp.apps.alumnos.models import Alumno, CARRERAS
from .models import TipoActividad, Actividad, CATEGORIAS
from .forms import TipoActividadForm

# Create your views here.
class ActividadesHomeView(AdminStaffRequiredMixin, TemplateView):
    template_name = 'pages/submenu.html'

class TiposActividadListView(AdminStaffRequiredMixin, ListView):
    template_name = 'actividades/tipoactividad_list.html'
    model = TipoActividad
    context_object_name = 'tipos'

class TiposActividadFormView(AdminStaffRequiredMixin, FormView):
    template_name = 'actividades/tipoactividad_form.html'
    form_class = TipoActividadForm
    success_url = reverse_lazy('actividades:lista_tipos')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

class TiposActividadUpdateView(AdminStaffRequiredMixin, UpdateView):
    template_name = 'actividades/tipoactividad_update.html'
    form_class = TipoActividadForm
    model = TipoActividad
    success_url = reverse_lazy('actividades:lista_tipos')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

class TiposActividadDeleteView(AdminStaffRequiredMixin, DeleteView):
    template_name = 'actividades/tipoactividad_confirm_delete.html'
    model = TipoActividad
    context_object_name = 'tipo'
    success_url = reverse_lazy('actividades:lista_tipos')

class RegistrarActividadView(AdminStaffRequiredMixin, TemplateView):
    template_name = 'actividades/actividad_registrar.html'
    error_url = reverse_lazy('actividades:corregir')
    success_url = reverse_lazy('actividades:home')

    def get_context_data(self, **kwargs):
        context = super(RegistrarActividadView, self).get_context_data(**kwargs)
        tipos = TipoActividad.objects.all().exclude(id=1)
        TIPOS = []
        for tipo in tipos:
            TIPOS.append((tipo.id,tipo.nombre))
        TIPOS = tuple(TIPOS)
        context['carreras'] = CARRERAS
        context['categorias'] = TIPOS
        return context

    def insertarActividad(self, alumno, duracion, tipo):
        creditos = alumno.creditos()
        actividad = Actividad(
            alumno=alumno,
            duracion=duracion,
            fecha=datetime.today(),
            tipo=TipoActividad.objects.get(id=tipo),
        )
        creditos += actividad.valor()
        actividad.save()

        if alumno.carrera == 'IN' and creditos >= 14:
            alumno.terminado = True
        elif alumno.carrera == 'AI' and creditos >= 18:
            alumno.terminado = True
        elif creditos >= 20:
            alumno.terminado = True
        alumno.save()

    def post(self, request, *args, **kwargs):
        params = request.POST.dict()
        cantidad = int(params["cantidad"])
        errores = False

        for i in range(1, cantidad+1):
            try:
                boleta = params["boleta_{0}".format(i)]
                duracion = params["duracion_{0}".format(i)]
                nombre = params["nombre_{0}".format(i)]
                carrera = params["carrera_{0}".format(i)]
                tipo = params["tipo_{0}".format(i)]

                try:
                    alumno = Alumno.objects.get(boleta=boleta)
                    if nombre == alumno.nombre and carrera == alumno.carrera:
                        self.insertarActividad(alumno, duracion, tipo)
                    else:
                        raise ValueError()
                except Alumno.DoesNotExist:
                    try:
                        alumno = Alumno(
                            boleta=boleta, 
                            nombre=nombre, 
                            carrera=carrera,
                        )
                        alumno.full_clean()
                        alumno.save()
                        time.sleep(1)
                        self.insertarActividad(alumno, duracion, tipo)
                    except ValidationError:
                        errores = True
                        messages.add_message(
                            request, 
                            messages.ERROR,
                            "'{0}' no es un valor válido para el nombre del alumno.".format(alumno.nombre),
                            "{0} {1} {2} {3}".format(boleta,carrera,tipo,duracion)
                        )

                except ValueError:
                    errores = True
                    messages.add_message(
                        request, 
                        messages.ERROR, 
                        "La boleta {0} no corresponde con el alumno y/o carrera especificados.".format(boleta),
                        "{0} {1} {2} {3}".format(boleta,carrera,tipo,duracion)
                    )
            except KeyError:
                pass
        if errores == False:
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(self.error_url)

class CorregirActividadView(AdminStaffRequiredMixin, TemplateView):
    template_name = 'actividades/actividad_corregir.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CorregirActividadView, self).get_context_data(**kwargs)
        tipos = TipoActividad.objects.all().exclude(id=1)
        TIPOS = []
        for tipo in tipos:
            TIPOS.append((tipo.id,tipo.nombre))
        TIPOS = tuple(TIPOS)
        context['carreras'] = CARRERAS
        context['categorias'] = TIPOS
        return context