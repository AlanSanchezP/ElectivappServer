from datetime import datetime, timezone, timedelta

from django.test import TestCase
from rest_framework import exceptions

from .api import registrarAsistencia
from .models import EventoAuditorio
from electivapp.apps.alumnos.models import Alumno, Responsable

# Create your tests here.
class Test_Registro_Asistencia(TestCase):
    def test_datos_iguales(self):
        evento = EventoAuditorio.objects.create(
            id=4,
            nombre = "Evento de prueba",
            fecha = datetime.now(timezone.utc),
            duracion = timedelta(hours=1),
            validado = True,
        )
        alumno = Alumno.objects.create(
            id=4,
            nombre = "Alan Sánchez Pineda",
            boleta = 2016601609,
            carrera = "IN",
        )
        responsable = Responsable.objects.create(
            id=4,
            alumno = alumno,
        )
        evento.responsables.add(responsable)

        self.assertRaises(exceptions.ValidationError, registrarAsistencia, 2016601609, "Alan Sánchez Pineda", "Ingeniería Industrial", evento, 4)