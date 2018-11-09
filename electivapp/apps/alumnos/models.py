from django.db import models

CARRERAS = (
    ('AI', 'Administración Industrial'),
    ('CC', 'Ciencias de la Informática'),
    ('II', 'Ingeniería Industrial'),
    ('IT', 'Ingeniería en Transportes'),
    ('IN', 'Ingeniería en Informática'),
)

# Create your models here.
class Alumno(models.Model):
    boleta = models.PositiveIntegerField(
        auto_created=False,
        primary_key=False,
    )

    nombre = models.CharField(
        max_length=150,
    )

    carrera = models.CharField(
        max_length=100,
        choices=CARRERAS,
    )

    estatus = models.BooleanField(
        default=False,
    )

class Responsable(models.Model):
    alumno = models.OneToOneField(
        Alumno,
        on_delete=models.CASCADE,
    )

    password = models.CharField(
        max_length=20,
    )