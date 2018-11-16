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
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            evento = EventoAuditorio.objects.get(id=request.data.get('evento'), validado=True)
            
            if not evento.esResponsable(user):
                raise exceptions.PermissionDenied('No tienes permiso para modificar este evento.')

            vigente = evento.vigente()

            if vigente != True:
                raise exceptions.ValidationError(vigente)

            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'evento_id': evento.id
            })

        except EventoAuditorio.DoesNotExist:
            raise exceptions.ValidationError({
                'detail': 'El evento indicado no existe.',
                'code': 101
            })