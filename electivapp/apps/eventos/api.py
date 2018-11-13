from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import EventoSerializer
from .models import EventoAuditorio

class EventosListAPI(APIView):
    def get(self, request, format=None):
        eventos = EventoAuditorio.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

class RegistrarEventoQRAPI(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        return Response({})

class RegistrarEventoFormAPI(APIView):
    def post(self, request, format=None):
        return Response({})