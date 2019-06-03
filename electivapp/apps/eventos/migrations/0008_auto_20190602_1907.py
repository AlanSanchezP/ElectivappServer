# Generated by Django 2.0.9 on 2019-06-03 00:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0007_auto_20190601_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventoauditorio',
            name='nombre',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(regex="^([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\\'])+([\\s]?[A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\\'])+[\\s]?([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\\'])?$")]),
        ),
    ]
