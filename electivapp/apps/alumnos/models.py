from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

CARRERAS = (
    ('AI', 'Administración Industrial'),
    ('CC', 'Ciencias de la Informática'),
    ('II', 'Ingeniería Industrial'),
    ('IT', 'Ingeniería en Transportes'),
    ('IN', 'Ingeniería en Informática'),
)

# Create your models here.
class Alumno(models.Model):
    boleta = models.PositiveIntegerField()

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

    terminado = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.nombre

    def creditos(self):
        creditos = 0.0
        for actividad in self.actividad_set.all():
            creditos += actividad.valor()
        return creditos

class Responsable(models.Model):
    alumno = models.OneToOneField(
        Alumno,
        on_delete=models.CASCADE,
    )

    password = EncryptedCharField(
        max_length=20,
    )

    def __str__(self):
        return self.alumno.nombre