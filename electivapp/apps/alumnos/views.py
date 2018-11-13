from datetime import datetime, timezone
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import View, TemplateView, FormView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from weasyprint import HTML

from .models import Alumno, Responsable, CARRERAS
from .forms import AlumnoForm, ResponsableForm, ResponsableUpdateForm
from electivapp.apps.actividades.models import Actividad
from electivapp.apps.eventos.models import EventoAuditorio

# Create your views here.
class AlumnosSearchView(LoginRequiredMixin, View):
    template_name = 'alumnos/alumno_search.html'

    def get(self, request, **kwargs):
        if request.GET.get("boleta"):
            boleta = request.GET.get("boleta")
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

class AlumnoListaView(LoginRequiredMixin, View):
    html_template = get_template('alumnos/alumnos_list.html')

    def get(self, request, **kwargs):
        fecha = datetime.datetime.now()
        alumnos = Alumno.objects.filter(terminado=True).filter(estatus=False)

        rendered_html = self.html_template.render(
            {"alumnos": alumnos, "fecha": fecha}
        ).encode(encoding="UTF-8")
        pdf_file = HTML(string=rendered_html).write_pdf()

        response = HttpResponse(pdf_file, content_type="application/pdf")
        response['Content-Disposition'] = 'filename="lista.pdf"'
        alumnos.update(estatus=True)

        return response

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
        password = Responsable.objects.make_random_password(length=8)
        responsable.set_password(password)
        responsable.save()
        return HttpResponse(password)

@api_view(['GET'])
# @authentication_classes((TokenAuthentication, ))
# @permission_classes((IsAuthenticated,))
def carreras_list(request):
    if request.method == 'GET':
        carreras = []
        for codigo, nombre in CARRERAS:
            carreras.append({
                'codigo': codigo,
                'nombre': nombre    
            })
        return Response(carreras)

class CustomAuthToken(ObtainAuthToken):
    def validarPermiso(self, responsable, evento_id):
        evento = EventoAuditorio.objects.get(id=evento_id, validado=True)
        duracion = evento.duracion
        today = datetime.now(timezone.utc)

        if not evento.responsables.all().filter(username=responsable).exists():
            raise exceptions.PermissionDenied('No tienes permiso para modificar este evento.')

        if today < evento.fecha:
            raise exceptions.ValidationError({
                'evento': 'El evento aun no esta disponible.',
                'code': 102
            })
        if today > evento.fecha+duracion:
            raise exceptions.ValidationError({
                'evento': 'El evento ha finalizado.',
                'code': 103
            })

    def post(self, request, *args, **kwargs):
        try:
            evento_id = request.data.get('evento')
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            self.validarPermiso(user, evento_id)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'evento_id': evento_id
            })

        except EventoAuditorio.DoesNotExist:
            raise exceptions.ValidationError({
                'evento': 'El evento indicado no existe.',
                'code': 101
            })