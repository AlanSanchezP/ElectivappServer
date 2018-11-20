from django.db import models

from electivapp.apps.alumnos.models import Alumno

CATEGORIAS = (
    ('IV', 'Inquietudes vocacionales'),
    ('CF', 'Complementarias a la formación'),
    ('EP', 'Enfásis en la profesión'),
    ('PE', 'Proyectos especiales'),
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

    horasRequeridas = models.PositiveIntegerField()

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

    def valor(self):
        valorPorHora = 1 / self.tipo.horasRequeridas
        return round(valorPorHora * float(self.duracion), 2)