from datetime import datetime, timezone
from django.db import models

from electivapp.core.errors import EVENT_HAS_NOT_STARTED, EVENT_HAS_FINISHED
from electivapp.apps.alumnos.models import Alumno, Responsable

# Create your models here.
class EventoAuditorio(models.Model):
    nombre = models.CharField(
        max_length=200
    )

    fecha = models.DateTimeField()

    duracion = models.DurationField()

    responsables = models.ManyToManyField(
        Responsable
    )

    asistentes = models.ManyToManyField(
        Alumno,
        blank=True,
    )

    validado = models.BooleanField(
        default=False
    )

    def vigente(self):
        today = datetime.now(timezone.utc)

        if today < self.fecha:
            return EVENT_HAS_NOT_STARTED
        if today > self.fecha + self.duracion:
            return EVENT_HAS_FINISHED

        return True

    def esResponsable(self, responsable):
        return self.responsables.all().filter(username=responsable).exists()