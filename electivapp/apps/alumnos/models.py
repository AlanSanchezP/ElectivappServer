from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from electivapp.apps.users.models import User
from electivapp.core.regex import NAME_REGEX

CARRERAS = (
    ('AI', 'Administración Industrial'),
    ('CC', 'Ciencias de la Informática'),
    ('II', 'Ingeniería Industrial'),
    ('IT', 'Ingeniería en Transportes'),
    ('IN', 'Ingeniería en Informática'),
)

# Create your models here.
class Alumno(models.Model):
    boleta = models.BigIntegerField(
        unique=True,
        default=2000160000,
        validators=[
            MaxValueValidator(9999999999),
            MinValueValidator(1936000000)
        ]
    )

    nombre = models.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex=NAME_REGEX,
            )
        ]
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

class Responsable(User):
    alumno = models.OneToOneField(
        Alumno,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "responsable"
        verbose_name_plural = "responsables"

    def save(self, *args, **kwargs):
        self.username = self.alumno.boleta
        super(Responsable, self).save(*args, **kwargs)

    def __str__(self):
        return self.alumno.nombre