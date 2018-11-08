from django.db import models

from electivapp.apps.alumnos.models import Responsable

# Create your models here.
class EventoAuditorio(models.Model):
    fecha = models.DateTimeField()

    duracion = models.DurationField()

    responsables = models.ManyToManyField(
        Responsable
    )

    validado = models.BooleanField()