from django.db import models

CATEGORIAS = (
    ('C1', 'Cat1'),
    ('C2', 'Cat2'),
    ('C3', 'Cat3'),
)

# Create your models here.
class TipoActividad(models.Model):
    id = models.BigIntegerField(
        auto_created=True,
        primary_key=True,
    )

    nombre = models.CharField(
        max_length=150,
    )

    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIAS,
    )

    valorHoras = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )