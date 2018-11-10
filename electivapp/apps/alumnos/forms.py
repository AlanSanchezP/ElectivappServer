import time
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Alumno, Responsable
from .utils import generarPassword

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['boleta', 'nombre', 'carrera']

class ResponsableForm(AlumnoForm):
    class Meta(AlumnoForm.Meta):
        fields = AlumnoForm.Meta.fields

    def clean(self):
        data = self.cleaned_data
        try:
            alumno = Alumno.objects.get(boleta=data["boleta"])
            if data["nombre"] != alumno.nombre or data["carrera"] != alumno.carrera:
                raise forms.ValidationError("La boleta {0} no coincide con el nombre y/o carrera especificados".format(data["boleta"]))
        except Alumno.DoesNotExist:
            alumno = Alumno(
                boleta=data["boleta"], 
                nombre=data["nombre"], 
                carrera=data["carrera"],
            )
            alumno.save()
            time.sleep(1)

    def save(self):
        data = self.cleaned_data
        responsable, created = Responsable.objects.get_or_create(
            alumno=Alumno.objects.get(boleta=data["boleta"])
        )
        if created:
            password = generarPassword()
            responsable.password = password
            responsable.save()
            return password

class ResponsableUpdateForm(ResponsableForm):
    def clean(self):
        data = self.cleaned_data        
        try:
            alumno = Alumno.objects.get(boleta=data["boleta"])
            if data["nombre"] != alumno.nombre:
                alumno.nombre = data["nombre"]
            if data["carrera"] != alumno.carrera:
                alumno.carrera = data["carrera"]
            alumno.save()
        except Alumno.DoesNotExist:
            alumno = Alumno(
                boleta=data["boleta"], 
                nombre=data["nombre"], 
                carrera=data["carrera"],
            )
            alumno.save()
            time.sleep(1)