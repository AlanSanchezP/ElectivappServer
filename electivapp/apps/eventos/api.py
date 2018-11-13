from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import EventoSerializer
from electivapp.apps.actividades.models import Actividad
from .models import EventoAuditorio

class EventosListAPI(APIView):
    def get(self, request, format=None):
        eventos = EventoAuditorio.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

class RegistrarAsistenciaAPI(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        try:
            evento = EventoAuditorio.objects.get(id=request.data.get('evento'), validado=True)
            boleta = request.data.get('boleta')
            nombre = request.data.get('nombre')
            carrera = request.data.get('carrera')

            # actividad = Actividad(evento, boleta, nombre, carrera, 1, duracion)
            
            return Response({})

        except EventoAuditorio.DoesNotExist:
            raise exceptions.ValidationError({
                'evento': 'El evento indicado no existe.',
                'code': 101
            })