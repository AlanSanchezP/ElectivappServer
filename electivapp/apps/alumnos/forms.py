import time
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import CARRERAS, Alumno, Responsable

class ResponsableForm(forms.Form):
    nombre = forms.CharField()
    boleta = forms.DecimalField(
        min_value=0,
        max_value=9999999999
    )
    carrera = forms.ChoiceField(
        choices=CARRERAS,
    )

    def clean(self):
        data = self.cleaned_data
        try:
            alumno = Alumno.objects.get(pk=data["boleta"])
            if data["nombre"] == alumno.nombre and data["carrera"] == alumno.carrera:
                pass
            else:
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
        responsable = Responsable(
            alumno=Alumno.objects.get(pk=data["boleta"]),
            password="aaa"
        )
        