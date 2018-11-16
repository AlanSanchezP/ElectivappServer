from datetime import datetime, timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import EventoSerializer
from electivapp.apps.actividades.models import Actividad
from .models import EventoAuditorio

class EventosListAPI(APIView):
    def get(self, request, format=None):
        eventos = EventoAuditorio.objects.filter(
            # fecha__gte=datetime.now(),
            validado=True
        )
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

class RegistrarAsistenciaQRAPI(APIView):
    def post(self, request, format=None):
        try:
            url = request.data.get('url')
            evento = EventoAuditorio.objects.get(id=request.data.get('evento'), validado=True)

            # Scrapping

            # boleta = request.data.get('boleta')
            # nombre = request.data.get('nombre')
            # carrera = request.data.get('carrera')

            # registrarAsistencia(boleta, nombre, carrera, evento.id)

            return Response({})

        except EventoAuditorio.DoesNotExist:
            raise exceptions.ValidationError({
                'evento': 'El evento indicado no existe.',
                'code': 101
            })

def registrarAsistencia(boleta, nombre, carrera, evento):
    # actividad = Actividad(evento, boleta, nombre, carrera, 1, duracion)
    return

class RegistrarAsistenciaAPI(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        try:
            evento = EventoAuditorio.objects.get(id=request.data.get('evento'), validado=True)
            boleta = request.data.get('boleta')
            nombre = request.data.get('nombre')
            carrera = request.data.get('carrera')

            registrarAsistencia(boleta, nombre, carrera, evento.id)
            
            return Response({})

        except EventoAuditorio.DoesNotExist:
            raise exceptions.ValidationError({
                'evento': 'El evento indicado no existe.',
                'code': 101
            })