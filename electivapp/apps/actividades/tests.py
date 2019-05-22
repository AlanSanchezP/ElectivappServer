from datetime import date

from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import TipoActividad, Actividad
from .views import RegistrarActividadView
from electivapp.apps.alumnos.models import Alumno, CARRERAS

def createTipoActividad(nombre="Nombre de prueba", categoria="IV", horasRequeridas=1):
    return TipoActividad.objects.create(
        nombre=nombre,
        categoria=categoria,
        horasRequeridas=horasRequeridas,
    )

def createAlumno(boleta=2016601609, nombre="Alan Sánchez Pineda", carrera="IN"):
    return Alumno.objects.create(
        boleta=boleta,
        nombre=nombre,
        carrera=carrera,
    )

def createActividad(alumno, tipo, duracion=1, fecha=date.today()):
    return Actividad.objects.create(
        duracion=duracion,
        alumno=alumno,
        tipo=tipo,
        fecha=fecha
    )

class Test_TipoActividad_Model(TestCase):
    def test_horas_mayor_cero(self):
        obj = createTipoActividad(horasRequeridas=0)
        self.assertRaises(ValidationError, obj.clean)

class Test_Actividad_Model(TestCase):
    def test_valor_function(self):
        tipo = createTipoActividad(horasRequeridas=10)
        alumno = createAlumno()

        obj = createActividad(
            duracion=3.2,
            alumno=alumno,
            tipo=tipo,
        )
        self.assertEquals(obj.valor(), 0.32)

class Test_Actividad_Views(TestCase):
    def test_insertar_actividad(self):
        obj = RegistrarActividadView()
        tipo = createTipoActividad()
        alumnoINTrue = createAlumno()
        alumnoINFalse = createAlumno(boleta=2016601610)
        alumnoAI = createAlumno(carrera= "AI", boleta=2016601238)
        alumnoELSE = createAlumno(carrera= "CC", boleta=2016601239)
        # Damos 15 creditos al alumno1 para que
        # le falte solo uno
        for i in range(0, 14):
            actividad = createActividad(tipo=tipo, alumno=alumnoINTrue)

        for i in range(0, 18):
            actividad = createActividad(tipo=tipo, alumno=alumnoAI)

        for i in range(0, 20):
            actividad = createActividad(tipo=tipo, alumno=alumnoELSE)

        obj.insertarActividad(alumno=alumnoINTrue, duracion=1, tipo=tipo.id)
        self.assertEquals(alumnoINTrue.terminado, True)

        obj.insertarActividad(alumno=alumnoINFalse, duracion=1, tipo=tipo.id)
        self.assertEquals(alumnoINFalse.terminado, False)

        obj.insertarActividad(alumno=alumnoAI, duracion=1, tipo=tipo.id)
        self.assertEquals(alumnoAI.terminado, True)

        obj.insertarActividad(alumno=alumnoELSE, duracion=1, tipo=tipo.id)
        self.assertEquals(alumnoELSE.terminado, True)

    def test_context_data(self):
        obj = RegistrarActividadView()
        tipo1= createTipoActividad()
        tipo2= createTipoActividad()
        TIPOS=(
            (tipo1.id, tipo1.nombre),
            (tipo2.id, tipo2.nombre),
        )
        context = obj.get_context_data()

        self.assertEquals(context['categorias'], TIPOS)

        self.assertEquals(context['carreras'], CARRERAS)
