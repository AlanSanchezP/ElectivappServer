from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime, timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

from .serializers import EventoSerializer
from electivapp.apps.actividades.models import TipoActividad, Actividad
from electivapp.apps.alumnos.models import Alumno, CARRERAS
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

            page = urlopen(url).read()
            document = BeautifulSoup(page, 'html.parser')

            boleta = document.find('div', attrs={'class': 'boleta'}).text.strip()
            nombre = document.find('div', attrs={'class': 'nombre'}).text.strip().title()
            carrera = document.find('div', attrs={'class': 'carrera'}).text.strip()
            escuela = document.find('div', attrs={'class': 'escuela'}).text.strip()
            valido = document.find('div', attrs={'class': 'cred cok'}).text.strip()

            if valido != 'CREDENCIAL VIGENTE':
                raise exceptions.ValidationError({
                    'detail': 'La boleta ha expirado.',
                    'code': 201
                })

            if escuela != 'UPIICSA':
                raise exceptions.ValidationError({
                    'detail': 'La boleta no corresponde a la escuela.',
                    'code': 202
                })

            response = registrarAsistencia(boleta, nombre, carrera, evento)

            return Response(response)

        except EventoAuditorio.DoesNotExist:
            raise exceptions.ValidationError({
                'detail': 'El evento indicado no existe.',
                'code': 101
            })

def registrarAsistencia(boleta, nombre, carrera, evento):
    alumno = None
    try:
        alumno = Alumno.objects.get(boleta=boleta)
        if evento.asistentes.filter(boleta=boleta).exists():
            raise exceptions.ValidationError({
                'detail': 'El alumno ya ha asistido a este evento.',
                'code': 203
            })
        
    except Alumno.DoesNotExist:
        code = None
        for key, value in CARRERAS:
            if value.upper() == carrera:
                code = key
                break

        if code == None:
            raise exceptions.ValidationError({
                'detail': 'Nombre de carrera invalido.',
                'code': 204
            })

        alumno = Alumno.objects.create(
            boleta=boleta,
            nombre=nombre,
            carrera=code,
        )

    evento.asistentes.add(alumno)
    actividad = Actividad.objects.create(
        fecha=evento.fecha,
        alumno=alumno, 
        tipo=TipoActividad.objects.get(id=1),
        duracion=evento.duracion.total_seconds()/3600,
    )
    evento.save()

    return {
        'detail': 'Asistencia registrada'
    }  

class RegistrarAsistenciaAPI(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        try:
            evento = EventoAuditorio.objects.get(id=request.data.get('evento'), validado=True)
            boleta = request.data.get('boleta')
            nombre = request.data.get('nombre')
            carrera = request.data.get('carrera')

            response = registrarAsistencia(boleta, nombre, carrera, evento)
            
            return Response(response)

        except EventoAuditorio.DoesNotExist:
            raise exceptions.ValidationError({
                'detail': 'El evento indicado no existe.',
                'code': 101
            })