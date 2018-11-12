from rest_framework import serializers

class EventoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    fecha = serializers.DateTimeField()