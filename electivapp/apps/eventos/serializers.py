from rest_framework import serializers
from .models import EventoAuditorio

class EventoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    fecha = serializers.DateTimeField()