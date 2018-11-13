from datetime import datetime, timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import exceptions

from .models import Alumno, Responsable, CARRERAS
from electivapp.apps.eventos.models import EventoAuditorio

class CarrerasListAPI(APIView):
    def get(self, request, format=None):
        carreras = []
        for codigo, nombre in CARRERAS:
            carreras.append({
                'codigo': codigo,
                'nombre': nombre    
            })
        return Response(carreras)

class CustomAuthToken(ObtainAuthToken):
    def validarPermiso(self, responsable, evento_id):
        evento = EventoAuditorio.objects.get(id=evento_id, validado=True)
        duracion = evento.duracion
        today = datetime.now(timezone.utc)

        if not evento.responsables.all().filter(username=responsable).exists():
            raise exceptions.PermissionDenied('No tienes permiso para modificar este evento.')

        if today < evento.fecha:
            raise exceptions.ValidationError({
                'evento': 'El evento aun no esta disponible.',
                'code': 102
            })
        if today > evento.fecha+duracion:
            raise exceptions.ValidationError({
                'evento': 'El evento ha finalizado.',
                'code': 103
            })

    def post(self, request, *args, **kwargs):
        try:
            evento_id = request.data.get('evento')
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            self.validarPermiso(user, evento_id)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'evento_id': evento_id
            })

        except EventoAuditorio.DoesNotExist:
            raise exceptions.ValidationError({
                'evento': 'El evento indicado no existe.',
                'code': 101
            })