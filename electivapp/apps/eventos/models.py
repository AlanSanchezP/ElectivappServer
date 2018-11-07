from django.db import models

from electivapp.apps.alumnos.models import Responsable

# Create your models here.
class EventoAuditorio(models.Model):
    id = models.BigIntegerField(
        auto_created=True,
        primary_key=True,
    )

    fecha = models.DateTimeField()

    duracion = models.DurationField()

    responsables = models.ManyToManyField(
        Responsable
    )

    validado = models.BooleanField()