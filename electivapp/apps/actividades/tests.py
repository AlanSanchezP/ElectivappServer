from datetime import date

from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import TipoActividad, Actividad
from electivapp.apps.alumnos.models import Alumno

class Test_TipoActividad(TestCase):
    def test_horas_mayor_cero(self):
        obj = TipoActividad.objects.create(
            nombre="Nombre de prueba",
            categoria="IV",
            horasRequeridas=0,
        )
        self.assertRaises(ValidationError, obj.clean)

class Test_Actividad(TestCase):
    def test_valor_function(self):
        tipo = TipoActividad.objects.create(
            nombre="Nombre de prueba",
            categoria="IV",
            horasRequeridas=10,
        )
        alumno = Alumno.objects.create(
            boleta=2016601609,
            nombre="Alan Sánchez Pineda",
            carrera="II",
        )

        obj = Actividad.objects.create(
            duracion=3.2,
            alumno=alumno,
            tipo=tipo,
            fecha=date.today()
        )
        self.assertEquals(obj.valor(), 0.32)