from django.test import TestCase
from .models import Alumno

def createAlumno(boleta=2016601609, nombre="Alan Sánchez Pineda", carrera="IN"):
    return Alumno.objects.create(
        boleta=boleta,
        nombre=nombre,
        carrera=carrera,
    )

#class Test_Alumno_Model(TestCase):
#	def test_str(self):
#		obj = createAlumno()
#		self.assertEquals(obj.__str__(), obj.nombre)
#
#	def test_creditos(self)
#		obj = createAlumno()

		

		
# Create your tests here.
