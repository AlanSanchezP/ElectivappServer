from .models import Alumno, Responsable
from electivapp.apps.eventos.models import EventoAuditorio
from rest_framework import authentication
from rest_framework import exceptions

from datetime import datetime, timezone

class ResponsableAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META['HTTP_BOLETA']
        password = request.META['HTTP_PASSWORD']
        evento_id = request.META['HTTP_EVENTO']

        try:
            responsable = Responsable.objects.get(username=username)
            if responsable.check_password(password) == False:
                raise exceptions.AuthenticationFailed('Contraseña y/o usuario invalidos.')
            evento = EventoAuditorio.objects.get(id=evento_id, validado=True)
            duracion = evento.duracion
            today = datetime.now(timezone.utc)

            if evento.responsables.all().filter(username=username).exists():
                if today < evento.fecha:
                    raise exceptions.AuthenticationFailed('El evento aun no esta disponible.')
                if today > evento.fecha+duracion:
                    raise exceptions.AuthenticationFailed('El evento ha finalizado.')

                # Caso exitoso
                return(responsable, None)
            else:
                raise exceptions.AuthenticationFailed('No tienes permiso para modificar este evento.')

        except Responsable.DoesNotExist:
            raise exceptions.AuthenticationFailed('Contraseña y/o usuario invalidos')
        except EventoAuditorio.DoesNotExist:
            raise exceptions.AuthenticationFailed('Evento inexistente')