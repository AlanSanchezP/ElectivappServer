from django.test import TestCase
from rest_framework.test import APIClient
from .models import Alumno


def createAlumno(boleta=2016601609, nombre="Alan Sánchez Pineda", carrera="IN"):
    return Alumno.objects.create(
        boleta=boleta,
        nombre=nombre,
        carrera=carrera,
    )

		
# Create your tests here.

class Test_Carreras_ListAPI(TestCase):
	def test_get_lista_carreras(self):
		
		client = APIClient()
		response = client.get('/api/carreras')
		
		self.assertEquals(response.data, [{
			'codigo': 'AI',
			'nombre': 'Administración Industrial'
			},
			{
			'codigo': 'CC',
			'nombre': 'Ciencias de la Informática'
			},
			{
			'codigo': 'II',
			'nombre': 'Ingeniería Industrial'
			},
			{
			'codigo': 'IT',
			'nombre': 'Ingeniería en Transportes'
			},
			{
			'codigo': 'IN',
			'nombre': 'Ingeniería en Informática'
			}])