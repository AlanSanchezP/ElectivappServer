from django.db import models

from electivapp.apps.alumnos.models import Alumno

CATEGORIAS = (
    ('C1', 'Cat1'),
    ('C2', 'Cat2'),
    ('C3', 'Cat3'),
)

# Create your models here.
class TipoActividad(models.Model):
    nombre = models.CharField(
        max_length=150,
    )

    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIAS,
    )

    valorHoras = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

class Actividad(models.Model):
    duracion = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
    )
    
    tipo = models.ForeignKey(
        TipoActividad, 
        on_delete=models.CASCADE,
    )

    fecha = models.DateField()