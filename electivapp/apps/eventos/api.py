from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
from datetime import datetime, timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

from .serializers import EventoSerializer
from electivapp.apps.actividades.models import TipoActividad, Actividad
from electivapp.apps.alumnos.models import Responsable, Alumno, CARRERAS
from electivapp.core import errors
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
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    
    def post(self, request, format=None):
        try:
            url = request.data.get('url')
            evento = EventoAuditorio.objects.get(id=request.data.get('evento'), validado=True)
            user = request.data.get('user')

            if url == None or user == None:
                raise exceptions.ValidationError(errors.ATTENDANCE_MISSING_PARAMETER)

            page = urlopen(url).read()
            document = BeautifulSoup(page, 'html.parser')

            boleta = document.find('div', attrs={'class': 'boleta'}).text.strip()
            nombre = document.find('div', attrs={'class': 'nombre'}).text.strip().title()
            carrera = document.find('div', attrs={'class': 'carrera'}).text.strip()
            escuela = document.find('div', attrs={'class': 'escuela'}).text.strip()
            valido = document.find('div', attrs={'class': 'cred cok'}).text.strip()

            if valido != 'CREDENCIAL VIGENTE':
                raise exceptions.ValidationError(errors.ATTENDANCE_EXPIRED_STUDENT)

            if escuela != 'UPIICSA':
                raise exceptions.ValidationError(errors.ATTENDANCE_FOREIGN_STUDENT)

            response = registrarAsistencia(boleta, nombre, carrera, evento, user)

            return Response(response)

        except EventoAuditorio.DoesNotExist:
            raise exceptions.ValidationError(errors.EVENT_DOES_NOT_EXIST)
        except URLError:
            raise exceptions.ValidationError(errors.ATTENDANCE_BAD_URL)
        except AttributeError:
            raise exceptions.ValidationError(errors.ATTENDANCE_MISSING_PARAMETER)

def registrarAsistencia(boleta, nombre, carrera, evento, user):
    alumno = None
    code = None

    try:
        responsable = evento.esResponsable(Responsable.objects.get(id=user).username)
        if responsable != True:
            raise exceptions.PermissionDenied(
                errors.AUTHENTICATION_PERMISSION_DENIED['detail'],
                errors.AUTHENTICATION_PERMISSION_DENIED['code']
            )

        vigente = evento.vigente()
        if vigente != True:
            raise exceptions.ValidationError(vigente)

    except Responsable.DoesNotExist:
        raise exceptions.ValidationError({
            'detail': 'Boleta y/o contraseña inválidos.',
            'code': 301
        })

    try:
        alumno = Alumno.objects.get(boleta=boleta)
        
        for key, value in CARRERAS:
            if value.upper() == carrera:
                code = key
                break

        if code == None:
            raise exceptions.ValidationError(errors.ATTENDANCE_INVALID_PROGRAM)

        if alumno.nombre != nombre or alumno.carrera != code:
            raise exceptions.ValidationError(errors.ATTENDANCE_NONMATCHING_DATA)

        if evento.asistentes.filter(boleta=boleta).exists():
            raise exceptions.ValidationError(errors.ATTENDANCE_DUPLICATED_STUDENT)
        
    except Alumno.DoesNotExist:
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
            user = request.data.get('user')

            if boleta == None or nombre == None or carrera == None or user == None:
                raise exceptions.ValidationError(errors.ATTENDANCE_MISSING_PARAMETER)

            response = registrarAsistencia(boleta, nombre, carrera, evento, user)
            
            return Response(response)

        except EventoAuditorio.DoesNotExist:
            raise exceptions.ValidationError(errors.EVENT_DOES_NOT_EXIST)