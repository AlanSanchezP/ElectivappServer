from django.test import TestCase
from .models import TipoActividad

# models test
class WhateverTest(TestCase):

    def create_whatever(self, nombre="only a test", categoria="IV", horasRequeridas=5):
        return TipoActividad.objects.create(nombre=nombre, categoria=categoria, horasRequeridas=horasRequeridas)

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, TipoActividad))