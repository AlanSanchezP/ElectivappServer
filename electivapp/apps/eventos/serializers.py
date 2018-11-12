from rest_framework import serializers

class EventoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField()
    fecha = serializers.DateTimeField()